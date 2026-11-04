# Social-sourced revision (Melody, Nov 4): play ideas from what parents post (XHS/Instagram), research only as safety check.
REFS_EN=[{"label":"Hands On As We Grow: pom-pom sorting + posting at 15 months (mom blog/IG)","url":"https://handsonaswegrow.com/pom-pom-sorting-posting-activity/"},
 {"label":"@thetwomamabears (Instagram): color sorting, 15–19 months","url":"https://twomamabears.com/pom-pom-color-sorting-activity-idea-with-tweezers-for-fine-motor-practice/"},
 {"label":"The Montessori Twin Mama: 12-month activities (coin drop, ball tracker)","url":"https://themontessoritwinmama.com/2024/01/16/engaging-montessori-activities-to-try-at-12-months-old/"},
 {"label":"Hellobee: DIY coin box, tube posting, pipe cleaners in a colander","url":"https://www.hellobee.com/2013/02/13/5-quick-and-easy-montessori-activities-for-toddlers/"},
 {"label":"Chinese parent site: 15-month “red and yellow beads” sorting game","url":"http://www.jiyifa.net/zaojiao/1042435.html"}]
REFS_ZH=[{"label":"15个月早教游戏：分红黄珠（中文）","url":"http://www.jiyifa.net/zaojiao/1042435.html"},
 {"label":"颜色分类游戏玩法（早教机构，中文）","url":"https://www.youkee.com/ziliao/14832.html"},
 {"label":"美国妈妈博主：15个月玩毛球分色、投洞（英文）","url":"https://handsonaswegrow.com/pom-pom-sorting-posting-activity/"},
 {"label":"Instagram @thetwomamabears：15–19个月颜色分类（英文）","url":"https://twomamabears.com/pom-pom-color-sorting-activity-idea-with-tweezers-for-fine-motor-practice/"},
 {"label":"蒙氏双胞胎妈妈：12个月教具（投币盒、滚球轨道，英文）","url":"https://themontessoritwinmama.com/2024/01/16/engaging-montessori-activities-to-try-at-12-months-old/"}]
CHOKE_EN="<b>Mouth-safe rule for every activity:</b> nothing that fits through a toilet-paper tube (~1¼ in / 3 cm). So: ball-pit balls or 2-inch+ balls, not small pom-poms or beads; big lids or wooden discs, not coins; you sit right there, and it goes up high after."
CHOKE_ZH="<b>所有游戏都守一条：</b>能穿过卫生纸筒（约3厘米）的东西不给。所以用海洋球或5厘米以上的大球，不用小毛球、小珠子；用大瓶盖或大木片，不用硬币。大人坐在旁边，玩完收高处。"

def add_social(NEW, add):
    add("color-match-1","🔴",("Red goes with red (step 1)","Two VERY different colors, identical objects: 3 red + 3 yellow ball-pit balls, one red cup, one yellow cup. You drop one: “Red goes with red.” Hand her one, point to the cup. Any ball in any cup is fine; just keep naming. (from parent posts)"),("红的找红的（第一步）","两种差别很大的颜色、一模一样的东西：红黄海洋球各三个，一个红杯、一个黄杯。您先放一个：“红的找红的。”递给她一个，指指杯子。放哪个杯子都行，您只管说颜色。（家长分享的玩法）"),["Curious","Self-led"],("3–5 min","3–5分钟"))
    add("color-match-2","🟡",("Find the same (step 2)","Hold up a red ball: “Where’s another red one?” with 2 balls on the floor (red, yellow). Then try a red block next to a red ball. Still two colors. (from parent posts)"),("找一样的（第二步）","举起红球：“另一个红的在哪儿？”地上只摆一红一黄。再试试红积木放红球旁边。还是只用两种颜色。（家长分享的玩法）"),["Curious","Self-led"],("3 min","3分钟"))
    add("posting-box","📮",("Posting box","Cut a slot in a formula-tin or oatmeal lid; post big lids or 2-inch wooden discs. Start with a round hole + balls, then the slot. Tilting the disc is the hard part. (Montessori “coin box”, IG favorite)"),("投币盒","奶粉罐或燕麦罐盖子上开个口，投大瓶盖或5厘米的大木片。先开圆洞投球，再换成长缝。把木片转过来对准缝，是最难的一步。（蒙氏投币盒，Instagram上很火）"),["Curious","Brave"],("5 min","5分钟"))
    add("tube-ball-drop","🎳",("Ball drop tube","Tape a paper-towel or wrapping-paper tube on the wall at a slant; she drops a ball in the top and watches it come out the bottom. Use a wide poster tube and balls bigger than a toilet-paper tube opening. (IG/XHS DIY)"),("滚球管道","把粗纸筒（海报筒）斜着贴在墙上，她从上面放球，看球从下面滚出来。球要比卫生纸筒口大。（Instagram、小红书都有人做）"),["Curious","Brave"],("5 min","5分钟"))
    add("big-sticker","⭐",("Big sticker peel","Large stickers (palm-size or bigger) on the back of your hand or her tray edge; she peels them off and sticks them on paper. Lift a corner for her at first. Supervised. (XHS 贴纸 favorite)"),("撕大贴纸","手掌大的贴纸贴在您手背或餐盘边上，她撕下来贴到纸上。一开始帮她翘起一个角。大人在旁边看着。（小红书很火的贴纸游戏）"),["Self-led","Curious"],("5 min","5分钟"))
    add("pipe-colander","🥣",("Colander poking (pre-threading)","Thick pipe cleaners or chopsticks poked into a colander’s holes; take them out, poke again. Real bead threading comes ~18 months+ with big 2-inch beads. Supervised. (IG Montessori favorite)"),("插漏勺（穿珠前练习）","粗扭扭棒或筷子插进漏勺的小洞，拔出来再插。真正穿珠子要18个月以后，用5厘米大珠子。大人看着。（Instagram蒙氏常见）"),["Curious","Self-led"],("5 min","5分钟"))
    add("sticky-wall","🧻",("Sticky wall","Contact paper taped sticky-side out on a low wall; she sticks big paper shapes or scarves on and pulls them off. Great while standing. (IG/XHS DIY)"),("粘粘墙","矮处墙上贴一张透明贴纸（粘面朝外），让她把大纸片、丝巾粘上去再撕下来。站着玩，还顺便练站。（Instagram、小红书DIY）"),["Curious","Healthy"],("5–10 min","5–10分钟"))

COLOR_EN={"icon":"🔴","title":"“Red goes with red”: start color matching","sub":"Curious · 3–5 min, once a day","roots":["Curious","Self-led"],"lines":[
"<b>When:</b> once a day after her morning nap, at a low table or on the floor. Stop when she wanders off.",
"<b>Set up:</b> just <b>2 very different colors</b> (red + yellow), <b>identical objects</b> (6 ball-pit balls), a red cup and a yellow cup. Nothing else on the tray.",
"<b>How:</b> you go first, slowly: pick up a red ball, look at it, drop it in the red cup. Then hand her one and point at its cup. Let her do it her way: dumping, mixing, mouthing a big ball are all fine.",
"<b>Say:</b> “<b>Red</b> goes with <b>red</b>.” “<b>Yellow</b> goes with <b>yellow</b>.” When she gets one in: “Red with red!” Wrong cup: just say what it is (“That’s yellow”) and move on. No “No, wrong!”",
"<b>Why it’s realistic:</b> lots of parents online show kids sorting 2 colors around 15–18 months after months of this kind of modeling. At 12 months she’s just learning that color is a thing. Naming colors comes much later (~2½–3+).",
CHOKE_EN],"videos":[]}
COLOR_ZH={"icon":"🔴","title":"“红的找红的”：从现在开始玩颜色配对","sub":"好奇 · 每天一次，3–5分钟","roots":["Curious","Self-led"],"lines":[
"<b>什么时候：</b>每天上午睡醒后玩一次，矮桌或地上。她走开了就收。",
"<b>准备：</b>只用<b>两种差别很大的颜色</b>（红、黄），<b>一模一样的东西</b>（六个海洋球），一个红杯、一个黄杯。托盘上别放别的。",
"<b>怎么玩：</b>您先来，慢一点：拿起红球，看一看，放进红杯。再递给她一个，指指该放的杯子。她怎么玩都行：倒出来、混在一起、啃一啃大球，都没关系。",
"<b>可以说：</b>“<b>红的</b>找<b>红的</b>。”“<b>黄的</b>找<b>黄的</b>。”放对了：“红的跟红的！”放错了：说一下就过去（“这是黄的”），别说“不对、错了”。",
"<b>心里有数：</b>小红书上很多宝宝15–18个月就能分两种颜色，都是这样天天示范出来的。她现在一岁，刚开始发现“颜色”这回事。会说颜色名字要晚得多（两岁半到三岁以后）。",
CHOKE_ZH],"videos":[]}
SOC_CARD_EN={"icon":"📱","title":"What real parents are doing at 12–18 months","sub":"Ideas from Instagram & Xiaohongshu","roots":["Curious","Self-led"],"lines":[
"The most-shared hands-on activities for this age: <b>color matching</b> (2 colors first), <b>posting boxes</b> (coin box, balls into a hole), <b>ball drops</b> through tubes, <b>sticker peeling</b>, <b>poking sticks into a colander</b> (before bead threading), and <b>sticky walls</b>.",
"Most are DIY from things at home: formula tins, cups, paper-towel tubes, contact paper.",
"Many posts use small pom-poms and beads. <b>Not for her yet</b>, because she still mouths: we swapped in ball-pit balls, big lids, and big stickers.",
"<b>Watch her, not the post:</b> if she pushes it away, it’s too hard or too easy. Put it away and try again in 1–2 weeks."],"refs":REFS_EN}
SOC_CARD_ZH={"icon":"📱","title":"别的爸妈在给12–18个月宝宝玩什么","sub":"来自Instagram和小红书","roots":["Curious","Self-led"],"lines":[
"这个年龄最多人晒的动手游戏：<b>颜色配对</b>（先两种颜色）、<b>投币盒、投球</b>、<b>纸筒滚球</b>、<b>撕贴纸</b>、<b>往漏勺里插棍子</b>（穿珠子前的练习）、<b>粘粘墙</b>。",
"大多是家里东西自己做：奶粉罐、杯子、纸筒、透明贴纸。",
"很多帖子用小毛球、小珠子。<b>她现在还啃东西，先别用</b>：我们换成海洋球、大瓶盖、大贴纸。",
"<b>看她，不看帖子：</b>她推开不玩，就是太难或太简单。先收起来，过一两周再拿出来。"],"refs":REFS_ZH}

def revise7(w,L):
    en=L=="en"; b=w["bigThree"]; milk=b[2]
    b[2]=b[1]; b[1]=COLOR_EN if en else COLOR_ZH
    milk=dict(milk); milk["sub"]=("This week" if en else "这周")
    w["cards"].insert(0,milk)
    w["cards"].insert(4,SOC_CARD_EN if en else SOC_CARD_ZH)
    w["oneLiner"]=("Happy first birthday week! 🎂 She’s <b>pointing to ask</b>, <b>standing alone</b>, and <b>opening everything</b>. This week: <b>answer every point</b>, start <b>“red goes with red”</b> color matching, and <b>practice floor-to-stand</b>. Also: milk in a cup and a mouth-safety sweep (cards below)." if en else
      "满一岁啦！🎂 她会<b>指着要东西</b>、能<b>自己站一会儿</b>、<b>什么门都想开</b>。这周三件事：<b>她指了，您就接</b>；开始玩<b>“红的找红的”</b>；<b>练从地上站起来</b>。另外：杯子喝牛奶、家里清一遍小东西（见下面卡片）。")
    w["daily"].insert(1,"🔴 Red goes with red: 3–5 min, 2 colors only" if en else "🔴 红的找红的：3–5分钟，只用两种颜色")
    w["todos"].insert(0,"Get 6 ball-pit balls (3 red, 3 yellow) + a red and a yellow cup" if en else "备六个海洋球（红黄各三）+ 一个红杯、一个黄杯")
    w["quiz"].append({"q":"She puts a yellow ball in the red cup. You say “No, wrong one!”","a":"dont","why":"Just name it: “That’s yellow.” Keep it a game."} if en else {"q":"她把黄球放进红杯，您说“不对，放错了！”？","a":"dont","why":"说一下“这是黄的”就行，保持好玩。"})
    w["quiz"].append({"q":"Use a bag of small craft pom-poms for color sorting.","a":"dont","why":"She still mouths; small pom-poms are a choking risk. Use ball-pit balls."} if en else {"q":"用一袋小手工毛球玩分颜色？","a":"dont","why":"她还啃东西，小毛球会噎着。用海洋球。"})

def revise8(w,L):
    en=L=="en"; b=w["bigThree"]
    b[2]=({"icon":"📮","title":"Home play after daycare: color step 2 + posting box","sub":"Curious · 5 min, weekends + calm evenings","roots":["Curious","Brave"],"lines":[
"<b>When:</b> weekend mornings, or 5 minutes after the reunion hour if she’s up for it. Tired? Skip it; connection first this week.",
"<b>Color step 2:</b> hold up a red ball: “Where’s another <b>red</b> one?” with just a red and a yellow ball on the floor. Then a red block next to the red ball: “Red with red!”",
"<b>Posting box:</b> formula tin with a round hole for balls; once she gets it, add a slot for big lids or 2-inch wooden discs. Show slowly, then wait. Say: “In it goes… <b>bye-bye</b>, ball!” (bye-bye practice too).",
"<b>Keep going:</b> floor-to-stand (squat to pick up the balls) and answering her points. <b>Milk week 2 of 4:</b> a second daytime bottle becomes whole milk in a cup; tell daycare.",
CHOKE_EN],"videos":[]} if en else
    {"icon":"📮","title":"托班回来在家玩：颜色第二步 + 投币盒","sub":"好奇 · 5分钟，周末或晚上状态好时","roots":["Curious","Brave"],"lines":[
"<b>什么时候：</b>周末早上，或者接回来黏够了、她有兴致时玩五分钟。累了就不玩，这周陪伴第一。",
"<b>颜色第二步：</b>举起红球：“另一个<b>红的</b>在哪儿？”地上只摆一红一黄。再把红积木放红球旁边：“红的跟红的！”",
"<b>投币盒：</b>奶粉罐盖子先开圆洞投球；会了再开长缝，投大瓶盖或5厘米大木片。慢慢示范，然后等。可以说：“进去啦……球球<b>拜拜</b>！”（顺便练拜拜）",
"<b>接着练：</b>从地上站起来（蹲下捡球）、接住她的“指”。<b>牛奶第二周：</b>白天再换一瓶成杯子喝牛奶，告诉托班。",
CHOKE_ZH],"videos":[]})
    w["cards"].insert(3,SOC_CARD_EN if en else SOC_CARD_ZH)
    w["oneLiner"]=("Daycare is starting. This week is <b>Secure first</b>: <b>the same goodbye every time</b>, <b>a calm reunion hour</b>, and short <b>home play</b> (color step 2 + posting box). Expect some clinginess; it’s the next cycle, not a step back." if en else
      "要上托班啦。这周<b>安全感第一</b>：<b>每次告别都一样</b>；<b>接回来先好好黏一小时</b>；在家<b>短短玩一会儿</b>（颜色第二步 + 投币盒）。会黏人一阵，这是新一轮成长，不是退步。")
    w["daily"].insert(3,"🔴 Color step 2 or posting box, 5 min if she’s up for it" if en else "🔴 有兴致就玩五分钟：找一样的颜色或投币盒")
    w["todos"].insert(1,"Make a posting box from a formula tin (round hole first)" if en else "用奶粉罐做个投币盒（先开圆洞）")
