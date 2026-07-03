© 2026 Jeremy Cox. Licensed under CC BY 4.0.

This work is licensed under a Creative Commons Attribution 4.0 International License.
https://creativecommons.org/licenses/by/4.0/

# No Shortcuts Manifesto

This manifesto gives cause to act and a methodology to stop taking shortcuts by utilizing AI Code Gen to generate free time to do engineering software right.

## Build the website

The full website is generated from `manifesto.md`, and the short version is
generated from `tldr.md`. Those Markdown files remain the canonical sources.
No third-party Python packages are required.

```powershell
python build.py
```

The command writes the static pages to `index.html` and `tldr.html`. Serve the
repository with any static file server to preview it locally.

```powershell
python -m http.server 8000
```

Then open `http://localhost:8000`.

The editable social-preview source is `social-card.svg`. Its published PNG is
`social-card.png` (1200×630). If ImageMagick is installed, regenerate it with:

```powershell
magick -background none social-card.svg social-card.png
```
