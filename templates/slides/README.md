# Lesson slides (Marp)

Two themes:

| Theme | Feel | Example deck |
| --- | --- | --- |
| `pycourse` | Hands-on lessons: editor-style cover, terminal code blocks, chat, quizzes, sticky notes | `lesson-template.md` (Lecture 04 · Functions) |
| `pycourse-academic` | "LaTeX Beamer meets Python": header bar, serif titles, footnotes, theorem blocks, booktabs tables | `lesson-academic.md` (Lecture 09 · Hashing) |

`pycourse-academic` is a modified copy of [kaisugi/marp-theme-academic](https://github.com/kaisugi/marp-theme-academic) (MIT, © 2022 Kaito Sugimoto; the notice is kept at the top of the CSS).
It is built on Marp's `gaia` theme, like the original, and has its own set of classes (listed further down).

## Start a new deck

```bash
cp templates/slides/lesson-template.md lectures/05-recursion/slides.md     # or lesson-academic.md
```

Then edit the front matter: `title`, `header`, `footer`, and the phase colour (`--phase-1` … `--phase-6`).
Because `lectures/NN-topic/` is two levels deep, like `templates/slides/`, the `../../assets/logo.svg` path still works after you copy the file.

## Preview and export

**VS Code:** install the *Marp for VS Code* extension (`marp-team.marp-vscode`) and open the deck. The repo's `.vscode/settings.json` already registers both themes and turns on HTML. Use the preview button, or run *Marp: Export slide deck…* to get HTML, PDF or PPTX.

**CLI** (needs Node.js 20+ and Chrome, Edge or Firefox):

```bash
npx @marp-team/marp-cli@latest lectures/05-recursion/slides.md \
  --theme-set templates/slides/ --html --allow-local-files \
  --pdf                      # or --pptx, or leave it out to get HTML
```

Passing the whole `templates/slides/` folder to `--theme-set` registers both themes.
Use `--preview` instead of `--pdf` for a live window with presenter view and speaker notes.

## `pycourse` slide layouts

Put `<!-- _class: name -->` at the top of a slide. Combine classes with spaces: `<!-- _class: dark compact hl-3 -->`.

| Class | Use it for | Markdown to write |
| --- | --- | --- |
| `cover` | Title slide drawn as a code editor | `###### file_name.py` (the tab), `# Title with *gradient words*`, a paragraph (shown as a `# comment`), `` `chips` ``; the footer becomes the status bar |
| `lead` | Title or closing slide | `###### kicker`, `# Title`, paragraphs, `` `chips` ``. |
| `divider` | Section break | `###### 01` (giant outlined number), `# Section title` (gets a `>>>` prompt and blinking cursor) |
| `agenda` | Session timeline | ordered list; `*10 min*` at the end of an item floats right |
| `objectives` | Learning objectives | ordered list → numbered cards |
| `big` | One key statement | a single `#` heading and an optional paragraph |
| `steps` | A process, left → right | ordered list; start each item with `**Name**` |
| `chat` | A conversation with Python | unordered list; items alternate you / 🐍 Python; start each with `**Name**` |
| `traceback` | Reading an error | `## **TypeError**: …`, a ` ```pytb ` block, an explanation |
| `quiz` | Multiple choice | unordered list of options; make the correct one `**bold**` (hidden until revealed) |
| `quiz reveal` | The answer | duplicate the quiz slide; the bold option turns green |
| `exercise` | "Your turn" | `###### ⏱ 20 min · pairs · ★★☆`, ordered list of steps, `>` stretch goal |
| `recap` | Summary | `###### 🏆 Achievement unlocked · +100 XP`, unordered list (ticks) |
| `dark`, `center`, `compact` | Code-heavy, centred, dense slides | anything |
| `hl-1` … `hl-15` | Spotlight one line of code | the line number inside the slide's code block(s) |

On every slide:

- `###### text` gives the small uppercase kicker above the title.
- `**bold**` inside a `##` heading gets a yellow highlighter stroke.
- `*text*` is shown in the phase colour (not italic).
- Code blocks look like a terminal window, with a label (`python`, `pycon`, `console`, `bash`, `pytb`, `text`, `yaml` …).
- `<kbd>Ctrl</kbd>` draws keys. `$…$` and `$$…$$` draw maths (KaTeX). `![center](img.png)` centres an image; add `shadow` to lift it.
- HTML comments become speaker notes.
- The bar along the top grows as you move through the deck where the browser supports it (recent Chrome / Edge / Firefox). Otherwise it stays full width.

## HTML helpers

Leave a blank line after each opening `<div>` so the Markdown inside still works.

```html
<div class="cols">            <!-- also: cols c3 | wide-left | wide-right; add "middle" to centre vertically -->
<div> left </div>
<div> right </div>
</div>

<div class="card"> … </div>
<div class="callout tip"> … </div>                    <!-- tip | warn | info | key -->
<div class="bad"> … </div>  <div class="good"> … </div>  <!-- ✗ Avoid / ✓ Prefer -->
<div class="theorem" data-title="Chaining"> … </div>  <!-- definition | theorem | lemma | example | proof (ends with ∎) -->
<div class="note br"> … </div>                        <!-- handwritten sticky note: tl | tr | bl | br; pink | mint | blue -->
<span class="pill">new</span>
```

## `pycourse-academic` slide layouts

It works like the original academic theme: `<!-- _class: lead -->` for the title page, `<!-- _header: Section name -->` per slide for the header bar, and `>` for a footnote.

| Class / syntax | What it does |
| --- | --- |
| `lead` | Title page: left spine, title in the accent colour, `**bold**` words drawn hollow, `###` subtitle, the paragraphs (authors, date) right-aligned |
| `_header: 2. Collisions` | Navy header bar with `§` and a yellow rule (set per slide, as in the original) |
| `> <sup>1</sup> text` | Footnote pinned to the bottom of the slide, with a short LaTeX-style rule above it |
| `toc` | Outline with dot leaders; ordered list of plain-text items, `*page*` at the end |
| `references` | Bibliography; ordered list → `[1]`, `[2]` … |
| `big` | One key statement |
| `invert` | Dark slide |
| `hl-1` … `hl-12` | Spotlight one line of code |
| `![center](img.png)` | Centred image; the next paragraph becomes its caption. Add `frame` for a border |
| tables | Booktabs style: thick top and bottom rules, no grid |
| page number | `N/Total` inside a ring that fills as the deck progresses (recent browsers; elsewhere a plain ring) |

Blocks, Beamer style (`data-title` is optional):

```html
<div class="theorem" data-title="Chaining"> … </div>   <!-- definition | theorem | lemma | corollary | example -->
<div class="block" data-title="Any title"> … </div>    <!-- block | alertblock (red) | exampleblock (green) -->
<div class="proof"> … </div>                           <!-- "Proof." … ∎ -->
<div class="columns"> <div>…</div> <div>…</div> </div> <!-- or columns-3 -->
```

To get the original maroon look back, set `section { --color-highlight: #800000; }` in the deck's `style:`.

Small print: the line spotlight assumes the code block is not shrunk to fit. If a line is too long, Marp scales the block down and the highlight drifts. The blinking cursors only move in HTML, not in PDF.
