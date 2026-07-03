"""Build the No Shortcuts website from manifesto.md.

The project intentionally uses only Python's standard library. The Markdown
renderer supports the small, deliberate subset used by the manifesto:
headings, paragraphs, blockquotes, horizontal rules, emphasis, and inline code.
"""

from __future__ import annotations

import html
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "manifesto.md"
OUTPUT = ROOT / "index.html"

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


def parse_source(source: str) -> tuple[str, str, str, str, list[str]]:
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
    subtitle = " ".join(metadata[2:])
    while index < len(lines) and not lines[index].strip():
        index += 1
    return title, copyright_line, publication_date, subtitle, lines[index:]


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


def build() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    title, copyright_line, publication_date, subtitle, body_lines = parse_source(
        source
    )
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
  <meta name="description" content="{html.escape(subtitle, quote=True)}">
  <meta name="theme-color" content="#132b2c">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#manifesto">Skip to the manifesto</a>
  <header class="hero">
    <div class="hero-inner">
      <p class="eyebrow">A manifesto for engineering with AI</p>
      <h1>{html.escape(title)}</h1>
      <p class="subtitle">{html.escape(subtitle)}</p>
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

  <footer class="site-footer">
    <p>{html.escape(copyright_line)}</p>
    <p><a href="manifesto.md">Read the source Markdown</a> <span aria-hidden="true">·</span> <a href="LICENSE.md">License</a></p>
  </footer>
</body>
</html>
"""
    validate_document(document, headings)
    OUTPUT.write_text(document, encoding="utf-8", newline="\n")
    print(
        f"Built {OUTPUT.name}: {len(headings)} headings, "
        f"{len(document):,} characters"
    )


if __name__ == "__main__":
    build()
