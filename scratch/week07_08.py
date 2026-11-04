import json, copy
W4=json.load(open("weeks/week-04.json"))
P4={L:{p["id"]:p for p in W4[L]["plays"]} for L in ("en","zh")}
P4["zh"].setdefault("echo-and-add",dict(P4["en"]["echo-and-add"],name="跟着说再多一点",how="她说“爸爸”，您接：“爸爸！爸爸上班去了。”她的词加一点点。",time="随时"))
FP='<a href="family-principles.html">'; DC='<a href="daycare-first-day.html">'; MK='<a href="milk-at-one.html">'
def carry(ids,L,tag):
    out=[]
    for i,h in ids:
        p=copy.deepcopy(P4[L][i])
        if h: p["how"]=h[0 if L=="en" else 1]
        p["how"]+= (" (Wk 4%s)"%tag[0] if L=="en" else "（第4周%s）"%tag[1]) if "(Wk" not in p["how"] and "周" not in p["how"][-6:] else ""
        out.append(p)
    return out
def P(i,emoji,en,zh,roots,t):
    return {"en":{"id":i,"emoji":emoji,"name":en[0],"how":en[1],"roots":roots,"time":t[0]},
            "zh":{"id":i,"emoji":emoji,"name":zh[0],"how":zh[1],"roots":roots,"time":t[1]}}

NEW={}
def add(*a): NEW[a[0]]=P(*a)
import sys; sys.path.insert(0,"scratch"); from week07_08_social import *
add_social(NEW, add)
add("floor-to-stand","🧸",("Floor to stand","She sits on the floor; a toy sits on a low stool just in front. Wait for her to get up on her own: hands down, bottom up, push. Help only at the hips, briefly."),("从地上站起来","她坐在地上，前面矮凳上放个玩具。等她自己撑起来：手撑地、屁股撅起来、往上推。实在要帮，就扶一下胯。"),["Brave","Healthy"],("3 min","3分钟"))
add("squat-to-stand","⬇️",("Squat, pick up, stand","Scatter 4–5 balls on a clear floor while she stands. “Can you get the red ball?” She squats, grabs, stands up. That’s the exact move she needs to stand from the floor."),("蹲下捡、再站起来","她站着的时候，地上撒四五个球：“把红球捡起来？”蹲下、抓、站起来，正是从地上站起来要练的那个动作。"),["Brave","Healthy"],("5 min","5分钟"))
add("point-honor","👉",("Honor her point","She points and calls out → go there, name it, and give it if it’s OK: “Ball! You want the ball. Here’s the ball.” If not OK: name it and offer something else."),("她指，您就接","她一边指一边“啊啊”叫，您就走过去，说出来，能给就给：“球！你要球呀，给你。”不能给：说出来，再换个能玩的。"),["Secure","Curious"],("all day","随时"))
add("door-open-close","🚪",("Open–close doors","Pick one cabinet she may open: fill it with safe things (pots, wooden spoons, a scarf). Lock the others. “Open… close! Bye-bye, pot!”"),("开门关门","专门给她留一个能开的柜子，里面放锅、木勺、丝巾这类安全的东西，其他柜子都上锁。“开……关！锅锅拜拜！”"),["Curious","Self-led"],("5–10 min","5–10分钟"))
add("faucet-pour","🚰",("Toy-kitchen turns","Her toy faucet: you turn it, then wait. Add a cup to “fill” and pour into a bowl. Name it: on, off, pour, all gone."),("玩具厨房轮流玩","玩具水龙头：您拧一下，停下来等她。再给个杯子“接水”，倒进碗里。边玩边说：开、关、倒、没啦。"),["Curious","Kind"],("5 min","5分钟"))
add("in-and-out","📥",("In and out","A tin or basket plus 3–4 big blocks or balls (all wider than a toilet-paper tube). In, dump, in again. “In! Out!”"),("放进去、倒出来","一个铁盒或篮子，三四个大积木或球（都要比卫生纸筒粗）。放进去、倒出来、再放。“进去！出来！”"),["Curious","Self-led"],("5 min","5分钟"))
add("cup-sips","🥛",("Open-cup sips","At meals: 1–2 oz in a small open or straw cup. Hold the bottom with her, tip slowly, let her set it down. Spills are practice."),("小杯子喝两口","吃饭时小敞口杯或吸管杯倒一两口（30–60毫升）。您托着杯底一起端，慢慢倾，让她自己放下。洒了就是在练。"),["Healthy","Self-led"],("meals","每顿饭"))
add("swim-bath-pour","🛁",("Bath pour and blow","Pour a cup of water slowly over the back of her head (warn first: “Water’s coming… splash!”). Blow bubbles in the water together. Keeps her swim calm about water on the face."),("洗澡倒水、吹泡泡","先说一声“水来啦……哗！”再用杯子慢慢从后脑勺浇。一起在水里吹泡泡。让她对水扑到脸上保持淡定，跟游泳课接上。"),["Brave","Healthy"],("bath","洗澡时"))
add("mouth-ok-basket","🦷",("Yes-to-mouth basket","A small basket of things that are fine to chew: a silicone teether, a cold washcloth, a big wooden ring. When she mouths something unsafe, swap: “That’s not for mouths. This one is!”"),("可以啃的小篮子","放几样可以啃的：硅胶牙胶、冰过的湿毛巾、大木环。她啃了不能啃的，就换：“这个不能放嘴里，这个可以！”"),["Healthy","Secure"],("anytime","随时"))
add("bye-bye-teddy","🧸",("Teddy goes to daycare","Act it out with a stuffed animal: Teddy gets a hug, “Mama comes back,” waves bye-bye, plays, then Mama comes back: “I came back!” Let her be Mama."),("小熊上托班","拿个毛绒玩具演一遍：抱一抱，“妈妈会回来”，挥手拜拜，小熊在托班玩，妈妈回来了：“我回来啦！”换她来当妈妈。"),["Secure","Brave"],("3 min","3分钟"))
add("hat-on-off","🧢",("Hats, socks, off and on","Let her pull off her hat or socks, then hold them out: “Your turn, on?” Undressing comes first; it’s her first self-care."),("帽子袜子，脱了再戴","让她自己扯掉帽子、袜子，再递给她：“你来戴？”先会脱再会穿，这是她最早的自理。"),["Self-led","Healthy"],("2 min","2分钟"))
add("mirror-signs","🪞",("Mirror signs","Sit in front of a mirror and sign EAT, MILK, ALL DONE slowly together, saying each word. She sees both of you do it."),("对着镜子比手语","坐在镜子前，一起慢慢比“吃”“奶”“吃完了”，边比边说。她能同时看到自己和您。"),["Curious","Kind"],("2 min","2分钟"))

def plays(L, carry_ids, new_ids, tag):
    return carry(carry_ids,L,tag)+[NEW[i][L] for i in new_ids]

# ---------- signs ----------
def signs(L, week):
    s=copy.deepcopy(W4[L]["signs"])
    milk_en={"id":"milk","emoji":"🥛","name":"MILK","sub":"Every cup of milk (and the bedtime bottle)","lines":[
      "<b>How:</b> one hand in a loose fist, squeeze open and closed twice, like milking a cow.",
      "<b>When:</b> right as you hold up her cup or bottle: “<b>Milk</b>? Here’s your milk.” Formula or whole milk, same sign: it’s all milk.",
      "<b>Why this one now:</b> she’s moving to whole milk in a cup, and she already reaches and points for it. A sign gives that point a word."],
      "images":[{"src":"assets/signs/milk.svg","alt":"MILK sign: 1, hand in a loose C shape; 2, squeeze into a fist, open again, twice.","caption":"① Loose “C” hand → ② squeeze into a fist, twice."}]}
    milk_zh={"id":"milk","emoji":"🥛","name":"奶","sub":"每次喝奶（包括睡前那瓶）","lines":[
      "<b>怎么比：</b>一只手半握拳，捏紧、松开，捏两下，像挤牛奶。",
      "<b>什么时候比：</b>把杯子或奶瓶举到她面前时：“要喝<b>奶</b>吗？给你。”配方奶、牛奶都比这个，都是“奶”。",
      "<b>为什么现在加：</b>她正在换杯子喝牛奶，本来就会伸手、指着要。比个手势，她的“指”就有了名字。"],
      "images":[{"src":"assets/signs/milk.svg","alt":"“奶”的手语：1. 手半握成C形；2. 捏成拳再松开，两下。","caption":"① 手半握成C形 → ② 捏紧、松开，两下"}]}
    s["items"].append(milk_en if L=="en" else milk_zh)
    if L=="en":
        s["hint"]="Comes back every week. Tick the tracker when she watches, tries, or uses a sign."
        s["intro"]=("Keep <b>EAT</b> and <b>ALL DONE</b>, and add one: <b>MILK</b>, timed with the switch to whole milk. Three signs is plenty for now." if week==7 else
                    "Same three: <b>EAT</b>, <b>ALL DONE</b>, <b>MILK</b>. No new sign this week: daycare is enough change. Show the teachers these three (print the pictures).")
    else:
        s["hint"]="每周都有。她看着您比、自己试着比、真的会用，就在下面打个勾。"
        s["intro"]=("“<b>吃</b>”和“<b>吃完了</b>”接着比，再加一个：“<b>奶</b>”，正好赶上换牛奶。三个就够了，别贪多。" if week==7 else
                    "还是这三个：“<b>吃</b>”“<b>吃完了</b>”“<b>奶</b>”。这周不加新的，上托班已经够多变化了。把这三个比给托班老师看（可以打印图片）。")
    return s

def tl(L):
    if L=="en":
        return {"now":1,"hint":"Each step can take days or weeks. She may skip around.","steps":[
          {"label":"Standing without noticing","note":"Lets go while busy (done)"},
          {"label":"Standing alone on purpose","note":"A few seconds, then sits (now)"},
          {"label":"Floor to stand, nothing to hold","note":"Hands down, bottom up, push"},
          {"label":"1–3 steps alone","note":"Toward you, falling into your arms"},
          {"label":"Walking more than crawling","note":"Feet wide, arms up, lots of falls"},
          {"label":"Steady walker","note":"Carries toys, turns, squats"}],
          "ruler":{"label":"When healthy babies first walk alone (WHO):","min":8,"max":18,"from":8.2,"to":17.6,"age":12,"ticks":[8,10,12,14,16,18]},
          "footer":"Many walk at 12–15 months; 16–18 is still normal. Ask the pediatrician if she isn’t walking alone by ~18 months."}
    return {"now":1,"hint":"每一步可能要几天到几周，也可能跳着来。","steps":[
          {"label":"不知不觉站住","note":"玩着玩着就松手了（会了）"},
          {"label":"自己站一会儿","note":"站几秒再坐下（现在）"},
          {"label":"不扶东西从地上站起来","note":"手撑地、屁股撅起、往上推"},
          {"label":"自己走一到三步","note":"朝您走，扑进怀里"},
          {"label":"走比爬多","note":"脚分得开、手举着、老摔，都正常"},
          {"label":"走得稳","note":"能拿着东西走、转弯、蹲下"}],
          "ruler":{"label":"健康宝宝第一次独立走路的时间（世卫组织）：","min":8,"max":18,"from":8.2,"to":17.6,"age":12,"ticks":[8,10,12,14,16,18]},
          "footer":"很多宝宝12–15个月会走，16–18个月也正常。18个月左右还不能自己走，就问问儿科医生。"}

WATCH={"en":['<b>Loses skills</b> she had: stops pointing, waving, babbling, or saying baba/mama','By 12 months: doesn’t point, wave, or respond to her name','Won’t bear weight, or one side much weaker','By ~18 months: not walking alone','Choking signs: can’t cough, cry, or breathe, or turns blue → call 911, start back blows/chest thrusts','A swallowed <b>button battery or magnet</b>, even if she seems fine → ER now','Fever 100.4°F / 38°C or higher in a baby who seems really unwell'],
 "zh":['会的本事<b>退步了</b>：不指、不挥手、不咿呀、不叫爸爸妈妈了','12个月还不会指、不会挥手，叫名字没反应','腿不肯承重，或者一边明显没劲','18个月左右还不能自己走','噎住了：咳不出、哭不出、喘不上气、发紫 → 马上打911，同时拍背/压胸','吞了<b>纽扣电池或磁铁</b>，看着没事也要马上去急诊','发烧38°C以上，而且精神很差']}
SRC={"en":[{"label":"WHO motor development milestones","url":"https://www.who.int/tools/child-growth-standards/standards/motor-development-milestones"},{"label":"CDC milestones: 12 months","url":"https://www.cdc.gov/ncbddd/actearly/milestones/milestones-1yr.html"},{"label":"AAP/HealthyChildren: Choking prevention","url":"https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx"},{"label":"AAP/HealthyChildren: Recommended drinks for young children","url":"https://www.healthychildren.org/English/healthy-living/nutrition/Pages/Recommended-Drinks-for-Young-Children-Ages-0-5.aspx"},{"label":"AAP/HealthyChildren: Separation anxiety","url":"https://www.healthychildren.org/English/ages-stages/baby/Pages/Soothing-Your-Childs-Separation-Anxiety.aspx"},{"label":"Harvard Center on the Developing Child: Serve and Return","url":"https://developingchild.harvard.edu/key-concept/serve-and-return/"}]}
SRC["zh"]=[{"label":"世界卫生组织：大运动里程碑（英文）","url":SRC["en"][0]["url"]},{"label":"美国疾控中心：12个月里程碑（英文）","url":SRC["en"][1]["url"]},{"label":"美国儿科学会：预防噎呛（英文）","url":SRC["en"][2]["url"]},{"label":"美国儿科学会：小宝宝该喝什么（英文）","url":SRC["en"][3]["url"]},{"label":"美国儿科学会：分离焦虑（英文）","url":SRC["en"][4]["url"]}]

NOW={"en":["🎂 Turning 1 this week · first birthday party done","🧍 Stands alone briefly · not yet floor-to-stand on her own","🤝 Walks holding ONE hand","🛒 Very fast with the push walker","👉 Points at what she wants + calls out","👋 Knows “bye-bye” (not every time)","🗣️ baba · mama with meaning","🚪 Opens/closes closet doors, the toy-kitchen faucet (copied Mama)","🏊 Swims since June · dips under 1–2 s, no coughing","🍗 Prefers bigger chunks to tiny pieces","🥛 First whole milk (Nov 3) · still formula + vitamin D","🎒 Daycare trial went well · starting soon","🦷 Mouths things","🏠 Grandparents back in China · just the three of you"],
 "zh":["🎂 这周满一岁 · 生日派对办完了","🧍 能自己站一小会儿 · 还不会不扶东西从地上站起来","🤝 牵一只手就能走","🛒 推学步车跑得飞快","👉 想要什么就一边指一边“啊啊”叫","👋 会“拜拜”（不是每次都做）","🗣️ 会有意思地叫爸爸、妈妈","🚪 会开关柜门，学妈妈拧玩具厨房的水龙头","🏊 六月开始游泳 · 能憋气潜水一两秒，不呛","🍗 喜欢大块的，不太爱小碎块","🥛 11月3日第一次喝牛奶 · 还在喝配方奶 + 维生素D","🎒 托班试园很顺利 · 快正式上了","🦷 什么都往嘴里放","🏠 爷爷奶奶回国了 · 家里就你们三个"]}

def wk7(L):
    en=L=="en"
    w={"title":"Week 7" if en else "第7周","age":"Turning 1" if en else "满一岁","dates":"Nov 2–8, 2026" if en else "2026年11月2日–8日","now":NOW[L]}
    if en:
        w["oneLiner"]="Happy first birthday week! 🎂 She’s <b>pointing to ask</b>, <b>standing alone</b>, and <b>opening everything</b>. This week: <b>answer every point</b>, <b>practice floor-to-stand</b>, and <b>start milk in a cup</b> plus a mouth-safety sweep before daycare."
        w["bigThree"]=[
{"icon":"👉","title":"Answer every point: name it, then honor it","sub":"Words · all day","roots":["Secure","Curious"],"lines":[
"<b>When:</b> every time she points and calls out, all week. Aim for at least 5 good answers a day (breakfast, play, walks, bath).",
"<b>How:</b> 1) look where she points; 2) name it in 2–4 words; 3) give it, or say why not and offer a swap; 4) pause 3 seconds so she can “talk” back.",
"<b>Say:</b> “Ball! You want the <b>ball</b>. Here’s the ball.” Not OK: “That’s Mama’s <b>phone</b>. Not for Xyla. Here’s your <b>cup</b>.”",
"<b>Don’t:</b> hand things over silently, or make her say it first (“Say ball!”). Her point <i>is</i> her sentence right now.",
"<b>Bonus:</b> point back. “Look! A <b>dog</b>!” and wait for her eyes to follow. That shared look grows words."],"videos":[]},
{"icon":"🧸","title":"Floor-to-stand: 3 tries, twice a day","sub":"Body · 5 min","roots":["Brave","Healthy"],"lines":[
"<b>When:</b> after morning nap and before dinner, barefoot, on a clear non-slip floor.",
"<b>How 1, squat-and-pick:</b> while she stands holding your one hand, drop 3 balls by her feet. She squats, picks one up, stands again. Let go of her hand for a second at the top.",
"<b>How 2, floor-to-stool:</b> she sits on the floor, a favorite toy on a low stool a step away. Wait. Let her work it out: hands down, bottom up, push. Help only at her hips, and only for a second.",
"<b>How 3, one-hand walk:</b> hold one hand <b>at her shoulder height or lower</b>, swap sides, and loosen your grip to one finger near the end.",
"<b>Say:</b> “Up, up… you’re up!” If she plops: “Plop! Try again?” Calm voice, no big cheering.",
"<b>Skip:</b> a sit-in baby walker (the push walker is fine)."],"videos":["bEHaCVLeMtE"]},
{"icon":"🥛","title":"Start whole milk in a cup + mouth-safety sweep","sub":"Healthy · this week","roots":["Healthy","Self-led"],"lines":[
"<b>When:</b> milk with breakfast and lunch in an open or straw cup. Bedtime bottle stays formula for now; it goes last (see "+MK+"Milk at one</a>).",
"<b>How (Week 1 of 4):</b> swap one daytime formula bottle for 2–4 oz whole milk in a cup. Next week, a second one. Target by ~4 weeks: about <b>16 oz/day</b> (no more than 24), keep vitamin D unless the doctor says stop.",
"<b>Say:</b> “<b>Milk!</b> Cold milk in your cup.” + MILK sign. Spills: “Oops, milk spilled. Wipe!”",
"<b>Mouth sweep (once, 15 min):</b> anything that fits through a toilet-paper tube goes up high. Hunt for <b>button batteries, small magnets</b>, coins, balloons. Do the same with her bag for daycare.",
"<b>When she mouths:</b> don’t yank. Swap: “Not for mouths. This one is!” and hand her the yes-to-mouth basket."],"videos":[]}]
        w["cards"]=[
{"icon":"🦵","title":"Where she is now: body","sub":"Standing, not yet getting up","roots":["Brave","Healthy"],"lines":["She can <b>stand alone briefly</b> and walk with <b>one</b> hand: balance is coming fast.","The missing piece is <b>getting up from the floor without holding on</b>. It needs a deep squat and a push through the legs, so squatting to pick things up is the best practice.","She’s fast on the push walker. Great for legs, but walking with one hand or alone teaches more balance.","<b>Heading toward:</b> floor-to-stand, then first independent steps. Anywhere up to ~18 months is normal."]},
{"icon":"🧠","title":"Where she is now: brain and words","sub":"Pointing to ask","roots":["Curious","Kind"],"lines":["Pointing at something she wants while making a noise is called <b>asking pointing</b>. It’s one of the biggest communication milestones of the first year.","It means she knows you have a mind she can direct. Answering it every time teaches her that communicating works.","Copying you at the faucet is <b>imitation learning</b>: she watches what you do and tries it. Let her see you do everyday things slowly.","Bye-bye and baba/mama show up when the moment calls for them, not on request. That’s normal."]},
{"icon":"😌","title":"Where she is now: feelings","sub":"Confident, but a big change is coming","roots":["Secure","Self-led"],"lines":["She’s in a confident, independent stretch: she adjusted fast at the daycare trial and the birthday crowd.","Big change already happened: <b>the grandparents left</b>. She may look for them, or be a bit clingier with you. Name it: “You miss Nainai. Nainai is in China. We can call her.”","<b>Next cycle:</b> daycare + walking often bring a clingy wave in the next weeks (more protest at goodbyes, more night waking). It isn’t going backwards."]},
{"icon":"✅","title":"Do & don’t: pointing","sub":"Her point is a sentence","roots":["Secure","Curious"],"lines":["<b>Do</b> look, name, and respond fast. Speed teaches her that pointing works.","<b>Do</b> say “no” to the object, not to the point: “That’s hot. Not for touching.”","<b>Don’t</b> ignore it to “make her use words.” Pointing is the bridge to words, not a replacement."]},
{"icon":"🚪","title":"Do & don’t: opening everything","sub":"Curiosity, made safe","roots":["Curious","Self-led"],"lines":["<b>Do</b> give her one “yes” cabinet she can open freely; lock the rest (cleaners, meds, dishwasher pods up high).","<b>Do</b> name what she’s doing: open, close, in, out, on, off. Those are her next words.","<b>Don’t</b> keep saying “no” at every door. Change the space instead (see "+FP+"Our family’s way</a>)."]},
{"icon":"🦷","title":"Do & don’t: mouthing","sub":"Normal, needs a safe space","roots":["Healthy","Secure"],"lines":["Mouthing is still how she explores; it’s also teething. It fades slowly over the next year.","<b>Choke check:</b> if it fits through a toilet-paper tube (~1¼ in / 3 cm), it’s too small to be in her space.","<b>Never:</b> button batteries, small strong magnets (like magnetic tiles with loose pieces), coins, balloons, marbles.","<b>Do</b> swap rather than grab; <b>don’t</b> make it a chase game."],"refs":[{"label":"AAP/HealthyChildren: Choking prevention","url":"https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx"}]},
{"icon":"🍗","title":"Do & don’t: bigger chunks","sub":"She’s right, mostly","roots":["Healthy","Self-led"],"lines":["Preferring bigger pieces is common at 12 months: she can bite off and chew more.","<b>Do</b> offer soft long strips she can hold and bite (banana, avocado, soft-cooked carrot, omelet strips, shredded meat).","<b>Don’t:</b> whole grapes, round hot dog slices, whole nuts, popcorn, hard raw veg. Quarter round foods lengthwise.","Always seated and watched, never while walking."]},
{"icon":"🏊","title":"Keep doing: swimming","sub":"Calm about water","roots":["Brave","Healthy"],"lines":["Dipping 1–2 seconds with no coughing is great water comfort. Keep it short and fun, always in an adult’s arms.","Swimming isn’t drowning-proofing at this age: touch supervision near any water, including the bath."]},
{"icon":"🔭","title":"What’s next","sub":"Next 1–3 months","roots":["Curious","Brave"],"lines":["<b>Body:</b> floor-to-stand, then first steps alone.","<b>Words:</b> more pointing, maybe a new word or sign. Understanding grows much faster than talking.","<b>Feelings:</b> a clingier stretch around daycare is likely. Same goodbye routine every day helps the most."]}]
        w["daily"]=["👉 Answer 5+ points: look, name, give or swap, pause","🧸 Floor-to-stand tries, twice (squat-and-pick, toy on a stool)","🤝 One-hand walk, your hand at her shoulder or lower","🥛 Whole milk in a cup at 1–2 meals","🤟 Sign EAT, MILK, ALL DONE, saying the word each time","👋 Bye-bye when anyone leaves (no sneaking out)","🦷 Swap, don’t grab, when she mouths","📞 Short video call with the grandparents","Brush teeth twice (rice-grain smear)"]
        w["todos"]=["Mouth-safety sweep: toilet-paper-tube test, batteries and magnets up high","Set up one “yes” cabinet; lock the others","Buy a small open cup or straw cup if you don’t have one","Review the "+MK+"Milk at one</a> 4-week plan","Book / prep questions for the 12-month checkup (vaccines, iron, milk)","Read "+DC+"Daycare: first day</a> and start the packing list"]
        w["quiz"]=[
{"q":"She points at the banana and shouts. You hand it over without a word.","a":"dont","why":"Name it first: “Banana! You want banana.” The word is the gift."},
{"q":"She points at your phone. You say “Phone. Mama’s phone” and give her a cup instead.","a":"do","why":"You honored her point and kept the limit."},
{"q":"Pull her up by both hands so she learns to stand from the floor.","a":"dont","why":"She needs to push up through her own legs. Toy on a stool, help at the hips if at all."},
{"q":"Switch all formula to whole milk tomorrow, bedtime too.","a":"dont","why":"Go gradually over ~4 weeks; drop the bedtime bottle last."},
{"q":"A loose button battery on the floor, she seems fine after you take it away.","a":"do","why":"Trick question: you did right to take it. If you think she swallowed one, ER now."},
{"q":"Let her open the one cabinet with pots and spoons as often as she likes.","a":"do","why":"A “yes” space for a real need: opening and closing."}]
        w["scripts"]=[
{"icon":"👉","when":"She points and shouts at something","steps":[{"do":"Look where she points.","say":"Oh! The <b>ball</b>."},{"do":"Give it, or swap.","say":"You want the ball. Here you go. / That’s hot. Here’s your cup."},{"do":"Pause 3 seconds.","say":"(wait for her sound, then answer it)"}],"note":"Same three steps every time."},
{"icon":"🦷","when":"Something not-OK goes in her mouth","steps":[{"do":"Calm, get close, open hand.","say":"Can Mama have that?"},{"do":"Trade.","say":"Not for mouths. This one is for mouths!"}],"note":"No chasing or yelling; it turns it into a game."},
{"icon":"🏠","when":"She looks for the grandparents","steps":[{"do":"Name it.","say":"You’re looking for Nainai. Nainai went to China."},{"do":"Connect.","say":"Let’s look at Nainai’s photo. We’ll call her later."}],"note":"Short, true, warm. A photo book helps."}]
        w["details"]=[
{"icon":"👉","title":"Why the point matters so much","roots":["Curious","Kind"],"lines":["Babies who point more around their first birthday tend to have bigger vocabularies later, and the strongest effect comes when adults name what they point at.","It’s the first time she uses another person’s attention as a tool: the root of conversation."],"refs":[{"label":"Colonnesi et al. 2010: pointing and language (meta-analysis)","url":"https://doi.org/10.1016/j.dr.2010.10.001"}]},
{"icon":"🧸","title":"Why floor-to-stand comes after standing","roots":["Brave","Healthy"],"lines":["Standing up in the open means moving her weight over her feet from a crouch, with nothing to pull on. Many babies take their first steps before they can do it. Either order is fine."]}]
    else:
        w["oneLiner"]="满一岁啦！🎂 她会<b>指着要东西</b>、能<b>自己站一会儿</b>、<b>什么门都想开</b>。这周三件事：<b>她指了，您就接</b>；<b>练从地上站起来</b>；<b>开始用杯子喝牛奶</b>，上托班前把家里能吞的小东西清一遍。"
        w["bigThree"]=[
{"icon":"👉","title":"她指了，您就接：说出来，再回应","sub":"说话 · 全天","roots":["Secure","Curious"],"lines":[
"<b>什么时候：</b>这周她每次一边指一边叫，都接住。一天至少好好接五次（早饭、玩、出门、洗澡）。",
"<b>怎么接：</b>① 顺着她指的看过去；② 用两三个字说出来；③ 能给就给，不能给就说为什么，换一样；④ 停三秒，等她“回话”。",
"<b>可以说：</b>“球！你要<b>球</b>呀，给你。”不能给：“这是妈妈的<b>手机</b>，不给玩。给你<b>杯子</b>。”",
"<b>别：</b>一声不吭就递过去，也别非要她先说（“说‘球’！”）。现在她这一指，就是一句话。",
"<b>再加一点：</b>您也指给她看：“看！<b>狗狗</b>！”等她眼睛跟过去。两个人一起看同一样东西，词就是这么长出来的。"],"videos":[]},
{"icon":"🧸","title":"练从地上站起来：每天两回，每回三次","sub":"大运动 · 5分钟","roots":["Brave","Healthy"],"lines":[
"<b>什么时候：</b>上午睡醒后、晚饭前。光脚，地面干净不打滑。",
"<b>练法一，蹲下捡：</b>她牵着您一只手站着，脚边扔三个球。她蹲下捡一个，再站起来。站直了，您松手一秒。",
"<b>练法二，从地上站到凳子边：</b>她坐地上，一步远放个矮凳，上面摆她喜欢的玩具。<b>等着</b>，让她自己琢磨：手撑地、屁股撅起来、往上推。实在要帮，只扶一下胯，一秒就松。",
"<b>练法三，牵一只手走：</b>手的高度<b>不超过她肩膀</b>，左右换着牵，走到最后只给一根手指。",
"<b>可以说：</b>“起、起……站起来啦！”一屁股坐下：“扑通！再来？”语气平常，不用大声叫好。",
"<b>别用：</b>坐在里面的那种学步车（推着走的学步车可以）。"],"videos":["bEHaCVLeMtE"]},
{"icon":"🥛","title":"开始用杯子喝牛奶 + 家里清一遍小东西","sub":"健康 · 这周","roots":["Healthy","Self-led"],"lines":[
"<b>什么时候：</b>早饭、午饭配牛奶，用敞口杯或吸管杯。睡前那瓶先还是配方奶，最后才换（看"+MK+"一岁转牛奶</a>）。",
"<b>怎么换（四周计划第一周）：</b>白天先换掉一瓶配方奶，改成杯子装60–120毫升全脂奶。下周再换一瓶。四周左右到每天<b>480毫升</b>左右（别超过720毫升）。维生素D接着吃，医生说停再停。",
"<b>可以说：</b>“<b>奶</b>！凉凉的牛奶在杯子里。”同时比“奶”的手语。洒了：“哎呀，洒啦。擦一擦！”",
"<b>清一遍（一次，15分钟）：</b>能从卫生纸筒里穿过去的东西，全放高处。特别找<b>纽扣电池、小磁铁</b>、硬币、气球。托班的包也查一遍。",
"<b>她往嘴里塞东西：</b>别硬抢。换：“这个不能放嘴里，这个可以！”把“可以啃的小篮子”递给她。"],"videos":[]}]
        w["cards"]=[
{"icon":"🦵","title":"现在的她：身体","sub":"会站了，还不会自己起来","roots":["Brave","Healthy"],"lines":["能<b>自己站一小会儿</b>，牵<b>一只手</b>就能走，平衡长得很快。","还差一步：<b>不扶东西从地上站起来</b>。这要深蹲再用腿往上推，所以“蹲下捡东西”是最好的练习。","推学步车跑得飞快，练腿挺好；但牵一只手走、自己走，更练平衡。","<b>接下来：</b>先会从地上站起来，再迈出自己的第一步。18个月以内都算正常。"]},
{"icon":"🧠","title":"现在的她：脑子和说话","sub":"会指着要了","roots":["Curious","Kind"],"lines":["一边指一边叫，想要什么就指什么，这是一岁前后<b>最重要的沟通里程碑</b>之一。","说明她明白：您有自己的想法，她可以“指挥”您。每次都接住，她就知道：表达有用。","看您拧水龙头马上学会，这叫<b>模仿学习</b>。平时做家务慢一点，让她看清楚。","“拜拜”、叫爸爸妈妈，都是碰到那个场景才说，让她说她不说，很正常。"]},
{"icon":"😌","title":"现在的她：情绪","sub":"挺自信，大变化要来了","roots":["Secure","Self-led"],"lines":["这阵子她挺自信、挺独立：托班试园、生日派对人那么多，都适应得很快。","已经有个大变化：<b>爷爷奶奶回国了</b>。她可能会到处找，或者更黏您一点。说出来：“你想奶奶了。奶奶回中国了，我们待会儿给她打视频。”","<b>下一波：</b>上托班加上学走路，接下来几周常会再黏人一阵（分开时哭得更厉害、夜里多醒）。这不是退步。"]},
{"icon":"🚪","title":"什么门都想开","sub":"好奇心，弄安全就好","roots":["Curious","Self-led"],"lines":["专门留一个“随便开”的柜子，其他的都锁上（清洁剂、药、洗碗块放高处）。","边玩边说：开、关、进去、出来、开、关。这些就是她接下来要学的词。","别每个门都喊“不行”。改环境，比管孩子省力（见"+FP+"家庭教养原则</a>）。"]},
{"icon":"🦷","title":"什么都往嘴里放","sub":"正常，但要安全","roots":["Healthy","Secure"],"lines":["这个年纪还在用嘴认识东西，也在长牙。明年会慢慢少下来。","<b>卫生纸筒测试：</b>能穿过卫生纸筒（直径约3厘米）的东西，不能放在她够得到的地方。","<b>绝对不行：</b>纽扣电池、强力小磁铁（比如会掉零件的磁力片）、硬币、气球、弹珠。","换，别抢；别弄成追着跑的游戏。"],"refs":[{"label":"美国儿科学会：预防噎呛（英文）","url":"https://www.healthychildren.org/English/health-issues/injuries-emergencies/Pages/Choking-Prevention.aspx"}]},
{"icon":"🍗","title":"喜欢大块的","sub":"她是对的，注意几样","roots":["Healthy","Self-led"],"lines":["一岁左右爱吃大块的很常见：她能咬下来、嚼得动了。","给软软的长条，她自己拿着啃：香蕉、牛油果、煮软的胡萝卜、蛋饼条、撕碎的肉。","<b>不给：</b>整颗葡萄、圆片香肠、整粒坚果、爆米花、硬的生蔬菜。圆的东西竖着切四瓣。","坐着吃、有人看着，别边走边吃。"]},
{"icon":"🏊","title":"继续保持：游泳","sub":"不怕水","roots":["Brave","Healthy"],"lines":["能潜水一两秒还不呛，说明她对水很放松。时间短、玩得开心、一直在大人怀里。","这么小学游泳不等于不会溺水：靠近任何水（包括洗澡盆），大人都要伸手就够得着。"]},
{"icon":"🔭","title":"接下来一到三个月","sub":"心里有个数","roots":["Curious","Brave"],"lines":["<b>身体：</b>从地上站起来，再自己走第一步。","<b>说话：</b>指得更多，可能冒出一个新词或新手语。听懂的比会说的多得多。","<b>情绪：</b>上托班前后多半会黏人一阵。每天用一样的方式告别，最管用。"]}]
        w["daily"]=["👉 好好接住她五次“指”：看、说、给或换、等","🧸 练两回从地上站起来（蹲下捡、凳子上放玩具）","🤝 牵一只手走，手不高过她肩膀","🥛 一两顿饭用杯子喝牛奶","🤟 比“吃”“奶”“吃完了”，边比边说","👋 谁出门都说拜拜，不偷偷走","🦷 她啃了不能啃的：换，别抢","📞 跟爷爷奶奶视频一小会儿","刷牙两次（米粒大小牙膏）"]
        w["todos"]=["家里清一遍：卫生纸筒测试，电池、磁铁放高处","留一个“随便开”的柜子，其他上锁","备一个小敞口杯或吸管杯","看看"+MK+"一岁转牛奶</a>的四周计划","准备12个月体检要问的（疫苗、铁、牛奶）","看"+DC+"上托班第一天</a>，开始打包"]
        w["quiz"]=[
{"q":"她指着香蕉叫，您一声不吭递过去？","a":"dont","why":"先说出来：“香蕉！你要香蕉呀。”这个词才是真正的礼物。"},
{"q":"她指着手机，您说“手机，妈妈的手机”，然后给她一个杯子？","a":"do","why":"接住了她的“指”，也守住了规矩。"},
{"q":"拉着她两只手把她从地上拽起来，帮她学站？","a":"dont","why":"得靠她自己的腿往上推。凳子上放玩具，要帮最多扶一下胯。"},
{"q":"明天开始配方奶全换成牛奶，睡前那瓶也换？","a":"dont","why":"四周左右慢慢换，睡前那瓶最后换。"},
{"q":"那个“随便开”的柜子（锅和勺子），她想开几次就开几次？","a":"do","why":"给她真实的需要（开开关关）一个“可以”的地方。"}]
        w["scripts"]=[
{"icon":"👉","when":"她指着东西大叫","steps":[{"do":"顺着她指的看过去。","say":"哦！<b>球</b>。"},{"do":"能给就给，不能给就换。","say":"你要球呀，给你。／这个烫，给你杯子。"},{"do":"停三秒。","say":"（等她出声，再接她的话）"}],"note":"每次都是这三步。"},
{"icon":"🦷","when":"她把不该啃的塞进嘴里","steps":[{"do":"别急，靠过去，摊开手。","say":"给妈妈好不好？"},{"do":"换一个。","say":"这个不能放嘴里，这个可以！"}],"note":"别追、别吼，不然她当游戏玩。"},
{"icon":"🏠","when":"她到处找爷爷奶奶","steps":[{"do":"说出来。","say":"你在找奶奶呀。奶奶回中国了。"},{"do":"连上。","say":"我们看看奶奶的照片，待会儿给她打视频。"}],"note":"简短、说实话、语气暖。"}]
        w["details"]=[{"icon":"👉","title":"为什么“指”这么重要","roots":["Curious","Kind"],"lines":["一岁前后指得多的宝宝，之后词汇量往往更大；大人跟着说出来，效果最明显。","这是她第一次把别人的注意力当工具来用，是“聊天”的起点。"],"refs":[{"label":"Colonnesi 等 2010：指物与语言发展（综述，英文）","url":"https://doi.org/10.1016/j.dr.2010.10.001"}]}]
    return w

def wk8(L):
    en=L=="en"
    w={"title":"Week 8" if en else "第8周","age":"~12 months" if en else "一岁","dates":"Nov 9–15, 2026" if en else "2026年11月9日–15日","now":NOW[L][1:]}
    if en:
        w["now"]=["🎂 Just turned 1"]+w["now"]
        w["oneLiner"]="Daycare is starting. This week is <b>Secure first</b>: <b>the same goodbye every time</b>, <b>a calm reunion hour</b>, and <b>keep floor-to-stand + pointing going</b> at home. Expect some clinginess; it’s the next cycle, not a step back."
        w["bigThree"]=[
{"icon":"👋","title":"Same goodbye, every drop-off","sub":"Feelings · 2 min","roots":["Secure","Brave"],"lines":[
"<b>When:</b> every daycare drop-off this week. Practice once at home first with Teddy (see plays).",
"<b>How:</b> arrive a few minutes early, stay 3–5 min at the play area, hand her to the same teacher, hug, say the line, wave, <b>leave</b>. Under 1 minute from the line to the door.",
"<b>Say:</b> “Mama’s going to work. Teacher stays with you. Mama comes back after nap. <b>Bye-bye!</b>” (wave, and give her a chance to wave).",
"<b>Don’t:</b> sneak out, come back in when she cries, or stretch the goodbye. Crying at drop-off is normal; ask the teacher how long it lasted.",
"Full checklist: "+DC+"Daycare: first day</a>."],"videos":[]},
{"icon":"🤗","title":"Reunion hour: reconnect before anything else","sub":"Feelings · 30–60 min","roots":["Secure","Kind"],"lines":[
"<b>When:</b> the first hour after pickup, every day.",
"<b>How:</b> greet her at her level, hold her as long as she wants, then floor time: <b>she leads</b>, you follow. Phones away. Easy dinner, early bedtime.",
"<b>Say:</b> “Mama came back! I missed you.” Then narrate, don’t quiz: “You’re pouring. Pour, pour.”",
"<b>Expect:</b> meltdowns or clinginess at home; she held it together all day and lets go with you. That’s trust.",
"<b>Night waking:</b> calm, brief comfort, same bedtime routine. Don’t start new habits you’ll want to undo."],"videos":[]},
{"icon":"🧸","title":"Keep floor-to-stand + pointing going (short)","sub":"Body & words · 5 min","roots":["Brave","Curious"],"lines":[
"<b>When:</b> weekend mornings and 5 minutes after the reunion if she’s up for it. If she’s tired, skip it; connection comes first this week.",
"<b>How:</b> squat-and-pick with 3 balls; toy on a low stool; one-hand walks. Keep answering her points: look, name, give or swap, pause.",
"<b>Say:</b> “Up, up… you’re up!” / “<b>Shoe!</b> You want your shoe.”",
"<b>Milk, week 2 of 4:</b> swap a second daytime bottle for whole milk in a cup. Bedtime bottle still last. Tell daycare: whole milk in a cup."],"videos":["bEHaCVLeMtE"]}]
        w["cards"]=[
{"icon":"😢","title":"Where she is now: feelings","sub":"A new cycle starting","roots":["Secure","Self-led"],"lines":["Two big changes close together: the grandparents left and daycare begins. A clingy wave is expected: crying at goodbyes, wanting to be held, waking at night.","It usually eases in <b>2–4 weeks</b> with a predictable routine. Her quick trial adjustment is a good sign.","Her secure base is you. The reunion hour refills it."]},
{"icon":"🦵","title":"Where she is now: body","sub":"Almost on her own feet","roots":["Brave","Healthy"],"lines":["Same phase as last week: stands briefly, walks with one hand. Daycare often speeds up walking (she watches other kids).","New tiredness may make her skip practice. That’s fine."]},
{"icon":"🦷","title":"Mouthing at daycare","sub":"Normal, and teachers know it","roots":["Healthy","Secure"],"lines":["Infant rooms are set up for mouthers: toys are big and washed often. Ask how they handle it; it’s a normal question.","Expect more colds in the first months. Wash hands at pickup and before eating.","Keep the yes-to-mouth basket at home."]},
{"icon":"✅","title":"Do & don’t: daycare start","sub":"Small things that help","roots":["Secure","Brave"],"lines":["<b>Do</b> send a comfort object (lovey, a T-shirt that smells like you) if daycare allows.","<b>Do</b> share her signs (EAT, MILK, ALL DONE) and that she points to ask.","<b>Do</b> keep weekends calm and familiar.","<b>Don’t</b> start other big changes this week (bedtime bottle, new crib)."]},
{"icon":"📞","title":"Grandparents, remotely","sub":"Keep the bond","roots":["Secure","Kind"],"lines":["Short video calls (5 min) when she’s fed and happy work better than long ones.","Grandparents can sing the same songs and say bye-bye at the end, a nice extra goodbye practice."]}]
        w["daily"]=["👋 Same goodbye line + wave at drop-off","🤗 Reunion hour: hold, floor time, she leads","👉 Answer her points: look, name, give or swap","🧸 One short floor-to-stand session (if she’s up for it)","🥛 Whole milk in a cup at 2 meals (bedtime bottle last)","🤟 EAT, MILK, ALL DONE with words","🧼 Hand-wash at pickup and before meals","😴 Same bedtime routine, earlier if tired"]
        w["todos"]=["Pack and label (see "+DC+"Daycare: first day</a>)","Practice the Teddy goodbye at home","Tell teachers: points to ask, signs EAT/MILK/ALL DONE, whole milk in a cup, mouths things","Ask about nap routine and how they handle mouthing","12-month checkup if not done"]
        w["quiz"]=[
{"q":"She’s playing happily, so you slip out without saying goodbye.","a":"dont","why":"Sneaking out makes her more watchful next time. Short, clear goodbye."},
{"q":"She cries at drop-off, so you go back in to calm her.","a":"dont","why":"Coming back stretches the hard part. The teacher takes over; call later."},
{"q":"Melts down after pickup: you hold her and keep the evening simple.","a":"do","why":"She saved it for her safe person. Comfort, not correction."},
{"q":"Drop the bedtime bottle this week too, to get it over with.","a":"dont","why":"One big change at a time. Bedtime bottle goes last."}]
        w["scripts"]=[
{"icon":"👋","when":"Drop-off","steps":[{"do":"Hug at her level.","say":"Mama’s going to work. Teacher stays with you."},{"do":"Wave and go.","say":"Mama comes back after nap. Bye-bye!"}],"note":"Same words every day."},
{"icon":"🤗","when":"Pickup","steps":[{"do":"Get low, open arms.","say":"Mama came back! I missed you."},{"do":"Hold as long as she wants.","say":"You had a big day."}],"note":"Questions for the teacher can wait 2 minutes."},
{"icon":"🌙","when":"She wakes at night","steps":[{"do":"Go in calm, low voice, short.","say":"Mama’s here. It’s night-night time."},{"do":"Settle the way you usually do.","say":"Shh… sleep time."}],"note":"Keep it boring and the same."}]
        w["details"]=[{"icon":"🔁","title":"Why a fixed goodbye works","roots":["Secure"],"lines":["A predictable goodbye-and-return lets her learn: Mama leaves, Mama comes back. Each repeat builds trust. Long or sneaky goodbyes make the pattern harder to learn."],"refs":[{"label":"AAP/HealthyChildren: Separation anxiety","url":"https://www.healthychildren.org/English/ages-stages/baby/Pages/Soothing-Your-Childs-Separation-Anxiety.aspx"}]}]
    else:
        w["now"]=["🎂 刚满一岁"]+w["now"]
        w["oneLiner"]="要上托班啦。这周<b>安全感第一</b>：<b>每次告别都一样</b>；<b>接回来先好好黏一小时</b>；在家<b>接着练站起来、接着接她的“指”</b>。会黏人一阵，这是新一轮成长，不是退步。"
        w["bigThree"]=[
{"icon":"👋","title":"每次送托班，告别都一样","sub":"情绪 · 2分钟","roots":["Secure","Brave"],"lines":[
"<b>什么时候：</b>这周每次送托班。先在家用小熊演一遍（见下面的游戏）。",
"<b>怎么做：</b>早到几分钟，在玩的地方陪她三五分钟，交给同一位老师，抱一抱，说那句话，挥手，<b>走</b>。从说完到出门不超过一分钟。",
"<b>可以说：</b>“妈妈去上班啦，老师陪着你。睡完午觉妈妈就来接你。<b>拜拜！</b>”（挥手，给她机会也挥一挥）",
"<b>别：</b>偷偷溜走、她一哭又折回去、拖拖拉拉。送的时候哭很正常，晚点问问老师哭了多久。",
"完整清单："+DC+"上托班第一天</a>。"],"videos":[]},
{"icon":"🤗","title":"接回来的第一个小时：先黏在一起","sub":"情绪 · 30–60分钟","roots":["Secure","Kind"],"lines":[
"<b>什么时候：</b>每天接回来后的第一个小时。",
"<b>怎么做：</b>蹲下迎她，她想抱多久就抱多久，然后在地上陪玩，<b>她说了算</b>，您跟着。手机收起来。晚饭简单点，早点睡。",
"<b>可以说：</b>“妈妈回来啦！想你了。”然后说她在干什么，别考她：“你在倒水，倒呀倒。”",
"<b>心里有数：</b>在家可能大哭、特别黏。她在托班撑了一天，回到您身边才放松。这是信任。",
"<b>夜里醒：</b>平静、简短地安抚，睡前程序照旧。别开始以后还得戒掉的新习惯。"],"videos":[]},
{"icon":"🧸","title":"接着练站起来、接着接“指”（短一点）","sub":"大运动 · 说话 · 5分钟","roots":["Brave","Curious"],"lines":[
"<b>什么时候：</b>周末早上，或者接回来黏够了、她有兴致时练五分钟。累了就不练，这周陪伴第一。",
"<b>怎么练：</b>扔三个球蹲下捡；矮凳上放玩具；牵一只手走。她指了照样接：看、说、给或换、等一等。",
"<b>可以说：</b>“起、起……站起来啦！”／“<b>鞋</b>！你要鞋呀。”",
"<b>牛奶第二周：</b>白天再换掉一瓶，改杯子喝牛奶。睡前那瓶还是最后换。跟托班说：杯子装全脂奶。"],"videos":["bEHaCVLeMtE"]}]
        w["cards"]=[
{"icon":"😢","title":"现在的她：情绪","sub":"新一轮开始了","roots":["Secure","Self-led"],"lines":["两件大事挨着来：爷爷奶奶回国、开始上托班。黏人一阵很正常：分开时哭、要抱、夜里醒。","作息固定下来，一般<b>两到四周</b>会好很多。试园适应得快，是好兆头。","她的“安全基地”是您。接回来那一小时，就是给她充电。"]},
{"icon":"🦵","title":"现在的她：身体","sub":"快自己走了","roots":["Brave","Healthy"],"lines":["跟上周差不多：能站一会儿，牵一只手能走。上托班看别的小朋友走，常常会走得更快。","累了不想练，就不练。"]},
{"icon":"🦷","title":"在托班啃东西","sub":"正常，老师都懂","roots":["Healthy","Secure"],"lines":["婴儿班本来就是给爱啃东西的宝宝准备的：玩具大、常消毒。问问老师怎么处理，这很正常。","头几个月感冒会多。接回来先洗手，吃饭前洗手。","家里那个“可以啃的小篮子”继续用。"]},
{"icon":"✅","title":"上托班，几件小事","sub":"有用的小细节","roots":["Secure","Brave"],"lines":["托班允许的话，带个安抚物（小毯子、有妈妈味道的T恤）。","告诉老师她会的手语（吃、奶、吃完了），还有她会指着要东西。","周末过得安静、熟悉一点。","这周别再加别的大变化（戒睡前奶、换床）。"]},
{"icon":"📞","title":"爷爷奶奶隔着屏幕陪","sub":"感情不断","roots":["Secure","Kind"],"lines":["她吃饱、心情好时打五分钟视频，比打很久效果好。","唱一样的儿歌，最后跟她挥手说拜拜，正好又练一次告别。"]}]
        w["daily"]=["👋 送托班：一样的话 + 挥手拜拜","🤗 接回来一小时：抱、地上陪玩、她说了算","👉 她指了就接：看、说、给或换","🧸 有兴致就练一会儿站起来","🥛 两顿饭用杯子喝牛奶（睡前那瓶最后换）","🤟 比“吃”“奶”“吃完了”，边比边说","🧼 接回来、吃饭前洗手","😴 睡前程序照旧，累了就早点睡"]
        w["todos"]=["打包贴名（见"+DC+"上托班第一天</a>）","在家用小熊演一遍告别","告诉老师：会指着要、手语（吃/奶/吃完了）、杯子喝全脂奶、爱啃东西","问问午睡怎么安排、宝宝啃东西怎么处理","12个月体检还没做的话约上"]
        w["quiz"]=[
{"q":"她玩得正开心，您趁机悄悄溜走？","a":"dont","why":"偷偷走，下次她会更提防。简短、说清楚地告别。"},
{"q":"送的时候她哭了，您又折回去哄？","a":"dont","why":"折回去会把最难的那段拖长。交给老师，晚点打电话问。"},
{"q":"接回来她大哭，您抱着她，晚上过得简单点？","a":"do","why":"她把情绪留给了最安心的人。要的是安抚，不是纠正。"},
{"q":"干脆这周把睡前奶也戒了？","a":"dont","why":"一次只改一件大事，睡前那瓶最后换。"}]
        w["scripts"]=[
{"icon":"👋","when":"送托班","steps":[{"do":"蹲下抱一抱。","say":"妈妈去上班啦，老师陪着你。"},{"do":"挥手，走。","say":"睡完午觉妈妈来接你。拜拜！"}],"note":"每天一样的话。"},
{"icon":"🤗","when":"接回来","steps":[{"do":"蹲下，张开手。","say":"妈妈回来啦！想你了。"},{"do":"她想抱多久抱多久。","say":"今天好棒呀，玩了一整天。"}],"note":"问老师的事，晚两分钟再说。"},
{"icon":"🌙","when":"夜里醒了","steps":[{"do":"平静进去，小声，简短。","say":"妈妈在呢，该睡觉觉了。"},{"do":"照平常的办法哄睡。","say":"嘘……睡觉啦。"}],"note":"越平淡、越一样越好。"}]
        w["details"]=[{"icon":"🔁","title":"为什么告别要固定","roots":["Secure"],"lines":["每次都一样地走、一样地回来，她才能学会：妈妈会走，妈妈也一定会回来。每重复一次，信任多一分。拖拖拉拉或偷偷走，反而让她学不会。"],"refs":[{"label":"美国儿科学会：分离焦虑（英文）","url":"https://www.healthychildren.org/English/ages-stages/baby/Pages/Soothing-Your-Childs-Separation-Anxiety.aspx"}]}]
    return w

harder7={"one-hand-walk":(["Hold one hand at her shoulder or lower, swap sides, end on one finger. Then let go for a step."],["牵一只手，不高过她肩膀，左右换，最后只给一根手指，再松手一步。"])}
C7=[("couch-to-mama",("Wider gap: couch to your arms, 2–3 steps. Hold nothing; she comes to you. (Wk 4, harder)","沙发到您怀里，拉开两三步，不扶，让她自己扑过来。（第4周，升级）")),
    ("stand-to-stand-gap",None),("one-hand-walk",("She walks with one hand now. Keep your hand at her shoulder or lower, swap sides, end on one finger. (Wk 4, harder)","她已经能牵一只手走了。手不高过她肩，左右换，最后只给一根手指。（第4周，升级）")),
    ("playground-mission",None),("bring-it",None),("throw-basket",None),("point-name-walk",None),("pen-book-turns",None),("echo-and-add",None),
    ("family-photo-book",("“Where’s Nainai? Where’s Yeye?” Pat the photos; grandparents are far away now, so this keeps them close. (Wk 4)","“奶奶在哪儿？爷爷在哪儿？”拍拍照片。爷爷奶奶回国了，翻翻相册让她记着。（第4周）")),
    ("quiet-board-book",None),("this-or-that",None),("cup-shuffle",None),("stack-crash",None),("lid-lab",None),("freeze-dance",None),("rhythm-copy",None),("gesture-songs",None),("copy-me",None),("wipe-up-helper",None),("solo-play-checkins",None),("peer-time",None),("messy-tray",None),("water-table",None),("daytime-night-night",None)]
N7=["color-match-1","posting-box","tube-ball-drop","big-sticker","sticky-wall","floor-to-stand","squat-to-stand","point-honor","door-open-close","faucet-pour","in-and-out","cup-sips","swim-bath-pour","mouth-ok-basket","mirror-signs"]
# week 8: carry from wk7 minus squat-pick-up (merged into squat-to-stand) and stand-to-stand-gap, cup-shuffle kept
C8=[c for c in C7 if c[0] not in ("squat-pick-up","stand-to-stand-gap","throw-basket","messy-tray")]
N8=N7+["color-match-2","pipe-colander","bye-bye-teddy","hat-on-off"]

def build(n,start,end,emoji,fn,ci,ni):
    d={"id":"week-%02d"%n,"emoji":emoji,"start":start,"end":end,"perLang":True,"videos":W4["videos"]}
    for L in ("en","zh"):
        w=fn(L); (revise7 if n==7 else revise8)(w,L); w["signs"]=signs(L,n); w["timeline"]=tl(L); w["watch"]=WATCH[L]; w["sources"]=SRC[L]
        w["plays"]=plays(L,ci,ni,("",""))
        d[L]=w
    assert [p["id"] for p in d["en"]["plays"]]==[p["id"] for p in d["zh"]["plays"]]
    s=json.dumps(d,ensure_ascii=False,indent=1)
    for bad in ["2025-11-05","Nov 5","11月5日"]: assert bad not in s, bad
    open("weeks/week-%02d.json"%n,"w").write(s)
    return d
d7=build(7,"2026-11-02","2026-11-08","🎂",wk7,C7,N7)
d8=build(8,"2026-11-09","2026-11-15","🎒",wk8,C8,N8)
print([p["id"] for p in d7["en"]["plays"]]); print(len(d8["en"]["plays"]))
