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
- Topic sections: `bigThree`, `paths` (picker), `schedule`, `counter`, `quiz`, `watch`, `disagree`, `details`. State is saved per topic in localStorage (`xyla:<id>:path`, `xyla:<id>:oz:<date>`, `xyla:<id>:quiz`).
