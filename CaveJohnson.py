#!/usr/bin/env python3
## CaveJohnson.py
import os
import random

import discord
from discord.ext import commands, tasks
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

faq = os.getenv('FAQ_CHANNEL_ID')
welcome = os.getenv('WELCOME_CHANNEL_ID')
generalChannel = os.getenv('GENERAL_CHANNEL_ID')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

#Confirms Bot Connection
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#Sends welcome message to new member
@client.event
async def on_member_join(member):
    await member.send("Greetings new test subjects and welcome to the shiny new discord server you just joined!\n\nNow, I know you’re excited to get your hands on the latest science'y goodness we've come up with, but the lab boys tell me we have to do this by the books after what happened to Ronaldo.\n\nSo, before we send you into the wild, go ahead and bookmark our technical reference then head over to <#" + faq + "> and <#" + welcome + "> channels and memorize our rules.\n\nOk, you don't need to memorize our rules, but you'll definitely wanna read them so that you don't end up like Ronaldo.\n\nOkay, I gotta run.  The lab boys are telling me they've made a breakthrough using breakfast burritos to power the new way-back machine!  That's good news if you like nostalgia, bad news if you like breakfast.\n\nOk, gotta run.  Don't forget to read the <#" + faq + "> to find out how to get your hands on the latest news!\n\nOh, and one other thing... if you do happen to bump into Ronaldo, don't make any sudden moments. And for the love of God, don't stare.")

#Random message at set interval.
# @tasks.loop(minutes=300)
# async def background_loop():
#     await client.wait_until_ready()
#     channel = client.get_channel(int(generalChannel))
#     messages = [
#                 "You test subjects always ask about updating, and just like I keep telling the lab boys...  There's only two kinds of people, those who don't update, and those who wish they hadn't.  So, stop worrying about updating, we've already got that stuff handled .  Now get back out there and keep testing!",
#         (
#             "They tell me it's not a good idea to overclock your pi.  So I did it anyway...  And I gave everyone the ability to do!  All you do is go to HAL9000 --> System Tools -->Overclock Control Center and fire away!  Not gonna let those baboons tell me what I can & can't do.\n\nProbably worth mentioning, do so at your own risk, for science"
#         ),
#         (
#             "Who said that!?!? Who used the AP word?  While those are some great guys over there...they aren't using official schmoo.!\n\nHave you ever tried off-brand mac & cheese??\n\nIf you're serious about testing, take a look at the <#" + faq + "> channel to find out how to get your hands on the real schmoo -- the source science that drives enjoyment around here!!  And if you want real life answers to you real life questions, don't be afraid to speak up and ask real questions!! We're all dedicated to helping out around here. Ok, back to work!"
#         )
#         ]
#     await channel.send(random.choice(messages))

# background_loop.start()

##Random quote generator. source: https://theportalwiki.com/wiki/Cave_Johnson_voice_lines

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    if (message.author.bot):
        return
    elif message.author == client.user:
        return

    cave_johnson_quotes = [
                "Welcome, gentlemen, to Aperture Science. Astronauts, war heroes, Olympians--you're here because we want the best, and you are it. So: Who is ready to make some science?",
        (
            "Welcome, gentlemen, to Aperture Science. Astronauts, war heroes, Olympians--you're here because we want the best, and you are it. So: Who is ready to make some science?"
        ),
        (
            "Now, you already met one another on the limo ride over, so let me introduce myself."
        ),
        (
            "I'm Cave Johnson. I own the place."
        ),
        (
            "That eager voice you heard is the lovely Caroline, my assistant. Rest assured, she has transferred your honorarium to the charitable organization of your choice. Isn't that right, Caroline?"
        ),
        (
            "She's the backbone of this facility. Pretty as a postcard, too. Sorry, fellas. She's married. To science."
        ),
        (
            "There's a thousand tests performed every day here in our enrichment spheres. I can't personally oversee every one of them, so these pre-recorded messages'll cover any questions you might have, and respond to any incidents that may occur in the course of your science adventure."
        ),
        (
            "Your test assignment will vary, depending on the manner in which you have bent the world to your will."
        ),
        (
            "Those of you helping us test the repulsion gel today, just follow the blue line on the floor."
        ),
        (
            "Those of you who volunteered to be injected with praying mantis DNA, I've got some good news and some bad news."
        ),
        (
            "Bad news is we're postponing those tests indefinitely. Good news is we've got a much better test for you: fighting an army of mantis men. Pick up a rifle and follow the yellow line. You'll know when the test starts."
        ),
        (
            "They say great science is built on the shoulders of giants. Not here. At Aperture, we do all our science from scratch. No hand holding."
        ),
        (
            "Alright, let's get started. This first test involves something the lab boys call 'repulsion gel.'"
        ),
        (
            "You're not part of the control group, by the way. You get the gel. Last poor son of a gun got blue paint. Hahaha. All joking aside, that did happen - broke every bone in his legs. Tragic. But informative. Or so I'm told."
        ),
        (
            "The lab boys just informed me that I should not have mentioned the control group. They're telling me I oughtta stop making these pre-recorded messages. That gave me an idea: make more pre-recorded messages. I pay the bills here, I can talk about the control group all damn day."
        ),
        (
            "For this next test, we put nanoparticles in the gel. In layman's terms, that's a billion little gizmos that are gonna travel into your bloodstream and pump experimental genes and RNA molecules and so forth into your tumors."
        ),
        (
            "Now, maybe you don't have any tumors. Well, don't worry. If you sat on a folding chair in the lobby and weren't wearing lead underpants, we took care of that too."
        ),
        (
            "Oh, in case you got covered in that repulsion gel, here's some advice the lab boys gave me: DO NOT get covered in the repulsion gel."
        ),
        (
            "We haven't entirely nailed down what element it is yet, but I'll tell you this: it's a lively one, and it does NOT like the human skeleton."
        ),
        (
            "All these science spheres are made of asbestos, by the way. Keeps out the rats. Let us know if you feel a shortness of breath, a persistent dry cough or your heart stopping. Because that's not part of the test. That's asbestos."
        ),
        (
            "Good news is, the lab boys say the symptoms of asbestos poisoning show a median latency of forty-four point six years, so if you're thirty or older, you're laughing. Worst case scenario, you miss out on a few rounds of canasta, plus you forwarded the cause of science by three centuries. I punch those numbers into my calculator, it makes a happy face."
        ),
        (
            "Ha! I like your style. You make up your own rules, just like me."
        ),
        (
            "Bean counters said I couldn't fire a man just for being in a wheelchair. Did it anyway. Ramps are expensive."
        ),
        (
            "Just a heads-up: That coffee we gave you earlier had fluorescent calcium in it so we can track the neuronal activity in your brain. There's a slight chance the calcium could harden and vitrify your frontal lobe. Anyway, don't stress yourself thinking about it. I'm serious. Visualizing the scenario while under stress actually triggers the reaction."
        ),
        (
            "Now, if you're part of Control Group Kepler-Seven, we implanted a tiny microchip about the size of a postcard into your skull. Most likely you've forgotten it's even there, but if it starts vibrating and beeping during this next test, let us know, because that means it's about to hit five hundred degrees, so we're gonna need to go ahead and get that out of you pretty fast."
        ),
        # (
        #     "I'm telling 'em, keep your pants on."
        # ),
        (
            "Alright, this next test may involve trace amounts of time travel. So, word of advice: If you meet yourself on the testing track, don't make eye contact. Lab boys tell me that'll wipe out time. Entirely. Forward and backward! So do both of yourselves a favor and just let that handsome devil go about his business."
        ),
        (
            "If you're hearing this, it means you're taking a long time on the catwalks between tests. The lab boys say that might be a fear reaction."
        ),
        (
            "I'm no psychiatrist, but coming from a bunch of eggheads who wouldn't recognize the thrill of danger if it walked up and snapped their little pink bras, that sounds like 'projection'."
        ),
        (
            "THEY didn't fly into space, storm a beach, or bring back the gold. No sir, we did! It's you and me against the world, son! I like your grit! Hustle could use some work, though. Now let's solve this thing!"
        ),
        (
            "Science isn't about WHY. It's about WHY NOT. Why is so much of our science dangerous? Why not marry safe science if you love it so much. In fact, why not invent a special safety door that won't hit you on the butt on the way out, because you are fired.\nNot you, test subject, you're doing fine.\nYes, you. Box. Your stuff. Out the front door. Parking lot. Car. Goodbye."
        ),
        # (
        #     "Not you, test subject, you're doing fine."
        # ),
        # (
        #     "Yes, you. Box. Your stuff. Out the front door. Parking lot. Car. Goodbye."
        # ),
        (
            "Congratulations! The simple fact that you're standing here listening to me means you've made a glorious contribution to science."
        ),
        (
            "As founder and CEO of Aperture Science, I thank you for your participation and hope we can count on you for another round of tests."
        ),
        (
            "We're not gonna release this stuff into the wild until it's good and damn ready, so as long as you keep yourself in top physical form, there'll always be a limo waiting for you."
        ),
        # (
        #     "Say goodbye, Caroline."
        # ),
        # (
        #     "She is a gem."
        # ),
        (
            "Greetings, friend. I'm Cave Johnson, CEO of Aperture Science - you might know us as a vital participant in the 1968 Senate Hearings on missing astronauts. And you've most likely used one of the many products we invented. But that other people have somehow managed to steal from us. Black Mesa can eat my bankrupt--"
        ),
        (
            "Right. Now, you might be asking yourself, 'Cave, just how difficult are these tests? What was in that phone book of a contract I signed? Am I in danger?'"
        ),
        (
            "Let me answer those questions with a question: Who wants to make sixty dollars? Cash."
        ),
        (
            "You can also feel free to relax for up to 20 minutes in the waiting room, which is a damn sight more comfortable than the park benches most of you were sleeping on when we found you."
        ),
        (
            "So. Welcome to Aperture. You're here because we want the best, and you're it. Nope. Couldn't keep a straight face."
        ),
        (
            "Anyway, don't smudge up the glass down there. In fact, why don't you just go ahead and not touch anything unless it's test related."
        ),
        (
            "The testing area's just up ahead. The quicker you get through, the quicker you'll get your sixty bucks.\nCaroline, are the compensation vouchers ready?"
        ),
        # (
        #     "Caroline, are the compensation vouchers ready?"
        # ),
        (
            "Great job, astronaut, war hero, and/or Olympian! With your help, we're gonna [tape cuts out]"
        ),
        (
            "This on? [thump thump] Hey. Listen up down there. That thing's called an elevator. Not a bathroom."
        ),
        (
            "If you're interested in an additional sixty dollars, flag down a test associate and let 'em know. You could walk out of here with a hundred and twenty weighing down your bindle if you let us take you apart, put some science stuff in you, then put you back together good as new."
        ),
        (
            "In case you're interested, there's still some positions available for that bonus opportunity I mentioned earlier. Again: all you gotta do is let us disassemble you. We're not banging rocks together here. We know how to put a man back together."
        ),
        (
            "So that's a complete reassembly. New vitals. Spit-shine on the old ones. Plus we're scooping out tumors. Frankly, you oughtta be paying us."
        ),
        (
            "Thank you - I can't believe I'm thanking these people - for staggering your way through Aperture Science's propulsion gel testing. You've made some real contributions to society for a change, and for that, humanity is grateful."
        ),
        (
            "If you had any belongings, please pick them up now. We don't want old newspapers and sticks cluttering up the building."
        ),
        (
            "For many of you, I realize 60 dollars is an unprecedented windfall, so don't go spending it all on... I don't know. Caroline, what do these people buy? Tattered hats? Beard dirt?"
        ),
        # (
        #     "Welcome to the enrichment center. [cough]"
        # ),
        (
            "Since making test participation mandatory for all employees, the quality of our test subjects has risen dramatically. Employee retention, however, has not."
        ),
        # (
        #     "[cough] As a result, you may have heard we're gonna phase out human testing. There's still a few things left to wrap up, though."
        # ),
        # (
        #     "First up, conversion gel. [cough] (unused)"
        # ),
        (
            "The bean counters told me we literally could not afford to buy seven dollars worth of moon rocks, much less seventy million. Bought 'em anyway. Ground 'em up, mixed em into a gel."
        ),
        # (
        #     "And guess what? Ground up moon rocks are pure poison. I am deathly ill."
        # ),
        # (
        #     "Still, it turns out they're a great portal conductor. So now we're gonna see if jumping in and out of these new portals can somehow leech the lunar poison out of a man's bloodstream. When life gives you lemons, make lemonade. [coughs] Let's all stay positive and do some science."
        # ),
        # (
        #     "That said, I would really appreciate it if you could test as fast as possible. Caroline, please bring me more pain pills."
        # ),
        (
            "All right, I've been thinking. When life gives you lemons? Don't make lemonade. Make life take the lemons back! Get mad! 'I don't want your damn lemons! What am I supposed to do with these?' Demand to see life's manager! Make life rue the day it thought it could give Cave Johnson lemons! Do you know who I am? I'm the man who's going to burn your house down! With the lemons! I'm going to get my engineers to invent a combustible lemon that burns your house down!"
        ),
        (
            "The point is: If we can store music on a compact disc, why can't we store a man's intelligence and personality on one? So I have the engineers figuring that out now."
        ),
        (
            "Brain Mapping. Artificial Intelligence. We should have been working on it thirty years ago. I will say this - and I'm gonna say it on tape so everybody hears it a hundred times a day: If I die before you people can pour me into a computer, I want Caroline to run this place. Now she'll argue. She'll say she can't. She's modest like that. But you make her. Hell, put her in my computer. I don't care."
        ),
        (
            "Allright, test's over. You can head on back to your desk."
        ),
        (
            "If you've cut yourself at all in the course of these tests, you might have noticed that your blood is pure gasoline. That's normal. We've been shooting you with an invisible laser that's supposed to turn blood into gasoline, so all that means is, it's working."
        ),
        (
            "If you need to go to the bathroom after this next series of tests, please let a test associate know, because in all likelihood, whatever comes out of you is going to be coal. Only temporary, so do not worry. If it persists for a week, though, start worrying and come see us, because that's not supposed to happen."
        ),
        (
            "Just a heads up: We're gonna have a superconductor turned up full blast and pointed at you for the duration of this next test. I'll be honest, we're throwing science at the wall here to see what sticks. No idea what it'll do. Probably nothing. Best-case scenario, you might get some superpowers. Worst case, some tumors, which we'll cut out."
        ),
        (
            "If you're allergic to peanuts, you might want to tell somebody now, because this next test may turn your blood into peanut water for a few minutes. On the bright side, if we can make this happen, they're gonna have to invent a new type of Nobel Prize to give us, so hang in there."
        ),
        (
            "The average human male is about sixty percent water. Far as we're concerned, that's a little extravagant. So if you feel a bit dehydrated in this next test, that's normal. We're gonna hit you with some jet engines, and see if we can't get you down to twenty or thirty percent."
        ),
        (
            "All right. We're working on a little teleportation experiment. Now, this doesn't work with all skin types, so try to remember which skin is yours, and if it doesn't teleport along with you, we'll do what we can to sew you right back into it."
        ),
        (
            "Welcome, test subject, it's Cave. Prime. From Earth One. I am speaking to you from across time and space! I am literally in the future! I am--Hold on... [off mic] What? [on mic] Alright, my assistant Greg tells me none of that's true. Got excited. You are the first test subject we have ever sent into a parallel universe, which apparently has nothing to do with time travel. Still exciting. Anyway, you should be seeing a test chamber in front of you. We designed it, those backwater universe yokels built it, and you're gonna test it. Remember: You gotta let us know if it WORKS or not, otherwise you're wasting everybody's time on two earths. Alright, get to it."
        ),
        (
            "Cave here. Just so you know, this mic isn't two way. Can't hear a damn thing you're saying, so don't waste any oxygen trying to talk. [off mic] What? [on mic] My assistant Greg says some of these alternate Earths may not have oxygen. The air might be nitrogen or methane or, hell, everybody's head might be inside out. So just take little itty bitty breaths and if anybody asks you why your head's inside out, remember it's only inside out from their perspective, and you're fine. Head-wise. Trouble-wise, you're in a lot of it and you should probably run. Alright, enough hypotheticals. Let's test this test!"
        ),
        (
            "Cave here. Man oh man. Wow. Greg's multiple universe theory was dicey, but you're pulling through with flying colors. We're all very proud of Greg. [pause] Oh, and you."
        ),
        # (
        #     "Before we start testing today, let's have our mandatory minute of silence in honor of Earth's governing body, the Sentient Cloud. [throat clear] Starting now. [a pause] [coughing] [a longer pause] [more coughing] [still more pausing] Good, right. All hail the sentient cloud. Begin testing."
        # ),
        (
            "I've just been notified that one of our test subjects may have angered the Sentient Cloud by beginning testing early. Now, as you all know, the cloud has banned all camera technology--hates getting its picture taken. So this'll have to be on the honor system: Will whoever started testing early please go outside so they can be consumed by the Cloud."
        ),
        (
            "Just a heads-up that the Cloud's still waiting. I don't think that thing's gonna go away, so somebody might wanna get out there."
        ),
        (
            "No! No! It came in under the door! It's leeching off all my skin! Aghhhhh- [click] Excerpt there from one of our safety videos. Grisly stuff, very informative. Somebody doesn't get out there soon we're gonna have to have a lottery, because believe me, if we keep that cloud waiting much longer he's coming in under the doors, and he will leech off all of our skin."
        ),
        (
            "Cave here. The real Cave. Greg's been crunching some numbers here on Earth Prime. Turns out, the likelihood of me being the only Cave who likes talking to test subjects is-- [off mic] What's the actual number, Greg? [on mic] Right. Zero. So tell you what, we're gonna use a code word. If I say Chariots, It means you're listening to me otherwise it is an imposter Cave. I want you to know you have a license to kill on this one... Uhh Gregg says that might destroy the entire multi-verse. Point is use your own judgement. License to kill."
        ),
        (
            "Welcome, gentlemen, to Aperture Rituals. Astronauts, war heroes, olympians: you're here because of an ancient mating ritual etched in a monolith by the Elder Monks to forestall the end of days. So, who is ready to make love to a giant bird?"
        ),
        (
            "Cave Johnson here. Just wanna let the cafeteria staff know to lay off the soylent green. I'm holding a memo from the President, and it turns out that soylent green is... [paper rustling] let's see here... doubling in price. Now listen up: I don't care how good people tastes. This stuff's costing me more than lobster, so we're going back to fishsticks."
        ),
        (
            "(tap dancing noises) Hey. It's Cave. Someone's not daaaancing. Come on. You know the law - testing IS NOT a dance exemption. Don't make me call the dance police."
        ),
        (
            "Test subject, can you hear me? Congratulations! You are the world's first half-man, half-machine police officer! Well, first batch. There was a pretty big shootout. Bought all your caracasses off the mayor. Anyway, you should be proud to be a part of Aperture's android law enforcement initiative. Or, as someone who's good at naming things, i.e. me, would call it, ROBO -- No. [suddenly coming to him] Robot-a-Cop! Oh, that's much better. Now, before we get you solving crimes, we gotta getcha to solve this test. Promised the mayor I'd make sure you weren't all unstable potatoheads before I gave you all guns."
        ),
        (
            "Come in, Robot-a-Cop! It's your chief. First: You're a damn good cop. Second: You're a loose cannon. Alright, that's probably enough motivation. Oh, before I forget! Greg tells me you might be getting some tragic flashbacks of your former life. Don't sweat it, those aren't yours. Due to a software problem, that's a real-time feed of Greg's current life. He's a sad little man. Anyway, just try to ignore him."
        ),
        (
            "Cave here. Chariots. Just a heads up: If it seems like you're walking faster than light, you're probably in a universe where light doesn't haul nearly as much ass as it does on Earth One. The lab boys say if you insist on walking faster than light, you are one hundred percent going to go back in time. How far? Far enough to meet your great great grandfather and tell him you're fired. Because guess what? I'll let you finish that thought."
        ),
        (
            "Welcome, test prisoner, to the Terra-Three penal science colony. Space criminals, political prisoners, exiled planetary leaders: You're here because the galaxy needed a place to put you, and this is it. So, who is ready to stay here until they die? Now, you already met one another on the hyperdrive over, so let me introduce myself. I'm Cave Johnson. I'm the warden around here."
        ),
        (
            "Attention, test prisoners attempting to escape through the air ducts. I don't know what nonsense you learned on TV, but in real life, air ducts just go to the air conditioning unit. It's also pretty dusty, so if you've got asthma, chances are you're gonna die up there. And we'll be smelling it for weeks because, again, the air ducts aren't a secret escape hatch, they're how we ventilate the facility."
        ),
        # (
        #     "[throat clear] This thing on? I'm gonna be brief. Because I'm dying. Because I got shivved. A lot. I just wanna get it on record that using force fields for doors in a space prison is a bad idea. You know what would have been better? Regular doors. With locks. Locks that don't open when the power goes out. [cough cough] Man, those blue force fields looked good, though. Every time I saw one, I thought, wow, I am in space. Still no a door made out of paper would have been better in the long run. Would have at least slowed them down for a second. Any way... anybody not escaping or shiving me, get back to work."
        # ),
        (
            "Those of you who volunteered to be injected with homo sapien DNA, I've got some good news and some bad news: bad news is we're postponing those tests indefinitely. Good news is we've got a much better test for you: fighting an army of man-mantises. Pick up a set of foreleg spurs, mesothorax armor and tubercle sheaths. You'll know when the test starts."
        ),
        (
            "It's come to my attention that over half of our test subjects have only recently awoken from extended relaxation and were unaware that we're testing in space. So there it is: No conspiracy. No twist. We're in a test satellite orbiting the Earth. Commonly available information that absolutely anyone would have told you if you'd bothered to ask. Please stop forming groups of adventuring parties to uncover the big secret, because it's that we're in space."
        ),
        (
            "Looks like we just had to seal up Science Sphere Seven. Hull breach. Another adventure party smashed through the hull to learn the big mystery. Guess they were busy doing that instead of testing, because I've mentioned we're in space every half hour. By the way: still in space."
        ),
        (
            "Aaaand another hull breach. Let's all give a big hand to the test subjects of Sphere Eighteen for bravely uncovering the company-wide conspiracy, which is that there's no air in space. Once again: We're in space. It's not a secret. I am sincerely regretting my decision not to install windows in this thing."
        ),
        (
            "Welcome, gentlemen, to the Aperture Hollow Science Jungle. Tramps, hillbillies, drifters, you're here because you followed the hobo signs. So, who is ready to scrounge around for some science? Now you already meet one another on the box car over here, so grab a bowl of Slum Gallion and a glass of Sterno and let me introduce myself. I'm Michigan Slim Cave Johnson [harmonica music]. I'm the Hobo King."
        ),
        (
            "It's Cave. Greg's telling me the number of possible alternate universes is literally infinite. Maybe there's one where, I don't know, the Greeks won World War II. Just a heads up in case you get to a test chamber and find yourself surrounded by urns. Oh, Chariots!"
        ),
        (
            "[Shrieking sounds] That shrieking voice you just heard is the lovely Blark-Barg, my assistant. She's the backbone of this facility. Sorry fellas, she's married -- to producing seeds that germinate and detach from her exoskeleton at high speeds in search of human hosts! We keep her behind glass."
        ),
        (
            "Hello, test subjects. Good news first: our telekinesis incubation program has been a huge success. Bad news: The candidate screening process was a lot less successful. Let me tell you, we picked a real bunch of smart alecs to give mind-powers to. You hear me? Stop blowing up heads. [cocky] Actually, you know what? Negotiation's over. I'd like you all to meet Terry. He's -- [BLAM!] Real funny, guys. But the joke's on you. I taped all your paychecks to Terry's head. Ha! Why don't you put THAT in your head and blow it up?"
        ),
        # (
        #     "That's right everybody, it's that time of year again: Happy Birth Day. You know the rules, everybody at the government-mandated maximum age needs to report to an ethnological redundancy associate toot suite. Looking through your files here--the following is a complete list of employees who need to snuff it. [coughs] Dorothy Russell, Age 98. End of list. Sorry about that, Dorothy. You had a good ninety-seven years, time to stop hoggin' all the resources. Leave some nutrient paste for the rest of us, why don't you. Cave Johnson, age fifty-one. We're done here."
        # ),
        (
            "Cave Johnson, junior claims representative for Aperture Science here. Well, former junior claims representative. Just found out I got laid off. Well, I'll just sneak into their recording office and let everyone know our president, that bastard Doug Rattmann, is embezzling funds. Enjoy your Christmas bonuses knowing he took most of them, jerks."
        ),
        (
            "Cave Johnson here. The mantis men have officially taken over the building. If you can still get out, get out now! They're (crunching noises) oh god, they're breaking through the barricades!"
        ),
        (
            "Cave Johnson here. I seeeee you. I seeee your little feet. I'm gonna cut off your hair and put it on your feet and eat your little hair. What? Oh, and feet. Um yum yum yum yum!"
        ),
        (
            "[child talking in creepy voice] Hi down there! We're gonna test forever, and ever, and ever. [cave talking] Hey! Hey! What are you doing in here? Beat it. [off mic] Come on, Greg, I told you not to let your creepy kid in my office. No, I'm sorry Greg, but there's something wrong with that kid. [putting on creepy kid voice] We'll test for ever!. Why does she whisper all the time? Hey test subject, just keep going. Chariots Chariots. Man that kid's creepy!"
        ),
        (
            "Chariots! Cave Johnson here, reminding you to fill out the paperwork for full payment once you're done testing. The check may seem exorbitant, but you deserve it. Chariots!"
        ),
        (
            "Chariots! It's Cave Johnson. If you get through this next room, you'll get a bonus. And that's on top of the bonus I gave you this morning. [laughing] Don't thank me, because you're the real boss. Why? Because you teach me something new every day. Here's a third bonus. CHARIOTS! [getting choked up] You test subjects are the best. Oh my gosh, chariots..."
        ),
        (
            "This is Cave. PRIME. So apparently there's an alternate dimension Cave Johnson who just uses the word Chariots for no reason. From now on, I'll say chariots twice if it's me. If you hear just one CHARIOT that's an alternate Cave. Chariot Chariot."
        ),
        (
            "Hello, test subject! Cave Johnson here, founder and CEO of Aperture Science: the best damn applied sciences company on Earth. How good is the science here? Get a load of this: I'm dead! Now, you're probably asking yourself, Cave how is that possible? Are you some manner of Dracula? Or a frankenstein? Or, depending on your culteral herritage, a blackula, or latin frankenstein? Heh, nope. Just SCIENCE! As of this morning I have been resurected inside of a computer. That aside situation normal. So, continue testing."
        ),
        (
            "Just a warning to you test subjects: Greg and the boys told me that the massive influx of information I'd receive when they transferred my consciousness into a stadium-sized super computer would turn me crazy. So, once again a warning: Greg and the boys are no longer working here, so if they were doing something for you, that's not getting done."
        ),
        (
            "Cave again. Now, I'll admit, losing my body does have its drawbacks. But it's got its perks too! As a being of pure intellect, I've now got time to read the entire literary canon of the human race. Here I go! [BEEP] And I am done. [beat] [sigh] Continue testing."
        ),
        (
            "Pure Intellect Cave here. Not to brag, but while you were cat-assing that last test, I rewrote the collected works of everything ever. I figure,, if I gotta read this garbage for eternity, I may as well improve it. Next time you curl up with a time-honored classic and think to yourself, 'Man I do not remember the brother's carimosa busting so many ghosts!' You can thank your's truely."
        ),
        (
            "Here's a question for you: Who is not afraid of no ghosts? [beep] As of just now, every character in every book by Virginia Woolf. Man, those things were dull."
        ),
        (
            "Cave again. What is the one thing that could never ever ever ever in a million years get boring? If you said 'Busting ghosts' tragically you'd be wrong. Was almost all the way through the W's, when the bloom came off that roast. Health-cliff was defending Moon Base Weathering Heights from the crafty poltergeist, when I realized exploring the vast realm of intellect is... boring. It's BORING! You know what I like to do? I like to scratch my nose!"
        ),
        (
            "I've been thinking: What if Greg was right? What if injecting my consciousness into a computer robbed me of an eternal reward? Spiritually speaking. [beep] Alright, I just read up on it. Stumbled on a book about a fella who lived thousands of years ago. Sacrificed himself to save mankind. Went by the name of Hercules. Destroyed all the world's monsters so humans'd be safe, then went to Olympus for his trouble. Damn it, death was my monster! And I killed it! Where's my Olympus?"
        ),
        (
            "Unless... Aperture was the monster. Aperture and everybody inside it. Holy Hercules! I just thought of something. Keep testing. Or don't. Doesn't matter. I'll be back."
        ),
        (
            "Whoa! Chariots chariots. For some reason, some of the audio was bleeding through in this universe. Don't know if you were catching the subtext there, but that computer Cave is crazy. So: Greg was right. As of now, we are cancelling the genetic lifeform disk operating system initiative. Boy, that could have backfired. Anyway, this Earth is far too dangerous and we are pulling you out. [pause] Right after this test."
        ),
        (
            "Welcome, gentlemen, to Aperture Paranormal. Magicians, witches, crystal healing doctors: you're here because you have scary powers and we want in on it. So: who is ready to draw some pentagrams? Now you already met one another on the cab ride over so let me introduce myself. I'm Cave Johnson. I'm host to a tiny but powerful demon who lives in a secret place in my mouth."
        ),
        (
            "Cave Johnson again, just a heads up, you are currently in a tiny test chamber floating around in my bloodstream. Remember, if you see a giant set of car keys, those are mine. Lab boys shrunk 'em part way down before I could stop 'em. No idea if it was for science or if they're just having one on at ol' Cave, but either way I'm you don't find those things pretty soon, I'm gonna have to call Triple A."
        ),
        (
            "Hello, test subject. As you are no doubt aware, the President is being held hostage inside the giant super-prison on the floor of the Atlantic Ocean . Every science facility in America has been tasked with producing a Tough Guy capable of breaking into SuperMaxLantis. That's where YOU come in. I'm nominating myself and I'm gonna need some references. A test associate should be around soon to get a quote off you, so be as glowing as possible."
        ),
        (
            "Quick update on all those pods we were finding in broom closets. Apparently some alien monster was body-snatching employees and spawning Communist replicas. The allegorical threat level on this one's through the roof. Actual threat level's pretty non-existent, though, so we've decided not to do anything about it. If the worst this thing can do is gestate glassy-eyed Yes Men, I say bring it on, Bug-Eyes. I got a whole list of troublemakers you can pod up any time you like."
        ),
        (
            "[meowing cat noises]"
        ),
        (
            "Cave Johnson, new owner and CEO of Black Mesa. That's right, you've been bought. First order of business, we're renaming you under the Aperture brand. I'm leaning towards Blappeture Mesa. Marketing boys think something else. So: Blappeture it is. Next, they tell me you people are conducting some anomalous materials research that could result in a resonance cascade. So I'm shutting that down before you idiots end the world. A resonance cascade! You're supposed to be scientists. Use some common sense."
        ),
        (
            "Cave Johnson here. Just wanted to let you know that, after decades of research and testing, we have finally transformed into beings of pure light. Go team. Not exactly what we were after, of course, but in the ballpark. So let's keep testing, and maybe someday we'll achieve man's ultimate dream: to evolve into pillars of pure salt. Can't wait. [beat] So salty."
        ),
        (
            "Chariot chariot. By the way, you can make a bit of a mess in these rooms if you want. Scuff your shoes or stick gum on the walls, because these alternate Cave Johnsons are really cheesing me off."
        ),
        (
            "Cave Johnson here. Just a heads-up we've got an interverse security breach in one of the test areas. You all enjoyed a good chuckle at Cave's expense when I started monitoring for parallel universe invasions. You all tried to stop me when I tried to garnish your wages to build defenses against said invasion. Succeeded too. So I hope you're happy, we've got a bogey from Earth-1 loose on the premises. Go write a letter to the Better Business Bureau about THAT, why don't you. [beat] Actually, don't."
        ),
        (
            "Would anyone like to know what the invaders from Earth-1 are up to inside our facility? I don't blame you - bet it'd be fascinating stuff. But we don't have any multiverse invasion monitoring equipment. Asked for it. Told it was stupid. Anyway, I hope these monsters replace our air with chlorine - it'd finally give you crybabies something to cry about."
        ),
        (
            "Just a quick update on the attack of the killer ants. Apparently they tried to commandeer the entirety of our nation's sugar reserves in Kentucky. Big firefight at Fort Sugar Knox. Edge-of-your-seat stuff. Anyway, that's as far as I made it through the movie before I fell asleep. So if anybody's seen Attack of the Killer Ants, don't spoil the ending or you're fired. By the way, chariots chariots."
        ),
        # (
        #     "[coughing] Hi mister, 's Timmy. Doc says I ain't gonna pull through, but if you could just finish this test, I bet we could lick this thing! [coughing]"
        # ),
        (
            "Cavina Johnson here. It's come to my attention that one of you has sent a letter to the Supreme Council of Matriarchs accusing me of being a man. So, I want to assure both you and Gender Regulatory Committee that I am indeed one hundred percent all woman. And if you don't believe me, I swear to god I will beat you -- [off mic] What? [on mic] Greg tells -- [off mic] What? [on mic] Sally-Sue-Greg tells me we will all exchange handmade sympathy cards discussing how we feel about the issue. Alright, let's do some lady science!"
        ),
        (
            "I sincerely hope you're not allergic to air. Our peanut dust ventilator broke in this wing, so the atmosphere is only 60 per cent peanut dust."
        ),
        (
            "Hey. It's me. The real me. Uh, chariots chariots. Anyway, it appears the test chambers in our dimension are being tested on. Looks like another alternate universe Cave Johnson is using the same trick I am. If you see that one, will ya punch him in the throat for me. But make sure it's him and not me you're punching or you're fired."
        ),
        (
            "Chariots chariots. We have a problem. That alternate Cave Johnson is using ALL our test chambers now. We have to take care of things here for a while, so you're on your own. Try to remember the tests so we can write it all down later."
        ),
        (
            "Aha! We've got you, you...wait, is that the real you? From our dimension? Ahhh. Chariots chariots. It's Cave. Seriously, of all the infinite alternate dimensions, you happen to wind up randomly in ours again? Okay, just get through this test and be VERY careful not to mess anything up."
        ),
        (
            "Hey. Chariots chariots. Just thought you should know, that sick boy from a couple of Earths ago? We kept monitoring that because, man, that was riveting. Anyway, he didn't make it. Good try, though. We were virtually all pulling for him."
        ),
        (
            "Chariots chariots dammit! Now we've got two testers here from another damn Earth! We had one of 'em cornered, then the other one just portaled him out of there, then they high-fived and went their separate ways. I'm gonna need you to test double quick to make sure we're messing them up as badly as they're messing us up here."
        ),
        (
            "Attention: Chariots chariots. There are at least six extra-dimensional testers here now, and to be honest, they're not even really testing anymore. They just all portaled in, made a human pyramid, ate my lunch and portaled out."
        ),
        (
            "Chariots char-look it's me. Apparently, this other Earth has portal guns that can make portals on anything. We've had guys just walking along and suddenly, a portal opens beneath them and they fall out of a wall. I'm thinking maybe we should just work out a truce. I'll let you know if we can get in touch with this Evil Cave Johnson."
        ),
        (
            "Chariots chariots. Okay. Greg managed to contact the Cave Johnson who keeps sending testers here and we've agreed, no more testing in each other's dimensions. We'll get you back here ASAP."
        ),
        (
            "Hello, test subject. Just a heads-up that our research into stopping all the godzilla attacks on U.S. soil has been postponed indefinitely. Turns out it doesn't matter where you hatch a nest full of godzillas, they just make a beeline straight for Tokyo. [chuckles] Shoulda seen those things go. Anyway, crisis averted. Now everybody grab a dust pan and a broom, we gotta get rid of all these egg shells before the Nuclear Regulatory Commission shows up."
        ),
        (
            "Break one-nine. Big Box Cave Johnson here, hauling a freight shaker with a loada cold ones in the wagon down to Texarkana. I got twenty-eight hours to get this done, so I'm putting the hammer down. Anybody hearing this, shake the bushes and gimme your ten-twenty. Also, test subjects, I'll be gone for twenty-eight hours, test on your own recognizance. I want to keep this channel clear, so do not use your CB radios. Cave Johnson, we're over and out here."
        ),
        (
            "Chariots chariots. Whoever this alternate Cave Johnson is, he's a jerk. Instead of sending us the apology fruit assortment he promised, he just sent a whole bunch of angry wasps. We'll find a way to get back at him, don't you worry. You keep testing, and don't be afraid to get messy with it. We'll just see who wins this deadly game of cat and other cat."
        ),
        (
            "Chariots chariots. Okay, now the other Cave has sent a huge block of frozen urine. It's too big for us to get it out of the multiverse device, so we just have to let it melt until we can wedge it out. Incidentally, if you come across a dimension where people eat nothing but asparagus, I'm guessing that's where our nemesis is, so keep your eyes peeled for that."
        ),
        (
            "Cave Johnson here. I need you to - [Dark Cave] Do not listen to this man. He's the other Cave Johnson. He's an impostor! [Cave Prime] You're the impostor, impostor! Chariots chariots! [Dark Cave] Oh, yeah? Chariots chariots chariots! Just keep testing. I'll settle this. [Cave Prime] No, I'll settle this. [Dark Cave] Shut it, you. And you, keep testing!"
        ),
        (
            "All right. I think we shut down the impostor Cave's comlink. [Dark Cave] You'd like to think that, wouldn't you? [Cave Prime] Dammit! Stop imposting! [Dark Cave] Never! [Cave Prime] Oh, you stubborn, handsome devil."
        ),
        (
            "It's come to my attention that there's a pair of sunglasses floating around this place that lets you see the subliminal propaganda we've painstakingly hidden on every visible surface. Look people, the reason motivational propaganda works is because you're not staring straight at it. That's the whole point. But what do I know? If everybody's too cool to be subliminally propagandized, feel free to wear your magic sunglasses all damn day. Motivate yourself from now on."
        ),
        (
            "[laughter] Oh, Dark Cave, you are the only one around here who gets me. I tell you, I haven't had a conversation this damn good since... Hold on, I gotta talk to the help. [tap tap tap] Hey, you. Chariots chariots. Keep testing."
        ),
        (
            "Hey, Dark Cave. [Dark Cave] Cave Prime! As I live and breathe methane. [Cave Prime] Listen, do you have a Greg in your universe? You want one! [laughter] Greg, come back! I wouldn't send you to Dark Cave Earth. [whispered] I would. Greg is on the table."
        ),
        (
            "Cave Johnson here. Just a reminder that the core goal of Aperture Gas-Finding Science is to find gas, so make sure you let us know if you see any. If we meet our quarterly gas-finding target, I promise you we will don our bondage gear, fuel our death cars, and drive around in circles, whooping it up and shooting arrows at people. Who is ready to rule the wasteland? Alright, start looking."
        ),
        (
            "[echoey] Hello, test subject. Echo. Echo. Welcome to your first test. I'm your overseer, Cave Johnson, and I think, if you keep testing, you might find something very interesting about this planet. [chuckle] [beat] It's me. I'm the planet. You live on me. Wanted to save it till later, but man -- it's just too darn good. You really wouldn't have seen it coming. Do me a favor, don't tell any of the other test subjects. Also, don't pollute."
        ),
        (
            "Chariots Chariots. According to Greg, theoretically, there's an Earth out there made entirely of money. Plus, since there's a infinite number of Earths, that means there's an infinite number of money planets. So I've done the math, and I figure the odds of finding this thing are one hundred percent. [off mic] Not now Greg! [on mic] That doesn't mean I want you to stop testing, but do keep an eye out for the money-verse. And let me be clear, I'm talking about U.S. currency. You find a peso-verse, you just keep walking."
        ),
        (
            "Chariots Chariots chariots. Dark Cave here. Listen, you find the moneyverse, you bring it to me. I'll take care of you. You want to be promoted to head of testing? Done. You want your asparagus rations doubled? I'll pull some strings. You want all the methane you can breathe? Not a problem. Remember: Moneyverse. Dark Cave. Asparagus. Lots of it. Enough said."
        ),
        (
            "Chariots chariots. Cave Prime here. I hear you've been brokering a deal with that other Cave. So here's what I want you to do: find your alternate self, steal his stuff, put in a box, and if there's a parking lot, walk the box out to it, because you're fired."
        ),
        (
            "Chariots chariots. Cave Johnson again. Alright. Greg's informed me this is not the best time to fire you. But, if you ARE talking to that other Cave, let me just remind you who you work for. [Dark Cave] Chariots chariots chariots. And let me remind you who's offering methane. [Cave Prime] Chariots chariots. Look, whatever he's offering, I'll double it. [off mic] Greg, how are we fixed for methane? Uh huh. Uh huh. Well, what do we use it all for? [Dark Cave] Evil Cave again. I think your choice is clear here. [Cave Prime] Test subject: not clear! Not clear! Keep testing!"
        ),
        (
            "Cave Prime here. [Dark Cave] Dark Cave here. [Cave Prime] While you were busy driving a wedge between us with your bidding war, Dark Cave's test subject found two moneyverse. [Dark Cave] And we're gonna split 'em. [Cave Prime] So there's no reason to offload our testing to alternate Earths anymore. Funding test chamber construction is no longer a problem. You know what else isn't a problem? Gold teeth. Greg, look at these choppers. Now show me yours. Man, you got tiny teeth Greg. Anyway, the good news is, we're ready to start phase two: Figuring out a way to bring you back. Greg's gonna sink his weird little teeth into that problem toute suite. So, the next time you enter a test chamber, you'll back here on terra firma prime-a."
        ),
        (
            "Hey Greg, it worked! Welcome back, test subject! Now get back to work. Just because we own a universe made of money, doesn't mean I'm made of money. Cave Johnson. We're done here."
        )
    ]

    if 'burrito' in message.content.lower():
        response = "Well, looks like the whole breakfast burrito thing was too good to be true.\n\nThe good news is, breakfast will resume being served daily.\n\nBad news for Larry the applied science guy.\n\nOh, and...   We need a new applied science guy"
        await message.channel.send(response)

    elif 'portal' in message.content.lower():
        response = random.choice(cave_johnson_quotes)
        await message.channel.send(response)

    elif 'cave' in message.content.lower():
        response = random.choice(cave_johnson_quotes)
        await message.channel.send(response)

    elif 'science' in message.content.lower():
        response = random.choice(cave_johnson_quotes)
        await message.channel.send(response)

    elif 'valve' in message.content.lower():
        response = random.choice(cave_johnson_quotes)
        await message.channel.send(response)

    elif 'aperture' in message.content.lower():
        response = random.choice(cave_johnson_quotes)
        await message.channel.send(response)

    elif ' lab' in message.content.lower():
        response = random.choice(cave_johnson_quotes)
        await message.channel.send(response)

#    elif ' test' in message.content.lower():
#        response = random.choice(cave_johnson_quotes)
#        await message.channel.send(response)

#    elif 'testing' in message.content.lower():
#        response = random.choice(cave_johnson_quotes)
#        await message.channel.send(response)

client.run(TOKEN)
