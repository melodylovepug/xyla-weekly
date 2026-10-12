# Xyla Weekly 🧸 (Melody’s English site)

Short, tappable weekly baby-development packs. **English only, for Melody.** Static HTML/CSS/vanilla JS, no build step. Hosted on GitHub Pages.

**Two sites (since Week 4):**
- This repo → https://melodylovepug.github.io/xyla-weekly/ : English only, written for Melody.
- [`xyla-weekly-zh`](https://github.com/melodylovepug/xyla-weekly-zh) → https://melodylovepug.github.io/xyla-weekly-zh/ : Simplified Chinese only, written for the grandparents (not a translation of this site; see its README).
- Both use the same `assets/app.js` + `style.css`. Copy them over unchanged when you change them. `<html data-site-lang="en">` locks the language and hides the toggle; `data-site-title` / `data-site-sub` / `data-site-how` (pipe-separated) override the home texts.

**Privacy:** this repo is public. First name only, no birth date, addresses, photos, daycare details, or private links.

## Weekly content rules (Melody)
- Order: (1) where she is now (body, brain, feelings, what she can/can’t understand, where it’s heading), (2) do & don’t with a why, (3) what’s next in clear detail, (4) exercises and plays. Secure-first, tagged with the six roots.
- **Big 3 must be actionable:** concrete things to do *this week*, each with **When**, **How**, and **Say** (exact words). Descriptions of where she is go in the “Where she is now” cards, not in the Big 3.
- **Feelings:** describe her actual current phase from Melody’s updates (calm/independent vs. clingy dip) and say what the next cycle will bring. Don’t default to “stranger anxiety.”
- **Plays carry over:** every week, review the plays from all earlier weeks. Carry over any that still fit (note “(Wk N)” or “(Wk N, harder)”), and leave out what she has outgrown or mastered (e.g. Ditty Bird cause-and-effect, give-and-take, leave-and-come-back peekaboo) unless there’s a harder version. Do the same in the Chinese site.

## How it works
- `index.html`: home page. Lists weeks from `weeks/weeks.json`.
- `week-XX.html`: tiny stub page with `<body data-week="week-XX">`.
- `weeks/week-XX.json`: that week's content, both languages side by side.
- `assets/app.js` + `assets/style.css`: shared template and UI labels (both languages) for any week.

Checklist and quiz progress are stored by item position.

## Week file shape
```json
{
  "id": "week-05", "emoji": "🌱", "start": "2026-11-01", "end": "2026-11-14",
  "videos": { "YOUTUBE_ID": { "title": "...", "titleZh": "...", "channel": "...", "channelZh": "...", "length": "1:43", "short": false, "lang": "en" } },
  "en": { "title": "Week 5", "age": "...", "dates": "...", "bigThree": [ ... ], "...": "..." }
}
```
Cards refer to videos by ID (`"videos": ["YOUTUBE_ID"]`).

## Add a new week
1. Copy `weeks/week-04.json` → `weeks/week-05.json`. Set `id`, `emoji`, `start`/`end` (`YYYY-MM-DD`). Write the `en` block only.
2. Put videos in the top-level `videos` map (`title`, `channel`, `length`).
3. Copy `week-04.html` → `week-05.html`, change `data-week`.
4. Add an entry to `weeks/weeks.json` (`id, file, emoji, start, end, en:{title, age, dates, tagline}`).
5. Write the grandparents’ Chinese week in `xyla-weekly-zh` too (its own content, see its README). Bump `?v=` in both repos, commit, push.

## Content fields (inside `en`)
| Field | What it shows |
|---|---|
| `oneLiner`, `now` | headline line, "Xyla right now" chips |
| `bigThree` | 3 big tappable cards: `{icon, title, sub, roots, lines[], videos[]}` |
| `cards` | short topic cards (same shape) |
| `daily` / `todos` | daily checklist (resets each day) / one-time list |
| `quiz` | Do or Don't: `{q, a: "do"|"dont", why}` |
| `plays` | Lucky play pool: `{emoji, name, how, roots[], time}` |
| `scripts` | What to say: `{icon, when, steps:[{do, say}], note}` |
| `timeline` | `{now, hint, steps:[{label, note}], ruler:{label,min,max,from,to,age,ticks}, footer}` |
| `details` | "More detail" tucked-away cards |
| `watch` | pediatrician red flags |
| `sources` | `{label, url}` |

Roots (tag keys): `Secure` 安全感, `Curious` 好奇, `Kind` 友善, `Brave` 勇敢, `Self-led` 自主, `Healthy` 健康.

Videos: only real YouTube IDs. Check with
`curl "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=ID&format=json"` (200 = exists and embeddable).
Lite embeds: only a thumbnail loads until tapped.

Strings may contain simple HTML (`<b>`). Use curly quotes ’ “ ” inside text to avoid JSON escaping.

Preview locally: `python3 -m http.server` then open http://localhost:8000.

---
General info, not medical advice; ask your pediatrician.

## Big topics (one-page deep dives)
- Topic pages are stubs like `milk-at-one.html` with `<body data-topic="milk-at-one">`; content lives in `topics/<id>.json` (`videos`, `sources`, then `en`).
- List every topic in `topics/topics.json` (`id, file, emoji, weeks:[...], en:{title,tagline}`). It shows on the home page under **Big topics**, and on any week listed in `weeks`.
- Topic sections: `bigThree`, `how` (rules), `schedule`, `tips`, `counter`, `quiz`, `watch`, `disagree`, `details`. State is saved per topic in localStorage (`xyla:<id>:oz:<date>`, `xyla:<id>:quiz`).
- **Guide pages** (`"kind": "guide"` in the topic JSON, e.g. `daycare-first-day`) use `buildGuide`: grouped checklists `pack` / `papers` (`items: [{id, text, note?, pre?}]`; `pre` = already done; ticks saved by id in `xyla:<id>:pack` / `:papers`), `plan` (countdown timeline), `about` (editable printable handout; edits in `xyla:<id>:about`), `scripts` (goodbye, tap to reveal), `normal` + `talk`, `why` (cards with refs).
- **Privacy on the daycare page:** the repo is public. No daycare name, address, phones, teacher names, start date, hours, fees, door codes or account info — generic words only ("daycare", "teacher", "first day"). `scratch/daycare.py` asserts a list of banned strings before writing the JSON.

## Cache-busting (important after every change to assets/ or data)
Phones cache `assets/app.js` and `style.css` (GitHub Pages sends `max-age=600`). An old cached script running against new data once broke the milk page. When you change `assets/` or any JSON, bump the version on **every** page stub:
`V=$(date +%Y%m%d%H%M); sed -i -E "s#(assets/(style\.css|app\.js))(\?v=[^\"]*)?\"#\1?v=$V\"#g" *.html`
`app.js` reads its own `?v=` and adds it to every data fetch. Each section renders inside `safe()`, so one bad section can't blank the whole page, and saved data is shape-checked before use.

## Video rule (Melody's standing rule)
"Not everything requires a video. Only things I need to understand how to do get a video. Things like 'why' just get a text reference, unless it's super important and from a very high-reputation source."
- **Embed** (`videos`) only for hands-on how-to skills: stairs feet-first, helping her stand, push-walker use, slide safety, safe-sleep setup, choking prevention, cup/straw-cup training, formula→milk mixing, bottle weaning.
- **Text reference** (`refs: [{label, url}]` on a card, shown as "📎 Learn more / 延伸阅读") for why/concept material: explainers, Q&As, talks.
- At most **one** top-tier concept video per page, only if it's central (currently Harvard Center's "5 Steps for Brain-Building Serve and Return").
- Every embedded video must pass the oEmbed check and come from a reputable channel.
