© 2026 Jeremy Cox. Licensed under CC BY 4.0.

This work is licensed under a Creative Commons Attribution 4.0 International License.
https://creativecommons.org/licenses/by/4.0/

# No Shortcuts Manifesto

This manifesto gives cause to act and a methodology to stop taking shortcuts by utilizing AI Code Gen to generate free time to do engineering software right.

## Build the website

The website is generated from `manifesto.md`, which remains the canonical source.
No third-party packages are required.

```powershell
python build.py
```

The command writes the static page to `index.html`. Serve the repository with any
static file server to preview it locally.

```powershell
python -m http.server 8000
```

Then open `http://localhost:8000`.
