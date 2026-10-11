/* Xyla Weekly: shared renderer (English + 简体中文).
   Each week page sets <body data-week="week-03">, each topic page <body data-topic="milk-at-one">; this file loads weeks/<id>.json or topics/<id>.json, which holds
   shared fields (id, start, end, videos) plus "en" and "zh" content side by side. No build step. */
(function () {
  'use strict';
  var ROOTS = ['Secure', 'Curious', 'Kind', 'Brave', 'Self-led', 'Healthy'];
  var ROOT_ICON = { Secure: '🫶', Curious: '🔍', Kind: '💞', Brave: '🦁', 'Self-led': '🧭', Healthy: '🌱' };
  var LANG_KEY = 'xyla:lang';

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
      home: '← Home', bigTopics: '📌 Big topics', bigTopicsHint: 'One page per big question. Read once, come back as needed.', weekTopic: '📌 Big topic this week', topicVideos: '🎬 Videos on this topic',
      tnav: { big3: '⭐ Big 3', path: '🧭 Path', plan: '📅 Plan', count: '🥛 Count', quiz: '🤔 Quiz', watch: '🚩 Red flags', disagree: '⚖️ Debates', more: '📚 More' }, big3T: '⭐ 3 big things', stepsT: 'Step by step', tipT: 'Tip: '
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
      home: '← 首页', bigTopics: '📌 重点话题', bigTopicsHint: '大问题单独整理成一页，看一遍，需要时再回来翻。', weekTopic: '📌 这周的重点话题', topicVideos: '🎬 相关视频',
      tnav: { big3: '⭐ 3件事', path: '🧭 选情况', plan: '📅 计划', count: '🥛 记奶量', quiz: '🤔 测一测', watch: '🚩 警惕', disagree: '⚖️ 分歧', more: '📚 更多' }, big3T: '⭐ 最重要的 3 件事', stepsT: '一步一步来', tipT: '小提示：'
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
  function localISO(d) { d = d || new Date(); return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0'); }

  /* ---------- language ---------- */
  function detectLang() {
    var saved = store(LANG_KEY);
    if (saved === 'en' || saved === 'zh') return saved;
    var langs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || 'en'];
    return /^zh/i.test(langs[0] || '') ? 'zh' : 'en';
  }
  var lang = detectLang(), t = T[lang], DATA = null, VIDEOS = {};
  function setLang(l) {
    if (l !== 'en' && l !== 'zh') return;
    store(LANG_KEY, l); lang = l; t = T[l];
    var y = window.scrollY; render(); window.scrollTo(0, y);
  }
  function langToggleHTML(big) {
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
  function cardHTML(c, numbered, i) {
    return '<details class="card"><summary>' + (numbered ? '<span class="num">' + (i + 1) + '</span>' : '') +
      '<span class="ico">' + esc(c.icon || '•') + '</span><span class="t">' + esc(c.title) + (c.sub ? '<small>' + esc(c.sub) + '</small>' : '') + '</span></summary>' +
      '<div class="body">' + tagsHTML(c.roots) + linesHTML(c.lines) + (c.html || '') + (c.videos || []).map(videoHTML).join('') + '</div></details>';
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
    var key = function (d) { return 'xyla:' + w.id + ':daily:' + d; };
    var todoKey = 'xyla:' + w.id + ':todo';
    var box = el('div');
    box.innerHTML = '<div class="tabs" role="tablist"><button role="tab" aria-selected="' + (checkTab === 'd') + '" data-tab="d">' + t.tabDaily + '</button>' +
      (w.todos ? '<button role="tab" aria-selected="' + (checkTab === 't') + '" data-tab="t">' + t.tabOnce + '</button>' : '') + '</div>' +
      '<div class="progress"><i></i></div><p class="small pl"></p><div class="card" id="cl"></div><div class="days"></div>';
    s.appendChild(box); root.appendChild(s);
    function list() { return checkTab === 'd' ? w.daily : w.todos; }
    function getDone() { return (checkTab === 'd' ? store(key(today)) : store(todoKey)) || []; }
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
          var iso = localISO(d), c = (store(key(iso)) || []).length, f = c / w.daily.length;
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
    if (!w.quiz) return;
    var qKey = 'xyla:' + w.id + ':quiz';
    var s = section('quiz', t.quiz, t.quizHint);
    s.insertAdjacentHTML('beforeend', '<p class="score">' + t.score + ': <span class="sc">0</span> / ' + w.quiz.length + ' <button type="button" class="reset">' + t.reset + '</button></p>');
    var g = el('div', { class: 'qgrid' });
    g.innerHTML = w.quiz.map(function (q, i) {
      return '<div class="q" data-i="' + i + '"><div class="qq">' + esc(q.q) + '</div><div class="btns"><button type="button" data-g="do">' + t.doBtn + '</button><button type="button" data-g="dont">' + t.dontBtn + '</button></div>' +
        '<div class="ans"><div class="verdict"></div><div>' + q.why + '</div></div></div>';
    }).join('');
    s.appendChild(g); root.appendChild(s);
    function apply() {
      var st = store(qKey) || {}, score = 0;
      g.querySelectorAll('.q').forEach(function (card) {
        var i = card.getAttribute('data-i'), q = w.quiz[+i], guess = st[i];
        card.classList.remove('flipped', 'right', 'wrong');
        if (!guess) return;
        var ok = guess === q.a; if (ok) score++;
        card.classList.add('flipped', ok ? 'right' : 'wrong');
        card.querySelector('.verdict').textContent = (ok ? t.right : t.wrong) + (q.a === 'do' ? t.DO : t.DONT);
      });
      s.querySelector('.sc').textContent = score;
    }
    g.addEventListener('click', function (e) {
      var b = e.target.closest('[data-g]'); if (!b) return;
      var st = store(qKey) || {}; st[b.closest('.q').getAttribute('data-i')] = b.getAttribute('data-g');
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
        }).join('') + (sc.note ? '<p class="small">' + sc.note + '</p>' : '') + '</div></details>';
    }).join(''));
    root.appendChild(s);
  }
  function renderDetails(w, root) {
    if (!w.details) return;
    var s = section('more', t.more, t.moreHint);
    s.insertAdjacentHTML('beforeend', w.details.map(function (c) { return cardHTML(c); }).join(''));
    root.appendChild(s);
  }
  function renderWatch(w, root) {
    if (!w.watch) return;
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
    if (!w.sources) return;
    var s = el('section', { id: 'sources' });
    s.innerHTML = '<details class="card"><summary><span class="ico">🔗</span><span class="t">' + t.sources + ' <small>' + t.sourcesSub + '</small></span></summary><div class="body">' + (t.sourcesNote ? '<p class="small">' + t.sourcesNote + '</p>' : '') + '<ul class="sources">' +
      w.sources.map(function (x) { return '<li><a href="' + esc(x.url) + '" target="_blank" rel="noopener">' + esc(x.label) + '</a></li>'; }).join('') + '</ul></div></details>';
    root.appendChild(s);
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
  function renderPaths(w, id, root) {
    var L = w.labels, key = 'xyla:' + id + ':path';
    var s = section('path', L.pathT, L.pathHint);
    s.insertAdjacentHTML('beforeend', '<div class="paths" role="tablist">' + w.paths.map(function (p) {
      return '<button type="button" role="tab" data-path="' + esc(p.key) + '"><span class="pi">' + esc(p.icon) + '</span><span>' + esc(p.label) + '</span></button>';
    }).join('') + '</div><div class="pathplan" aria-live="polite"></div>');
    root.appendChild(s);
    function draw(k) {
      var p = w.paths.filter(function (x) { return x.key === k; })[0];
      s.querySelectorAll('[data-path]').forEach(function (b) { b.setAttribute('aria-selected', b.getAttribute('data-path') === k); });
      s.querySelector('.pathplan').innerHTML = p ? '<div class="card pcard"><p class="pintro">' + esc(p.icon) + ' ' + p.intro + '</p><b class="small">' + t.stepsT + '</b>' +
        p.steps.map(function (st, i) { return '<div class="step"><span class="n">' + (i + 1) + '</span><div class="c">' + st + '</div></div>'; }).join('') +
        (p.tip ? '<p class="ptip">💡 ' + t.tipT + p.tip + '</p>' : '') + (p.videos || []).map(videoHTML).join('') + '</div>' : '';
    }
    s.querySelector('.paths').addEventListener('click', function (e) {
      var b = e.target.closest('[data-path]'); if (!b) return;
      store(key, b.getAttribute('data-path')); draw(b.getAttribute('data-path'));
    });
    draw(store(key) || '');
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
    function get() { return store(key) || []; }
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
    renderNav(root, ['big3', 'path', 'plan', 'count', 'quiz', 'watch', 'disagree', 'more'], t.tnav);
    var b3 = section('big3', t.big3T, t.big3Hint); b3.className = 'big3';
    b3.insertAdjacentHTML('beforeend', w.bigThree.map(function (c, i) { return cardHTML(c, true, i); }).join(''));
    root.appendChild(b3);
    renderPaths(w, d.id, root); renderSchedule(w, root); renderCounter(w, d.id, root);
    var q = { id: d.id, quiz: w.quiz }; var tq = t.quiz; t.quiz = L.quizT; renderQuiz(q, root); t.quiz = tq;
    var tw = t.watch; t.watch = L.watchT; renderWatch(w, root); t.watch = tw;
    var ds = section('disagree', L.disagreeT, L.disagreeHint);
    ds.insertAdjacentHTML('beforeend', w.disagree.map(function (c) { return cardHTML(c); }).join('')); root.appendChild(ds);
    var tm = t.more; t.more = L.moreT; renderDetails(w, root); t.more = tm;
    renderVideos({ bigThree: w.bigThree, details: w.details }, root, t.topicVideos);
    var tn = t.sourcesNote; if (lang === 'zh') t.sourcesNote = '大部分是英文网站，最后两条是国内的。'; renderSources({ sources: d.sources }, root); t.sourcesNote = tn; footer(root);
  }

  /* ---------- pages ---------- */
  function buildWeek(d) {
    var w = d[lang] || d.en; w.id = d.id; w.emoji = d.emoji;
    document.title = w.title + ' · ' + t.pageTitle;
    var root = document.getElementById('app'); root.innerHTML = '';
    renderHero(w, root);
    var have = { big3: w.bigThree, topics: w.cards, today: w.daily, quiz: w.quiz, play: w.plays, scripts: w.scripts, next: w.timeline, more: w.details, watch: w.watch };
    renderNav(root, ['big3', 'topics', 'today', 'quiz', 'play', 'scripts', 'next', 'more', 'watch'].filter(function (k) { return have[k]; }));
    renderBig3(w, root); renderWeekTopics(w, root); renderCards(w, root); renderChecklist(w, root); renderQuiz(w, root);
    renderPlay(w, root); renderScripts(w, root); renderTimeline(w, root); renderDetails(w, root);
    renderWatch(w, root); renderVideos(w, root); renderSources(w, root); footer(root);
  }
  function buildHome(list) {
    document.title = t.pageTitle;
    var root = document.getElementById('app'); root.innerHTML = '';
    root.insertAdjacentHTML('beforeend', '<header class="hero"><div class="toprow end"><span class="small">🌐</span>' + langToggleHTML(false) + '</div><h1>🧸 ' + t.pageTitle + '</h1><p class="sub">' + t.homeSub + '</p>' +
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
    if (topicId) buildTopic(DATA); else if (isWeek) buildWeek(DATA); else buildHome(DATA);
  }
  function fail(msg) { document.getElementById('app').innerHTML = '<p style="padding:20px">' + t.loadFail + ' (' + esc(msg) + '). ' + t.retry + '</p>'; }
  document.documentElement.lang = t.htmlLang;
  var url = topicId ? 'topics/' + topicId + '.json' : isWeek ? 'weeks/' + document.body.getAttribute('data-week') + '.json' : 'weeks/weeks.json';
  function getJSON(u) { return fetch(u, { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); }); }
  Promise.all([getJSON(url), topicId ? Promise.resolve([]) : getJSON('topics/topics.json').catch(function () { return []; })])
    .then(function (res) {
      var d = res[0]; TOPICS = Array.isArray(res[1]) ? res[1] : [];
      DATA = d; VIDEOS = d.videos || {}; render();
      if (location.hash) { var x = document.querySelector(location.hash); if (x) x.scrollIntoView(); }
    })
    .catch(function (e) { fail(e.message); });
})();
