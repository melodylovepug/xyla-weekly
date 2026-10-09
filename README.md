# Xyla Weekly 🧸

Short, tappable weekly baby-development packs (instead of long docs). Static HTML/CSS/vanilla JS, no build step. Hosted on GitHub Pages.

**Privacy:** this repo is public. First name only, no birth date, addresses, photos, or private links.

## How it works
- `index.html`: home page, lists weeks from `weeks/weeks.json`.
- `week-XX.html`: tiny stub page with `<body data-week="week-XX">`.
- `weeks/week-XX.json`: all of that week's content.
- `assets/app.js` + `assets/style.css`: shared template that renders any week JSON.

## Add a new week (3 steps)
1. Copy `weeks/week-03.json` → `weeks/week-05.json` and edit the content (set `"id": "week-05"`, `start`/`end` dates as `YYYY-MM-DD`).
2. Copy `week-03.html` → `week-05.html` and change `data-week="week-03"` to `data-week="week-05"`.
3. Add a line to `weeks/weeks.json` (`id`, `file`, `emoji`, `title`, `age`, `dates`, `start`, `end`, `tagline`). Commit and push. Pages updates in ~1 minute.

## Week JSON fields (all optional except id/title)
| Field | What it shows |
|---|---|
| `now` | chips: "Xyla right now" |
| `bigThree` | the 3 big tappable cards: `{icon, title, sub, roots, lines[], videos[]}` |
| `cards` | short topic cards (same shape) |
| `daily` / `todos` | daily checklist (resets each day) / one-time list. Saved in localStorage |
| `quiz` | Do or Don't: `{q, a: "do"|"dont", why}` |
| `plays` | Lucky play pool: `{emoji, name, how, roots[], time}` |
| `scripts` | What to say: `{icon, when, steps:[{do, say}], note}` |
| `timeline` | `{now, steps:[{label, note}], ruler:{min,max,from,to,age,ticks}, footer}` |
| `details` | "More detail" tucked-away cards |
| `watch` | pediatrician red flags |
| `sources` | `{label, url}` |

Roots (tags): `Secure`, `Curious`, `Kind`, `Brave`, `Self-led`, `Healthy`.

Videos: `{id, title, channel, length, short}`. Only use real YouTube IDs. Check with
`curl "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=ID&format=json"` (200 = exists and embeddable).
Videos are lite embeds: only a thumbnail loads until tapped.

Strings may contain simple HTML (`<b>`). Use curly quotes ’ “ ” inside text to avoid JSON escaping.

Preview locally: `python3 -m http.server` then open http://localhost:8000.

---
General info, not medical advice; ask your pediatrician.
