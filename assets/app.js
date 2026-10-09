/* Xyla Weekly: shared renderer. Each week page sets <body data-week="week-03"> and this file
   loads weeks/<id>.json and builds the page. No build step, no dependencies. */
(function () {
  'use strict';
  var ROOTS = ['Secure', 'Curious', 'Kind', 'Brave', 'Self-led', 'Healthy'];
  var ROOT_ICON = { Secure: '🫶', Curious: '🔍', Kind: '💞', Brave: '🦁', 'Self-led': '🧭', Healthy: '🌱' };

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
  function tagsHTML(roots) { return roots && roots.length ? '<div class="tags">' + roots.map(function (r) { return '<span class="tag ' + esc(r) + '">' + (ROOT_ICON[r] || '') + ' ' + esc(r) + '</span>'; }).join('') + '</div>' : ''; }

  /* ---------- lite YouTube embed ---------- */
  function videoHTML(v) {
    if (!v) return '';
    var thumb = 'https://i.ytimg.com/vi/' + encodeURIComponent(v.id) + '/hqdefault.jpg';
    var url = (v.short ? 'https://www.youtube.com/shorts/' : 'https://www.youtube.com/watch?v=') + encodeURIComponent(v.id);
    return '<button class="yt" type="button" data-yt="' + esc(v.id) + '" style="background-image:url(' + thumb + ')" aria-label="Play video: ' + esc(v.title) + '">' +
      '<span class="play"></span><span class="cap"><b>▶ ' + esc(v.title) + '</b>' + esc(v.channel) + (v.length ? ' · ' + esc(v.length) : '') + (v.short ? ' · Short' : '') + '</span></button>' +
      '<a class="ytlink" href="' + url + '" target="_blank" rel="noopener">Open in YouTube ↗</a>';
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('button.yt');
    if (!b || b.querySelector('iframe')) return;
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(b.getAttribute('data-yt')) + '?autoplay=1&playsinline=1&rel=0';
    f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen';
    f.allowFullscreen = true;
    f.title = b.getAttribute('aria-label') || 'YouTube video';
    b.innerHTML = ''; b.style.backgroundImage = 'none'; b.appendChild(f);
  });

  function linesHTML(lines) { return lines && lines.length ? '<ul class="lines">' + lines.map(function (l) { return '<li>' + l + '</li>'; }).join('') + '</ul>' : ''; }
  function cardHTML(c, numbered, i) {
    return '<details class="card"><summary>' + (numbered ? '<span class="num">' + (i + 1) + '</span>' : '') +
      '<span class="ico">' + esc(c.icon || '•') + '</span><span class="t">' + esc(c.title) + (c.sub ? '<small>' + esc(c.sub) + '</small>' : '') + '</span></summary>' +
      '<div class="body">' + tagsHTML(c.roots) + linesHTML(c.lines) + (c.html || '') + (c.videos || (c.video ? [c.video] : [])).map(videoHTML).join('') + '</div></details>';
  }

  function section(id, title, hint) {
    var s = el('section', { id: id });
    s.appendChild(el('h2', null, title));
    if (hint) s.appendChild(el('p', { class: 'hint' }, hint));
    return s;
  }

  /* ---------- sections ---------- */
  function renderHero(w, root) {
    var h = el('header', { class: 'hero' });
    h.innerHTML = '<a class="back" href="./">← All weeks</a><h1>' + esc(w.emoji || '') + ' ' + esc(w.title) + '</h1>' +
      '<p class="sub">' + esc(w.age) + ' · ' + esc(w.dates) + '</p>' +
      (w.oneLiner ? '<p style="margin:10px 0 0">' + w.oneLiner + '</p>' : '') +
      (w.now && w.now.length ? '<details class="card" style="margin-top:14px"><summary><span class="ico">👶</span><span class="t">Xyla right now <small>' + w.now.length + ' things she’s doing · tap to see</small></span></summary><div class="body"><ul class="chips" style="margin:0">' + w.now.map(function (n) { return '<li>' + esc(n) + '</li>'; }).join('') + '</ul></div></details>' : '');
    root.appendChild(h);
  }

  function renderNav(w, root, ids) {
    var n = el('nav', { class: 'jump', 'aria-label': 'Jump to' });
    n.innerHTML = ids.map(function (x) { return '<a href="#' + x[0] + '">' + x[1] + '</a>'; }).join('');
    root.appendChild(n);
  }

  function renderBig3(w, root) {
    var s = section('big3', '⭐ This week’s 3 big things', 'Tap a card. 30 seconds each.');
    s.className = 'big3';
    s.insertAdjacentHTML('beforeend', w.bigThree.map(function (c, i) { return cardHTML(c, true, i); }).join(''));
    root.appendChild(s);
  }

  function renderCards(w, root) {
    if (!w.cards || !w.cards.length) return;
    var s = section('topics', '💬 Your questions this week', 'Short answers to things you asked about.');
    s.insertAdjacentHTML('beforeend', w.cards.map(function (c) { return cardHTML(c); }).join(''));
    root.appendChild(s);
  }

  function renderTimeline(w, root) {
    var t = w.timeline; if (!t) return;
    var s = section('next', '🗺️ What’s next', t.hint || '');
    var html = '<div class="card" style="padding:14px 16px"><ul class="tl">' + t.steps.map(function (st, i) {
      var cls = i < t.now ? 'past' : (i === t.now ? 'now' : '');
      return '<li class="' + cls + '"><span class="dot"></span><b>' + esc(st.label) + (i === t.now ? '<span class="here">Xyla is here</span>' : '') + '</b><span>' + esc(st.note || '') + '</span></li>';
    }).join('') + '</ul>';
    if (t.ruler) {
      var r = t.ruler, span = r.max - r.min, pct = function (m) { return ((m - r.min) / span * 100).toFixed(1) + '%'; };
      html += '<p class="small" style="margin:6px 0 0">' + esc(r.label) + '</p><div class="ruler" aria-hidden="true">' +
        '<div class="bar" style="left:' + pct(r.from) + ';width:calc(' + pct(r.to) + ' - ' + pct(r.from) + ')"></div>' +
        '<div class="mark" style="left:' + pct(r.age) + '"></div>' +
        r.ticks.map(function (m) { return '<span class="lab" style="left:' + pct(m) + '">' + m + ' mo</span>'; }).join('') + '</div>' +
        '<p class="small" style="margin:6px 0 0"><span style="color:var(--accent)">▍</span> Xyla (~' + r.age + ' mo) · green = normal range for walking alone</p>';
    }
    html += (t.footer ? '<p class="small">' + t.footer + '</p>' : '') + '</div>';
    s.insertAdjacentHTML('beforeend', html);
    root.appendChild(s);
  }

  function renderChecklist(w, root) {
    if (!w.daily) return;
    var s = section('today', '✅ Today’s checklist', 'Saved on this phone. Resets every day. Small wins count.');
    var today = localISO();
    var key = function (d) { return 'xyla:' + w.id + ':daily:' + d; };
    var todoKey = 'xyla:' + w.id + ':todo';
    var box = el('div');
    box.innerHTML = '<div class="tabs" role="tablist"><button role="tab" aria-selected="true" data-tab="d">Every day</button>' +
      (w.todos ? '<button role="tab" aria-selected="false" data-tab="t">Once this week</button>' : '') + '</div>' +
      '<div class="progress"><i></i></div><p class="small pl"></p><div class="card" id="cl"></div><div class="days"></div>';
    s.appendChild(box);
    root.appendChild(s);
    var tab = 'd';
    function list() { return tab === 'd' ? w.daily : w.todos; }
    function getDone() { return (tab === 'd' ? store(key(today)) : store(todoKey)) || []; }
    function draw() {
      var done = getDone(), items = list();
      box.querySelector('#cl').innerHTML = items.map(function (it, i) {
        var on = done.indexOf(i) > -1;
        return '<label class="check' + (on ? ' done' : '') + '"><input type="checkbox" data-i="' + i + '"' + (on ? ' checked' : '') + '><span>' + esc(it) + '</span></label>';
      }).join('');
      var pct = items.length ? Math.round(done.length / items.length * 100) : 0;
      box.querySelector('.progress i').style.width = pct + '%';
      box.querySelector('.pl').textContent = done.length + ' of ' + items.length + (tab === 'd' ? ' today' : ' done') + (pct === 100 ? ' 🎉 Amazing.' : '');
      var days = box.querySelector('.days');
      if (tab === 'd' && w.start && w.end) {
        var d = new Date(w.start + 'T12:00:00'), end = new Date(w.end + 'T12:00:00'), out = '';
        while (d <= end) {
          var iso = localISO(d), n = (store(key(iso)) || []).length, f = n / w.daily.length;
          var bg = n ? 'rgba(47,158,107,' + (0.25 + 0.75 * f).toFixed(2) + ')' : '';
          out += '<span class="day' + (iso === today ? ' today' : '') + '" title="' + iso + ': ' + n + ' done" style="' + (bg ? 'background:' + bg + ';color:#fff' : '') + '">' + d.getDate() + '</span>';
          d.setDate(d.getDate() + 1);
        }
        days.innerHTML = out; days.style.display = '';
      } else days.style.display = 'none';
    }
    box.addEventListener('change', function (e) {
      if (!e.target.matches('input[type=checkbox]')) return;
      var done = getDone(), i = +e.target.getAttribute('data-i'), at = done.indexOf(i);
      if (e.target.checked && at < 0) done.push(i); else if (!e.target.checked && at > -1) done.splice(at, 1);
      store(tab === 'd' ? key(today) : todoKey, done); draw();
    });
    box.addEventListener('click', function (e) {
      var b = e.target.closest('[data-tab]'); if (!b) return;
      tab = b.getAttribute('data-tab');
      box.querySelectorAll('[data-tab]').forEach(function (x) { x.setAttribute('aria-selected', x === b); });
      draw();
    });
    draw();
  }

  function renderQuiz(w, root) {
    if (!w.quiz) return;
    var s = section('quiz', '🤔 Do or Don’t?', 'Guess first, then see why.');
    s.insertAdjacentHTML('beforeend', '<p class="score">Score: <span class="sc">0</span> / ' + w.quiz.length + ' <button type="button" class="reset" style="margin-left:8px;font:inherit;font-size:13px;border:1px solid var(--line);background:#fff;border-radius:99px;padding:4px 10px">Reset</button></p>');
    var g = el('div', { class: 'qgrid' });
    g.innerHTML = w.quiz.map(function (q, i) {
      return '<div class="q" data-i="' + i + '"><div class="qq">' + esc(q.q) + '</div><div class="btns"><button type="button" data-g="do">✅ Do</button><button type="button" data-g="dont">❌ Don’t</button></div>' +
        '<div class="ans"><div class="verdict"></div><div>' + q.why + '</div></div></div>';
    }).join('');
    s.appendChild(g); root.appendChild(s);
    var score = 0;
    g.addEventListener('click', function (e) {
      var b = e.target.closest('[data-g]'); if (!b) return;
      var card = b.closest('.q'), q = w.quiz[+card.getAttribute('data-i')], ok = b.getAttribute('data-g') === q.a;
      card.classList.add('flipped', ok ? 'right' : 'wrong');
      card.querySelector('.verdict').textContent = (ok ? '👍 Right! ' : '🙂 Not quite. ') + (q.a === 'do' ? '✅ DO' : '❌ DON’T');
      if (ok) score++; s.querySelector('.sc').textContent = score;
    });
    s.querySelector('.reset').addEventListener('click', function () {
      score = 0; s.querySelector('.sc').textContent = 0;
      g.querySelectorAll('.q').forEach(function (c) { c.classList.remove('flipped', 'right', 'wrong'); });
    });
  }

  function renderPlay(w, root) {
    if (!w.plays) return;
    var s = section('play', '🎲 Lucky play', 'Not sure what to do? Tap the button. Filter by root if you like.');
    var filter = null, last = -1;
    s.insertAdjacentHTML('beforeend', '<button type="button" class="lucky-btn">🎲 Pick a play for us!</button><div class="lucky-out" aria-live="polite"></div>' +
      '<div class="filters"><button type="button" aria-pressed="true" data-r="">All</button>' + ROOTS.map(function (r) { return '<button type="button" aria-pressed="false" data-r="' + r + '">' + ROOT_ICON[r] + ' ' + r + '</button>'; }).join('') + '</div>' +
      '<details class="card"><summary><span class="ico">📋</span><span class="t">See all plays <small class="cnt"></small></span></summary><div class="body plist" style="padding:0"></div></details>');
    root.appendChild(s);
    function pool() { return w.plays.map(function (p, i) { return i; }).filter(function (i) { return !filter || (w.plays[i].roots || []).indexOf(filter) > -1; }); }
    function drawList() {
      var p = pool();
      s.querySelector('.cnt').textContent = p.length + ' ideas' + (filter ? ' · ' + filter : '');
      s.querySelector('.plist').innerHTML = p.map(function (i) { var x = w.plays[i]; return '<div class="play"><b>' + esc(x.name) + '</b><p>' + x.how + '</p>' + tagsHTML(x.roots) + '</div>'; }).join('');
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
    var s = section('scripts', '🗣️ What to say', 'Tap a moment to reveal the exact words.');
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
    var s = section('more', '📚 More detail (optional)', 'Only if you want it. Everything is tucked away.');
    s.insertAdjacentHTML('beforeend', w.details.map(function (c) { return cardHTML(c); }).join(''));
    root.appendChild(s);
  }

  function renderWatch(w, root) {
    if (!w.watch) return;
    var s = section('watch', '🩺 Call or ask the pediatrician if…', '');
    s.insertAdjacentHTML('beforeend', '<div class="callout"><ul>' + w.watch.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul><p class="small" style="margin:6px 0 0">Gut feeling something’s off? It’s always okay to ask.</p></div>');
    root.appendChild(s);
  }

  function renderVideos(w, root) {
    var seen = {}, all = [];
    function add(v) { if (v && !seen[v.id]) { seen[v.id] = 1; all.push(v); } }
    (w.bigThree || []).concat(w.cards || [], w.details || []).forEach(function (c) { (c.videos || (c.video ? [c.video] : [])).forEach(add); });
    (w.extraVideos || []).forEach(add);
    if (!all.length) return;
    var s = section('videos', '🎬 All videos this week', all.length + ' short videos from reputable channels. Tap to play.');
    s.insertAdjacentHTML('beforeend', '<details class="card"><summary><span class="ico">🎬</span><span class="t">Show all ' + all.length + ' videos</span></summary><div class="body">' + all.map(videoHTML).join('') + '</div></details>');
    root.appendChild(s);
  }

  function renderSources(w, root) {
    if (!w.sources) return;
    var s = el('section', { id: 'sources' });
    s.innerHTML = '<details class="card"><summary><span class="ico">🔗</span><span class="t">Sources <small>Research and guidelines behind this page</small></span></summary><div class="body"><ul class="sources">' +
      w.sources.map(function (x) { return '<li><a href="' + esc(x.url) + '" target="_blank" rel="noopener">' + esc(x.label) + '</a></li>'; }).join('') + '</ul></div></details>';
    root.appendChild(s);
  }

  function footer(root) {
    root.insertAdjacentHTML('beforeend', '<footer><strong>General info, not medical advice; ask your pediatrician.</strong><br>Made with love for Xyla 💛</footer>');
  }

  /* ---------- page boot ---------- */
  function buildWeek(w) {
    document.title = w.title + ' · Xyla Weekly';
    var root = document.getElementById('app'); root.innerHTML = '';
    renderHero(w, root);
    var nav = [['big3', '⭐ Big 3'], ['topics', '💬 Questions'], ['today', '✅ Today'], ['quiz', '🤔 Quiz'], ['play', '🎲 Play'], ['scripts', '🗣️ Say'], ['next', '🗺️ Next'], ['more', '📚 More'], ['watch', '🩺 Doctor']];
    renderNav(w, root, nav.filter(function (n) {
      return ({ big3: w.bigThree, topics: w.cards, today: w.daily, quiz: w.quiz, play: w.plays, scripts: w.scripts, next: w.timeline, more: w.details, watch: w.watch })[n[0]];
    }));
    renderBig3(w, root); renderCards(w, root); renderChecklist(w, root); renderQuiz(w, root);
    renderPlay(w, root); renderScripts(w, root); renderTimeline(w, root); renderDetails(w, root);
    renderWatch(w, root); renderVideos(w, root); renderSources(w, root); footer(root);
    if (location.hash) { var t = document.querySelector(location.hash); if (t) t.scrollIntoView(); }
  }

  function buildHome(list) {
    var root = document.getElementById('app'); root.innerHTML = '';
    root.insertAdjacentHTML('beforeend', '<header class="hero"><h1>🧸 Xyla Weekly</h1><p class="sub">Short, tappable weekly packs. The most important things first.</p></header>');
    var s = section('weeks', '📅 Weeks', ''); s.className = 'weeks';
    var today = localISO();
    s.insertAdjacentHTML('beforeend', list.slice().reverse().map(function (x) {
      var cur = x.start && x.end && today >= x.start && today <= x.end;
      return '<a class="card' + (cur ? ' current' : '') + '" href="' + esc(x.file) + '"><span class="e">' + esc(x.emoji || '📘') + '</span><div><b>' + esc(x.title) + (cur ? '<span class="badge">This week</span>' : '') + '</b><span>' + esc(x.age) + ' · ' + esc(x.dates) + '</span><br><span>' + esc(x.tagline || '') + '</span></div></a>';
    }).join(''));
    root.appendChild(s);
    root.insertAdjacentHTML('beforeend', '<section><div class="callout"><b>How to use this</b><ul><li>Open this week → read the <b>3 big things</b> (2 minutes).</li><li>Tick the <b>daily checklist</b> (saved on your phone).</li><li>Stuck? Hit <b>🎲 Lucky play</b>.</li></ul></div></section>');
    footer(root);
  }

  function fail(msg) { document.getElementById('app').innerHTML = '<p style="padding:20px">Couldn’t load this page (' + esc(msg) + '). Try refreshing.</p>'; }
  var body = document.body, week = body.getAttribute('data-week');
  var url = week ? 'weeks/' + week + '.json' : 'weeks/weeks.json';
  fetch(url, { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) { week ? buildWeek(d) : buildHome(d); })
    .catch(function (e) { fail(e.message); });
})();
