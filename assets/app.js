/* Xyla Weekly: shared renderer (English + 简体中文).
   Each week page sets <body data-week="week-03">, each topic page <body data-topic="milk-at-one">; this file loads weeks/<id>.json or topics/<id>.json, which holds
   shared fields (id, start, end, videos) plus "en" and "zh" content side by side. No build step. */
(function () {
  'use strict';
  var ROOTS = ['Secure', 'Curious', 'Kind', 'Brave', 'Self-led', 'Healthy'];
  var ROOT_ICON = { Secure: '🫶', Curious: '🔍', Kind: '💞', Brave: '🦁', 'Self-led': '🧭', Healthy: '🌱' };
  var LANG_KEY = 'xyla:lang';
  /* Cache-busting: the page stubs load this file as app.js?v=<version>; data files get the same ?v=. */
  var VER = (function () { try { var m = /[?&]v=([^&#]+)/.exec((document.currentScript && document.currentScript.src) || ''); return m ? m[1] : String(Date.now()); } catch (e) { return String(Date.now()); } })();

  var T = {
    en: {
      htmlLang: 'en', roots: { Secure: 'Secure', Curious: 'Curious', Kind: 'Kind', Brave: 'Brave', 'Self-led': 'Self-led', Healthy: 'Healthy' },
      allWeeks: '← All weeks', nowTitle: 'Xyla right now', nowSub: function (n) { return n + ' things she’s doing · tap to see'; },
      big3: '⭐ This week’s 3 big things', big3Hint: 'Tap a card. 30 seconds each.',
      topics: '💬 Your questions this week', topicsHint: 'Short answers to things you asked about.',
      next: '🗺️ What’s next', hereBadge: 'Xyla is here', rulerLegend: function (a) { return 'Xyla (~' + a + ' mo) · green = normal range for walking alone'; }, mo: 'mo',
      today: '✅ Today’s checklist', todayHint: 'Saved on this phone. Resets every day. Small wins count.',
      tabDaily: 'Every day', tabOnce: 'Once this week', ofToday: function (d, n) { return d + ' of ' + n + ' today'; }, ofDone: function (d, n) { return d + ' of ' + n + ' done'; }, allDone: ' 🎉 Amazing.',
      quiz: '🤔 Do or Don’t?', quizHint: 'Guess first, then see why.', score: 'Score', reset: 'Reset', doBtn: '✅ Do', dontBtn: '❌ Don’t',
      right: '👍 Right! ', wrong: '🙂 Not quite. ', DO: '✅ DO', DONT: '❌ DON’T',
      play: '🎲 Lucky play', playHint: 'Not sure what to do? Tap the button. Filter by root if you like.', lucky: '🎲 Pick a play for us!', all: 'All', seeAll: 'See all plays', ideas: function (n) { return n + ' ideas'; },
      scripts: '🗣️ What to say', scriptsHint: 'Tap a moment to reveal the exact words.',
      more: '📚 More detail (optional)', moreHint: 'Only if you want it. Everything is tucked away.',
      watch: '🩺 Call or ask the pediatrician if…', watchFoot: 'Gut feeling something’s off? It’s always okay to ask.',
      videos: '🎬 All videos this week', videosHint: function (n) { return n + ' short videos from reputable channels. Tap to play.'; }, showAll: function (n) { return 'Show all ' + n + ' videos'; },
      openYT: 'Open in YouTube ↗', short: 'Short', enOnly: '', playVideo: 'Play video: ',
      sources: 'Sources', sourcesSub: 'Research and guidelines behind this page', sourcesNote: '',
      footer: 'General info, not medical advice; ask your pediatrician.', made: 'Made with love for Xyla 💛',
      nav: { big3: '⭐ Big 3', topics: '💬 Questions', today: '✅ Today', quiz: '🤔 Quiz', play: '🎲 Play', scripts: '🗣️ Say', next: '🗺️ Next', more: '📚 More', watch: '🩺 Doctor' },
      homeSub: 'Short, tappable weekly packs. The most important things first.', weeks: '📅 Weeks', thisWeek: 'This week',
      howTitle: 'How to use this', how: ['Open this week → read the <b>3 big things</b> (2 minutes).', 'Tick the <b>daily checklist</b> (saved on your phone).', 'Stuck? Hit <b>🎲 Lucky play</b>.'],
      chooseLang: 'Language / 语言', loadFail: 'Couldn’t load this page', retry: 'Try refreshing.', pageTitle: 'Xyla Weekly',
      home: '← Home', refs: '📎 Learn more: ', bigTopics: '📌 Big topics', bigTopicsHint: 'One page per big question. Read once, come back as needed.', weekTopic: '📌 Big topic this week', topicVideos: '🎬 Videos on this topic',
      tnav: { big3: '⭐ Big 3', how: '🔁 Rules', plan: '📅 4 weeks', tips: '🧊 Tips', count: '🥛 Count', quiz: '🤔 Quiz', watch: '🚩 Red flags', disagree: '⚖️ Debates', more: '📚 More' }, big3T: '⭐ 3 big things', stepsT: 'Step by step', tipT: 'Tip: '
    },
    zh: {
      htmlLang: 'zh-Hans', roots: { Secure: '安全感', Curious: '好奇心', Kind: '友爱', Brave: '勇敢', 'Self-led': '自主', Healthy: '健康' },
      allWeeks: '← 全部', nowTitle: 'Xyla 最近', nowSub: function (n) { return '最近会的 ' + n + ' 件事，点开看'; },
      big3: '⭐ 这周最重要的 3 件事', big3Hint: '点开看，一张半分钟。',
      topics: '💬 你最近问的', topicsHint: '挑重点，简单说。',
      next: '🗺️ 接下来会怎样', hereBadge: '现在在这', rulerLegend: function (a) { return 'Xyla（约 ' + a + ' 个月）· 绿色是独立走路的正常范围'; }, mo: '月',
      today: '✅ 今天的小目标', todayHint: '存在这台手机里，每天自动清空。做到一点也算赢。',
      tabDaily: '每天', tabOnce: '这周做一次', ofToday: function (d, n) { return '今天完成 ' + d + '/' + n; }, ofDone: function (d, n) { return '已完成 ' + d + '/' + n; }, allDone: ' 🎉 全部搞定！',
      quiz: '🤔 这样做对吗？', quizHint: '先猜一猜，再看原因。', score: '答对', reset: '重来', doBtn: '✅ 可以', dontBtn: '❌ 别这样',
      right: '👍 答对啦！', wrong: '🙂 差一点～', DO: '✅ 可以', DONT: '❌ 别这样',
      play: '🎲 今天玩什么', playHint: '没主意？点一下随机抽一个，也可以按方向筛选。', lucky: '🎲 随机抽一个游戏！', all: '全部', seeAll: '全部游戏', ideas: function (n) { return '共 ' + n + ' 个'; },
      scripts: '🗣️ 这时候怎么说', scriptsHint: '点开场景，直接照着说。',
      more: '📚 想多了解再看', moreHint: '都折起来了，想看再点。',
      watch: '🩺 有这些情况，问问儿科医生', watchFoot: '总觉得哪里不对劲？随时问，不用不好意思。',
      videos: '🎬 这周的视频', videosHint: function (n) { return '共 ' + n + ' 个，都来自靠谱的频道，点一下就能看。视频是英文的，可以在 YouTube 里打开字幕，选“自动翻译 → 中文（简体）”。'; }, showAll: function (n) { return '展开全部 ' + n + ' 个视频'; },
      openYT: '去 YouTube 看 ↗', short: '短视频', enOnly: '英文', playVideo: '播放：', origTitle: '原标题：',
      sources: '参考资料', sourcesSub: '这页内容的出处', sourcesNote: '链接都是英文网站。',
      footer: '以上是一般育儿信息，不是医疗建议，具体请问儿科医生。', made: '给 Xyla 的，满满都是爱 💛',
      nav: { big3: '⭐ 3件事', topics: '💬 问答', today: '✅ 今天', quiz: '🤔 测一测', play: '🎲 玩什么', scripts: '🗣️ 怎么说', next: '🗺️ 接下来', more: '📚 更多', watch: '🩺 就医' },
      homeSub: '每周一份，点开就看，重要的先说。', weeks: '📅 每周内容', thisWeek: '本周',
      howTitle: '怎么用', how: ['打开本周，先看<b>最重要的 3 件事</b>，两分钟搞定。', '每天勾一勾<b>今天的小目标</b>，进度存在手机里。', '不知道玩什么？点<b>🎲 随机抽一个</b>。'],
      chooseLang: 'Language / 语言', loadFail: '页面没加载出来', retry: '刷新一下试试。', pageTitle: 'Xyla 成长周记',
      home: '← 首页', refs: '📎 延伸阅读：', bigTopics: '📌 重点话题', bigTopicsHint: '大问题单独整理成一页，看一遍，需要时再回来翻。', weekTopic: '📌 这周的重点话题', topicVideos: '🎬 相关视频',
      tnav: { big3: '⭐ 3件事', how: '🔁 规矩', plan: '📅 4周计划', tips: '🧊 贴士', count: '🥛 记奶量', quiz: '🤔 测一测', watch: '🚩 警惕', disagree: '⚖️ 分歧', more: '📚 更多' }, big3T: '⭐ 最重要的 3 件事', stepsT: '一步一步来', tipT: '小提示：'
    }
  };

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    if (attrs) for (var k in attrs) { if (k === 'class') e.className = attrs[k]; else e.setAttribute(k, attrs[k]); }
    if (html != null) e.innerHTML = html;
    return e;
  }
  function store(key, val) {
    try {
      if (val === undefined) { var v = localStorage.getItem(key); return v ? JSON.parse(v) : null; }
      localStorage.setItem(key, JSON.stringify(val));
    } catch (e) { return null; }
  }
  /* Defensive readers: old or corrupted saved data is ignored instead of crashing the page. */
  function storeArr(key) { var v = store(key); return Array.isArray(v) ? v.filter(function (x) { return typeof x === 'number' && isFinite(x); }) : []; }
  function storeObj(key) { var v = store(key); return v && typeof v === 'object' && !Array.isArray(v) ? v : {}; }
  function arr(x) { return Array.isArray(x) ? x : []; }
  function localISO(d) { d = d || new Date(); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }

  /* ---------- language ---------- */
  function detectLang() {
    var q = (location.search.match(/[?&]lang=(en|zh)\b/) || [])[1];
    if (q) { store(LANG_KEY, q); return q; }
    var saved = store(LANG_KEY);
    if (saved == null) { try { saved = localStorage.getItem(LANG_KEY); } catch (e) {} } // tolerate a raw, non-JSON value
    if (saved === 'en' || saved === 'zh') return saved;
    var langs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || 'en'];
    return /^zh/i.test(langs[0] || '') ? 'zh' : 'en';
  }
  var lang = detectLang(), t = T[lang], DATA = null, VIDEOS = {};
  // Single-language sites: <html data-site-lang="en|zh"> locks the language and hides the toggle.
  var HTML = document.documentElement, SITE = HTML.getAttribute('data-site-lang');
  if (SITE === 'en' || SITE === 'zh') { lang = SITE; t = T[lang]; } else SITE = null;
  (function siteText() {
    var a = HTML.getAttribute('data-site-title'), b = HTML.getAttribute('data-site-sub'), c = HTML.getAttribute('data-site-how');
    if (a) t.pageTitle = a; if (b) t.homeSub = b; if (c) t.how = c.split('|');
  })();
  function setLang(l) {
    if (SITE || (l !== 'en' && l !== 'zh')) return;
    store(LANG_KEY, l); lang = l; t = T[l];
    var y = window.scrollY; render(); window.scrollTo(0, y);
  }
  function langToggleHTML(big) {
    if (SITE) return '';
    return '<div class="lang' + (big ? ' big' : '') + '" role="group" aria-label="Language / 语言">' +
      '<button type="button" data-lang="zh" aria-pressed="' + (lang === 'zh') + '" lang="zh-Hans">中文</button>' +
      '<button type="button" data-lang="en" aria-pressed="' + (lang === 'en') + '" lang="en">English</button></div>';
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('[data-lang]');
    if (b) setLang(b.getAttribute('data-lang'));
  });

  function rootName(r) { return t.roots[r] || r; }
  function tagsHTML(roots) { return roots && roots.length ? '<div class="tags">' + roots.map(function (r) { return '<span class="tag ' + esc(r) + '">' + (ROOT_ICON[r] || '') + ' ' + esc(rootName(r)) + '</span>'; }).join('') + '</div>' : ''; }

  /* ---------- lite YouTube embed ---------- */
  function videoHTML(id) {
    var v = VIDEOS[id]; if (!v) return '';
    var zh = lang === 'zh';
    var title = zh && v.titleZh ? v.titleZh : v.title, channel = zh && v.channelZh ? v.channelZh : v.channel;
    var thumb = 'https://i.ytimg.com/vi/' + encodeURIComponent(id) + '/hqdefault.jpg';
    var url = (v.short ? 'https://www.youtube.com/shorts/' : 'https://www.youtube.com/watch?v=') + encodeURIComponent(id);
    var meta = [channel]; if (v.length) meta.push(v.length); if (v.short) meta.push(t.short); if (zh && v.lang === 'en') meta.push(t.enOnly);
    return '<button class="yt" type="button" data-yt="' + esc(id) + '" style="background-image:url(' + thumb + ')" aria-label="' + esc(t.playVideo + title) + '">' +
      '<span class="play"></span><span class="cap"><b>▶ ' + esc(title) + '</b>' + esc(meta.join(' · ')) + '</span></button>' +
      '<a class="ytlink" href="' + url + '" target="_blank" rel="noopener">' + t.openYT + '</a>' +
      (zh && v.lang === 'en' ? '<span class="ytlink"> · ' + t.origTitle + esc(v.title) + '</span>' : '');
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('button.yt');
    if (!b || b.querySelector('iframe')) return;
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(b.getAttribute('data-yt')) + '?autoplay=1&playsinline=1&rel=0' + (lang === 'zh' ? '&hl=zh-CN&cc_lang_pref=zh-Hans' : '');
    f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';
    f.allowFullscreen = true;
    f.title = b.getAttribute('aria-label') || 'YouTube';
    b.innerHTML = ''; b.style.backgroundImage = 'none'; b.appendChild(f);
  });

  function linesHTML(lines) { return lines && lines.length ? '<ul class="lines">' + lines.map(function (l) { return '<li>' + l + '</li>'; }).join('') + '</ul>' : ''; }
  function refsHTML(refs) {
    refs = Array.isArray(refs) ? refs.filter(function (r) { return r && r.url; }) : [];
    return refs.length ? '<p class="refs">' + t.refs + refs.map(function (r) { return '<a href="' + esc(r.url) + '" target="_blank" rel="noopener">' + esc(r.label || r.url) + '</a>'; }).join(' · ') + '</p>' : '';
  }
  function cardHTML(c, numbered, i) {
    return '<details class="card"><summary>' + (numbered ? '<span class="num">' + (i + 1) + '</span>' : '') +
      '<span class="ico">' + esc(c.icon || '•') + '</span><span class="t">' + esc(c.title) + (c.sub ? '<small>' + esc(c.sub) + '</small>' : '') + '</span></summary>' +
      '<div class="body">' + tagsHTML(c.roots) + linesHTML(c.lines) + (c.html || '') + (c.videos || []).map(videoHTML).join('') + refsHTML(c.refs) + '</div></details>';
  }
  function section(id, title, hint) {
    var s = el('section', { id: id });
    s.appendChild(el('h2', null, title));
    if (hint) s.appendChild(el('p', { class: 'hint' }, hint));
    return s;
  }

  /* ---------- week sections ---------- */
  function renderHero(w, root) {
    var h = el('header', { class: 'hero' });
    h.innerHTML = '<div class="toprow"><a class="back" href="./">' + t.allWeeks + '</a>' + langToggleHTML(false) + '</div>' +
      '<h1>' + esc(w.emoji || '') + ' ' + esc(w.title) + '</h1>' +
      '<p class="sub">' + esc(w.age) + ' · ' + esc(w.dates) + '</p>' +
      (w.oneLiner ? '<p style="margin:10px 0 0">' + w.oneLiner + '</p>' : '') +
      (w.now && w.now.length ? '<details class="card" style="margin-top:14px"><summary><span class="ico">👶</span><span class="t">' + t.nowTitle + ' <small>' + esc(t.nowSub(w.now.length)) + '</small></span></summary><div class="body"><ul class="chips" style="margin:0">' + w.now.map(function (n) { return '<li>' + esc(n) + '</li>'; }).join('') + '</ul></div></details>' : '');
    root.appendChild(h);
  }
  function renderNav(root, ids, labels) {
    labels = labels || t.nav;
    var n = el('nav', { class: 'jump', 'aria-label': 'Jump' });
    n.innerHTML = ids.map(function (x) { return '<a href="#' + x + '">' + labels[x] + '</a>'; }).join('');
    root.appendChild(n);
  }
  function renderBig3(w, root) {
    if (!w.bigThree || !w.bigThree.length) return;
    var s = section('big3', t.big3, t.big3Hint); s.className = 'big3';
    s.insertAdjacentHTML('beforeend', w.bigThree.map(function (c, i) { return cardHTML(c, true, i); }).join(''));
    root.appendChild(s);
  }
  function renderCards(w, root) {
    if (!w.cards || !w.cards.length) return;
    var s = section('topics', t.topics, t.topicsHint);
    s.insertAdjacentHTML('beforeend', w.cards.map(function (c) { return cardHTML(c); }).join(''));
    root.appendChild(s);
  }
  function renderTimeline(w, root) {
    var tl = w.timeline; if (!tl) return;
    var s = section('next', t.next, tl.hint || '');
    var html = '<div class="card" style="padding:14px 16px"><ul class="tl">' + tl.steps.map(function (st, i) {
      var cls = i < tl.now ? 'past' : (i === tl.now ? 'now' : '');
      return '<li class="' + cls + '"><span class="dot"></span><b>' + esc(st.label) + (i === tl.now ? '<span class="here">' + t.hereBadge + '</span>' : '') + '</b><span>' + esc(st.note || '') + '</span></li>';
    }).join('') + '</ul>';
    if (tl.ruler) {
      var r = tl.ruler, span = r.max - r.min, pct = function (m) { return ((m - r.min) / span * 100).toFixed(1) + '%'; };
      html += '<p class="small" style="margin:6px 0 0">' + esc(r.label) + '</p><div class="ruler" aria-hidden="true">' +
        '<div class="bar" style="left:' + pct(r.from) + ';width:calc(' + pct(r.to) + ' - ' + pct(r.from) + ')"></div>' +
        '<div class="mark" style="left:' + pct(r.age) + '"></div>' +
        r.ticks.map(function (m) { return '<span class="lab" style="left:' + pct(m) + '">' + m + ' ' + t.mo + '</span>'; }).join('') + '</div>' +
        '<p class="small" style="margin:6px 0 0"><span style="color:var(--accent)">▍</span> ' + esc(t.rulerLegend(r.age)) + '</p>';
    }
    html += (tl.footer ? '<p class="small">' + tl.footer + '</p>' : '') + '</div>';
    s.insertAdjacentHTML('beforeend', html);
    root.appendChild(s);
  }

  /* Checklist + quiz state is stored by item index, so it is shared by both languages. */
  var checkTab = 'd';
  function renderChecklist(w, root) {
    if (!w.daily) return;
    var s = section('today', t.today, t.todayHint);
    var today = localISO();
    var key = function (d) { return 'xyla:' + (w.pid || w.id) + ':daily:' + d; };
    var todoKey = 'xyla:' + (w.pid || w.id) + ':todo';
    var box = el('div');
    box.innerHTML = '<div class="tabs" role="tablist"><button role="tab" aria-selected="' + (checkTab === 'd') + '" data-tab="d">' + t.tabDaily + '</button>' +
      (w.todos ? '<button role="tab" aria-selected="' + (checkTab === 't') + '" data-tab="t">' + t.tabOnce + '</button>' : '') + '</div>' +
      '<div class="progress"><i></i></div><p class="small pl"></p><div class="card" id="cl"></div><div class="days"></div>';
    s.appendChild(box); root.appendChild(s);
    function list() { return checkTab === 'd' ? w.daily : w.todos; }
    function getDone() { return checkTab === 'd' ? storeArr(key(today)) : storeArr(todoKey); }
    function draw() {
      var done = getDone(), items = list();
      box.querySelector('#cl').innerHTML = items.map(function (it, i) {
        var on = done.indexOf(i) > -1;
        return '<label class="check' + (on ? ' done' : '') + '"><input type="checkbox" data-i="' + i + '"' + (on ? ' checked' : '') + '><span>' + esc(it) + '</span></label>';
      }).join('');
      var n = done.filter(function (i) { return i < items.length; }).length;
      var pct = items.length ? Math.round(n / items.length * 100) : 0;
      box.querySelector('.progress i').style.width = pct + '%';
      box.querySelector('.pl').textContent = (checkTab === 'd' ? t.ofToday(n, items.length) : t.ofDone(n, items.length)) + (pct === 100 ? t.allDone : '');
      var days = box.querySelector('.days');
      if (checkTab === 'd' && DATA.start && DATA.end) {
        var d = new Date(DATA.start + 'T12:00:00'), end = new Date(DATA.end + 'T12:00:00'), out = '';
        while (d <= end) {
          var iso = localISO(d), c = storeArr(key(iso)).length, f = c / w.daily.length;
          var bg = c ? 'rgba(47,158,107,' + (0.25 + 0.75 * f).toFixed(2) + ')' : '';
          out += '<span class="day' + (iso === today ? ' today' : '') + '" title="' + iso + ': ' + c + '" style="' + (bg ? 'background:' + bg + ';color:#fff' : '') + '">' + d.getDate() + '</span>';
          d.setDate(d.getDate() + 1);
        }
        days.innerHTML = out; days.style.display = '';
      } else days.style.display = 'none';
    }
    box.addEventListener('change', function (e) {
      if (!e.target.matches('input[type=checkbox]')) return;
      var done = getDone(), i = +e.target.getAttribute('data-i'), at = done.indexOf(i);
      if (e.target.checked && at < 0) done.push(i); else if (!e.target.checked && at > -1) done.splice(at, 1);
      store(checkTab === 'd' ? key(today) : todoKey, done); draw();
    });
    box.addEventListener('click', function (e) {
      var b = e.target.closest('[data-tab]'); if (!b) return;
      checkTab = b.getAttribute('data-tab');
      box.querySelectorAll('[data-tab]').forEach(function (x) { x.setAttribute('aria-selected', x === b); });
      draw();
    });
    draw();
  }

  function renderQuiz(w, root) {
    if (!w.quiz || !w.quiz.length) return;
    var qKey = 'xyla:' + (w.pid || w.id) + ':quiz';
    var s = section('quiz', t.quiz, t.quizHint);
    s.insertAdjacentHTML('beforeend', '<p class="score">' + t.score + ': <span class="sc">0</span> / ' + w.quiz.length + ' <button type="button" class="reset">' + t.reset + '</button></p>');
    var g = el('div', { class: 'qgrid' });
    g.innerHTML = w.quiz.map(function (q, i) {
      return '<div class="q" data-i="' + i + '"><div class="qq">' + esc(q.q) + '</div><div class="btns"><button type="button" data-g="do">' + t.doBtn + '</button><button type="button" data-g="dont">' + t.dontBtn + '</button></div>' +
        '<div class="ans"><div class="verdict"></div><div>' + q.why + '</div></div></div>';
    }).join('');
    s.appendChild(g); root.appendChild(s);
    function apply() {
      var st = storeObj(qKey), score = 0;
      g.querySelectorAll('.q').forEach(function (card) {
        var i = card.getAttribute('data-i'), q = w.quiz[+i], guess = st[i];
        card.classList.remove('flipped', 'right', 'wrong');
        if (!q || (guess !== 'do' && guess !== 'dont')) return;
        var ok = guess === q.a; if (ok) score++;
        card.classList.add('flipped', ok ? 'right' : 'wrong');
        card.querySelector('.verdict').textContent = (ok ? t.right : t.wrong) + (q.a === 'do' ? t.DO : t.DONT);
      });
      s.querySelector('.sc').textContent = score;
    }
    g.addEventListener('click', function (e) {
      var b = e.target.closest('[data-g]'); if (!b) return;
      var st = storeObj(qKey); st[b.closest('.q').getAttribute('data-i')] = b.getAttribute('data-g');
      store(qKey, st); apply();
    });
    s.querySelector('.reset').addEventListener('click', function () { store(qKey, {}); apply(); });
    apply();
  }

  function renderPlay(w, root) {
    if (!w.plays) return;
    var s = section('play', t.play, t.playHint);
    var filter = null, last = -1;
    s.insertAdjacentHTML('beforeend', '<button type="button" class="lucky-btn">' + t.lucky + '</button><div class="lucky-out" aria-live="polite"></div>' +
      '<div class="filters"><button type="button" aria-pressed="true" data-r="">' + t.all + '</button>' + ROOTS.map(function (r) { return '<button type="button" aria-pressed="false" data-r="' + r + '">' + ROOT_ICON[r] + ' ' + esc(rootName(r)) + '</button>'; }).join('') + '</div>' +
      '<details class="card"><summary><span class="ico">📋</span><span class="t">' + t.seeAll + ' <small class="cnt"></small></span></summary><div class="body plist" style="padding:0"></div></details>');
    root.appendChild(s);
    function pool() { return w.plays.map(function (p, i) { return i; }).filter(function (i) { return !filter || (w.plays[i].roots || []).indexOf(filter) > -1; }); }
    function drawList() {
      var p = pool();
      s.querySelector('.cnt').textContent = t.ideas(p.length) + (filter ? ' · ' + rootName(filter) : '');
      s.querySelector('.plist').innerHTML = p.map(function (i) { var x = w.plays[i]; return '<div class="play"><b>' + esc((x.emoji || '') + ' ' + x.name) + '</b><p>' + x.how + '</p>' + tagsHTML(x.roots) + '</div>'; }).join('');
    }
    s.querySelector('.lucky-btn').addEventListener('click', function () {
      var p = pool(); if (!p.length) return;
      var i = p[Math.floor(Math.random() * p.length)];
      if (p.length > 1) while (i === last) i = p[Math.floor(Math.random() * p.length)];
      last = i; var x = w.plays[i];
      s.querySelector('.lucky-out').innerHTML = '<div class="lucky-card"><h3>' + esc(x.emoji || '✨') + ' ' + esc(x.name) + '</h3><p style="margin:4px 0">' + x.how + '</p>' + tagsHTML(x.roots) + (x.time ? '<p class="small">⏱ ' + esc(x.time) + '</p>' : '') + '</div>';
    });
    s.querySelector('.filters').addEventListener('click', function (e) {
      var b = e.target.closest('[data-r]'); if (!b) return;
      filter = b.getAttribute('data-r') || null;
      s.querySelectorAll('.filters button').forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
      drawList();
    });
    drawList();
  }

  function renderScripts(w, root) {
    if (!w.scripts) return;
    var s = section('scripts', t.scripts, t.scriptsHint);
    s.insertAdjacentHTML('beforeend', w.scripts.map(function (sc) {
      return '<details class="card"><summary><span class="ico">' + esc(sc.icon || '💬') + '</span><span class="t">' + esc(sc.when) + '</span></summary><div class="body">' +
        sc.steps.map(function (st, i) {
          return '<div class="step"><span class="n">' + (i + 1) + '</span><div class="c">' + (st.do ? esc(st.do) : '') + (st.say ? '<span class="say">“' + esc(st.say) + '”</span>' : '') + '</div></div>';
        }).join('') + (sc.note ? '<p class="small">' + sc.note + '</p>' : '') + arr(sc.videos).map(videoHTML).join('') + '</div></details>';
    }).join(''));
    root.appendChild(s);
  }
  function renderDetails(w, root) {
    if (!w.details || !w.details.length) return;
    var s = section('more', t.more, t.moreHint);
    s.insertAdjacentHTML('beforeend', w.details.map(function (c) { return cardHTML(c); }).join(''));
    root.appendChild(s);
  }
  function renderWatch(w, root) {
    if (!w.watch || !w.watch.length) return;
    var s = section('watch', t.watch, '');
    s.insertAdjacentHTML('beforeend', '<div class="callout"><ul>' + w.watch.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul><p class="small" style="margin:6px 0 0">' + t.watchFoot + '</p></div>');
    root.appendChild(s);
  }
  function renderVideos(w, root, title) {
    var seen = {}, all = [];
    (w.bigThree || []).concat(w.cards || [], w.details || []).forEach(function (c) { (c.videos || []).forEach(function (id) { if (!seen[id]) { seen[id] = 1; all.push(id); } }); });
    Object.keys(VIDEOS).forEach(function (id) { if (!seen[id]) { seen[id] = 1; all.push(id); } });
    if (!all.length) return;
    var s = section('videos', title || t.videos, t.videosHint(all.length));
    s.insertAdjacentHTML('beforeend', '<details class="card"><summary><span class="ico">🎬</span><span class="t">' + t.showAll(all.length) + '</span></summary><div class="body">' + all.map(videoHTML).join('') + '</div></details>');
    root.appendChild(s);
  }
  function renderSources(w, root) {
    if (!w.sources || !w.sources.length) return;
    var s = el('section', { id: 'sources' });
    s.innerHTML = '<details class="card"><summary><span class="ico">🔗</span><span class="t">' + t.sources + ' <small>' + t.sourcesSub + '</small></span></summary><div class="body">' + (t.sourcesNote ? '<p class="small">' + t.sourcesNote + '</p>' : '') + '<ul class="sources">' +
      w.sources.map(function (x) { return '<li><a href="' + esc(x.url) + '" target="_blank" rel="noopener">' + esc(x.label) + '</a></li>'; }).join('') + '</ul></div></details>';
    root.appendChild(s);
  }
  /* Run one section; if it throws, log it and keep rendering the rest of the page. */
  function safe(fn) {
    var args = Array.prototype.slice.call(arguments, 1);
    try { fn.apply(null, args); } catch (e) { if (window.console) console.warn('Section skipped:', fn.name, e); }
  }
  function footer(root) {
    root.insertAdjacentHTML('beforeend', '<footer><strong>' + t.footer + '</strong><br>' + t.made + '</footer>');
  }

  /* ---------- big topics ---------- */
  function topicCardsHTML(list) {
    return list.map(function (x) {
      var c = x[lang] || x.en;
      return '<a class="card" href="' + esc(x.file) + '"><span class="e">' + esc(x.emoji || '📌') + '</span><div><b>' + esc(c.title) + '</b><span>' + esc(c.tagline || '') + '</span></div></a>';
    }).join('');
  }
  function renderWeekTopics(w, root) {
    var list = TOPICS.filter(function (x) { return (x.weeks || []).indexOf(w.id) > -1; });
    if (!list.length) return;
    var s = section('bigtopic', t.weekTopic, ''); s.className = 'weeks';
    s.insertAdjacentHTML('beforeend', topicCardsHTML(list));
    root.appendChild(s);
  }
  function renderHow(w, root) {
    var p = w.how, L = w.labels || {}; if (!p || !Array.isArray(p.steps)) return;
    var s = section('how', L.howT, L.howHint);
    s.insertAdjacentHTML('beforeend', '<div class="card pcard"><p class="pintro">🍼 ' + p.intro + '</p>' +
      p.steps.map(function (st, i) { return '<div class="step"><span class="n">' + (i + 1) + '</span><div class="c">' + st + '</div></div>'; }).join('') +
      (p.tip ? '<p class="ptip">💡 ' + t.tipT + p.tip + '</p>' : '') + (p.videos || []).map(videoHTML).join('') + '</div>');
    root.appendChild(s);
  }
  function renderTips(w, root) {
    if (!w.tips || !w.tips.length) return;
    var s = section('tips', w.labels.tipsT, w.labels.tipsHint);
    s.insertAdjacentHTML('beforeend', w.tips.map(function (c) { return cardHTML(c); }).join(''));
    root.appendChild(s);
  }
  function renderSchedule(w, root) {
    var sc = w.schedule, L = w.labels;
    var s = section('plan', L.planT, L.planHint);
    s.insertAdjacentHTML('beforeend', '<div class="card" style="padding:14px 16px"><ul class="tl sched">' + sc.steps.map(function (st, i) {
      return '<li class="' + (i === 0 ? 'now' : '') + '"><span class="dot"></span><b>' + esc(st.t) + '</b><ul>' + st.lines.map(function (l) { return '<li>' + l + '</li>'; }).join('') + '</ul></li>';
    }).join('') + '</ul>' + (sc.note ? '<p class="small" style="margin:0">' + sc.note + '</p>' : '') + '</div>' +
      ((sc.videos || []).length ? '<details class="card"><summary><span class="ico">🎬</span><span class="t">' + t.showAll(sc.videos.length) + '</span></summary><div class="body">' + sc.videos.map(videoHTML).join('') + '</div></details>' : ''));
    root.appendChild(s);
  }
  function renderCounter(w, id, root) {
    var C = w.counter, L = w.labels, MAX = 32;
    var key = 'xyla:' + id + ':oz:' + localISO();
    var s = section('count', L.countT, L.countHint);
    s.insertAdjacentHTML('beforeend', '<div class="card counter"><div class="cbig"><span class="cnum"></span><span class="csub"></span></div>' +
      '<div class="cbar"><i></i><span class="m" style="left:' + (16 / MAX * 100) + '%"></span><span class="m over" style="left:' + (24 / MAX * 100) + '%"></span></div>' +
      '<p class="small cleg">' + esc(C.legend) + '</p><p class="cmsg" aria-live="polite"></p>' +
      '<div class="cbtns">' + C.add.map(function (n) { return '<button type="button" data-add="' + n + '">' + esc(C.addLabel[String(n)]) + '</button>'; }).join('') + '</div>' +
      '<div class="cbtns sm"><button type="button" data-undo>' + esc(C.undo) + '</button><button type="button" data-clear>' + esc(C.reset) + '</button></div></div>');
    root.appendChild(s);
    function get() { return storeArr(key); }
    function draw() {
      var list = get(), oz = list.reduce(function (a, b) { return a + b; }, 0), ml = oz * 30;
      s.querySelector('.cnum').textContent = lang === 'zh' ? ml + ' ml' : oz + ' oz';
      s.querySelector('.csub').textContent = lang === 'zh' ? '（约 ' + oz + ' oz）' : ' ≈ ' + ml + ' ml';
      var bar = s.querySelector('.cbar i'); bar.style.width = Math.min(oz / MAX * 100, 100) + '%';
      var z = oz === 0 ? 'msg0' : oz < 8 ? 'msgLow' : oz <= 16 ? 'msgOk' : oz <= 24 ? 'msgHigh' : 'msgOver';
      var card = s.querySelector('.counter'); card.className = 'card counter z-' + z;
      s.querySelector('.cmsg').textContent = C[z];
    }
    s.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      var list = get();
      if (b.hasAttribute('data-add')) list.push(+b.getAttribute('data-add'));
      else if (b.hasAttribute('data-undo')) list.pop();
      else if (b.hasAttribute('data-clear')) list = [];
      else return;
      store(key, list); draw();
    });
    draw();
  }
  function buildTopic(d) {
    var w = d[lang] || d.en, L = w.labels; w.id = d.id;
    document.title = w.title + ' · ' + t.pageTitle;
    var root = document.getElementById('app'); root.innerHTML = '';
    var h = el('header', { class: 'hero' });
    h.innerHTML = '<div class="toprow"><a class="back" href="./">' + t.home + '</a>' + langToggleHTML(false) + '</div>' +
      '<h1>' + esc(d.emoji || '') + ' ' + esc(w.title) + '</h1><p class="sub">' + esc(w.sub) + '</p>' +
      '<div class="callout answer">' + w.oneLiner + '</div>';
    root.appendChild(h);
    try {
      localStorage.removeItem('xyla:' + d.id + ':path'); // old picker (removed)
      var vk = 'xyla:' + d.id + ':v';
      if (d.version && store(vk) !== d.version) { localStorage.removeItem('xyla:' + d.id + ':quiz'); store(vk, d.version); } // quiz items changed
    } catch (e) {}
    renderNav(root, ['big3', 'how', 'plan', 'tips', 'count', 'quiz', 'watch', 'disagree', 'more'], t.tnav);
    w.bigThree = arr(w.bigThree); w.quiz = arr(w.quiz); w.disagree = arr(w.disagree); w.details = arr(w.details); w.tips = arr(w.tips); w.labels = L = L || {};
    safe(function big3() {
      var b3 = section('big3', t.big3T, t.big3Hint); b3.className = 'big3';
      b3.insertAdjacentHTML('beforeend', w.bigThree.map(function (c, i) { return cardHTML(c, true, i); }).join(''));
      root.appendChild(b3);
    });
    safe(renderHow, w, root);
    if (w.schedule && Array.isArray(w.schedule.steps)) safe(renderSchedule, w, root);
    safe(renderTips, w, root);
    if (w.counter) safe(renderCounter, w, d.id, root);
    safe(function quiz() { var tq = t.quiz; t.quiz = L.quizT || tq; try { renderQuiz({ id: d.id, quiz: w.quiz }, root); } finally { t.quiz = tq; } });
    safe(function watch() { var tw = t.watch; t.watch = L.watchT || tw; try { renderWatch(w, root); } finally { t.watch = tw; } });
    safe(function disagree() {
      if (!w.disagree.length) return;
      var ds = section('disagree', L.disagreeT, L.disagreeHint);
      ds.insertAdjacentHTML('beforeend', w.disagree.map(function (c) { return cardHTML(c); }).join('')); root.appendChild(ds);
    });
    safe(function more() { var tm = t.more; t.more = L.moreT || tm; try { renderDetails(w, root); } finally { t.more = tm; } });
    safe(function videos() { renderVideos({ bigThree: w.bigThree, details: w.details.concat(w.how ? [w.how] : []) }, root, t.topicVideos); });
    safe(function sources() { var tn = t.sourcesNote; if (lang === 'zh') t.sourcesNote = '大部分是英文网站，也有两条国内的。'; try { renderSources({ sources: d.sources }, root); } finally { t.sourcesNote = tn; } });
    footer(root);
  }

  /* ---------- guide pages (checklists, countdown, printable handout) ---------- */
  function fill(s, d, n) { return String(s || '').replace('{d}', d).replace('{n}', n); }
  function renderCheckGroups(id, key, groups, L, title, hint, sid, root) {
    groups = arr(groups).filter(function (g) { return g && Array.isArray(g.items) && g.items.length; });
    if (!groups.length) return;
    var s = section(sid, title, hint);
    var sk = 'xyla:' + id + ':' + key;
    s.insertAdjacentHTML('beforeend', '<div class="progress"><i></i></div><p class="small pl"></p>' + groups.map(function (g) {
      return '<div class="card cgroup"><p class="gtitle">' + esc(g.title || '') + '</p>' + g.items.map(function (it) {
        if (!it || !it.id) return '';
        return '<label class="check"><input type="checkbox" data-id="' + esc(it.id) + '"><span>' + (it.text || '') + (it.note ? '<small>' + it.note + '</small>' : '') + (it.pre ? ' <em class="badge ok">' + esc(L.preBadge || '✓') + '</em>' : '') + '</span></label>';
      }).join('') + '</div>';
    }).join('') + '<div class="cbtns sm"><button type="button" data-reset>' + esc(L.resetList || 'Reset') + '</button></div>');
    root.appendChild(s);
    var pre = {}; groups.forEach(function (g) { g.items.forEach(function (it) { if (it && it.id) pre[it.id] = !!it.pre; }); });
    function isOn(st, k) { return typeof st[k] === 'boolean' ? st[k] : pre[k]; }
    function draw() {
      var st = storeObj(sk), boxes = s.querySelectorAll('input[data-id]'), n = 0;
      boxes.forEach(function (b) { var on = !!isOn(st, b.getAttribute('data-id')); b.checked = on; b.closest('.check').classList.toggle('done', on); if (on) n++; });
      var pct = boxes.length ? Math.round(n / boxes.length * 100) : 0;
      s.querySelector('.progress i').style.width = pct + '%';
      s.querySelector('.pl').textContent = fill(L.progress || '{d} / {n}', n, boxes.length) + (pct === 100 ? t.allDone : '');
    }
    s.addEventListener('change', function (e) {
      var b = e.target; if (!b.matches || !b.matches('input[data-id]')) return;
      var st = storeObj(sk); st[b.getAttribute('data-id')] = b.checked; store(sk, st); draw();
    });
    s.querySelector('[data-reset]').addEventListener('click', function () { try { localStorage.removeItem(sk); } catch (e) {} draw(); });
    draw();
  }
  function renderAbout(d, w, root) {
    var A = w.about, L = w.labels; if (!A || !Array.isArray(A.fields) || !A.fields.length) return;
    var sk = 'xyla:' + d.id + ':about';
    var s = section('about', L.aboutT, L.aboutHint);
    s.insertAdjacentHTML('beforeend', '<div class="card aform">' + A.fields.map(function (f) {
      return '<label class="afield"><b>' + esc(f.label) + '</b><textarea rows="' + (f.rows || 2) + '" data-f="' + esc(f.id) + '" placeholder="' + esc(f.ph || L.blank || '') + '"></textarea></label>';
    }).join('') + '<div class="cbtns"><button type="button" data-print="' + lang + '">' + esc(L.printBtn) + '</button>' +
      (lang !== 'en' && d.en && d.en.about ? '<button type="button" data-print="en">' + esc(L.printEn || 'English') + '</button>' : '') + '</div>' +
      '<div class="cbtns sm"><button type="button" data-areset>' + esc(L.resetForm || 'Reset') + '</button></div><p class="small">' + (L.aboutFoot || '') + '</p></div><div class="psheet" aria-hidden="true"></div>');
    root.appendChild(s);
    function vals() { return storeObj(sk); }
    function draw() {
      var v = vals();
      s.querySelectorAll('textarea[data-f]').forEach(function (ta) {
        var k = ta.getAttribute('data-f'), f = A.fields.filter(function (x) { return x.id === k; })[0] || {};
        ta.value = typeof v[k] === 'string' ? v[k] : (f.value || '');
      });
    }
    s.addEventListener('input', function (e) {
      var ta = e.target; if (!ta.matches || !ta.matches('textarea[data-f]')) return;
      var v = vals(); v[ta.getAttribute('data-f')] = ta.value; store(sk, v);
    });
    s.querySelector('[data-areset]').addEventListener('click', function () { try { localStorage.removeItem(sk); } catch (e) {} draw(); });
    s.addEventListener('click', function (e) {
      var b = e.target.closest('[data-print]'); if (!b) return;
      var pl = b.getAttribute('data-print'), PA = (d[pl] && d[pl].about) || A, v = vals();
      var ids = {}; A.fields.forEach(function (f) { ids[f.id] = f; });
      s.querySelector('.psheet').innerHTML = '<h2>' + esc(PA.title || '') + '</h2>' + (PA.intro ? '<p>' + esc(PA.intro) + '</p>' : '') + '<table>' + arr(PA.fields).map(function (f) {
        var own = typeof v[f.id] === 'string' && v[f.id] !== (ids[f.id] || {}).value ? v[f.id] : null; // typed by Melody wins
        var val = own != null ? own : (f.value || '');
        return '<tr><th>' + esc(f.label) + '</th><td>' + (val.trim() ? esc(val).replace(/\n/g, '<br>') : '<span class="blank"></span><span class="blank"></span>') + '</td></tr>';
      }).join('') + '</table>' + (PA.foot ? '<p class="pfoot">' + esc(PA.foot) + '</p>' : '');
      document.body.classList.add('printing-about');
      var done = function () { document.body.classList.remove('printing-about'); window.removeEventListener('afterprint', done); };
      window.addEventListener('afterprint', done);
      try { window.print(); } catch (err) {}
      setTimeout(done, 60000);
    });
    draw();
  }
  function buildGuide(d) {
    var w = d[lang] || d.en; w.id = d.id; var L = w.labels = w.labels || {};
    document.title = w.title + ' · ' + t.pageTitle;
    var root = document.getElementById('app'); root.innerHTML = '';
    var h = el('header', { class: 'hero' });
    h.innerHTML = '<div class="toprow"><a class="back" href="./">' + t.home + '</a>' + langToggleHTML(false) + '</div>' +
      '<h1>' + esc(d.emoji || '') + ' ' + esc(w.title) + '</h1><p class="sub">' + esc(w.sub || '') + '</p>' +
      (w.oneLiner ? '<div class="callout answer">' + w.oneLiner + '</div>' : '');
    root.appendChild(h);
    var nav = L.nav || {};
    renderNav(root, ['pack', 'papers', 'plan', 'about', 'scripts', 'normal', 'why'].filter(function (k) { return nav[k]; }), nav);
    safe(renderCheckGroups, d.id, 'pack', w.pack, L, L.packT, L.packHint, 'pack', root);
    safe(renderCheckGroups, d.id, 'papers', w.papers, L, L.papersT, L.papersHint, 'papers', root);
    safe(function plan() { if (w.plan && Array.isArray(w.plan.steps) && w.plan.steps.length) renderSchedule({ schedule: w.plan, labels: L }, root); });
    safe(renderAbout, d, w, root);
    safe(function bye() { var ts = t.scripts, th = t.scriptsHint; t.scripts = L.byeT || ts; t.scriptsHint = L.byeHint || th; try { if (arr(w.scripts).length) renderScripts(w, root); } finally { t.scripts = ts; t.scriptsHint = th; } });
    safe(function normal() {
      var cards = arr(w.normal); if (!cards.length && !arr(w.talk).length) return;
      var s = section('normal', L.normalT, L.normalHint);
      s.insertAdjacentHTML('beforeend', cards.map(function (c) { return cardHTML(c); }).join('') +
        (arr(w.talk).length ? '<div class="callout"><b>' + esc(L.talkT || '') + '</b><ul>' + w.talk.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul></div>' : ''));
      root.appendChild(s);
    });
    safe(function why() {
      var cards = arr(w.why); if (!cards.length) return;
      var s = section('why', L.whyT, L.whyHint);
      s.insertAdjacentHTML('beforeend', cards.map(function (c) { return cardHTML(c); }).join('')); root.appendChild(s);
    });
    safe(function sources() { var tn = t.sourcesNote; if (lang === 'zh') t.sourcesNote = '都是英文网站。'; try { renderSources({ sources: d.sources }, root); } finally { t.sourcesNote = tn; } });
    footer(root);
  }

  /* ---------- pages ---------- */

  /* ---------- baby signs (recurring section; tracker is global per sign id, so it carries across weeks) ---------- */
  // Sign pictures: repo-hosted, freely licensed or our own SVGs in assets/signs/. {src, alt, caption?, credit?}
  function signImgHTML(im) {
    if (!im || !im.src || !/^assets\/signs\//.test(im.src)) return '';
    return '<figure class="signimg"><img src="' + esc(im.src) + (VER ? '?v=' + encodeURIComponent(VER) : '') + '" alt="' + esc(im.alt || '') + '" loading="lazy" width="360" height="170">' +
      (im.caption || im.credit ? '<figcaption>' + (im.caption ? esc(im.caption) : '') + (im.credit ? ' <span class="small">' + im.credit + '</span>' : '') + '</figcaption>' : '') + '</figure>';
  }
  function renderSigns(w, root) {
    var g = w.signs; if (!g || !Array.isArray(g.items) || !g.items.length) return;
    var stages = arr(g.stages).length ? g.stages : ['Seen', 'Tried', 'Uses'];
    var s = section('signs', g.title || '🤟 Baby signs', g.hint || '');
    var key = function (id) { return 'xyla:sign:' + id; };
    function trackHTML(it) {
      var lv = store(key(it.id)); lv = typeof lv === 'number' ? lv : 0;
      return '<div class="filters" role="group" aria-label="' + esc(it.name) + '">' + stages.map(function (st, i) {
        return '<button type="button" data-sign="' + esc(it.id) + '" data-lv="' + (i + 1) + '" aria-pressed="' + (lv >= i + 1) + '">' + (lv >= i + 1 ? '✓ ' : '') + esc(st) + '</button>';
      }).join('') + '</div>';
    }
    s.insertAdjacentHTML('beforeend', (g.intro ? '<p class="small">' + g.intro + '</p>' : '') +
      g.items.map(function (it) {
        return '<details class="card" open><summary><span class="ico">' + esc(it.emoji || '🤟') + '</span><span class="t">' + esc(it.name) + (it.sub ? '<small>' + esc(it.sub) + '</small>' : '') + '</span></summary><div class="body">' +
          linesHTML(it.lines) + arr(it.images).map(signImgHTML).join('') + // signs use still images (start→end / arrows), never videos

          '<p class="small" style="margin:8px 0 4px"><b>' + esc(g.trackLabel || 'Tracker') + '</b></p><div class="strack">' + trackHTML(it) + '</div></div></details>';
      }).join('') +
      arr(g.cards).map(function (c) { return cardHTML(c); }).join(''));
    s.addEventListener('click', function (e) {
      var b = e.target.closest && e.target.closest('[data-sign]'); if (!b) return;
      var id = b.getAttribute('data-sign'), lv = +b.getAttribute('data-lv'), cur = store(key(id));
      store(key(id), cur === lv ? lv - 1 : lv); // tap the current top stage again to undo it
      var it = g.items.filter(function (x) { return x.id === id; })[0];
      b.closest('.strack').innerHTML = trackHTML(it);
    });
    root.appendChild(s);
  }
  function buildWeek(d) {
    var w = d[lang] || d.en; w.id = d.id; w.emoji = d.emoji; w.pid = d.perLang ? d.id + ':' + lang : d.id; // perLang: en/zh lists differ, so progress is saved per language
    var t0 = t; if (w.labels && typeof w.labels === 'object') { t = Object.assign({}, t, w.labels); if (w.labels.nav) t.nav = Object.assign({}, t0.nav, w.labels.nav); } // per-page section titles
    try {
    document.title = w.title + ' · ' + t.pageTitle;
    var root = document.getElementById('app'); root.innerHTML = '';
    renderHero(w, root);
    var have = { big3: w.bigThree, topics: w.cards, signs: w.signs, today: w.daily, quiz: w.quiz, play: w.plays, scripts: w.scripts, next: w.timeline, more: w.details, watch: w.watch };
    if (w.signs && w.signs.nav) t.nav = Object.assign({}, t.nav, { signs: w.signs.nav });
    renderNav(root, ['big3', 'topics', 'signs', 'today', 'quiz', 'play', 'scripts', 'next', 'more', 'watch'].filter(function (k) { return have[k]; }));
    [renderBig3, renderWeekTopics, renderCards, renderSigns, renderChecklist, renderQuiz, renderPlay, renderScripts, renderTimeline, renderDetails, renderWatch, renderVideos, renderSources]
      .forEach(function (fn) { safe(fn, w, root); });
    footer(root);
    } finally { t = t0; }
  }
  function buildHome(list) {
    document.title = t.pageTitle;
    var root = document.getElementById('app'); root.innerHTML = '';
    root.insertAdjacentHTML('beforeend', '<header class="hero"><div class="toprow end">' + (SITE ? '' : '<span class="small">🌐</span>' + langToggleHTML(false)) + '</div><h1>🧸 ' + t.pageTitle + '</h1><p class="sub">' + t.homeSub + '</p>' +
      '</header>');
    var s = section('weeks', t.weeks, ''); s.className = 'weeks';
    var today = localISO();
    s.insertAdjacentHTML('beforeend', list.slice().reverse().map(function (x) {
      var c = x[lang] || x.en, cur = x.start && x.end && today >= x.start && today <= x.end;
      return '<a class="card' + (cur ? ' current' : '') + '" href="' + esc(x.file) + '"><span class="e">' + esc(x.emoji || '📘') + '</span><div><b>' + esc(c.title) + (cur ? '<span class="badge">' + t.thisWeek + '</span>' : '') + '</b><span>' + esc(c.age) + ' · ' + esc(c.dates) + '</span><br><span>' + esc(c.tagline || '') + '</span></div></a>';
    }).join(''));
    root.appendChild(s);
    if (TOPICS.length) {
      var ts = section('topics', t.bigTopics, t.bigTopicsHint); ts.className = 'weeks';
      ts.insertAdjacentHTML('beforeend', topicCardsHTML(TOPICS)); root.appendChild(ts);
    }
    root.insertAdjacentHTML('beforeend', '<section><div class="callout"><b>' + t.howTitle + '</b><ul>' + t.how.map(function (h) { return '<li>' + h + '</li>'; }).join('') + '</ul></div></section>');
    footer(root);
  }

  var isWeek = !!document.body.getAttribute('data-week'), topicId = document.body.getAttribute('data-topic'), TOPICS = [];
  function render() {
    document.documentElement.lang = t.htmlLang;
    if (!DATA) return;
    try { if (topicId) (DATA && DATA.kind === 'guide' ? buildGuide : buildTopic)(DATA); else if (isWeek) buildWeek(DATA); else buildHome(DATA); }
    catch (e) { if (window.console) console.error(e); fail(e.message); }
  }
  function fail(msg) { document.getElementById('app').innerHTML = '<p style="padding:20px">' + t.loadFail + ' (' + esc(msg) + '). ' + t.retry + '</p><p style="padding:0 20px"><a href="./?r=' + Date.now() + '">↻ ' + (lang === 'zh' ? '回首页' : 'Home') + '</a></p>'; }
  document.documentElement.lang = t.htmlLang;
  var url = topicId ? 'topics/' + topicId + '.json' : isWeek ? 'weeks/' + document.body.getAttribute('data-week') + '.json' : 'weeks/weeks.json';
  function getJSON(u) { return fetch(u + '?v=' + encodeURIComponent(VER), { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }); }
  Promise.all([getJSON(url), topicId ? Promise.resolve([]) : getJSON('topics/topics.json').catch(function () { return []; })])
    .then(function (res) {
      var d = res[0]; TOPICS = Array.isArray(res[1]) ? res[1] : [];
      DATA = d; VIDEOS = d.videos || {}; render();
      if (location.hash) { var x = document.querySelector(location.hash); if (x) x.scrollIntoView(); }
    })
    .catch(function (e) { fail(e.message); });
})();
