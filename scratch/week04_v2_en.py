import json
d=json.load(open("weeks/week-04.json")); e=d["en"]
DC='<a href="daycare-first-day.html">'
e["oneLiner"]="She’s in a <b>calmer, more independent</b> stretch. This week: <b>step practice twice a day</b>, <b>echo-and-point</b> for words, and start a <b>goodbye routine</b> before the next wave (walking + daycare) arrives."
e["now"]=[c for c in e["now"] if "Stranger" not in c]
e["now"].insert(-2,"😌 Calmer · explores on her own · warms up to people faster")
now_cards=[dict(c) for c in e["bigThree"]]
for c in now_cards: c["videos"]=[]
now_cards[2]={"icon":"😌","title":"Where she is now: feelings","sub":"Calmer, more independent","roots":["Secure","Self-led"],"lines":[
"Last week’s fussy, clingy dip has passed. Now that she can <b>get around and explore on her own</b>, she is happier and calmer.",
"She plays alone longer, goes farther from you, and glances back to check in. That glance is how she refuels.",
"She warms up to new people faster. She may still watch from your lap first, and that’s fine.",
"Throwing food and watching your face is still experimenting (what happens? how does Mama react?), not naughtiness.",
"<b>What comes next:</b> babies move in cycles. A calm, capable stretch often comes before a new wave of clinginess when a big change arrives. For her, that’s <b>walking</b> (the world suddenly feels bigger) and <b>daycare</b>. Expect more protest at goodbyes, extra night waking, and wanting you close. It’s the next cycle starting, not going backwards."]}
e["bigThree"]=[
{"icon":"👣","title":"Do “couch to Mama” steps, twice a day","sub":"Body · 5 min","roots":["Brave","Healthy"],"lines":[
"<b>When:</b> after her morning nap and before the afternoon playground, barefoot, on a clear floor. Stop while she’s still having fun.",
"<b>How:</b> she sits on your lap one small step from the couch, with a toy on the seat. Stand her up and let her step to it. Next time, sit a little farther away. Then switch: she starts at the couch and steps to you.",
"<b>Help less each day:</b> hold her hips, then her forearms (no higher than her shoulders), then just a finger. Give her a big ball to carry so her hands are busy.",
"<b>Say:</b> “Come to Mama!” (open arms, wait). If she steps: “You walked to me!” If she sits down: “Plop! Up again?” No big cheers or clapping, which can startle her down.",
"If she crawls instead, that’s fine. Try again later."],
"videos":["bEHaCVLeMtE"]},
{"icon":"🗣️","title":"Echo, point, name: 3 times a day","sub":"Words · no testing","roots":["Curious","Kind"],"lines":[
"<b>When:</b> breakfast, pen-book time, and the walk to the playground.",
"<b>How 1, echo and add:</b> she says “baba” → you say <b>“Baba! Baba’s at work.”</b> Repeat her word and add a little.",
"<b>How 2, follow her point:</b> look where she points, then name it: <b>“Bird! A bird is flying.”</b> Then point to something yourself and wait for her to look.",
"<b>How 3, pen-book turns:</b> she presses, you say the word (“Cat! Meow.”), then it’s her turn again.",
"<b>Pause</b> 3–5 seconds before a word she knows (“Bai…”). If she doesn’t say it, just say it yourself and move on.",
"<b>Don’t say:</b> “Say mama! Say it again!” She says words when she needs them, not on request."],
"videos":[]},
{"icon":"👋","title":"Start a goodbye routine before the next wave","sub":"Feelings · 3 practices","roots":["Secure","Brave"],"lines":[
"<b>When:</b> 3 times this week, while she’s calm and fed, with a grandparent or another familiar adult. Try 5 minutes, then 10, then 20.",
"<b>How:</b> same steps every time. Get down to her level, give a hug, say the goodbye line, wave, and leave even if she cries. Come back warm and unhurried.",
"<b>Say leaving:</b> “Mama’s going out. Grandma stays with you. Mama comes back.” → “Bye bye!”",
"<b>Say returning:</b> “Mama’s back! I said I’d come back.” Then sit with her for a few minutes.",
"<b>Don’t:</b> sneak out while she’s busy. Use this exact routine on the "+DC+"daycare first day</a>."],
"videos":[]}]
cards=e["cards"]
for c in cards:
    if c["icon"]=="🙈":
        c.update({"title":"Do & don’t: the next goodbye wave","sub":"Walking + daycare","lines":[
"She’s calmer now and warms up faster. Enjoy it, and use this calm stretch to build the routine she’ll need next.",
"✅ <b>Do</b> let new people take their time. They talk to you first while she watches. <i>Why:</i> she reads your face to decide if someone is safe.",
"✅ <b>Do</b> practice short goodbyes now, while she’s calm. <i>Why:</i> each time you come back, her trust grows, and that carries her through the daycare wave.",
"✅ <b>Do</b> expect more clinginess when she starts walking or starts daycare. <i>Why:</i> a big new skill or change often brings a new round of needing you. It’s a new cycle, not going backwards.",
"🚫 <b>Don’t</b> sneak out. <i>Why:</i> she learns you can disappear without warning, and she clings harder.",
DC+"Daycare first-day page</a> has the full goodbye script and packing list."]})
    if c["title"].startswith("What’s next: feelings"):
        c["lines"][0]="<b>Feelings:</b> the calm stretch now usually gives way to a new wave around walking and daycare: more protest at goodbyes, wanting you close, night waking for a week or two. After that comes “I do it myself.” Hold limits calmly and comfort her; that’s the whole plan."
e["cards"]=now_cards+cards
for x in e["details"]:
    if x["icon"]=="🙈":
        x["title"]="Why calm now, and a new wave soon"
        x["lines"]=["Development comes in cycles: a new skill brings a fussy, clingy dip, then a calmer stretch once the skill settles. Exploring on her own has brought her into a calm stretch.","Walking and daycare are the next big changes. Separation protest often peaks somewhere between 9 and 18 months, as she understands you exist when you’re gone but can’t yet predict when you’ll be back.","A consistent goodbye and a warm return teach her the pattern. Most babies settle into daycare within a few weeks."]
e["todos"]=[t for t in e["todos"]]
# plays: carry-overs + new
P=[
("🛋️","Couch to Mama","Lap → step to toys on the couch, then couch → your arms. Move a little farther each day. (from Wk 3 “One step to me”)",["Brave","Healthy"],"5 min"),
("⚽","Hands-busy standing","Big light ball or two clappers to hold. Busy hands let go without noticing. (Wk 3)",["Brave","Healthy"],"3 min"),
("↔️","Wider stand-to-stand gap","Two sturdy pieces of furniture, now a full step apart, so she has to let go and step across. (Wk 3, harder)",["Brave","Healthy"],"3 min"),
("⬇️","Squat-to-pick-up, in the open","Toy by her feet while she stands without holding on. Squat, grab, stand back up. (Wk 3, harder)",["Healthy"],"3 min"),
("🤝","One-hand walk","Hold one hand at her shoulder height, toy in her other hand. Switch sides.",["Healthy","Self-led"],"5 min"),
("🛒","Push-walker delivery","A toy in the walker: “Take it to Baba!” Weigh it down if it rolls too fast. (Wk 3)",["Healthy","Kind"],"5 min"),
("🪜","Stairs down with a rail","She already steps down smoothly. Now: one hand on the rail or wall, you one step below. (Wk 3, harder)",["Brave","Healthy"],"3 min"),
("🛝","Playground mission","Pick ONE stretch per visit (a new climber, a bigger slide with you at the bottom). Stop while she’s happy. (Wk 1)",["Brave","Healthy"],"per visit"),
("📦","Bring-it delivery, 2 steps","“Pick up the ball and give it to Grandma.” Help with a gesture. (Wk 1, harder)",["Curious","Kind"],"3 min"),
("🧺","Throw into the basket","Balls into a laundry basket: “Throw! In!” The yes-place for throwing.",["Curious","Self-led"],"5–10 min"),
("👉","Point-and-name walk","Carry or walk her around: “Where’s the light?” When she points, look and name it. (Wk 3)",["Curious","Kind"],"5 min"),
("🖊️","Pen-book turns","She presses, you say the word and add one, then it’s her turn. (Wk 3)",["Curious","Kind"],"5–10 min"),
("🔁","Echo-and-add","“Baibai” → “Baibai! Bye-bye, car!” (Wk 3)",["Curious","Kind"],"all day"),
("📸","Family photo book","“Where’s yeye?” Let her pat the photo. Echo any name she says. (Wk 3)",["Kind","Secure"],"5 min"),
("📖","Quiet board book","No buttons. Point and name, wait for her to point back. (Wk 1)",["Curious"],"5 min"),
("🍌","Banana or cracker?","Hold up two things. Any reach, look or point is her answer: name it. (Wk 3)",["Self-led","Curious"],"1 min"),
("🥤","Three-cup shuffle","Hide a toy under one of three cups and move it while she watches. (Wk 3, harder)",["Curious"],"3 min"),
("🗼","Stack & crash","Stack blocks together; she tries to put one on top, then crashes them. (Wk 1)",["Curious","Self-led"],"5 min"),
("🫙","Lid lab, harder","Lids that pull off, then lids that push on; a box with a slot to post things through. (Wk 1, harder)",["Curious","Self-led"],"5 min"),
("🕺","Freeze dance","Music on: bounce. Off: “FREEZE!” (Wk 3)",["Self-led","Healthy"],"3 min"),
("🥁","Rhythm copy","Tap a pot twice, wait, copy what she does. (Wk 3)",["Curious","Kind"],"3 min"),
("🕷️","Gesture songs","Itsy Bitsy, Wheels on the Bus. Pause before the gesture so she fills it in. (Wk 3)",["Kind","Curious"],"5 min"),
("🪞","Copy-me","Wipe the table, phone to ear, brush hair. She copies, then you copy her. (Wk 3)",["Kind","Self-led"],"3 min"),
("💧","Wipe-up helper","Damp cloth after meals; she “cleans” her tray. (Wk 1)",["Self-led","Kind"],"2 min"),
("🧩","Solo play + check-ins","4–6 toys out, play together briefly, then “I’ll be right here.” Smile when she looks back. (Wk 3)",["Self-led","Secure"],"10+ min"),
("👯","Peer time side by side","1–2 babies at the playground or a class. No need to share. (Wk 3, good daycare prep)",["Kind","Brave"],"20 min"),
("😴","Daytime night-night","Lie on her floor bed together, “shhh”… “Good morning!” (Wk 3)",["Secure","Healthy"],"2 min"),
("🫧","Messy tray","Yogurt, soft noodles or water on a tray. Squish, pour; you name “sticky, wet, cold.”",["Curious","Healthy"],"10 min"),
("💦","Water table pouring","Cups, a funnel, floating toys. Always within arm’s reach; empty after play.",["Curious","Healthy"],"10–15 min")]
e["plays"]=[{"emoji":a,"name":b,"how":c,"roots":r,"time":t} for a,b,c,r,t in P]
for v in d["videos"].values(): v.pop("titleZh",None); v.pop("channelZh",None)
d.pop("zh",None)
json.dump(d,open("weeks/week-04.json","w"),ensure_ascii=False,indent=1)
