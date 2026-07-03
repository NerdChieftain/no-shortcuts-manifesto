"""Build the No Shortcuts website from manifesto.md.

The project intentionally uses only Python's standard library. The Markdown
renderer supports the small, deliberate subset used by the manifesto:
headings, paragraphs, blockquotes, horizontal rules, emphasis, and inline code.
"""

from __future__ import annotations

import html
import re
import struct
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "manifesto.md"
OUTPUT = ROOT / "index.html"
SHORT_SOURCE = ROOT / "tldr.md"
SHORT_OUTPUT = ROOT / "tldr.html"

SITE_URL = "https://nerdchieftain.github.io/no-shortcuts-manifesto/"
SOCIAL_IMAGE_URL = f"{SITE_URL}social-card.png"
DISCUSSIONS_URL = (
    "https://github.com/NerdChieftain/no-shortcuts-manifesto/discussions"
)
DESCRIPTION = (
    "AI code generation should make us better engineers—not merely faster "
    "coders. The No Shortcuts framework reinvests AI-created time in design, "
    "tests, documentation, feedback, and human review."
)
SOCIAL_DESCRIPTION = "AI gave us time back. Use it like engineers."

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
CODE_RE = re.compile(r"`([^`]+)`")


@dataclass(frozen=True)
class Heading:
    level: int
    text: str
    anchor: str


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_value.lower()).strip("-")
    return slug or "section"


def plain_text(value: str) -> str:
    value = CODE_RE.sub(r"\1", value)
    return re.sub(r"[*_]", "", value).strip()


def render_inline(value: str) -> str:
    code_spans: list[str] = []

    def stash_code(match: re.Match[str]) -> str:
        code_spans.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"\x00CODE{len(code_spans) - 1}\x00"

    value = CODE_RE.sub(stash_code, value)
    value = html.escape(value, quote=False)
    value = re.sub(
        r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", value
    )
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", value)

    for index, code in enumerate(code_spans):
        value = value.replace(f"\x00CODE{index}\x00", code)
    return value


def unique_anchor(text: str, anchors: set[str]) -> str:
    base = slugify(text)
    anchor = base
    suffix = 2
    while anchor in anchors:
        anchor = f"{base}-{suffix}"
        suffix += 1
    anchors.add(anchor)
    return anchor


def render_markdown(lines: list[str]) -> tuple[str, list[Heading]]:
    output: list[str] = []
    headings: list[Heading] = []
    paragraph: list[str] = []
    quote: list[str] = []
    anchors: set[str] = set()

    def flush_paragraph() -> None:
        if paragraph:
            text = " ".join(part.strip() for part in paragraph)
            css_class = ' class="credits"' if text.startswith("Co-authored ") else ""
            output.append(f"<p{css_class}>{render_inline(text)}</p>")
            paragraph.clear()

    def flush_quote() -> None:
        if quote:
            text = " ".join(part.strip() for part in quote)
            output.append(f"<blockquote><p>{render_inline(text)}</p></blockquote>")
            quote.clear()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            flush_quote()
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            flush_paragraph()
            flush_quote()
            level = len(heading_match.group(1))
            text = plain_text(heading_match.group(2))
            anchor = unique_anchor(text, anchors)
            headings.append(Heading(level, text, anchor))
            output.append(
                f'<h{level} id="{anchor}">{render_inline(heading_match.group(2))}'
                f'<a class="heading-link" href="#{anchor}" aria-label="Link to {html.escape(text, quote=True)}">#</a>'
                f"</h{level}>"
            )
            continue

        if stripped == "---":
            flush_paragraph()
            flush_quote()
            output.append('<hr aria-hidden="true">')
            continue

        if line.startswith(">"):
            flush_paragraph()
            quote.append(line[1:].lstrip())
            continue

        flush_quote()
        paragraph.append(line)

    flush_paragraph()
    flush_quote()
    return "\n".join(output), headings


def render_toc(headings: list[Heading]) -> str:
    items = []
    for heading in headings:
        if heading.level < 2 or heading.level > 4:
            continue
        items.append(
            f'<li class="toc-level-{heading.level}">'
            f'<a href="#{heading.anchor}">{html.escape(heading.text)}</a></li>'
        )
    return "\n".join(items)


def parse_source(source: str) -> tuple[str, str, str, list[str], list[str]]:
    lines = source.splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError("manifesto.md must begin with a level-one title")

    title = plain_text(lines[0][2:])
    metadata: list[str] = []
    index = 1
    while index < len(lines) and lines[index].strip():
        metadata.append(lines[index].strip())
        index += 1
    if len(metadata) < 3:
        raise ValueError("Expected copyright, date, and subtitle below the title")

    copyright_line, publication_date = metadata[:2]
    subtitle_lines = metadata[2:]
    while index < len(lines) and not lines[index].strip():
        index += 1
    return title, copyright_line, publication_date, subtitle_lines, lines[index:]


def validate_document(document: str, headings: list[Heading]) -> None:
    if document.count("<h1>") != 1:
        raise RuntimeError("The generated page must contain exactly one h1")

    document_ids = set(re.findall(r'\bid="([^"]+)"', document))
    fragment_links = re.findall(r'\bhref="#([^"]+)"', document)
    missing_targets = sorted(set(fragment_links) - document_ids)
    if missing_targets:
        raise RuntimeError(
            "Missing targets for fragment links: " + ", ".join(missing_targets)
        )

    for heading in headings:
        if document.count(f'id="{heading.anchor}"') != 1:
            raise RuntimeError(f"Heading anchor is missing or repeated: {heading.anchor}")


def validate_site_assets(*documents: str) -> None:
    local_references: set[str] = set()
    for document in documents:
        for reference in re.findall(r'\b(?:href|src)="([^"]+)"', document):
            if reference.startswith(("#", "http://", "https://", "mailto:")):
                continue
            path = reference.split("#", 1)[0]
            if path:
                local_references.add(path)

    missing = sorted(
        reference for reference in local_references if not (ROOT / reference).exists()
    )
    if missing:
        raise RuntimeError("Missing local site assets: " + ", ".join(missing))

    card = ROOT / "social-card.png"
    data = card.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError("social-card.png is not a valid PNG")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (1200, 630):
        raise RuntimeError(
            f"social-card.png must be 1200x630, found {width}x{height}"
        )


def render_metadata(page_title: str, canonical_url: str) -> str:
    return f"""  <meta name="description" content="{html.escape(DESCRIPTION, quote=True)}">
  <meta name="author" content="Jeremy Cox">
  <meta name="theme-color" content="#132b2c">
  <link rel="canonical" href="{html.escape(canonical_url, quote=True)}">

  <meta property="og:title" content="{html.escape(page_title, quote=True)}">
  <meta property="og:description" content="{html.escape(SOCIAL_DESCRIPTION, quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{html.escape(canonical_url, quote=True)}">
  <meta property="og:site_name" content="No Shortcuts Manifesto">
  <meta property="og:image" content="{SOCIAL_IMAGE_URL}">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="No Shortcuts. AI gave us time back. Use it like engineers.">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(page_title, quote=True)}">
  <meta name="twitter:description" content="{html.escape(SOCIAL_DESCRIPTION, quote=True)}">
  <meta name="twitter:image" content="{SOCIAL_IMAGE_URL}">
  <meta name="twitter:image:alt" content="No Shortcuts. AI gave us time back. Use it like engineers.">"""


def render_footer(copyright_line: str) -> str:
    return f"""  <footer class="site-footer">
    <p>{html.escape(copyright_line)}</p>
    <p><a href="manifesto.md">Read the source Markdown</a> <span aria-hidden="true">·</span> <a href="LICENSE.md">License</a></p>
  </footer>"""


def build() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    title, copyright_line, publication_date, subtitle_lines, body_lines = (
        parse_source(source)
    )
    occasion_html = " ".join(html.escape(line) for line in subtitle_lines)
    article, headings = render_markdown(body_lines)
    toc = render_toc(headings)

    source_heading_count = sum(
        1 for line in body_lines if HEADING_RE.match(line) is not None
    )
    if source_heading_count != len(headings):
        raise RuntimeError("Not every source heading was rendered")
    if len({heading.anchor for heading in headings}) != len(headings):
        raise RuntimeError("Generated heading anchors are not unique")

    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{render_metadata(title, SITE_URL)}
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#manifesto">Skip to the manifesto</a>
  <header class="hero">
    <div class="hero-inner">
      <p class="eyebrow">A manifesto for engineering with AI LLM</p>
      <h1>{html.escape(title)}</h1>
      <p class="hero-thesis">AI code generation should make us better engineers—not merely faster coders.</p>
      <p class="hero-support">The No Shortcuts framework reinvests AI-created time in design, tests, documentation, feedback, and human review.</p>
      <div class="hero-actions" aria-label="Ways to read and discuss the manifesto">
        <a class="button button-primary" href="tldr.html">Read the short version</a>
        <a class="button button-secondary" href="#preamble">Start the manifesto</a>
        <a class="button button-text" href="{DISCUSSIONS_URL}">Challenge the framework <span aria-hidden="true">↗</span></a>
      </div>
      <p class="occasion">{occasion_html}</p>
      <div class="publication-meta" aria-label="Publication details">
        <span>{html.escape(publication_date)}</span>
        <span>{html.escape(copyright_line)}</span>
      </div>
    </div>
  </header>

  <div class="page-shell">
    <aside class="toc" aria-labelledby="contents-title">
      <div class="toc-inner">
        <p class="toc-title" id="contents-title">Contents</p>
        <nav aria-label="Manifesto sections">
          <ol>
            {toc}
          </ol>
        </nav>
      </div>
    </aside>

    <main id="manifesto" tabindex="-1">
      <article>
        {article}
      </article>
    </main>
  </div>

{render_footer(copyright_line)}
</body>
</html>
"""
    validate_document(document, headings)
    OUTPUT.write_text(document, encoding="utf-8", newline="\n")

    short_article, short_headings = render_markdown(
        SHORT_SOURCE.read_text(encoding="utf-8").splitlines()
    )
    short_title = "No Shortcuts — The Short Version"
    short_url = f"{SITE_URL}tldr.html"
    short_document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{render_metadata(short_title, short_url)}
  <title>{html.escape(short_title)}</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body class="short-page">
  <a class="skip-link" href="#short-version">Skip to the short version</a>
  <header class="short-hero">
    <div class="short-hero-inner">
      <a class="wordmark" href="index.html">No Shortcuts Manifesto</a>
      <p class="eyebrow">The short version</p>
      <h1>No Shortcuts in 30 Seconds</h1>
      <p class="short-deck">Code faster, or use AI-created time to make the whole product better?</p>
    </div>
  </header>

  <main class="short-main" id="short-version" tabindex="-1">
    <article class="short-article">
      {short_article}
      <div class="short-actions">
        <a class="button button-primary button-dark" href="index.html#preamble">Read the full manifesto</a>
        <a class="button button-outline" href="{DISCUSSIONS_URL}">Challenge the framework <span aria-hidden="true">↗</span></a>
      </div>
    </article>
  </main>

{render_footer(copyright_line)}
</body>
</html>
"""
    validate_document(short_document, short_headings)
    SHORT_OUTPUT.write_text(short_document, encoding="utf-8", newline="\n")
    validate_site_assets(document, short_document)
    print(
        f"Built {OUTPUT.name}: {len(headings)} headings, {len(document):,} characters; "
        f"{SHORT_OUTPUT.name}: {len(short_document):,} characters"
    )


if __name__ == "__main__":
    build()
