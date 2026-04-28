# Jiayu Zhao — Academic Homepage

Personal academic homepage built with Jekyll.

## Project Structure

```
.
├── _config.yml                    ← Site config: name, bio, email, links, etc.
├── _data/
│   └── navigation.yml             ← Top navigation bar items
├── _includes/                     ← Reusable HTML partials
│   ├── head/custom.html           ← Favicon, MathJax, extra CSS
│   ├── author-profile.html        ← Left sidebar profile card
│   ├── masthead.html              ← Top navigation bar
│   ├── sidebar.html               ← Sidebar wrapper
│   ├── head.html                  ← HTML <head> block
│   ├── seo.html                   ← SEO meta tags
│   ├── analytics.html             ← Google Analytics
│   ├── fetch_google_scholar_stats.html  ← Scholar citation loader
│   ├── scripts.html               ← JS includes
│   └── browser-upgrade.html       ← IE upgrade notice
├── _layouts/
│   └── default.html               ← Main page layout
├── _pages/
│   └── about.md                   ← ★ Main homepage content (edit here)
├── _sass/                         ← SCSS source files
│   ├── _variables.scss            ← Colors, fonts, breakpoints
│   ├── _sidebar.scss              ← Sidebar layout/style
│   ├── _masthead.scss             ← Nav bar style
│   ├── _page.scss                 ← Main content area style
│   └── ...                        ← Other partials + vendor libs
├── assets/
│   ├── css/
│   │   ├── main.scss              ← SCSS entry point (imports _sass/*)
│   │   └── academicons.min.css    ← Academic icon font CSS
│   ├── fonts/                     ← Icon font files (FA + Academicons)
│   └── js/
│       ├── main.min.js            ← Compiled JS bundle (do not edit)
│       ├── plugins/               ← jQuery plugins used by main.min.js
│       └── vendor/jquery/         ← jQuery library
├── files/
│   └── Jiayu_Zhao_CV.pdf          ← [UPLOAD] Your CV PDF
├── images/
│   ├── avatar.jpg                 ← [UPLOAD] Your profile photo
│   └── favicon*.png / *.ico       ← Site favicons
├── google_scholar_crawler/        ← GitHub Actions Scholar stats bot
│   ├── main.py
│   └── requirements.txt
├── .github/workflows/
│   └── google_scholar_crawler.yaml  ← Daily cron: fetches citation counts
├── cv.tex                         ← LaTeX source of your CV
├── Gemfile                        ← Ruby gem dependencies
└── run_server.sh                  ← Local dev: runs `bundle exec jekyll serve`
```

## Quick Start

```bash
# Install dependencies (once)
bundle install

# Start local dev server
bash run_server.sh
# or: bundle exec jekyll serve --livereload
```

Open `http://localhost:4000` in your browser.

## Common Edits

| What to change | Where |
|---|---|
| Name, bio, email, phone, links | `_config.yml` → `author:` section |
| Navigation items | `_data/navigation.yml` |
| Homepage content (About, Research, Publications…) | `_pages/about.md` |
| Sidebar profile card | `_includes/author-profile.html` |
| Color scheme / fonts | `_sass/_variables.scss` |
| Custom CSS overrides | `_sass/_page.scss` or `assets/css/main.scss` |
| Profile photo | `images/avatar.jpg` |
| CV PDF download | `files/Jiayu_Zhao_CV.pdf` |
| Google Analytics ID | `_config.yml` → `google_analytics_id` |
| Google Scholar ID (for citation counts) | GitHub repo secret `GOOGLE_SCHOLAR_ID` |

## Placeholders to Fill In

- [ ] `_config.yml`: Replace `YOUR_GOOGLE_SCHOLAR_ID` with actual Scholar profile URL
- [ ] `images/avatar.jpg`: Upload your profile photo
- [ ] `files/Jiayu_Zhao_CV.pdf`: Upload your CV PDF
- [ ] `_pages/about.md`: Update GitHub and Google Scholar links in Contact section
