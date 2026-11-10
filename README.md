# Python Programming Course

Course website built with [Jupyter Book](https://jupyterbook.org) and deployed to GitHub Pages.

## Run the website locally

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter book start                 # live preview at http://localhost:3000
```

Pages reload automatically when you edit files. Stop the server with `Ctrl+C`.
Jupyter Book needs [Node.js](https://nodejs.org) (v20+); if it is missing, it will offer to install it.

To build the static site (the same output GitHub Pages serves): `jupyter book build --html`
(the result is in `_build/html/`).

## Structure

- `myst.yml` — book configuration and table of contents
- `index.md` — home page
- `lectures/NN-topic/index.md` — one folder per lecture; put slides and materials in the same folder
- `.github/workflows/deploy.yml` — builds and deploys the site on every push to `main`

## Customising the look

- `assets/custom.css` — colours, fonts, hero, roadmap timeline, lecture banners, footer
  (phase colours are the `--phase-1` … `--phase-5` variables at the top)
- `assets/logo.svg`, `assets/logo-dark.svg`, `assets/favicon.png` — branding
- `parts/footer.md`, `parts/sidebar-footer.md` — site footer and sidebar footer
- `myst.yml` → `site.nav` / `site.actions` — top navigation links and buttons
