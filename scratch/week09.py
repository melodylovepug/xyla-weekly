# Week 9 (Nov 16–22, 2026) generator. Base structure from week-08.json; plays carried by stable id.
import json, copy
W8=json.load(open("weeks/week-08.json"))
P8={L:{p["id"]:p for p in W8[L]["plays"]} for L in ("en","zh")}
FP='<a href="family-principles.html">'; MK='<a href="milk-at-one.html">'
def P(i,emoji,en,zh,roots,t):
    return {"en":{"id":i,"emoji":emoji,"name":en[0],"how":en[1],"roots":roots,"time":t[0]},
            "zh":{"id":i,"emoji":emoji,"name":zh[0],"how":zh[1],"roots":roots,"time":t[1]}}
NEW={}
def add(*a): NEW[a[0]]=P(*a)
# ---- carried plays: (id, None | (en_how, zh_how), harder?) ----
def strip(h):
    import re
    return re.sub(r"\s*[（(](Wk|第)[^）)]*[）)]\s*$","",h).strip()
CARRY=[
 ("couch-to-mama",("Couch to you, 2–3 steps. Kneel with open arms instead of holding both her hands; let her lean and fall into you. (Wk 4, harder)","沙发到您怀里，两三步。您蹲着张开手等，别牵她两只手，让她自己往前倒、扑过来。（第4周，升级）")),
 ("one-hand-walk",None),
 ("playground-mission",None),
 ("bring-it",None),
 ("point-name-walk",None),
 ("pen-book-turns",("She taps a picture; you name it and <b>pause</b> before the music plays. Add one word: “Cat! Soft cat.” Then her turn. (Wk 3)","她点一个图，您先说名字，<b>停一下</b>再让音乐响。多加一个词：“猫！软软的猫。”再轮到她。（第3周）")),
 ("echo-and-add",("Any sound counts: she says “ba” while pointing → “Ball! Big ball.” Add one word, never “say ball.” (Wk 3)","她发什么音都算：指着说“ba”→“球！大球。”加一个词就行，别让她“说球”。（第3周）")),
 ("family-photo-book",None),
 ("quiet-board-book",("Lift-the-flap or real-photo book. She turns the pages; you point, name, pause 5 s for her point or sound. Stop when she wanders off. (Wk 1)","翻翻书或实物照片书。她自己翻，您指着说名字，停5秒等她指或发音。她走开就结束。（第1周）")),
 ("this-or-that",None),
 ("cup-shuffle",None),
 ("stack-crash",("Aim for 3, then 4 blocks: you build 2, hand her the third. Crash and cheer. (Wk 1, harder)","目标三块、四块：您先搭两块，递给她第三块。推倒了一起欢呼。（第1周，升级）")),
 ("lid-lab",None),
 ("freeze-dance",None),
 ("rhythm-copy",None),
 ("gesture-songs",("Itsy Bitsy Spider, Pat-a-Cake, or a Chinese finger rhyme. Pause right before the motion so she fills it in. (Wk 3)","《小蜘蛛》《拍拍手》或者手指谣（“一个手指点点点”）。做动作前停一下，等她接。（第3周）")),
 ("copy-me",None),
 ("wipe-up-helper",None),
 ("solo-play-checkins",None),
 ("water-table",("Winter version at the sink or in the tub: cups, a colander, a funnel. Pour, watch it rain through. You right there, always. (Wk 4)","冬天就在水池边或澡盆里玩：杯子、漏勺、漏斗。倒水、看水从洞里“下雨”。大人一直在旁边。（第4周）")),
 ("floor-to-stand",("Toy on the couch while she half-kneels: one foot forward, push up. Switch which leg leads. Lean her body slightly forward as she rises. (Wk 7, harder)","她单膝跪着时把玩具放沙发上：一只脚往前迈、撑起来。换条腿来。她起身时扶着让身体稍微往前倾。（第7周，升级）")),
 ("squat-to-stand",None),
 ("point-honor",None),
 ("faucet-pour",None),
 ("in-and-out",("Fill-and-dump, harder: a basket she fills, pushes across the room, and dumps. All pieces wider than a toilet-paper tube. (Wk 7, harder)","装了倒，升级：她把小篮子装满、推着走、再倒出来。东西都要比卫生纸筒粗。（第7周，升级）")),
 ("cup-sips",None),
 ("swim-bath-pour",None),
 ("mouth-ok-basket",None),
 ("mirror-signs",("In front of a mirror: EAT, MILK, ALL DONE, and the new one, MORE. Slowly, saying each word. (Wk 7)","对着镜子比：吃、奶、吃完了，再加新的“还要”。慢慢比，边比边说。（第7周）")),
 ("hat-on-off",None),
 ("color-match-2",None),
 ("posting-box",None),
 ("tube-ball-drop",None),
 ("big-sticker",None),
 ("sticky-wall",None),
 ("pipe-colander",None),
 ("bye-bye-teddy",None),
]
DROPPED=["daytime-night-night","peer-time","door-open-close","color-match-1"]
def carried(L):
    out=[]
    for i,h in CARRY:
        p=copy.deepcopy(P8[L][i])
        if h: p["how"]=h[0 if L=="en" else 1]
        out.append(p)
    return out
# ---- new plays (parent-sourced; research only as safety/age check) ----
add("bubbles-more","🫧",("Bubbles: “More?”","You blow 3 bubbles, then stop with the wand up. Look at her and wait. Any sound, reach, or a MORE sign → “More! More bubbles!” and blow. If she just points, blow anyway and say “more.” You hold the bottle. (Speech-therapist favorite, e.g. @speechsisters)"),("吹泡泡：“还要吗？”","吹三个泡泡就停，举着泡泡棒看着她等一等。她出个声、伸手、比“还要”，您就：“还要！还要泡泡！”接着吹。她光指也照样吹，嘴里说“还要”。泡泡水大人拿着。（语言治疗师常用的玩法）"),["Curious","Kind"],("3 min","3分钟"))
add("ready-set-go","🏁",("Ready, set… GO!","Roll a ball or a car down a cushion ramp: “Ready, set…” pause, look at her, “GO!” After a few rounds, pause longer so she can fill in “go” with a sound or a look. (Parent SLP accounts)"),("预备……走！","球或小车从靠垫斜坡上滚下去：“预备……”停一下，看着她，“走！”玩几轮后停久一点，让她用声音或眼神来接“走”。（家长和语言治疗师常用）"),["Curious","Brave"],("3 min","3分钟"))
add("open-help-jar","🫙",("“Open? Help?” jar","Put a favorite toy or snack in a clear jar she can’t open. Hand it to her and wait. When she brings it or pushes it at you: “Open! Help, open.” Open it right away; don’t hold out for a word. (Speech-therapist tip)"),("“打开？帮忙？”透明罐","把她喜欢的玩具或零食放进她打不开的透明罐子，递给她，等一等。她拿过来塞给您，您就说：“打开！帮你打开。”马上打开，别非等她说出来。（语言治疗师的小技巧）"),["Curious","Self-led"],("2 min","2分钟"))
add("show-me-basket","🧺",("Look what I found!","Hide 3–4 interesting things in a basket (a big pinecone, a whisk, a scarf). When she holds one up to you, react to the <b>showing</b>: “Oh, you’re showing me! A whisk!” Pointing to share is the next step after pointing to ask. (Montessori-parent treasure basket)"),("百宝篮：“看我找到啥！”","篮子里放三四样好玩的东西（大松果、打蛋器、丝巾）。她举起来给您看时，接住她的“给您看”：“哦，给妈妈看呀！打蛋器！”指给别人看，是“指着要”之后的下一步。（蒙氏家长的百宝篮）"),["Curious","Kind"],("5 min","5分钟"))
add("stack-cups","🥤",("Stacking-cup games","One set of nesting cups, four games: hide a toy under one, nest them by size, stack a tower and knock it down, “find the red one.” About 10 min a day; when it falls, laugh, never scold. (Parent tip)"),("套杯四种玩法","一套套杯，玩四样：扣住藏玩具、按大小套进去、摞高再推倒、“红的在哪儿”。一天十分钟左右。倒了就笑，千万别说她。（家长分享的玩法）"),["Curious","Self-led"],("10 min","10分钟"))
add("tower-steps","🧱",("Road to a 4-block tower","Easiest first: drop blocks into a cup → ring stacker → soft cups or tins → big blocks. Move up only when one feels easy. Falling is part of it. (Parent tip; 3–4 block towers usually come around 15–18 months)"),("一步步搭到四块","从简单的来：积木丢进杯子 → 套圈 → 软杯子或铁罐摞 → 大积木。这一步玩得轻松了再往下走。倒了很正常。（家长分享；搭三四块一般在15–18个月左右）"),["Curious","Brave"],("10 min","10分钟"))
add("trade-and-back","🔄",("Swap and swap back","Turn-taking as a game: “Can I have a turn?” She holds out the toy (or not). You play 3 seconds, hand it right back: “Your turn!” Then offer a trade: “Spoon for the cup?” She learns giving isn’t losing. (Parent tip)"),("换过来、再换回去","把轮流变成游戏：“可以给我玩一下吗？”她给（或不给）都行。您玩三秒，马上还给她：“轮到你啦！”再试试交换：“勺子换杯子好不好？”让她知道给出去不等于没了。（家长分享）"),["Kind","Self-led"],("3 min","3分钟"))
add("stool-stand-steps","🪑",("Stool stand, then steps to you","She stands at a small sturdy stool or the couch playing; you kneel 2–3 steps away with a toy and open arms. Coax, don’t pull: let her let go and come to you. Hold one hand at most, never both arms up high. (Parent tip)"),("扶凳子站，再朝您走","她扶着结实的小凳子或沙发站着玩，您蹲在两三步外，拿着玩具张开手。逗她过来，别拉：让她自己松手走过来。最多牵一只手，别把她两只胳膊高高拎起来。（家长分享）"),["Brave","Healthy"],("5 min","5分钟"))
add("first-scribble","🖍️",("First scribbles","Tape big paper to the high-chair tray or floor; one chunky egg-shaped or palm crayon. You scribble a line, then hand it over. Any mark counts. Crayon goes away when it goes in her mouth. (IG toddler-art parents)"),("第一次涂鸦","大纸贴在餐椅托盘上或地上，给一支粗粗的蛋形蜡笔。您先画一道，再递给她。画出什么都算。放进嘴里就收起来。（Instagram 幼儿美术家长）"),["Curious","Self-led"],("5 min","5分钟"))
add("shape-sorter-circle","⚪",("Shape sorter: circle only","Cover every hole but the circle (tape), give her only round pieces. Add the square next week if it’s easy. (Montessori-parent tip)"),("形状盒：只留圆洞","其他洞用胶带贴住，只留圆洞，只给圆的块。玩得轻松了，下周再开方洞。（蒙氏家长的做法）"),["Curious","Brave"],("5 min","5分钟"))
add("sock-helper","🧦",("Socks in the basket","Real helping job: hand her socks one by one from the laundry, she drops them in the basket. “Thank you, helper!” Also: wipe the table after meals. (@busytoddler-style real jobs)"),("袜子放进篮子","真正的小家务：收衣服时把袜子一只只递给她，让她丢进篮子。“谢谢小帮手！”吃完饭一起擦桌子也算。（Instagram 上很多家长这么做）"),["Kind","Self-led"],("3 min","3分钟"))
add("nature-basket","🍂",("Nature walk basket","Outside with a small basket: collect a big leaf, a pinecone, a stick. Name each one, feel it, smell it. Too-small things stay outside. (Reggio/forest-school parents)"),("散步捡宝贝","带个小篮子出门，捡大叶子、松果、小树枝。一样样说名字，摸摸、闻闻。太小的不带回家。（瑞吉欧、森林学校家长的做法）"),["Curious","Healthy"],("15 min","15分钟"))
add("book-pick","📚",("She picks the book","2–3 board books face-out on a low shelf or basket. Let her choose, hold it, and turn the pages (even backward). Read one page or ten; stop when she’s done. (Parent tip)"),("她自己挑书","两三本纸板书封面朝外放在矮书架或篮子里。让她自己挑、自己拿、自己翻（倒着翻也行）。读一页还是十页都行，她不想看了就停。（家长分享）"),["Self-led","Curious"],("2–5 min","2–5分钟"))
NEW_IDS=["bubbles-more","ready-set-go","open-help-jar","show-me-basket","stack-cups","tower-steps","trade-and-back","stool-stand-steps","first-scribble","shape-sorter-circle","sock-helper","nature-basket","book-pick"]
def plays(L): return carried(L)+[NEW[i][L] for i in NEW_IDS]

VID={
 "qgga0egtdu0":{"title":"3 Shortcuts to Get Your Toddler Talking Sooner","titleZh":"让宝宝早点开口的3个小窍门","channel":"Emma Hubbard","channelZh":"Emma Hubbard（儿科物理治疗师）","length":"4:53","lang":"en"},
 "mFTwsPVn6dk":{"title":"Half Kneel to Stand at Furniture","titleZh":"单膝跪到扶着家具站起来","channel":"Pediatric Physical Therapy Exercises","channelZh":"Pediatric Physical Therapy Exercises（儿科康复）","length":"1:34","lang":"en"},
 "jKT9ICWs6oU":{"title":"Help Your Baby Stand Up from the Middle of the Floor","titleZh":"帮宝宝不扶东西，从地上站起来","channel":"Pediatric Physical Therapy Exercises","channelZh":"Pediatric Physical Therapy Exercises（儿科康复）","length":"1:56","lang":"en"},
 "Dwj2reELIlg":{"title":"Learn Open Cup Drinking For Your Infant With an Occupational Therapist","titleZh":"职业治疗师教：宝宝怎么用敞口杯喝水","channel":"Emerge Pediatric Therapy","channelZh":"Emerge Pediatric Therapy（儿童康复）","length":"2:23","lang":"en"}}

CDC="https://www.cdc.gov/act-early/milestones/15-months.html"
ZTT="https://www.zerotothree.org/wp-content/uploads/2023/03/Year-2_-From-13-24-Months.pdf"
ASHA="https://www.asha.org/public/developmental-milestones/communication-milestones-13-to-18-months/"
PATH="https://pathways.org/activities/sit-to-stand"
SS="https://www.instagram.com/speechsisters/"
EN={}
EN["title"]="Week 9"; EN["age"]="12 months"; EN["dates"]="Nov 16–22, 2026"
EN["now"]=["🧍 Stands alone · still learning sit-to-stand","🛒 Walks fast with the push walker or one hand","🧗 Climbs stairs and playground stuff, up and down","🏊 Swims since June · dips under 1–2 s","🧱 Stacks 2 blocks · uses a spoon","🖊️ Uses the pointer pen on her music book","🚪 Opens/closes closets, the toy faucet · copies adults","👏 Copies clapping and bye-bye","👉 Points + calls out to ask, very confidently","🗣️ baba/mama faded since pointing took off","✋ “Mine!” Won’t give things up without agreeing","🍽️ Wants what we eat · bigger chunks · less milk","🥛 Whole milk since Nov 3 · no open cup yet","🎒 Goes to daycare · still mouths things"]
EN["oneLiner"]="One year old and very much <b>her own person</b>. This week, three things: <b>turn her points into words</b> (name it, pause, give it anyway), <b>play her way up from the floor</b>, and <b>start a tiny open cup</b>. Plus a new <b>reading</b> rhythm: short and often."
EN["bigThree"]=[
{"icon":"👉","title":"Turn her points into words","sub":"Words · all day","roots":["Curious","Kind"],"lines":[
"<b>When:</b> every time she points and calls out. Aim for 10 good moments a day: meals, bath, getting dressed, books.",
"<b>How:</b> ① Name it, short: “<b>Banana.</b>” ② <b>Pause 5–10 seconds</b>, looking at her, for any sound, look, or sign. ③ Then give it, <b>even if she only points</b>. Never hold it back until she says a word: pressure makes talking harder, and meltdowns don’t teach.",
"<b>Two choices:</b> hold up two things: “Apple or banana?” A point or a sound is her answer: “Banana! Here’s banana.”",
"<b>Three power words:</b> say “<b>more</b>,” “<b>open</b>,” “<b>help</b>” many times a day, with the MORE sign (see Baby signs). Give a little at a time so “more” has a reason.",
"<b>Expand, don’t quiz:</b> she says “ba” → “<b>Ball!</b> Big ball.” Not “Say ball!” Mandarin, English, or both: each person speaks their own language.",
"<b>Gently, for later:</b> her early baba/mama faded once pointing took off. That’s common, but mention it at her next checkup (CDC: tell the doctor about any skill that fades). Keep a two-week log of sounds, signs, and words to bring."],"videos":["qgga0egtdu0"],"refs":[{"label":"ASHA: communication at 13–18 months","url":ASHA},{"label":"Speech Sisters (SLP parent tips)","url":SS}]},
{"icon":"🧸","title":"Up from the floor: sit-to-stand play","sub":"Body · 2 × 5 min a day","roots":["Brave","Healthy"],"lines":[
"<b>When:</b> two short floor sessions a day, when she’s fresh (after nap, before dinner).",
"<b>How 1, half-kneel:</b> she kneels at the couch; put a toy on the cushion just out of reach. She brings one foot forward and pushes up. Next time, the other leg leads.",
"<b>How 2, lap-to-stand:</b> she sits on your lap facing the couch, feet flat on the floor. A light hand on her hips, <b>lean her body slightly forward</b>, and she stands; then sits back onto your lap. Repeat 5 times.",
"<b>How 3, squat:</b> once she’s up, put toys at knee height, then on the floor, so she squats and comes back up.",
"<b>Steps:</b> stand her at a sturdy stool, kneel 2–3 steps away with open arms, and let her come. Hold one hand at most, not both arms up high.",
"<b>Say:</b> “Up… you did it!” If she plops: “Plop! Again?” Calm, no big fuss either way."],"videos":["mFTwsPVn6dk","jKT9ICWs6oU"],"refs":[{"label":"Pathways.org: sit-to-stand activity","url":PATH}]},
{"icon":"🥛","title":"First open-cup sips","sub":"Eating · 1–2 meals","roots":["Healthy","Self-led"],"lines":[
"<b>When:</b> at 1–2 meals a day, sitting in her high chair. Start with water.",
"<b>How:</b> a <b>tiny</b> cup (shot-glass size), 1–2 sips of water in it. Hold it with her, both hands on the cup, bring it to her lip, tip slowly, let her take a sip, then set it down together.",
"<b>Next:</b> after a few days, let her hold it with your hand just under. Spills are practice: keep a towel close, no fuss.",
"<b>Say:</b> “Sip… sip. You did it!” Spill: “Oops, water fell. Wipe!”",
"<b>Milk:</b> whole milk in her cup or straw cup at meals is fine; keep it to about 16 oz/day. She’s eating more family food, so less milk is OK (see "+MK+"Milk at one</a>)."],"videos":["Dwj2reELIlg"]}]
EN["cards"]=[
{"icon":"🦵","title":"Where she is now: body","sub":"Strong, almost walking","roots":["Brave","Healthy"],"lines":["She <b>stands alone</b>, climbs stairs and playground equipment up and down, walks fast with the push walker or one hand, and dips underwater calmly. That’s a strong, brave mover.","The missing piece is getting <b>up from sitting with nothing to hold</b>. It often comes <b>around 13–14 months, sometimes after first steps</b>, so she isn’t behind.","<b>Heading toward (next 3 months):</b> a few steps alone, squatting to pick things up, getting on and off the couch, then early running. Anywhere up to ~18 months for walking alone is normal."]},
{"icon":"🧠","title":"Where she is now: hands and thinking","sub":"A little engineer","roots":["Curious","Self-led"],"lines":["She stacks 2 blocks, uses a spoon, and taps a pointer pen to make music: she already <b>knows touching a spot makes something happen</b> (cause and effect). Those are 15-month skills.","She <b>loves figuring out how things work</b> (doors, faucets, lids) and doesn’t love sitting and listening. So: short, hands-on, and let her lead.","<b>Next:</b> 3–4 block towers, scribbling, a simple shape sorter, fill-and-dump, real helping jobs."]},
{"icon":"🗣️","title":"Where she is now: words and understanding","sub":"Understands much more than she says","roots":["Curious","Kind"],"lines":["<b>She can:</b> point to ask, clap and wave when you do, understand familiar names (Mama, milk, ball), simple routines (“bath time”), and often “give me” with your hand out.","<b>Not yet:</b> “wait,” “later,” “gently,” reasons, or “don’t” (she hears the action word). So say what TO do: “Feet on the floor,” not “Don’t climb.”","Words often pause while a big motor skill takes off; pointing has become her main tool. <b>Coming next:</b> trying 1–2 words or word-bits (“ba” for ball counts) by ~15 months, and <b>pointing to show</b> you things, not just to ask."],"refs":[{"label":"CDC: milestones by 15 months","url":CDC}]},
{"icon":"💛","title":"Where she is now: feelings and self","sub":"“Mine!” is healthy","roots":["Secure","Self-led"],"lines":["She won’t let you take something unless she agrees. That’s <b>her sense of self growing</b>: “This is mine, and I get a say.” It’s a good sign.","Asking first is the right instinct. See <b>What to say</b> for the exact words (ask, trade, warn-and-count, two choices).","<b>Coming next:</b> more “no,” more big feelings, showing you things she likes, and checking you’re near while she explores. The whole family uses the same simple rules (see "+FP+"Our family’s way</a>)."]},
{"icon":"🍽️","title":"Eating: family food, chunks, and spitting out","sub":"Exploring with her mouth","roots":["Healthy","Self-led"],"lines":["She wants what you eat and likes bigger pieces: great. Offer soft long strips she can bite; quarter round foods; always seated and watched.","Holding beef or sardines in her mouth for minutes, then spitting them out, is <b>normal oral exploration</b>: she’s learning texture and how to move food around.","<b>Do:</b> eat together, chew big and slow so she can see, say “chomp, chomp.” <b>Don’t:</b> fish it out, praise or scold the spit. Stay neutral. Tell the doctor if she gags often or swallows almost nothing."]},
{"icon":"📚","title":"Reading: short and often","sub":"New this week","roots":["Curious","Kind"],"lines":["Keep the calm <b>1–2 bedtime books</b>. Add <b>2–3 tiny reading moments</b> in the day (2–5 min): after nap, after breakfast, in the basket corner.","<b>She leads:</b> she picks the book, turns the pages (backward is fine), and stops when she’s done. Reading three pages counts.","<b>Read with her, not to her:</b> point and name, add sound effects (“woof!”), <b>pause 5 seconds</b> for her point or sound, then expand it: she points at the dog → “Yes, a <b>big dog</b>! Woof!”","<b>Repeat favorites</b> again and again; that’s how words stick. Use her pointer-pen book the same way: name, pause, then press.","<b>Good books now:</b> lift-the-flap, touch-and-feel, one picture per page, real-photo first-words books, and repetitive rhythm books like <i>Brown Bear, Brown Bear</i> and <i>Dear Zoo</i>.","<b>Songs count as reading:</b> Itsy Bitsy Spider, Pat-a-Cake, Chinese finger rhymes (手指谣), always with the motions."],"refs":[{"label":"Reach Out and Read: reading with babies and toddlers","url":"https://www.reachoutandread.org/"}]},
{"icon":"🦷","title":"Mouthing at daycare","sub":"Normal, made safer","roots":["Healthy","Secure"],"lines":["Mouthing is still how she explores, and she’s teething. It fades slowly through the second year.","Ask the teacher how they handle it: toys cleaned daily, nothing smaller than a toilet-paper tube opening, no button batteries or loose magnets.","At home: a yes-to-mouth basket, and swap rather than grab."],"refs":[{"label":"AAP/HealthyChildren: Choking prevention","url":"https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx"}]},
{"icon":"🔭","title":"Where the stage is heading","sub":"Next 3–6 months","roots":["Curious","Brave"],"lines":["<b>Body:</b> first steps alone, squat and stand, on and off the couch, early running.","<b>Hands:</b> towers of 3–4, scribbles, using things the right way (cup, spoon, toy phone).","<b>Words:</b> a few words or word-bits, then 3+ by 18 months; much more understanding.","<b>Self:</b> more “no” and “mine,” more pride (“I did it!”), more wanting to help with real jobs."],"refs":[{"label":"ZERO TO THREE: Year 2, 13–24 months","url":ZTT}]}]
EN["daily"]=["👉 Answer her points: name it, pause 5–10 s, then give it","🔁 Say “more,” “open,” “help” in real moments","🧸 Sit-to-stand play, twice (half-kneel, lap-to-stand, squat)","🥛 Tiny open cup: 1–2 sips of water at a meal, with help","📚 2–3 short reading moments + calm 1–2 bedtime books","🤟 EAT, MILK, ALL DONE, MORE, saying the word each time","🤝 Ask or trade before taking something from her hand","🍽️ Eat together, chew slowly where she can see","🦷 Swap, don’t grab, when she mouths","Brush teeth twice (rice-grain smear)"]
EN["todos"]=["Get a tiny cup (shot-glass size or a small open cup)","Book basket: 3–5 board books face-out, low, where she plays","Start a 2-week log of sounds, signs, and words for the checkup","Write checkup questions: faded words, length, iron, milk amount","Show daycare teachers the MORE sign; ask how they handle mouthing","Make an “Open? Help?” clear jar with a favorite toy inside"]
EN["quiz"]=[
{"q":"She points at the water bottle. You wait until she says “wa” before handing it over.","a":"dont","why":"Name it, pause, then give it anyway. Holding it hostage adds pressure and meltdowns."},
{"q":"She points at the dog in the book. You say “Yes, a big dog! Woof!”","a":"do","why":"You named it, added a word and a sound: that’s how words grow."},
{"q":"She’s clutching a spoon you need. You pull it out of her hand.","a":"dont","why":"Ask or trade first. Take right away only when it’s unsafe, then offer a safe yes."},
{"q":"She holds meat in her mouth, then spits it out. You stay calm and keep eating.","a":"do","why":"Normal mouth exploration. Neutral, and show her how you chew."},
{"q":"Read a long story to the end even when she climbs off your lap.","a":"dont","why":"Short and often wins. Stop when she’s done; come back later."},
{"q":"Lean her body slightly forward as she pushes up from sitting.","a":"do","why":"Weight over her feet is the move she’s learning. Light hands at the hips only."},
{"q":"Give her a big sippy cup of milk to carry around all day.","a":"dont","why":"Milk at meals and snacks, about 16 oz/day. Water in the tiny open cup for practice."}]
EN["scripts"]=[
{"icon":"✋","when":"She won’t let go of something","steps":[{"do":"Ask, and wait for her answer.","say":"Can I have a turn? (可以给我玩一下吗？)"},{"do":"If she says no, respect it.","say":"Okay, when you’re done, give it to me."},{"do":"Or trade.","say":"You hold the lid, I’ll take the keys."},{"do":"Or warn and count.","say":"In a moment it’s Mama’s turn… one, two… thank you!"},{"do":"Or two yeses.","say":"Put it in the basket, or Mama helps?"},{"do":"If she’s upset, name it and hold the limit.","say":"You wanted to keep it. You’re mad. It’s okay to be mad."}],"note":"Only take it straight away if it’s dangerous, then offer a safe yes: “Not this. You can have this.” Family rule, every time: dirty = OK; dangerous = remove calmly; crying = comfort, then something new."},
{"icon":"👉","when":"She points and shouts","steps":[{"do":"Look and name it.","say":"Banana."},{"do":"Pause 5–10 seconds, looking at her.","say":"(wait)"},{"do":"Give it, and say it again.","say":"Banana! Here’s banana."}],"note":"Even if she only points: give it. Words come with no pressure."},
{"icon":"🍖","when":"She holds food in her mouth, then spits it out","steps":[{"do":"Stay neutral.","say":"All done with that one? Okay."},{"do":"Show chewing.","say":"Mama chews… chomp, chomp."}],"note":"No fishing it out, no praise or scolding. Offer again another day."},
{"icon":"📚","when":"She grabs the book and turns pages before you finish","steps":[{"do":"Follow her page.","say":"Oh, you turned it! What’s here?"},{"do":"Point, name, pause.","say":"A duck! Quack… (wait)"}],"note":"The story isn’t the point; the talking is."},
{"icon":"🦷","when":"Something not-OK goes in her mouth","steps":[{"do":"Calm, close, open hand.","say":"Can Mama have that?"},{"do":"Trade.","say":"Not for mouths. This one is for mouths!"}],"note":"No chasing; it turns into a game."}]
EN["details"]=[
{"icon":"👉","title":"Why words can fade when pointing takes off","roots":["Curious","Kind"],"lines":["Babies often focus on one big skill at a time. Pointing works so well that words can take a back seat for a few weeks.","Pointing is a strong predictor of later words, especially when adults name what she points at.","Still, any lost skill is worth mentioning calmly to the pediatrician, who may suggest a quick developmental screening. A free early-intervention evaluation can be requested by parents directly in most US states."],"refs":[{"label":"ASHA: communication at 13–18 months","url":ASHA},{"label":"CDC: milestones by 15 months","url":CDC}]},
{"icon":"🧸","title":"Why sit-to-stand comes late","roots":["Brave","Healthy"],"lines":["Standing up in open space means shifting weight forward over her feet from a crouch, with nothing to pull on. Many babies take first steps before they can do it. Either order is fine."],"refs":[{"label":"Pathways.org: sit-to-stand","url":PATH}]},
{"icon":"🍽️","title":"Why she holds food then spits it out","roots":["Healthy"],"lines":["Moving a chunk around her mouth teaches her tongue and jaw what to do with new textures. Many toddlers ‘taste-test’ like this for weeks. Neutral repetition is what helps."]}]
EN["watch"]=["<b>Loses skills</b> she had: stops pointing, waving, babbling, or turning to her name","By ~15 months: no new word attempts at all (word-bits count)","Doesn’t understand “give me” or simple routines by ~15 months","By ~18 months: not walking alone","Gags or chokes often at meals, or swallows almost nothing","Choking: can’t cough, cry, or breathe, or turns blue → call 911, start back blows/chest thrusts","A swallowed <b>button battery or magnet</b>, even if she seems fine → ER now","Fever 100.4°F / 38°C or higher in a baby who seems really unwell"]
EN["sources"]=[{"label":"CDC: milestones by 15 months","url":CDC},{"label":"ZERO TO THREE: Year 2, 13–24 months (PDF)","url":ZTT},{"label":"ASHA: communication milestones 13–18 months","url":ASHA},{"label":"Pathways.org: sit-to-stand","url":PATH},{"label":"Speech Sisters (SLP parent tips, Instagram)","url":SS},{"label":"AAP/HealthyChildren: Choking prevention","url":"https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx"},{"label":"AAP/HealthyChildren: Recommended drinks for young children","url":"https://www.healthychildren.org/English/healthy-living/nutrition/Pages/Recommended-Drinks-for-Young-Children-Ages-0-5.aspx"},{"label":"Reach Out and Read","url":"https://www.reachoutandread.org/"}]

ZH={}
ZH["title"]="第9周"; ZH["age"]="1岁"; ZH["dates"]="2026年11月16日–22日"
ZH["now"]=["🧍 能自己站 · 从坐到站还在学","🛒 推着学步车或牵一只手走得飞快","🧗 楼梯、游乐设施上上下下都会","🏊 六月开始游泳 · 能潜水一两秒","🧱 会摞两块积木 · 会用勺子","🖊️ 会用点读笔点书放音乐","🚪 会开关柜门、玩具水龙头 · 爱学大人","👏 会跟着拍手、拜拜","👉 指着东西“啊啊”要，特别有底气","🗣️ 会指以后，爸爸妈妈反而说得少了","✋ 手里的东西，她不同意就不给","🍽️ 想吃大人吃的 · 爱吃大块 · 奶喝得少了","🥛 11月3日开始喝全脂奶 · 还没用过敞口杯","🎒 上托班了 · 还爱往嘴里塞东西"]
ZH["oneLiner"]="满一岁了，越来越<b>有自己的主意</b>。这周三件事：<b>把她的“指”变成话</b>（说出来、等一等、照样给）、<b>玩着练从地上站起来</b>、<b>开始用小敞口杯喝水</b>。另外加一个<b>读书</b>的新习惯：每次短短的，一天多几次。"
ZH["bigThree"]=[
{"icon":"👉","title":"把她的“指”变成话","sub":"说话 · 全天","roots":["Curious","Kind"],"lines":[
"<b>什么时候：</b>她一边指一边叫，每次都接。一天争取好好接十次：吃饭、洗澡、穿衣服、看书。",
"<b>怎么接：</b>① 简单说出来：“<b>香蕉。</b>” ② 看着她<b>等5到10秒</b>，等她出个声、看一眼或比个手势。③ 然后就给，<b>她光指不说也照样给</b>。千万别“不说就不给”：一逼她更不愿开口，闹起来也学不到东西。",
"<b>让她选：</b>两样东西举起来：“苹果还是香蕉？”她指一下、哼一声就算回答：“香蕉！给你。”",
"<b>三个好用的词：</b>“<b>还要</b>”“<b>打开</b>”“<b>帮忙</b>”，一天说很多遍，“还要”配上手势（见宝宝手语）。东西一次少给点，她才有机会“还要”。",
"<b>跟着说，别考她：</b>她说“ba”→“<b>球！</b>大球。”别说“说‘球’！”。说中文、英文或者两样都说都行，每个人说自己最顺口的语言。",
"<b>轻轻记一笔：</b>她之前会叫的爸爸妈妈，会指以后说得少了。这很常见，但下次体检跟医生提一句（美国疾控中心建议：会过又不会了的本事都告诉医生）。记两周她发的音、比的手势、说的词，带去给医生看。"],"videos":["qgga0egtdu0"],"refs":[{"label":"美国言语听力协会：13–18个月的交流能力（英文）","url":ASHA},{"label":"Speech Sisters（语言治疗师，Instagram，英文）","url":SS}]},
{"icon":"🧸","title":"玩着练：从地上站起来","sub":"大运动 · 一天两次，每次5分钟","roots":["Brave","Healthy"],"lines":[
"<b>什么时候：</b>一天两次，挑她精神好的时候（睡醒后、晚饭前）。",
"<b>玩法一，单膝跪：</b>她跪在沙发前，把玩具放在沙发垫上、够不着一点点。她会一只脚往前迈、撑起来。下次换另一条腿先迈。",
"<b>玩法二，从腿上站：</b>她坐在您腿上，面朝沙发，两脚踩地。您手轻轻扶着她的胯，<b>让她身体稍微往前倾</b>，她就站起来了；再坐回您腿上。来五次。",
"<b>玩法三，蹲下：</b>站起来以后，把玩具先放膝盖高，再放地上，让她蹲下去拿、再站起来。",
"<b>迈步：</b>让她扶着结实的小凳子站，您蹲在两三步外张开手等她过来。最多牵一只手，别把她两只胳膊高高拎着走。",
"<b>可以说：</b>“起来……站起来啦！”坐下了：“扑通！再来？”语气平静，成不成都别大惊小怪。"],"videos":["mFTwsPVn6dk","jKT9ICWs6oU"],"refs":[{"label":"Pathways.org：从坐到站练习（英文）","url":PATH}]},
{"icon":"🥛","title":"开始用敞口杯喝两口","sub":"吃喝 · 一天一两顿","roots":["Healthy","Self-led"],"lines":[
"<b>什么时候：</b>一天一两顿饭，坐在餐椅上。先用白水。",
"<b>怎么练：</b>用一个<b>很小</b>的杯子（小酒杯那么大），倒一两口水。您和她一起端，两只手都扶着杯子，送到她嘴边，慢慢倾，让她喝一小口，再一起放下。",
"<b>过几天：</b>让她自己端，您的手在下面虚托着。洒了就是在练，旁边放块毛巾，别着急。",
"<b>可以说：</b>“喝一口……真棒，自己喝的！”洒了：“哎呀，水掉了，擦一擦！”",
"<b>喝奶：</b>吃饭时用杯子或吸管杯喝全脂奶没问题，一天大约480毫升（16盎司）就够。她饭吃得多了，奶少点没关系（见"+MK+"一岁转牛奶</a>）。"],"videos":["Dwj2reELIlg"]}]
ZH["cards"]=[
{"icon":"🦵","title":"她现在：身体","sub":"很有劲，快会走了","roots":["Brave","Healthy"],"lines":["能<b>自己站</b>，楼梯和游乐设施上上下下，推学步车或牵一只手走得飞快，潜水也不慌。大运动又强又勇敢。","还差一步：<b>不扶东西从坐着站起来</b>。很多宝宝<b>13–14个月左右</b>才会，有的先会走才会这个，所以她一点都不晚。","<b>接下来三个月：</b>自己走几步、蹲下捡东西再站起来、自己上下沙发，然后开始小跑。18个月之前会自己走都正常。"]},
{"icon":"🧠","title":"她现在：小手和脑子","sub":"小小工程师","roots":["Curious","Self-led"],"lines":["会摞两块积木、会用勺子、会拿点读笔点出音乐：她已经<b>明白点一下就会有反应</b>（因果关系）。这些都是15个月的本事。","她<b>最爱琢磨东西怎么弄</b>（门、水龙头、盖子），不爱坐着听。所以：时间短、动手玩、让她带头。","<b>接下来：</b>搭三四块积木、乱涂乱画、简单的形状盒、装了倒、帮着做点真家务。"]},
{"icon":"🗣️","title":"她现在：说话和听懂","sub":"懂的比说的多得多","roots":["Curious","Kind"],"lines":["<b>她能：</b>指着要东西，您拍手挥手她跟着做，听得懂熟悉的名字（妈妈、奶、球）、简单的日常（“洗澡啦”），您伸手说“给我”她常常会给。","<b>还听不懂：</b>“等一下”“待会儿”“轻一点”、讲道理、“不要……”（她只听进去后面那个动作）。所以要说该做什么：“脚踩地上”，别说“不许爬”。","大运动突飞猛进时，说话常常会停一停；现在“指”是她最好用的工具。<b>接下来：</b>15个月左右试着说一两个词或半个词（“ba”就是球，算数），还会<b>指给您看</b>东西，不光是指着要。"],"refs":[{"label":"美国疾控中心：15个月里程碑（英文）","url":CDC}]},
{"icon":"💛","title":"她现在：情绪和“我”","sub":"“我的！”是好事","roots":["Secure","Self-led"],"lines":["手里的东西，她不同意您就拿不走。这是<b>自我意识在长</b>：“这是我的，我说了算。”是好兆头。","先问她，这个直觉是对的。具体怎么说，见下面<b>怎么说</b>（问一问、换一换、数一数、两个都行的选择）。","<b>接下来：</b>会更多说“不”、情绪更大，会拿东西给您看，玩着玩着回头确认您在不在。全家用同样简单的规矩（见"+FP+"家庭教养原则</a>）。"]},
{"icon":"🍽️","title":"吃饭：吃大人的饭、爱大块、含着再吐","sub":"用嘴巴探索","roots":["Healthy","Self-led"],"lines":["想吃大人吃的、爱吃大块，很好。给软软的长条让她自己咬；圆的东西切成四瓣；一定坐着吃、大人看着。","牛肉、沙丁鱼含在嘴里好几分钟再吐出来，是<b>正常的口腔探索</b>：她在学怎么对付新口感、舌头怎么搬运食物。","<b>要：</b>一起吃，大口慢慢嚼给她看，说“嚼嚼嚼”。<b>别：</b>伸手抠出来，也别夸或说她吐。表情平平的就好。如果常常干呕，或者几乎什么都不咽，就告诉医生。"]},
{"icon":"📚","title":"读书：每次短一点，次数多一点","sub":"这周新加","roots":["Curious","Kind"],"lines":["睡前<b>一两本</b>照旧，安安静静的。白天再加<b>两三次小读书</b>，每次两到五分钟：睡醒后、早饭后、书篮边上。","<b>她做主：</b>她挑书、她翻页（倒着翻也行），她不想看就停。读三页也算读了。","<b>陪她读，不是读给她听：</b>指着说名字，加点声音（“汪汪！”），<b>停5秒</b>等她指或发音，再帮她说长一点：她指着狗 →“对，<b>大狗狗</b>！汪汪！”","<b>喜欢的书反复读</b>，词就是这么记住的。点读书也一样：先说名字，停一停，再点。","<b>现在适合的书：</b>翻翻书、触摸书、一页一个图、实物照片认知书，还有重复句式的书，比如《棕色的熊，棕色的熊》《亲爱的动物园》。","<b>唱儿歌也算读书：</b>《小蜘蛛》、拍拍手、各种手指谣，都要配上动作。"],"refs":[{"label":"Reach Out and Read：和小宝宝一起读书（英文）","url":"https://www.reachoutandread.org/"}]},
{"icon":"🦷","title":"在托班啃东西","sub":"正常，做好安全就行","roots":["Healthy","Secure"],"lines":["往嘴里放东西还是她探索的方式，加上在长牙。一岁到两岁会慢慢少。","问问老师怎么处理：玩具每天消毒，比卫生纸筒口小的东西不放在宝宝能拿到的地方，没有纽扣电池和散落的小磁铁。","在家：准备一篮“可以啃的”，看到她啃不该啃的就换，别硬抢。"],"refs":[{"label":"美国儿科学会：预防噎呛（英文）","url":"https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx"}]},
{"icon":"🔭","title":"接下来会怎样","sub":"之后3–6个月","roots":["Curious","Brave"],"lines":["<b>身体：</b>自己迈出第一步，蹲下再站起，上下沙发，开始小跑。","<b>小手：</b>搭三四块，乱涂乱画，东西会“正确地”用（杯子、勺子、玩具电话）。","<b>说话：</b>先有几个词或半个词，18个月左右三个以上；听懂的会多很多。","<b>自我：</b>更多“不要”“我的”，更多得意（“我做到了！”），更想帮大人干活。"],"refs":[{"label":"ZERO TO THREE：宝宝第二年，13–24个月（英文PDF）","url":ZTT}]}]
ZH["daily"]=["👉 接住她的“指”：说出来、等5–10秒、再给她","🔁 在真实场景里说“还要”“打开”“帮忙”","🧸 从坐到站的小游戏，两次（单膝跪、从腿上站、蹲下捡）","🥛 小敞口杯：吃饭时喝一两口水，大人帮着","📚 白天两三次小读书 + 睡前安静读一两本","🤟 比“吃”“奶”“吃完了”“还要”，边比边说","🤝 要拿她手里的东西，先问或者换","🍽️ 一起吃饭，慢慢嚼给她看","🦷 她啃了不该啃的，换，别抢","刷牙两次（米粒大小的牙膏）"]
ZH["todos"]=["买个小杯子（小酒杯大小或小敞口杯）","弄个书篮：三到五本纸板书，封面朝外，放在她玩的地方","开始记两周：她发的音、比的手势、说的词，体检带去","写下体检要问的：说的词变少了、身长、补铁、奶量","把“还要”的手势比给托班老师看；问问他们怎么处理啃东西","准备一个“打开？帮忙？”透明罐，里面放她喜欢的玩具"]
ZH["quiz"]=[
{"q":"她指着水杯，您非等她说出“水”才给。","a":"dont","why":"说出来、等一等，然后照样给。拿东西“要挟”她只会更有压力、更容易闹。"},
{"q":"她指着书上的狗，您说：“对，大狗狗！汪汪！”","a":"do","why":"说了名字，又加了一个词和声音，词就是这么长出来的。"},
{"q":"她手里攥着您要用的勺子，您直接抽走。","a":"dont","why":"先问或者换。只有危险的东西才马上拿走，再给她一个能玩的。"},
{"q":"她把肉含在嘴里，最后吐了，您不动声色继续吃。","a":"do","why":"正常的口腔探索。表情平平的，嚼给她看就好。"},
{"q":"她从腿上爬走了，您还坚持把长故事读完。","a":"dont","why":"短一点、多几次更好。她不想看就停，过会儿再读。"},
{"q":"她从坐着往上撑时，扶着她身体稍微往前倾。","a":"do","why":"把重心移到脚上，正是她在学的动作。手只轻轻扶胯。"},
{"q":"给她一大杯牛奶，让她拿着走来走去喝一天。","a":"dont","why":"奶在正餐和点心时喝，一天大约480毫升。小敞口杯用白水练。"}]
ZH["scripts"]=[
{"icon":"✋","when":"她攥着东西不肯给","steps":[{"do":"先问，等她回应。","say":"可以给我玩一下吗？"},{"do":"她不给，就尊重她。","say":"好，等你玩完再给我。"},{"do":"或者换一换。","say":"你拿着盖子，妈妈拿钥匙，好不好？"},{"do":"或者提前说、数一数。","say":"等一下轮到妈妈哦……一、二……谢谢你！"},{"do":"或者给两个都行的选择。","say":"放进篮子里，还是妈妈帮你放？"},{"do":"她不高兴了，说出她的感受，规矩不变。","say":"你还想玩，生气了。生气没关系。"}],"note":"只有危险的东西才马上拿走，然后马上给一个能玩的：“这个不行，这个可以。”全家统一：脏了没关系；危险的每次都平静地拿走；哭了先抱抱，再换个新玩意。"},
{"icon":"👉","when":"她指着东西大叫","steps":[{"do":"看过去，说出来。","say":"香蕉。"},{"do":"看着她，等5到10秒。","say":"（等一等）"},{"do":"给她，再说一遍。","say":"香蕉！给你香蕉。"}],"note":"她光指不说也给。没有压力，话才会来。"},
{"icon":"🍖","when":"她把食物含半天又吐出来","steps":[{"do":"表情平平的。","say":"这块不吃啦？好。"},{"do":"嚼给她看。","say":"妈妈嚼嚼嚼……"}],"note":"别抠，别夸也别说她。改天再给。"},
{"icon":"📚","when":"书还没读完，她抢过去自己翻","steps":[{"do":"跟着她翻到的那页。","say":"哦，你翻过来啦！这是什么？"},{"do":"指一指、说一说、等一等。","say":"小鸭子！嘎嘎……（等她）"}],"note":"重点不是讲完故事，而是一来一往地“聊”。"},
{"icon":"🦷","when":"她把不能吃的东西放进嘴里","steps":[{"do":"别慌，靠近，摊开手。","say":"给妈妈好吗？"},{"do":"换一个。","say":"这个不能放嘴里，这个可以！"}],"note":"别追着抢，不然她会当成游戏。"}]
ZH["details"]=[
{"icon":"👉","title":"为什么会指了，说的反而少了","roots":["Curious","Kind"],"lines":["宝宝常常一阵子专攻一样大本事。“指”太好用了，说话就可能先放一放，过几周再回来。","会指，是以后说话的好苗头，尤其是大人能接住、说出她指的东西。","不过，会过又不会了的本事，都值得心平气和地跟儿科医生提一下，医生可能建议做个简单的发育筛查。在美国大多数州，家长也可以自己申请免费的早期干预评估。"],"refs":[{"label":"美国言语听力协会：13–18个月的交流能力（英文）","url":ASHA},{"label":"美国疾控中心：15个月里程碑（英文）","url":CDC}]},
{"icon":"🧸","title":"为什么“从坐到站”学得晚","roots":["Brave","Healthy"],"lines":["不扶东西站起来，要从蹲着把重心往前移到脚上，手上没有可以借力的地方。很多宝宝先会走才会这个，哪个先都正常。"],"refs":[{"label":"Pathways.org：从坐到站（英文）","url":PATH}]},
{"icon":"🍽️","title":"为什么含着再吐出来","roots":["Healthy"],"lines":["把一块食物在嘴里挪来挪去，是在教舌头和下巴怎么对付新口感。很多宝宝会这样“试吃”好几周。大人淡定、多给几次，最管用。"]}]
ZH["watch"]=["会的本事<b>退步了</b>：不指了、不挥手、不咿呀、叫名字不回头","15个月左右还完全不试着说词（半个词也算）","15个月左右还听不懂“给我”或简单的日常指令","18个月左右还不能自己走","吃饭常常干呕、噎着，或者几乎什么都不咽","噎住了：咳不出、哭不出、喘不上气、发紫 → 马上打911，同时拍背/压胸","吞了<b>纽扣电池或磁铁</b>，看着没事也要马上去急诊","发烧38°C以上，而且精神很差"]
ZH["sources"]=[{"label":"美国疾控中心：15个月里程碑（英文）","url":CDC},{"label":"ZERO TO THREE：宝宝第二年（英文PDF）","url":ZTT},{"label":"美国言语听力协会：13–18个月交流能力（英文）","url":ASHA},{"label":"Pathways.org：从坐到站（英文）","url":PATH},{"label":"Speech Sisters（语言治疗师，Instagram，英文）","url":SS},{"label":"美国儿科学会：预防噎呛（英文）","url":"https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx"},{"label":"美国儿科学会：小宝宝该喝什么（英文）","url":"https://www.healthychildren.org/English/healthy-living/nutrition/Pages/Recommended-Drinks-for-Young-Children-Ages-0-5.aspx"},{"label":"Reach Out and Read（英文）","url":"https://www.reachoutandread.org/"}]

def signs(L):
    s=copy.deepcopy(W8[L]["signs"])
    if L=="en":
        s["intro"]="Keep <b>EAT</b>, <b>ALL DONE</b>, <b>MILK</b>, and add one: <b>MORE</b>. She’s pointing to ask, and MORE gives that point a sign. Just <b>say</b> “open” and “help” for now; their signs can come once MORE sticks. Show the daycare teachers MORE too."
        s["items"].append({"id":"more","emoji":"➕","name":"MORE","sub":"Snacks, bubbles, tickles, songs","lines":["<b>How:</b> both hands pinched (fingertips to thumb), tap the fingertips together twice.","<b>When:</b> give a little at a time (two pieces of banana, three bubbles), pause, then: “<b>More?</b>” + sign. Any reach or sound counts → give more right away.","<b>Why now:</b> she points to request all day. MORE is the most useful first “asking” sign, and it works at meals and in play."],"images":[{"src":"assets/signs/more.svg","alt":"MORE sign: 1, both hands pinched, fingertips to thumbs, apart; 2, the fingertips tap together, twice.","caption":"① Pinch both hands → ② tap the fingertips together, twice."}]})
    else:
        s["intro"]="“<b>吃</b>”“<b>吃完了</b>”“<b>奶</b>”接着比，再加一个：“<b>还要</b>”。她整天指着要东西，“还要”正好给她的“指”配个手势。“打开”“帮忙”这周先<b>说</b>，等“还要”比顺了再加手势。也比给托班老师看看。"
        s["items"].append({"id":"more","emoji":"➕","name":"还要","sub":"零食、泡泡、挠痒痒、唱歌","lines":["<b>怎么比：</b>两只手都捏成一撮（指尖碰拇指），两手指尖对着碰两下。","<b>什么时候比：</b>一次少给一点（两块香蕉、三个泡泡），停一下，再问：“<b>还要</b>吗？”同时比。她伸手、出声都算 → 马上再给。","<b>为什么现在加：</b>她一天到晚指着要东西。“还要”是最好用的第一个“要东西”的手势，吃饭玩耍都用得上。"],"images":[{"src":"assets/signs/more.svg","alt":"“还要”的手语：1. 两手捏成一撮，分开；2. 两手指尖对碰两下。","caption":"① 两手捏成一撮 → ② 指尖对碰两下"}]})
    return s

def tl(L):
    t=copy.deepcopy(W8[L]["timeline"])
    if L=="en":
        t["steps"][1]["note"]="Stands well alone (now)"; t["steps"][2]["note"]="Hands down, bottom up, push (working on it)"
    else:
        t["steps"][1]["note"]="能自己站稳（现在）"; t["steps"][2]["note"]="手撑地、屁股撅起、往上推（正在练）"
    return t

out={"id":"week-09","emoji":"🗣️","start":"2026-11-16","end":"2026-11-22","perLang":True,"videos":VID}
for L,B in (("en",EN),("zh",ZH)):
    B["signs"]=signs(L); B["timeline"]=tl(L); B["plays"]=plays(L)
    order=list(W8[L].keys())
    out[L]={k:B[k] for k in order}

# ---- Nov 15 trim (Melody): milk transition done, daycare going well → no milk-transition or daycare-adjustment content ----
def trim(o):
    e,z=o["en"],o["zh"]
    e["now"][11]="🍽️ Wants what we eat · prefers bigger chunks"; z["now"][11]="🍽️ 想吃大人吃的 · 爱吃大块"
    e["now"][12]="🥤 Hasn’t tried an open cup yet"; z["now"][12]="🥤 还没用过敞口杯"
    e["now"][13]="🦷 Still mouths things"; z["now"][13]="🦷 还爱往嘴里塞东西"
    for L in (e,z):
        b=L["bigThree"][2]; b["lines"]=b["lines"][:4]
    e["bigThree"][2]["title"]="First open-cup sips"; e["bigThree"][2]["sub"]="Drinking skill · 1–2 meals"
    z["bigThree"][2]["sub"]="喝水本领 · 一天一两顿"
    e["bigThree"][2]["lines"].append("<b>Why it matters:</b> sipping from an open cup trains lip closure and controlled swallowing, the same mouth skills she uses for chewing and talking.")
    z["bigThree"][2]["lines"].append("<b>为什么练：</b>用敞口杯小口喝，练的是嘴唇闭合和控制吞咽，跟嚼东西、说话用的是同一套口腔本领。")
    e["cards"][6]={"icon":"🦷","title":"Mouthing: normal toddler exploring","sub":"Made safer, not stopped","roots":["Healthy","Secure"],"lines":["Mouthing is still how one-year-olds explore, plus teething. It fades slowly through the second year.","<b>Choke check:</b> if it fits through a toilet-paper tube opening, it’s too small to be in her space. Never button batteries, loose small magnets, coins, balloons.","<b>Do:</b> keep a yes-to-mouth basket and swap rather than grab. <b>Don’t:</b> chase her for it; it becomes a game."],"refs":e["cards"][6]["refs"]}
    z["cards"][6]={"icon":"🦷","title":"啃东西：一岁宝宝的正常探索","sub":"做好安全，不用禁止","roots":["Healthy","Secure"],"lines":["往嘴里放东西还是一岁宝宝探索的方式，加上在长牙。一岁到两岁会慢慢少。","<b>噎呛自查：</b>能塞进卫生纸筒口的东西，就太小了，别放在她够得着的地方。纽扣电池、散落的小磁铁、硬币、气球一律不行。","<b>要：</b>准备一篮“可以啃的”，看到就换，别硬抢。<b>别：</b>追着她抢，她会当成游戏。"],"refs":z["cards"][6]["refs"]}
    e["todos"][3]="Write checkup questions: faded words, length, iron"; z["todos"][3]="写下体检要问的：说的词变少了、身长、补铁"
    e["todos"][4]="Show everyone who cares for her the MORE sign"; z["todos"][4]="把“还要”的手势比给照顾她的每个人看"
    e["quiz"][6]={"q":"Fill the open cup to the top so she gets a good drink.","a":"dont","why":"1–2 sips only. A tiny amount is easier to control, and spills stay small."}
    z["quiz"][6]={"q":"敞口杯倒满，让她一次喝个够。","a":"dont","why":"只倒一两口。量少她才好控制，洒了也不多。"}
    e["signs"]["intro"]="Keep <b>EAT</b>, <b>ALL DONE</b>, <b>MILK</b>, and add one: <b>MORE</b>. She’s pointing to ask, and MORE gives that point a sign. Just <b>say</b> “open” and “help” for now; their signs can come once MORE sticks."
    z["signs"]["intro"]="“<b>吃</b>”“<b>吃完了</b>”“<b>奶</b>”接着比，再加一个：“<b>还要</b>”。她整天指着要东西，“还要”正好给她的“指”配个手势。“打开”“帮忙”这周先<b>说</b>，等“还要”比顺了再加手势。"
    for L,sub,l1 in ((e,"Every cup of milk","<b>When:</b> right as you hold up her cup: “<b>Milk</b>? Here’s your milk.”"),(z,"每次喝奶","<b>什么时候比：</b>把杯子举到她面前时：“要喝<b>奶</b>吗？给你。”")):
        it=[x for x in L["signs"]["items"] if x["id"]=="milk"][0]; it["sub"]=sub; it["lines"]=[it["lines"][0],l1]
    for L in (e,z):
        L["plays"]=[p for p in L["plays"] if p["id"]!="bye-bye-teddy"]
        L["sources"]=[s for s in L["sources"] if "Recommended-Drinks" not in s["url"]]
    return o
out=trim(out)

# ---- Nov 15 evening (Melody): pause standing as a focus; rebuild around observer strength;
# no "Our family way" on weekly pages (it stays on the home page) ----
CDC12="https://www.cdc.gov/act-early/milestones/1-year.html"
DROP_STAND=["floor-to-stand","squat-to-stand","stool-stand-steps"]

def refocus(o):
    e,z=o["en"],o["zh"]
    # where she is now
    e["now"][0]="🧍 Stands alone on purpose · trying floor-to-stand on her own"
    z["now"][0]="🧍 能自己站，而且是有意识地站 · 从地上站起来她自己在摸索"
    e["now"][2]="🧗 Climbs stairs and playground stuff · has loved slides since 10 months"
    z["now"][2]="🧗 会爬楼梯和游乐设施 · 10个月起就爱滑梯"
    e["now"][4]="🧱 Prefers big soft blocks · uses a spoon"
    z["now"][4]="🧱 更喜欢大软积木 · 会用勺子"
    e["now"][6]="🚪 Opens the faucet herself after watching · knows tongs go in the pot"
    z["now"][6]="🚪 看过就会自己开水龙头 · 知道夹子要伸进锅里"
    e["now"][9]="🗣️ Softly, unclearly copies some two-word phrases you say · she’s learning"
    z["now"][9]="🗣️ 会轻轻、不太清楚地跟着您学两个字的话 · 正在学"
    e["now"].insert(10,"🧩 Tries a two-piece puzzle and stays curious · early baba/mama faded after pointing took off")
    z["now"].insert(10,"🧩 在玩两块的拼图，还拼不上也照样好奇 · 会指以后爸爸妈妈说得少了")

    e["oneLiner"]="One year old, a keen <b>observer</b> and a little problem-solver. This week, three things: <b>turn her points into words</b> (name it, pause, give it anyway), <b>show her slowly, then hand it over and wait</b>, and <b>start a tiny open cup</b>. Plus a new <b>reading</b> rhythm: short and often."
    z["oneLiner"]="满一岁了，最会<b>看</b>，也爱自己琢磨新东西。这周三件事：<b>把她的“指”变成话</b>（说出来、等一等、照样给）、<b>您先慢慢做给她看，再交给她、等一等</b>、<b>开始用小敞口杯喝水</b>。另外加一个<b>读书</b>的新习惯：每次短短的，一天多几次。"

    e["bigThree"][1]={"icon":"👀","title":"Show me, then her turn","sub":"Play · short moments all day","roots":["Curious","Self-led"],"lines":[
        "<b>When:</b> little pockets in real life — the kitchen, the sink, toys, getting dressed. One or two slow demos, then stop.",
        "<b>How:</b> ① Do it slowly where she can see, once or twice. ② Hand her the same thing, or a toddler-safe version. ③ <b>Pause and wait.</b> Any try counts: a miss, a mouth, a new idea. Don’t take over, and don’t ask her to copy.",
        "<b>Say, in two words:</b> “Tongs in.” “Lid off.” “Light on.” “Faucet on.” Then wait for her sound or her move.",
        "<b>Why this fits her:</b> she already watches how things work — she knows the tongs go in the pot, and she can open the faucet after seeing you do it. Showing, then waiting, uses that strength.",
        "<b>Keep it safe:</b> stay right there. Only big pieces (nothing that fits through a toilet-paper tube). No hot pots, and no climbing to a light switch or the faucet. Water not too hot."
    ]}
    z["bigThree"][1]={"icon":"👀","title":"先看您做，再轮到她","sub":"玩耍 · 日常里的一小会儿","roots":["Curious","Self-led"],"lines":[
        "<b>什么时候：</b>就在过日子的空当——厨房、水池边、玩具、穿衣服。慢慢做给她看一两遍，就停。",
        "<b>怎么做：</b>① 让她看得见，慢慢做一两遍。② 把同样的东西交给她，或者换成宝宝能安全用的。③ <b>停下来等一等。</b>她怎么试都算：没夹住、放进嘴里、自己换种玩法，都好。别抢过来做，也别说“你学一下”。",
        "<b>两个字就够：</b>“夹进去。”“盖打开。”“灯开了。”“水龙头开。”然后等她出声或动手。",
        "<b>为什么适合她：</b>她已经会看东西怎么用——知道夹子要伸进锅里，看您开过水龙头自己也会开。先演示、再等她，正好用上她会看的本事。",
        "<b>注意安全：</b>大人一直在旁边。只给大块的东西（能塞进卫生纸筒口的太小）。不要热锅，也别让她爬高够开关或水龙头。水不要太烫。"
    ]}

    # body, hands, words
    e["cards"][0]={"icon":"🦵","title":"Where she is now: body","sub":"Strong, almost walking","roots":["Brave","Healthy"],"lines":[
        "She <b>stands alone on purpose</b>, climbs stairs and playground equipment, walks fast with the push walker or one hand, and has loved slides since she was 10 months. That’s a strong, brave mover.",
        "She’s tried getting <b>up from the floor</b> a few times and is close, but hasn’t made it all the way yet. She’s figuring this out herself — no need to practice it on a schedule. <b>Just give her safe space</b> on the floor and let her try when she wants.",
        "<b>Heading toward:</b> first steps and floor-to-stand often arrive in their own order. Anywhere up to ~18 months for walking alone is normal."
    ]}
    z["cards"][0]={"icon":"🦵","title":"她现在：身体","sub":"很有劲，快会走了","roots":["Brave","Healthy"],"lines":[
        "能<b>自己站，而且是有意识地站</b>，楼梯和游乐设施都会爬，推学步车或牵一只手走得飞快，10个月起就爱滑梯。大运动又强又勇敢。",
        "从地上站起来，她已经试过几次，很接近了，还差一点点。这事她自己就在摸索，不必专门安排练习。<b>给她一块安全的地板</b>，想试的时候让她自己试就好。",
        "<b>接下来：</b>自己走几步和从地上站起来，哪个先来都正常。18个月之前会自己走都算正常。"
    ]}
    e["cards"][1]={"icon":"🧠","title":"Where she is now: hands and thinking","sub":"A little engineer who learns by watching","roots":["Curious","Self-led"],"lines":[
        "She uses a spoon and taps a pointer pen to make music: she already <b>knows touching a spot makes something happen</b> (cause and effect).",
        "<b>Watching is her strength.</b> She studies how you use things she’s never used — she knows the tongs go in the pot, even before she can grab with them — then she wants to figure it out. She’s a little problem-solver.",
        "She prefers <b>big soft blocks</b> (small hard blocks can wait), and she’ll work at a <b>two-piece puzzle</b> even when the piece doesn’t go in yet. Stay with that curiosity; no need to finish it for her.",
        "<b>Next:</b> show-me turns with everyday tools, lids, in-and-out, a knob puzzle, a safe faucet or light switch, and soft-block towers to crash."
    ]}
    z["cards"][1]={"icon":"🧠","title":"她现在：小手和脑子","sub":"会看、爱琢磨的小小工程师","roots":["Curious","Self-led"],"lines":[
        "会用勺子，也会拿点读笔点出音乐：她已经<b>明白点一下就会有反应</b>（因果关系）。",
        "<b>会看，是她的本事。</b>没见过的东西，她先盯着您怎么用——还不会夹，就已经知道夹子要伸进锅里——然后再自己琢磨。她是个爱想办法的小家伙。",
        "她更喜欢<b>大软积木</b>（小硬积木可以再等一等），两块的<b>拼图</b>还拼不进去，她也照样好奇。陪着这份好奇就好，不必替她拼完。",
        "<b>接下来：</b>用日常工具、盖子、放进去拿出来、带把手的拼图、安全的水龙头或灯开关，还有大软积木搭了推倒，都用“先看再试”的方式和她玩。"
    ]}
    e["cards"][2]["lines"]=[
        "<b>She can:</b> point to ask, clap and wave when you do, understand familiar names (Mama, milk, ball) and simple routines (“bath time”), and often “give me” with your hand out. She’s also started to <b>quietly copy some of your two-word phrases</b>, still soft and unclear. That’s real learning.",
        "<b>How to help:</b> repeat what she tried, warmly, add one word, then <b>pause and wait</b>. She says a fuzzy “more ba” → “More banana.” Never “Say banana!” Pressure makes talking harder.",
        "<b>Not yet:</b> “wait,” “later,” “gently,” reasons, or “don’t” (she hears the action word). So say what TO do: “Feet on the floor,” not “Don’t climb.”",
        "Words often pause while a big motor skill takes off; pointing is still her main tool. <b>Coming next:</b> clearer word-bits, and <b>pointing to show</b> you things, not just to ask."
    ]
    z["cards"][2]["lines"]=[
        "<b>她能：</b>指着要东西，您拍手挥手她跟着做，听得懂熟悉的名字（妈妈、奶、球）和简单的日常（“洗澡啦”），您伸手说“给我”她常常会给。她也开始<b>轻轻跟着您学两个字的话</b>，声音还小、还不太清楚。这就是在学。",
        "<b>怎么帮她：</b>她试着说了，您温暖地跟着说一遍，再加一个词，然后<b>停一停等她</b>。她轻轻说了有点糊的“还要 ba”→“还要香蕉。”别说“说‘香蕉’！”一逼她，更不愿开口。",
        "<b>还听不懂：</b>“等一下”“待会儿”“轻一点”、讲道理、“不要……”（她只听进去后面那个动作）。所以要说该做什么：“脚踩地上”，别说“不许爬”。",
        "大运动突飞猛进时，说话常常会停一停；现在“指”还是她最好用的工具。<b>接下来：</b>音会更清楚一点，还会<b>指给您看</b>东西，不光是指着要。"
    ]
    # drop the Our family's way link; keep the rest of the feelings card
    e["cards"][3]["lines"][-1]="<b>Coming next:</b> more “no,” more big feelings, showing you things she likes, and checking you’re near while she explores."
    z["cards"][3]["lines"][-1]="<b>接下来：</b>会更多说“不”、情绪更大，会拿东西给您看，玩着玩着回头确认您在不在。"

    cap_en={"icon":"🌟","title":"What she’s ready to try at 12 months","sub":"Because she learns by watching","roots":["Curious","Self-led"],"lines":[
        "Watching first is her superpower. She studies a new thing, then wants to figure out how it works — that’s a real problem-solver at one.",
        "Parents who notice this often invite the same everyday tries: in-and-out, lids on and off, a slow “your turn” with a real tool (toddler tongs, a scoop, a whisk, a brush), a chunky knob puzzle, big soft blocks, the faucet or a light switch with you right there.",
        "<b>What most one-year-olds can already do</b> (CDC): put something in a container, look for a toy they saw you hide, drink from a cup you hold, and pick up small bits with thumb and finger.",
        "<b>What often comes next</b> (by ~15 months): taking a lid off while holding a container, trying a word or two, showing you something she likes. A two-piece puzzle may not “solve” yet — staying curious is the win.",
        "Your job is to show slowly, hand it over, and wait. No quiz, and no pressure to finish."
    ],"refs":[{"label":"CDC: milestones by 1 year","url":CDC12},{"label":"CDC: milestones by 15 months","url":CDC}]}
    cap_zh={"icon":"🌟","title":"凭她现在的本事，1岁可以试试什么","sub":"因为她最会看、爱琢磨","roots":["Curious","Self-led"],"lines":[
        "会先看，是她的本事。一样新东西，她先琢磨您怎么用，再自己想办法——一岁就能这样观察、解决问题，很难得。",
        "很多家长会这样请她试试：放进去拿出来、开盖盖盖、您慢慢做一遍再换她来（宝宝夹子、小勺、打蛋器、刷子）、带大把手的拼图、大软积木，还有大人陪着开水龙头或灯开关。",
        "<b>一岁大多数宝宝已经会的</b>（美国疾控中心）：把东西放进盒子里，找您当着她面藏起来的玩具，您端着杯子她能喝，能用拇指和食指捏起小东西。",
        "<b>接下来常常会的</b>（大约15个月）：一只手拿着盒子，另一只手打开盖子；试着说一两个词；把喜欢的东西拿给您看。两块的拼图这会儿还不一定拼得上——她肯继续试，就很好。",
        "您要做的就是：慢慢做给她看，交到她手里，等一等。别考她，也别急着帮她做完。"
    ],"refs":[{"label":"美国疾控中心：1岁（12个月）里程碑（英文）","url":CDC12},{"label":"美国疾控中心：15个月里程碑（英文）","url":CDC}]}
    e["cards"].insert(2,cap_en); z["cards"].insert(2,cap_zh)

    e["daily"][1]="🔁 Model two-word phrases in real moments (“more bubbles,” “open lid”); pause and wait, no pressure to copy"
    z["daily"][1]="🔁 在真实场景里说两个字的话（“还要泡泡”“打开盖子”）；说完等一等，别逼她学"
    e["daily"][2]="👀 Show her slowly, hand it over, wait (tools, lids, faucet, puzzle)"
    z["daily"][2]="👀 先慢慢做给她看，交到她手里，等一等（工具、盖子、水龙头、拼图）"

    e["todos"].append("Set out a two-piece or knob puzzle, and toddler tongs with a play pot (pieces bigger than a toilet-paper tube)")
    z["todos"].append("准备一套两块或带大把手的拼图，再加宝宝夹子和一只玩具锅（东西都要比卫生纸筒口粗）")

    e["quiz"][5]={"q":"You show her the tongs once, slowly, then hand them over and wait, even if her first try misses.","a":"do","why":"That’s how she learns: watch, then try. Any attempt counts. No need to do it for her."}
    z["quiz"][5]={"q":"您慢慢夹一次给她看，再把夹子交给她，她没夹住您也等着，不抢过来。","a":"do","why":"她就是这样学的：先看，再试。试了就算。不必替她做对。"}

    e["details"][1]={"icon":"👀","title":"Why quiet, messy copies still count","roots":["Curious","Kind"],"lines":[
        "When she whispers a two-word phrase, or pokes the tongs toward the pot without grabbing yet, she’s practicing what she saw. Unclear and unfinished is how this age learns.",
        "Repeating her attempt warmly, adding one word, and waiting teaches more than asking her to say it or do it “right.”"
    ]}
    z["details"][1]={"icon":"👀","title":"为什么声音很小、做得还不像，也算在学","roots":["Curious","Kind"],"lines":[
        "她轻轻跟着说两个字，或者把夹子往锅里伸、还不会夹，都是在练她刚看到的事。一岁这个阶段，不清楚、做不完，才是正常的学法。",
        "您温暖地跟着说一遍、再加一个词、等一等，比让她“说对”或“做对”更有用。"
    ]}

    e["timeline"]["steps"][2]["note"]="She’s trying it on her own. Safe floor space is enough — no need to drill it."
    z["timeline"]["steps"][2]["note"]="她自己在试。给她安全的地板就好，不必专门练。"

    # sources: drop sit-to-stand how-to; add CDC 1-year
    def src(L, path=False):
        out=[]
        seen=set()
        first={"label":"CDC: milestones by 1 year" if L is e else "美国疾控中心：1岁（12个月）里程碑（英文）","url":CDC12}
        out.append(first); seen.add(CDC12)
        for s in L["sources"]:
            if "pathways.org" in s["url"]: continue
            if s["url"] in seen: continue
            out.append(s); seen.add(s["url"])
        return out
    e["sources"]=src(e); z["sources"]=src(z)

    # plays: drop standing practice; retune texts; add show-then-wait plays
    hows={
    "stack-crash":(
        "Big soft blocks only (skip small hard ones for now): you stack two, hand her the third, crash and cheer. Towers can be short. (Wk 1, now with soft blocks)",
        "只用大软积木（小硬积木这会儿先不用）：您先搭两块，递给她第三块，推倒了一起欢呼。塔矮一点也行。（第1周，改用软积木）"
    ),
    "tower-steps":(
        "Road to a soft-block tower: start by dropping big soft blocks into a basket, then stack two or three and knock them down. Laugh when it falls. Small hard blocks can wait. (Parent tip)",
        "用大软积木来搭：先把大软积木丢进篮子，再试着摞两三块、推倒。倒了就笑。小硬积木可以再等一等。（家长分享）"
    ),
    "playground-mission":(
        "She’s loved slides since 10 months. This week add language and turns: “Up… down… whee!” Then “Your turn, my turn.” You stay at the bottom. Stop while she’s happy. (Wk 1)",
        "她10个月起就爱滑梯。这周加上话和轮流：“上去……下来……呀！”再来：“该你了，该我了。”您在下面接。她还开心时就收。别抱着她一起滑。（第1周）"
    ),
    "faucet-pour":(
        "Handwashing at the real faucet: you turn it on slowly, say “Faucet on,” wash together, “Faucet off.” Then her turn, with you right there. Water warm, not hot; no climbing. The toy faucet is good practice too. (Parent tip)",
        "在真水龙头边洗手：您慢慢打开，说“水龙头开”，一起洗手，“水龙头关。”然后换她来，您就在旁边。水要温、不要烫，别让她爬上去。玩具水龙头也可以先练。（家长分享）"
    ),
    "echo-and-add":(
        "She’s already softly copying some of your two-word phrases, even if they’re unclear. Keep going: she says “ba” → “Ball! Big ball.” Repeat, add one word, pause and wait. Never “say ball.” (Wk 3)",
        "她已经会轻轻跟着您学两个字的话，哪怕还不清楚。继续这样就好：她说“ba”→“球！大球。”跟着说、加一个词、停一停等她。别让她“说球”。（第3周）"
    ),
    "lid-lab":(
        "Show me, then her turn: you slowly pull a lid off, or push one on, then hand her the container and wait. Boxes with a slot to post big pieces through count too. (Wk 1, harder)",
        "先看再试：您慢慢把盖子拔开或按上，再把盒子交给她，等一等。盒子开个口、让她塞进大块的东西，也算。（第1周，升级）"
    ),
    "in-and-out":(
        "Show me, then her turn: you put one big piece in a basket and take it out, then hand the basket over. She can fill it, push it, dump it. All pieces wider than a toilet-paper tube. (Wk 7, harder)",
        "先看再试：您先把一块大的放进篮子再拿出来，再把篮子交给她。她可以装满、推着走、倒出来。东西都要比卫生纸筒粗。（第7周，升级）"
    ),
    "pen-book-turns":(
        "Show me, then her turn with the pointer pen: you tap one picture, name it, pause, then hand her the pen. “Cat. Soft cat.” Don’t rush the music. (Wk 3)",
        "点读书也用先看再试：您先点一个图、说出名字、停一下，再把笔交给她。“猫。软软的猫。”别急着放音乐。（第3周）"
    ),
    "copy-me":(
        "Show me, then her turn: slowly wipe the table, brush hair, or hold a phone to your ear, then hand her the cloth or brush and wait. After she tries, you can copy her back. (Wk 3)",
        "先看再试：您慢慢擦一下桌子、梳一下头、或把电话放在耳边，再把布或刷子交给她，等一等。她试了以后，您也可以学她。（第3周）"
    ),
    "color-match-2":(
        "Hold up a red ball: “Where’s another red one?” with 2 balls on the floor (red, yellow). Then try a red soft block next to a red ball. Still two colors. (from parent posts)",
        "举起红球：“另一个红的在哪儿？”地上只摆一红一黄。再试试红色软积木放红球旁边。还是只用两种颜色。（家长分享的玩法）"
    ),
    }
    new_plays={
    "watch-try-tools":{
        "en":{"id":"watch-try-tools","emoji":"🥄","name":"Show me: tongs, scoop, whisk, brush","how":"Toddler-safe tools and a play pot (not a hot one). You slowly drop a big pom-pom or cloth ball in with tongs or a scoop, or stir with a whisk, or brush a doll’s hair. Hand it over and wait. Big pieces only; watch little fingers with tongs. (Parent kitchen-helper play)","roots":["Curious","Self-led"],"time":"5 min"},
        "zh":{"id":"watch-try-tools","emoji":"🥄","name":"先看再试：夹子、小勺、打蛋器、刷子","how":"用宝宝能安全拿的工具和一只玩具锅（千万别用热锅）。您慢慢用夹子或小勺把大毛球或布球放进去，或用打蛋器搅一搅，或给娃娃梳梳头。交到她手里，等一等。只给大块的；用夹子时看好她的小手指。（家长在厨房带宝宝帮忙的玩法）","roots":["Curious","Self-led"],"time":"5分钟"}
    },
    "knob-puzzle":{
        "en":{"id":"knob-puzzle","emoji":"🧩","name":"Two-piece or knob puzzle","how":"A two-piece puzzle or a chunky wooden knob puzzle (knobs easy to grab, pieces too big to swallow). Show once: take a piece out, put it back, slowly. Then her turn. Hand-over-hand only if she accepts it; otherwise show and wait. It may not fit yet — staying curious is enough. (Parent / Montessori-shelf favorite)","roots":["Curious","Brave"],"time":"5 min"},
        "zh":{"id":"knob-puzzle","emoji":"🧩","name":"两块拼图或带大把手的拼图","how":"两块的拼图，或带粗把手的木制拼图（把手好抓，块要大，不能整块咽下去）。您先做一遍：慢慢拿出来、再放回去。然后换她。她愿意您才手把手帮一下，不然就做给她看、等着。这会儿还不一定拼得上——她肯继续试，就很好。（家长、蒙氏架子上常见）","roots":["Curious","Brave"],"time":"5分钟"}
    },
    "light-switch":{
        "en":{"id":"light-switch","emoji":"💡","name":"Show me: light on, light off","how":"If a switch is already within reach, or you hold her, show “Light on… light off,” then her turn. Never let her climb to it. A push night-light or a toy switch board works too. Cover outlets; fingers stay off the bulb and the fixture. (Everyday parent play)","roots":["Curious","Self-led"],"time":"2 min"},
        "zh":{"id":"light-switch","emoji":"💡","name":"先看再试：灯开了，灯关了","how":"开关本来就够得着，或您抱着她，先做给她看：“灯开了……灯关了。”再换她。千万别让她爬高去按。按一按的小夜灯或开关玩具也可以。插座要挡住；小手不要碰灯泡和灯具。（日常里家长常这样玩）","roots":["Curious","Self-led"],"time":"2分钟"}
    },
    }
    for L,lang in ((e,"en"),(z,"zh")):
        L["plays"]=[p for p in L["plays"] if p["id"] not in DROP_STAND]
        for p in L["plays"]:
            if p["id"] in hows:
                p["how"]=hows[p["id"]][0 if lang=="en" else 1]
            if p["id"]=="tower-steps":
                p["name"]="Soft-block towers" if lang=="en" else "大软积木搭一搭"
        have={p["id"] for p in L["plays"]}
        for i in ("watch-try-tools","knob-puzzle","light-switch"):
            if i not in have:
                L["plays"].append(new_plays[i][lang])

    # drop unused sit-to-stand how-to videos
    for k in ("mFTwsPVn6dk","jKT9ICWs6oU"):
        o.get("videos",{}).pop(k,None)
    return o

out=refocus(out)

# Home page keeps "Our family’s way"; weekly pages should not show that topic card
T=json.load(open("topics/topics.json"))
for t in T:
    if t["id"]=="family-principles":
        t["weeks"]=[]
json.dump(T,open("topics/topics.json","w"),ensure_ascii=False,indent=1)

W=json.load(open("weeks/weeks.json"))
for w in W:
    if w["id"]=="week-09":
        w["en"]["tagline"]="Points → words · show me, then her turn · first open cup · short, often reading · new sign: MORE"
        w["zh"]["tagline"]="把“指”变成话 · 先看再试 · 小敞口杯 · 读书短而多 · 新手语：还要"
json.dump(W,open("weeks/weeks.json","w"),ensure_ascii=False,indent=1)

# privacy guard
txt=json.dumps(out,ensure_ascii=False)
for bad in ["Love","2025-11","Nov 5","11月5","98115","53rd","Ct NE","Seattle","UCDS"]:
    assert bad not in txt, bad
# no leftover family-way or sit-to-stand focus
assert "family-principles.html" not in txt
assert "Our family’s way" not in txt
assert "家庭教养原则" not in txt
assert "Up from the floor" not in txt
assert "从地上站起来：" not in txt  # title form; body may mention it as a one-line note
for L in ("en","zh"):
    ids=[p["id"] for p in out[L]["plays"]]; assert len(ids)==len(set(ids))
    for d in DROP_STAND:
        assert d not in ids, d
assert [p["id"] for p in out["en"]["plays"]]==[p["id"] for p in out["zh"]["plays"]]
for k in ("daily","quiz","scripts","bigThree","cards","details","watch","sources","todos"):
    assert len(out["en"][k])==len(out["zh"][k]),k
# keep the sections Melody asked to keep
assert out["en"]["bigThree"][0]["title"].startswith("Turn her points")
assert "open cup" in out["en"]["bigThree"][2]["title"].lower() or "open-cup" in out["en"]["bigThree"][2]["title"].lower()
assert any("Reading" in c["title"] for c in out["en"]["cards"])
assert out["en"]["signs"] and out["en"]["signs"]["items"]
json.dump(out,open("weeks/week-09.json","w"),ensure_ascii=False,indent=1)
print("plays",len(out["en"]["plays"]),"dropped standing",DROP_STAND,"cards",len(out["en"]["cards"]),"big3",[b["title"] for b in out["en"]["bigThree"]])
