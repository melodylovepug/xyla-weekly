# Xyla Weekly 🧸

Short, tappable weekly baby-development packs, in **English and 简体中文**. Static HTML/CSS/vanilla JS, no build step. Hosted on GitHub Pages.

**Rule:** every page ships in both Simplified Chinese and English at the same time.

**Privacy:** this repo is public. First name only, no birth date, addresses, photos, or private links.

## How it works
- `index.html`: home page with a compact 中文 / English toggle (top right, same as week pages). Lists weeks from `weeks/weeks.json`.
- `week-XX.html`: tiny stub page with `<body data-week="week-XX">` (and a small 中文/English toggle in the header).
- `weeks/week-XX.json`: that week's content, both languages side by side.
- `assets/app.js` + `assets/style.css`: shared template and UI labels (both languages) for any week.

Language: the choice is saved in localStorage (`xyla:lang`). With no saved choice, the browser language decides (zh* → 中文, otherwise English).
Checklist and quiz progress are stored by item **position**, so they're shared by both languages. **Keep the `en` and `zh` arrays in the same order and length.**

## Week file shape
```json
{
  "id": "week-05", "emoji": "🌱", "start": "2026-11-01", "end": "2026-11-14",
  "videos": { "YOUTUBE_ID": { "title": "...", "titleZh": "...", "channel": "...", "channelZh": "...", "length": "1:43", "short": false, "lang": "en" } },
  "en": { "title": "Week 5", "age": "...", "dates": "...", "bigThree": [ ... ], "...": "..." },
  "zh": { "title": "第5周", "age": "...", "dates": "...", "bigThree": [ ... ], "...": "..." }
}
```
Cards refer to videos by ID (`"videos": ["YOUTUBE_ID"]`), so both languages use the same videos. In 中文 mode, an English video shows the Chinese title plus a note that it's in English (`"lang": "en"`).

## Add a new week (both languages required)
1. Copy `weeks/week-03.json` → `weeks/week-05.json`. Set `id`, `emoji`, `start`/`end` (`YYYY-MM-DD`).
2. Write the **`en`** block and the **`zh`** block. They must have the same sections, the same number of items in each list, in the same order (checklist, todos, quiz, plays, scripts and their steps, timeline steps, details, watch, sources). Non-text fields (`icon`, `emoji`, `roots`, quiz `a`, `url`, `videos`, `timeline.now`, ruler numbers) should be identical in both.
3. Put videos in the top-level `videos` map with both `title`/`titleZh` and `channel`/`channelZh`.
4. Copy `week-03.html` → `week-05.html`, change `data-week="week-03"` to `data-week="week-05"`.
5. Add an entry to `weeks/weeks.json` with `id`, `file`, `emoji`, `start`, `end`, plus `en` and `zh` objects (`title`, `age`, `dates`, `tagline`). Commit and push. Pages updates in ~1 minute.
6. Check both languages on a phone-width screen (tap 中文 / English at the top).

Chinese style: write the zh block **from the meaning, not sentence by sentence**, the way an experienced mainland mom / 小红书育儿博主 would tell a friend. Short 口语 sentences, native word order, common parenting words (认生、大运动、精细动作、长牙、辅食、手指食物、独立入睡、陪玩、情绪安抚、修复关系、安全感). Avoid translationese (“当…的时候”chains, “进行…”, passive 被, overused “你的”, literal English metaphors). Facts and safety guidance must stay exactly the same as the English. Self-check every line: would a native speaker actually say it this way?

## Content fields (inside `en` / `zh`)
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

Roots (tag keys, always English in JSON; the page shows them translated): `Secure` 安全感, `Curious` 好奇, `Kind` 友善, `Brave` 勇敢, `Self-led` 自主, `Healthy` 健康.

Videos: only real YouTube IDs. Check with
`curl "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=ID&format=json"` (200 = exists and embeddable).
Lite embeds: only a thumbnail loads until tapped.

Strings may contain simple HTML (`<b>`). Use curly quotes ’ “ ” inside text to avoid JSON escaping.

Preview locally: `python3 -m http.server` then open http://localhost:8000.

---
General info, not medical advice; ask your pediatrician. 一般信息，不是医疗建议；请咨询儿科医生。

## Big topics (one-page deep dives)
- Topic pages are stubs like `milk-at-one.html` with `<body data-topic="milk-at-one">`; content lives in `topics/<id>.json` (shared `videos`, `sources`, then `en` and `zh` with identical shape).
- List every topic in `topics/topics.json` (`id, file, emoji, weeks:[...], en:{title,tagline}, zh:{...}`). It shows on the home page under **Big topics / 重点话题**, and on any week listed in `weeks`.
- Topic sections: `bigThree`, `how` (rules), `schedule`, `tips`, `counter`, `quiz`, `watch`, `disagree`, `details`. State is saved per topic in localStorage (`xyla:<id>:oz:<date>`, `xyla:<id>:quiz`).
- **Guide pages** (`"kind": "guide"` in the topic JSON, e.g. `daycare-first-day`) use `buildGuide`: grouped checklists `pack` / `papers` (`items: [{id, text, note?, pre?}]`; `pre` = already done; ticks saved by id in `xyla:<id>:pack` / `:papers`), `plan` (countdown timeline), `about` (editable printable handout; edits in `xyla:<id>:about`; zh view can print the English version for teachers), `scripts` (goodbye, tap to reveal), `normal` + `talk`, `why` (cards with refs).
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

## Weekly rules (added Oct 2026)
- **One bilingual site** (this repo). A separate Chinese site was tried and dropped; `xyla-weekly-zh` now only redirects here with `?lang=zh`. `?lang=en|zh` in any URL sets (and saves) the language.
- **Each language in its own voice.** English for Melody; Chinese natural and warm, readable by the grandparents. Not line-by-line translation. Facts and safety must match.
- When the two languages’ lists differ in length/content, set `"perLang": true` at the top of the week JSON: checklist/quiz progress is then saved per language (`xyla:<id>:<lang>:…`). Weeks 1 and 3 still use shared, same-order lists.
- **One week per page:** exactly 7 days (Week 4 = Oct 18–24, 2026). Never “these two weeks”. Past pages keep their dates (Week 3 = Oct 4–17).
- Order: where she is now (body, brain, feelings, understanding, where it’s heading) → do & don’t with why → what’s next in detail → plays. Secure-first, six roots.
- **Big 3 must be actionable this week:** each with When / How / Say (exact words). Descriptions go in the “Where she is now” cards.
- **Feelings:** describe her real current phase from Melody’s updates and what the next cycle brings; don’t default to “stranger anxiety.”
- **Plays carry over:** review all earlier weeks’ plays; keep those that still fit (mark “(Wk N)” / “(Wk N, harder)”), drop outgrown ones (Ditty Bird, give-and-take, leave-and-come-back peekaboo…) unless there’s a harder version.
- **Space to grow / 给爷爷奶奶的话** (`philosophy.html`, `weeks/philosophy.json`, week-style page listed in `topics/topics.json`): the Montessori / Reggio / RIE-Pikler space-and-independence philosophy. Link it from each new week (add the week id to its `weeks`). Chinese side keeps the warm grandparent tone (您, never preachy).
