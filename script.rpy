# Game by: Moop Open-source Games
# Nairda Nun: Chapter 1 (*The Halloween Episode* - For LGBTQ+ Horror Jam 2025)

# Game summary: Nairda Nun, the private detective.
# Based in the 90's, general crime type genre, all characters are animal-based,
# proportions and style similar to Sylvanian Families.

# -----------------------------------------------------------------------------
## To Do List / Needs

# - Arm photo and edit, opaque, to use for showing a human is holding the characters
# at random intervals.
# - Audio of human in "real world" for different immersion / fourth wall
# breaking.
# Ezekiel photos (baby rabbit) needed for his character. Rabbits hate garlic so Tony using that as
# revenge for water flowing noises might be good

# -----------------------------------------------------------------------------

# Game Contents:

# SCENE 00 - Introduction
# 1. Discuss the silly world lore again:
# - Such as hills being a crime zone as old laws say you can't
# arrest people standing on hills.
# - How only criminals wear shoes/footware because it conceals their
# foot prints and thus their species.

# 2. Previously on Nairda Nun:
# - Murder and Giant Opal stolen from the Museum of Frogs and Fancies.
# - It was the care takers, using a mace, due to bullet proof glass, etc.


# SCENE 01 - Nairda Nun normal day of crime solving
# 1. Nun having a normal day of work. Case of a missing wife, gone 72 hours, husband
# is sad and wanting any information about his wife. Does a press conference.


# SCENE 02 - Molly Stone finds the wife / curses Nun
# 1. Molly Stone wakes up at murder scene with the dead wife
# 2. Police show up, Molly has been taken back to her institution, husband Beaks is coming to
# confirm the body, Chief tells Nairda and Strudle to go to the institution to find out how
# Molly Stone broke out and more about the case in general


# SCENE 3 - Institution Questioning
# 1. Nun and Strudle make way to the institution, discussing Molly Stone's general background as
# a phychic. Strudle has to wait in the car whiles Nairda goes in.

# 2. Molly Stone doesn't like helping the police, even if she knows where something is, due
# to being institutionalised and seen as a "quack". She's also being arrested and convicted of some crimes, due
# to knowing so much about the crime that only the perp would have known those details / etc.

# 3. She pleas that she doesn't know how she escaped the institution, why she went to Beaks home, how she didn't
# know where the Beaks Mansion was, but Nairda is not convinced and insults her "powers".

# 4. Cause of the start of the game fourth wall breaking. He insults Molly Stone, but she's actually real.
# She curses Nun with the ability to break the fourth wall/see reality (aka: that they're all toys).

# 5. Nairda can see a giant, faint hand holding Molly Stone up

# 6. His vision goes to black and he's suddenly back to the car.

# 7. CHOICE - Truth (I blacked out? Don't remember) or Lie (I'm just tired, it's nothing)


# SCENE 04 - Pizza Time
# 1. Pizza time getting a pizza at pizza place
# 2. Noticing the pizza place is a bit.... weird looking, almost plastic
# 3. CHOICE? - mention it to husband or no?


# SCENE 05 - Funeral
# 1. Wife funeral, Nun has to go wash his hands and finds the husband has been
# throwing all of his wife's stuff into boxes to bin. When husband says Nun would understand
# wanting to have a fresh start asap after tradjedy, Nun mentions when his partner died he never threw anything
# out of theirs in the office.

# 2. Nun keeps seeing a weird ghost-like arm every so often holding the other characters in place
# Choice - Mention it or no?

# 3. The doorway to the house has unopened letters and a perfume smelling parcel that has a denied acceptance/delivery
# label on it.
# Nun thinks maybe husband had a mistress, noted the address and name


# SCENE 06 - Talking about the case
# 1. Current evidence is only speculation about husband because he thrown the stuff away

# 2. Possible Mistress? Has address and name noted down

# 3. He seemed more proactive about finding her than finding the murderer


# SCENE 07 Mistress scene
# 1. Go to apartment of the parcel returnee

# 2. She says the man is insane and manipulative and she broke up with him but he keeps love bombing her

# 3. Says she'd be happy to help if she isn't named directly and is kept from dangers as he's a dangerous man


# SCENE 08 - Worried about Nairda? and/or Ignoring "reality" (we're all actually toys and not real)
# 1.

# 2.

# 3...


# ENDINGS ENDINGS ENDINGS ENDINGS
# Scene XX - #ENDINGS: This checks which ending Nairda gets:
# - Tells truth about visions && solves the case - You tell the truth and take meds to stop it / solve case too
#    label which_end:
#        if truth >= 3 and solved >= 3:
#            jump truthsolved_end
# - Tells truth about visions && does not solve case - You tell the truth and take meds to stop it / don't solve case (due to this stress)
#        elif truth >= 3 and solved <= 3:
#            jump truthnotsolved_end
# - Lies about visions && solves the case - You lie out of fear and don't take meds to stop it & you can see you're in a simulation type situation for the rest of
# your life/ but at least you solved the case (maybe visit Molly)
#        elif truth <= 3 and solved >= 3:
#            jump liesolved_end
#- Lies about visions and does not solve the case - You lie out of fear & can see you're in a simulation type situation for the rest of your life / don't solve case (due to the stress) / Everyone is worried about you
#        elif truth <= 3 and solved <= 3:
#            jump lienotsolved_end


# Game End.

# -----------------------------------------------------------------------------

# Movie / Cutscenes (where needed)
image officevideo1 movie = Movie(play="officevideo1.webm")
init:
    image movie = Movie(size=(1280, 720), xalign=0.5, yalign=0.5)

# The game starts here
label start:
# Disclaimer screen
    scene screenstart
    "Any similarities to real events are purely coincidental."
    "No real animals were dressed in tiny suits and forced to solve crimes in the making of this videogame."

# SCENE 00: Introduction (world lore)
    scene classroom
    "Welcome to Chapter 01"
# QUESTION: Do you want a lore refresher?
    "Would you like a quick refresher on the world lore?"
    menu:
        "Sure!":
            jump Lore
        "No thanks, let's just start the game":
            jump GameStart

label Lore:
    scene apartmentdoor
    show tony n
    t "Am I on? Ok, just read the teleprompter? Ok!"
    t "Welcome to... Lore?"
    t "In our world, you don't wear shoes. Shoes hide your footprints, so nobody knows your species,
    and only criminals would purposefully hide that!"
    t "Have you ever heard of someone running for the hills?"
    t "Well it comes from an old law that has never been rectified!"
    t "If you stand on a hill, you're above the law, and thus, you can not be
    charged with any crime whiles on that hill."
    t "Crazy I know!"
    scene apartmentdoor
    show tony confused
    t "I'm not sure why they need to know this? It's common knowledge isn't it?"
    "(Tony see's the cameraman pointing to the teleprompter and mouthing to please just read from that)"
    scene apartmentdoor
    show tony n
    t "Ah, ok! and last but not least you should never..."
    play sound "audio/toiletnoise.mp3"
    "(a toilet flushes above)"
    scene apartmentdoor
    show tony angry
    t "Dammit Ezekiel! I'm trying to!"
    t "I'm sorry everyone, I have to stop the water!"
    stop sound
    scene apartmentdoor
    "(Tony runs back into his apartment, you hear a broom hitting on the ceiling
    and a faint 'Fuck you, Tony!' coming from above)"
    GameDev "*sigh* I don't think he's coming back, let's just start the game..."
    jump GameStart

# SCENE 00: Previously on Nairda Nun
label GameStart:
    scene apartmentdoor
    "(Previously on Nairda Nun Chapter 00:)"
    scene screenstart1
    "(There was a murder robbery at the Museum of Frogs and Fancies.)"
    "(It was the care takers, killing a guard, using a mace to open the opal case,
    and stealing it! Nairda solved the case and they were caught before they made a run for the hills...)"
    scene apartmentlongshot
    "(And now the story continues...)"

# SCENE 01 - Nairda Nun normal day of crime solving
# 1. Nun having a normal day of work. Case of a missing wife, gone 72 hours, husband
# is sad and wanting any information about his wife.
    scene apartmentdoor
    #BGM
    play music "audio/cafe.mp3"
    "(Nairda Nun received a phone call about a missing person's case)"
    "(A powerful man's wife hasn't been seen in the past 72 hours)"
    "(Nairda has been called to attend a live news conference where the man will be asking for witnesses to come
    forward)"
    show nun n
    nun "I'm on my way!"
    scene apartmentdoor
    "(Nairda's husband rushes out of the apartment from behind him)"
    scene apartmentdoor
    show snun angry at right
    hubby "I know you haven't had a case in a while but that's not an excuse to forget me!"
    scene apartmentdoor
    show snun angry
    hubby "I mean I am the one driving for croak's sake!"

    scene stairs
    "(Catching up to Nairda, they head off to the conference together)"
    scene messhall
    "(A large group of reporters and police have flocked inside of a conference room listening to the husband's pleas)"
    "(Nairda and Strudle arrive right at the end of the speech)"
    show beaks n
    beaks "My wife... My BELOVED wife!"
    beaks "If you hear this..."
    play sound "audio/crowd.mp3"
    beaks "Don't give up!"
    play sound "audio/camerashutter.mp3"
    "(The reporters go wild, taking photos and shouting questions whiles Beaks leaves the stage)"
    play sound "audio/crowd.mp3"
    scene messhall
    show nun sad at right
    show snun sad at left
    nun "That poor man"
    hubby "I know, I'd be besides myself if you ever went missing"
    "(Nairda goes to Beaks to offer his condolenses)"
    scene messhall
    show nun n at right
    show beaks n at left
    stop sound
    nun "Anything I can do, I'm available 24/7!"
    beaks "Ah, you must be Nairda Nun. I've heard great things about you."
    beaks "I'm sure you'll find my wife in no time at all"
    scene messhall
    show nun shy at right
    show beaks n at left
    nun "Thank you, sir."
    show hare happy
    d "Don't worry sir Beaks!"
    "(Detective Harry Hare nudges Nairda back and takes over the scene)"
    scene messhall
    show beaks n at left
    show hare happy at right
    d "We've got everything covered! We're searching the whole town! I guarantee she'll be safe at home by the 'morrow!"

    scene messhall
    "(Nairda goes back to his husband)"
    "(Noticing Beaks has a phone call and has waved Detective Harry Hare away from him)"
    show nun sad at right
    show snun n at left
    nun "I'm not sure what his issue is with me..."
    scene messhall
    show nun sad at right
    show snun angry at left
    hubby "Ohhhhh if there weren't so many cameras I'd give him a clip on the ear!"
    show nun happy at right
    show snun n at left
    nun "You know just how to cheer me up"
    hubby "..."
    hubby "I could cheer you up more, how about we get fly pie for tea?"
    scene messhall
    show nun shy
    show snun happy at left
    nun "This is why I love you"
    scene messhall
    show nun shy
    show snun shy at left
    "(Beaks can still be seen on the phone, covering his mouth with his flippers and avoiding the cameras)"
    hubby "Shall we?"
    "(With the conference coming to a close)"
    scene stairs
    "(Strudle grabs Nairda's hand and they go back to the car"
    "(Grabbing a take away and heading home for the evening)"
    "(To enjoy fly pie for tea)"

    #ENG BGM "Cafe"
    stop music

# SCENE 02 - Molly Stone finds the wife / curses Nun
# 1. Molly Stone wakes up at murder scene with the dead wife there
    scene morning1
    play music "audio/hailstorm.mp3"
    "(Meanwhile... The next morning...)"
    scene morning2
    molly "Ouch, my head..."

    # thunder sound
    play sound "audio/thunderboom.mp3"
    scene darkness2
    molly "What happened?"
    # Heavy rain noises

    scene darkness3
    # scene slightly lighter but still dark, maybe circle with dead body in the background faintly
    # thunder sounds
    molly "Am I outside?"

    # More spooky noises
    # More scene coming into focus?
    scene darkness2
    molly "How did I get outside?"

    # Dead body imminently visible
    # spooky noises
    scene darkness1
    molly "Who's...?"

    scene darkness4
    molly "Mrs Beaks...? From the news?"

    scene darkness5
    play sound "audio/thunderboom.mp3"
    play sound "audio/scream1.mp3"
    molly "MRS BEAKS!!?!!"

    scene morning3
    "(Molly's scream echoes out in the distance)"


    scene morning4
    stop music
    "(A short while later)"
    play music "audio/cafe.mp3"
    nun "I came here as fast as I could!"
    hubby "We heard Mrs Beaks had been found?"
    chief "Her body was discovered at 7.43am this morning"
    hubby "Her body? Oh no..."
    nun "Who discovered the body?"
    "(Tension can be felt in the air as everyone else turns to the Chief to answer)"
    chief "Molly Stone"
    nun "Molly Stone?"
    nun "I thought Molly Stone was in an institution?"
    chief "So did we... It seems she broke out and come across the body a mere 400 metres from the Beaks Mansion"
    chief "She claims she doesn't know how she got here, and was in histerics upon finding the body"
    chief "The only reason we know about it is due to some joggers hearing her screams from down the hillside"
    chief "Once we figured out it was her, we called the institution and some doctors came by to pick her up"
    "(An uneasy feeling circles in the air)"
    hubby "You don't think that...?"
    chief "I'm not sure what to think yet, but I had to break the news to Mr Beaks about his wife"
    chief "He said not to move the body until he got here"
    chief "Something about not believing it until he sees it for himself"
    "(A commotion from above could be heard as Beaks toppled down the hillside to get to his wife)"
    chief "I'll take it from here, you two go to the institution and see what you can find out"
    "(The Chief of police composes himself, whiles Beaks can be seen throwing himself onto his wife's body screaming out in pain)"
    chief "sigh... Nobody should have to see their significant other this way"
    "(The sound of the Chief shouting to Beaks can be heard in the distance)"
    "(Something about not tampering with possible evidence, mixed with being sorry for his loss)"
    "(Nairda and Strudle head back to their car and make way to the institution)"



# SCENE 3 - Institution Questioning
# 1. Nun and Strudle make way to the institution, discussing Molly Stone's general background as
# a phychic. Strudle has to wait in the car whiles Nairda goes in.
    scene hospital
    "(The institution: A small brown building, with gold patterns painted meticulously on the roof)"
    "(If you didn't have claustrophobia before, you most certainly do now.)"
    hubby "I think I best wait outside..."
    nun "I'll try to be quick"
    "(Nobody wants to be in the institution.)"
    "(The inside feels like one long room wrapped in white fabric, shielding everyone from each other's gaze)"
    "(The air isn't thick)"
    "(It's just absent)"
    "(Molly Stone is in the corner)"


# 2. Molly Stone doesn't like helping the police, even if she knows where something is, due
# to being institutionalised and seen as a "quack". She's also being arrested and convicted of some crimes, due
# to knowing so much about the crime that only the perp would have known those details / etc.
# 3. She pleas that she doesn't know how she escaped the institution, why she went to Beaks home, how she didn't
# know where the Beaks Mansion was, but Nairda is not convinced and insults her "powers".

    nun "Molly? I'm Nairda Nun, detective. I heard you found Mrs Beaks this morning?"
    "(Molly takes in deep breathes, like a weight had been lifted from her upon being found in the institution)"
    molly "Thank you for coming. I needed that."
    show nun confused
    nun "You needed... that?"
    "(Her face is grave, if she says too much, an orderly might overhear)"
    "(You don't want them to hear)"
    nun "Can you tell me what happened? From start to finish?"
    molly "I woke up and Mrs Beaks was in front of me, covered in blood, laying on the rocks at the bottom of the hillside"
    nun "And before that?"
    molly "Before that I was here."
    nun "..."
    nun "Are you saying you don't remember how you come to being near the Beaks Mansion?"
    "(Molly seems upset)"
    molly "I've never been there before, I didn't even see a damn mansion!"
    molly "I woke up. Found Mrs Beaks. I started screaming. The police came..."
    molly "... then an orderly came..."
    molly "And now I'm back here..."
    "(Nairda knows the institute is a stressful place, but it doesn't usually cause memory loss.)"
    "(It also is inescapible. Unless you're allowed to leave, you know you aren't leaving it.)"
    nun "How did you escape?"
    "(Molly screams)"
    play sound "audio/scream1.mp3"
    molly "I DIDN'T ESCAPE!!!"
    "(She's stifling for breath)"
    molly "I didn't even see the hands!"
    "(Molly holds her mouth shut)"
    molly "I didn't..."
    "(Hoping an Orderly did not hear that)"
    molly "I was just... there..."
    "(Nairda knows about these 'hands' she speaks of)"
    "(Molly Stone is rather infamous for her stories. It's how she was placed into the institute in the first place)"
    "(Giant, unidentified animal paws, apparently grabbing at the world)"
    "(Moving it around like it's puppet)"
    "(But it's stupid...)"
    "(To even humour her is illogical)"
    nun "You can't keep telling these lies, Molly"
    nun "Faining psychic abilities to give anonymous tips to the police"
    nun "Saying your friend gave you this 'power' before they were... what was it?"
    nun "Thrown into the void? For being broken?"
    nun "The only reason you're in here instead of a prison is because you're a danger to yourself..."
    nun "And others."
    "(Molly Stone is irritated. As is Nairda.)"
    "(She takes a moment to compose herself)"
    molly "I didn't say I was psychic. YOU all did!"
    molly "The things I saw, I saw them from above"
    molly "Everything was just happening with no way to stop it or even interact!"
    molly "The murder robbery at the Museum of Frogs and Fancies!"
    molly "I saw it happen but I wasn't there!"
    "(Nairda has had enough)"
    "(He tries to be understanding, he too struggles with his own mental health)"
    "(But Molly has known too much information at several crime scenes)"
    "(Especially for someone who 'was not there')"
    "(Using the excuse some kind of god is causing all of this, or she could just see it from 'above')"
    "(Feels too much like she's suffering from Delisions of Grandeur)"
    nun "It was a waste of time coming here..."
    "(He goes to knock on the wall to let the orderly know he's ready to leave)"

# 4. Cause of the start of the game fourth wall breaking. He insults Molly Stone, but she's actually real.
# She curses Nun with the ability to break the fourth wall/see reality (aka: that they're all toys).
    molly "You know what!"
    "(Nairda stops and turns around)"
    molly "Do you want to know what it feels like?"
    "(Nairda has never seen such conviction come from someone before)"
    "(He almost believes she's innocent)"
    molly "THIS! Is what it feels like!"
    "(Darting to Nairda she holds on to his head and whispers into his ears)"
# Curse
    molly "Hocus pocus diddly dee"
    molly "You'll now see... the reality!"

# 5. Nairda can see a giant, faint hand holding Molly Stone up, he rubs his eyes and goes back to the car.
    "(He jumps back in shock, and starts banging on the wall to leave)"
    nun "Are you craz...?!"
    "(He stops for a moment)"
    nun "What's...?"
    "(Rubbing his eyes, he takes another look towards Molly Stone)"
    molly "Welcome to the club, Nairda Nun."

# 6. His vision goes to black and he's suddenly back to the car.

    "(Nairda's vision turns to black)"
    scene stairs
    hubby "How did it go? Did you find out how she escaped?"
    "(Nairda is in the car with Strudle, who is looking expectantly for an answer)"
    nun "When did I?..."
    hubby "When did you what?"

    # choice 1 : Tell Hubby you teleported/blacked out, or stay silent
# QUESTION: I teleported? Or no?
    "(You don't know how you got into the car, what do you want to say?)"
    menu:
        "Oh nothing... I think I'm just tired.":
            $ truth = truth -1  #Lie choice!
            play sound "audio/no.mp3"
            jump lie1
        "When did I get back into the car? When did I leave the institution?":
            $ truth = truth +1  #Truth choice!
            play sound "audio/yes.mp3"
            jump truth1

label lie1:
    "(Strudle looks at Nairda a little confused)"
    nun "It's nothing..."
    hubby "Well, it's been a long day! How about we get some lunch?"
    nun "Good idea"
    jump pizzatime

label truth1:
    "(Strudle looks at Nairda a little confused)"
    hubby "What do you mean, Nairda? You walked out a few minutes ago and got into the car..."
    nun "I think I blacked out. I was talking to Molly and now I'm just?"
    nun "... here?"
    hubby "I feel like this has never happened before, but it's your first case in a while and it's been a long day so maybe you're just tired?"
    "(Strudle takes a longer look at his husband)"
    hubby "How about we get some lunch and take a break for a while?"
    nun "Y-yeah... That might do us some good..."
    jump pizzatime


# SCENE 04 - Pizza Time
# 1. Pizza time getting a pizza at pizza place
# 2. Noticing the pizza place is a bit.... weird looking, almost plastic
# 3. CHOICE? - mention it to husband or no?
label pizzatime:
    scene pizza
    "(The two of them head for the pizza shop)"
    "(Peckish: Owned by the same Chicken and Rooster family since as far back as anyone can remember)"
    nun "Hey Fry~ the pizza guy~!"
    fry "Yo!"
    hubby "How's the wife and kids?"
    fry "Haha! Don't say that too loud, you'll get my dad's hopes up!"
    "(Everybody knows that Fry doesn't like having romantic relationships, and he plans on never having kids)"
    "(Nairda looks at Fry and smirks)"
    nun "Can we have the usual?"
    fry "The amount of customers that say that! And YOU order something different every time!"
    "(They share a laugh)"
    fry "So, what can I actually get you both?"
    "(They take a moment to look at the menu)"
    nun "Veggie feast pizza sounds good!"
    hubby "Yeah, make it a large to share"
    fry "Roger that!"
    "(Fry salutes, then goes to make the pizza)"
    hubby "This is nice, we haven't had a pizza in a while"
    nun "..."
    "(Nairda stares off into the distance whiles Strudle scrolls on his phone)"
    show veggiepizza2
    hubby "This looks GREAT!"
    "(Nairda looks over)"
    show pizza1
    nun "...?"
    nun "What's...?"
    scene pizza
    "(Strudle looks at Nairda)"
    hubby "Are you ok?"
    "(Nairda looks back at the pizza)"
    show veggiepizza2
    nun "Yeah, it's just the pizza is...?"
    scene pizza1
    hubby "The pizza is?"
    scene veggiepizza2

        # choice 2 : Tell Hubby pizza was toy, or stay silent
    # QUESTION: Pizza toy or real
    "(The pizza looked like it was made of kids clay? No wait, now it's clearly a real pizza. Now it looks like? What do you say?)"
    menu:
        "Oh nothing, it's just a normal pizza":
            $ truth = truth -1  #Lie choice!
            play sound "audio/no.mp3"
            fry "Should I take that as a compliment or an insult?"
            "(Fry and Strudle laugh)"
            hubby "He's just been tired today from a case. Come'on, Nairda! Let's dig in!"
            "(After eating the pizza Nairda and Strudle both return home)"
            "(The funeral for Mrs Beaks is soon, and they've been asked to attend it as a sign of respect from the department)"
            jump funeral

        "The pizza looked like it was made of clay for a minute, like the entire scene was a giant children's doll house":
            $ truth = truth +1  #Truth choice!
            play sound "audio/yes.mp3"
            "(Suddenly you are unable to move)"
            nun "I can't..."
            scene pizza2
            "(The world around you turns to plastic)"
            "(You no longer feel your body the same)"
            "(It is as though you're covered in felt, your limbs a solid resin)"
            "(Everyone is silent and motionless around you)"
            "(There's a weird pulling sensation)"
            "(You can not move)"
            "(You see them)"
            "(YOU)"
            "(SEE)"
            scene pizza
            hubby "Nairda?"
            hubby "NAIRDA!??"
            "(Strudle is shaking you)"
            nun "What?"
            hubby "Hey! What was that? You just stood there like an unresponsive mannequin for three minutes!"
            fry "Do we still need the ambulance?"
            hubby "No, I think he's ok? He's back again anyway, whatever that was..."
            nun "I couldn't move"
            "(Strudle is very worried about you)"
            hubby "Can we get the rest of the pizza to go, I want to take him home"
            fry "Of course, just a sec!"
            "(The remaining bits of the pizza is boxed up)"
            "(Nairda and Strudle go back to the car and drive home)"
            scene apartmentdoor
            "(Back at the apartment, Strudle fiddles with the house keys)"
            hubby "Hey, are you sure you're alright?"
            hubby "You've been weird ever since the institution..."
            nun "I'm not sure what's wrong with me, I can't even begin to explain it"
            hubby "Should we make an appointment with Dr Krieger? She might know what's wrong?"
            nun "Not just yet, we're going to busy for the next few days, the funeral of Mrs Beaks is coming up"
            nun "The chief wants us to go to it to show our respect and support for Mr Beaks"
            "(Strudle doesn't look too optimistic)"
            hubby "Ok"
            hubby "But after the funeral we should probably get a session"
            "(Nun looks at Strudle reassuringly)"
            nun "Of course. I promise."

            jump funeral


# SCENE 05 - Funeral
label funeral:
# 1. Wife funeral intro

    scene funeral
    "(The funeral was beautifully decorated and her coffin was covered in roses spelling out 'My Beloved Wife')"
    "(It looked a little over the top)"
    "(There were press at the church, and the burial site)"
    "(Nairda couldn't help but notice how Beaks seemingly posed for the cameras every few sentences during his heartfelt speech)"
    "(But now it's time for the wake at the Beaks Mansion)"
    "(If the funeral and burial site were anything to go by, the wake will likely have some good eats!)"
    "(Strudle tries to hide his excitement, he loves a good buffet)"
    "(Nairda on the other hand, isn't very keen on food left in the open for long periods of time)"
    "(He also doesn't know when the food was prepared, it could have been days ago! Nairda will abstain from partaking in the food.)"

    scene beaksmansion
    "(Their predictions were correct. They did not hold back on the buffet!)"
    hubby "By the gods! By the gods!"
    "(Strudle is practically salivating)"
    nun "Hey, at least try to look like you're grieving!"
    hubby "I've never seen this many types of tomatoes before! I don't even like tomatoes but I have to TRY. THEM. ALL!"
    "(Strudle runs to the buffet and starts to fill his plate whiles Nairda looks at the other guests in the vicinity apologetically)"
    nun "He's truely crushed by Mrs Beaks death he... eats his feelings is all..."
    "(Nairda hopes that is enough to stop the judgemental stares towards his husband, now seven deep into the tomato dishes)"
    "(Mr Beaks comes in, looks around, and starts to dab his eyes with a clean pocket square)"
    nun "Mr Beaks, I'm so sorry for your loss."
    "(Beaks grabs Nairda's hands and shakes them vigourously)"
    "(Nairda has no idea why Beak's hands feel clammy)"
    beaks "Thank you Nairda, who's here at the moment?"
    "(Beaks lets go of Nairda's hands and looks around some more, making a mental note of the guests)"
    nun "Ah, I'm not sure. I haven't introduced myself yet."
    "(Beaks looks disappointed with the turn out)"
    beaks "Is the mayor?"
    "(Beaks spots the mayor in the corner, and goes over for a photo opportunity)"

# 2. Nun has to go wash his hands and finds the husband has been
# throwing all of his wife's stuff into boxes to bin. When husband says Nun would understand
# wanting to have a fresh start asap after tradjedy, Nun mentions when his partner died he never threw anything
# out of theirs in the office.

    "(Strudle comes back to Nairda, plate filled with the most fanciful of buffet treats)"
    hubby "Are you ok? You look like you've seen a ghost."
    "(The damp, almost greasy handprints of Beaks still lingers on Nairda's hands)"
    nun "He did a two hander... BOTH hands, wrapped around BOTH of my hands!"
    nun "And he was... moist?!? Like all of his sweat is released out of his flipper fins!"
    "(Nairda turns left and right to find any direction that'll possibly have a sink to wash them)"
    "(Hands still frozen in place mid-air as if moving them will dirty them up more)"
    nun "I'm going to the bathroom, there has to be one upstairs!"
    nun "Cover for me... I need to clean this off..."
    "(Strudle nods acceptingly, mouth full of several types of tomatoes and squares of cheese"
    hubby "Uh-hum... can do... uhm... go clean"

# Hand clean bathroom / wife stuff in boxes
    "(Heading upstairs, Nairda goes into the master bedroom after noticing it has an En Suite)"
    "(Boxes packed with Mrs Beaks' stuff is piled into the corner)"
    "(Completely erasing her memory from every part of the bedroom)"
    nun "This is the polar opposite to downstairs..."
    "(Nairda whispers to himself, whiles going into the En suite to wash his hands)"
    "(The water feels fantastic, and Beaks even buys the fancy antibacterial soap)"
    "(Nairda is lost in thought whiles thoroughly cleaning his hands and wrists to a godly level)"
    beaks "What are you doing in here?"
    nun "AH!"
    beaks "The guest bathrooms are downstairs..."
    nun "Mr Beaks! I'm sorry, I was looking for a bathroom and thought it'd be logical for one to be upstairs"
    beaks "Well, the guest bathrooms are downstairs so let me show you to those..."
    "(Beaks gestures to the bedroom doorway, waiting for Nairda to follow)"
    nun "Of course, thank you."
    "(Nairda stops in the bedroom and looks at the boxes of Mrs Beaks' items again)"
    nun "Why did you pack up all of her stuff?"
    beaks "Well you know, after a death it's best to get rid of their stuff so you can have a fresh start"
    beaks "You get it, right?"
    "(Nairda looks up confused)"
    nun "But it's memories? I haven't even moved my detective partner's stuff out of the office and he passed over a year ago"
    "(Beaks looks back at Nairda)"
    beaks "I guess people mourn in different ways. Let me show you to the bathrooms downstairs."
    nun "Ah, yes. Of course. My apologies!"
    "(The two of them head downstairs and Beaks leads Nairda to not one but two separate bathrooms on the ground floor)"
    beaks "Use these next time."
    "(More guests to the wake walk in, peaking Beaks' interest)"
    beaks "Now if you'll excuse me!"
    "(He quickly waddles over and leads the new guests to the lounge)"
    "(Strudle, halfway through a second plate of food, comes over to Nairda)"
    hubby "Sooo.... Beaks saw you go upstairs ey?"
    nun "It was very awkward, but it was worth it for the soap alone! I feel like I won't need to wash my hands for another year!"
    "(Nairda is rubbing his hands, whispering to himself)"
    nun "So clean, so smooth..."

# 3. The doorway to the house has unopened letters and a perfume smelling parcel that has a denied acceptance/delivery
# label on it.
# Nun thinks maybe husband had a mistress, noted the address and name
    "(Strudle finishes the plate and lays it onto a cart)"
    hubby "Do you think we need to be here much longer? It feels more like a photo shoot for the elites than a funeral wake"
    nun "I think we can go, he's not going to notice us unless I go upstairs again to use more of his hand soap"
    "(Strudle tries to stifle a laugh, and they walk towards the door)"
    "(At the front door, letters are piled up along with a nice smelling box)"
    "(It wasn't for this address and has a random woman's name on it)"
    "(Along with a stamp saying it was a refused delivery and returned to sender)"
    nun "Does this smell like perfume to you?"
    "(Nairda holds the parcel to Strudles nose, causing Strudle to panic in a hushed whisper)"
    hubby "Wha?! What are you doing? You can't go through someone elses mail!"
    nun "It's not for either of the Beaks though... It's for an Olivia at..."
    "(Nairda makes a mental note of the name and address)"
    nun "Something isn't right here... Did Beaks have a mistress?"
    hubby "Can we just go before he sees us snooping?"
    nun "Yeah... we should go..."

    # CHANGE TO ROADS AND FANCY HOUSES
    "(The drive home is rather long, the Beaks Mansion is so deep into the richest part of town that you get an
    uncanny valley vibe from the sheer size of the plots and oddly laid out housing designs)"
    "(After longer than they wished to have needed to drive to finally get out of there)"
    "(Both Strudle and Nairda get back home, change into their pajamas, and watch a few episodes of their favourite
    comfort show before having an early night)"

# SCENE 06 - Talking about the case
    scene lab
    "(The next day: At the police station.)"
    chief "We need to find the killer of Mrs Beaks, Nairda! What do you have for me?"

    # QUESTION: Evidence
    "(What do you wish to talk about?)"
    menu:
# 1. Current evidence is only speculation about husband because he thrown the stuff away
        "Mr Beaks had packed up all of his wife's things, he said he's getting rid of it all":
            $ solved = solved +1  #Solved yes choice!
            play sound "audio/yes.mp3"
            chief "All of it?"
            nun "Yeah, in the master bedroom everything was in boxes"
            nun "He said he is getting rid of it all so he can have a fresh start"
            chief "That seems a little quick, doesn't it? She's only been dead for a week..."
            nun "That's what I thought too"
            chief "Good catch, we should look into that a little more"
            jump evidence1
# 2. He seemed more proactive about finding her than finding the murderer
        "He seemed more proactive about finding her body than the killer":
            $ solved = solved +1  #Solved yes choice!
            play sound "audio/yes.mp3"
            chief "What do you mean?"
            nun "Since finding her body, he hasn't mentioned anything about the case"
            hubby "At the funeral and the wake, he seemed more interested in doing photo ops than talking to Nun about the case"
            nun "Yeah, come to think of it he only asked me who else had arrived yet, nothing about his wife or finding out who killed her at all"
            chief "Did he mention Molly Stone?"
            "(Strudle and Nairda look at each other and shrug)"
            nun "No, he hasn't mentioned her at all. Does he assume she's been arrested for the murder?"
            hubby "He might do? She found the body, after escaping from the institution..."
            nun "But did she escape? She said she blacked out and was just there at the scene of the murder"
            nun "She claims she doesn't know the Beaks, and didn't know the location of the Beaks Mansion either"
            jump evidence2

# 3. Bad choice - links to possible Mistress? Has address and name noted down
        "I don't have anything...":
            $ correct = solved -1 #Solved no choice!
            play sound "audio/no.mp3"
            hubby "Really Nairda? There's been loads of stuff!"
            hubby "What about that parcel?"
            nun "Oh, well there was a returned parcel that was addressed to a random woman by the door of the mansion"
            chief "Okay, and?"
            nun "It had 'refused delivery' stamps on it, also smelled like perfume."
            chief "So it wasn't accepted by this woman, and was returned to the Beaks Mansion?"
            hubby "Yeah it did seem a little odd"
            chief "Do you remember the name and address?"
            nun "I made a note of them, yes."
            chief "Go check it out... He might have had a jealous mistress"
            jump mistress


label evidence1:
# 2. He seemed more proactive about finding her than finding the murderer
    menu:
        "He seemed more proactive about finding her body than the killer":
            $ correct = solved +1  #Solved yes choice!
            play sound "audio/yes.mp3"
            chief "What do you mean?"
            nun "Since finding her body, he hasn't mentioned anything about the case"
            hubby "At the funeral and the wake, he seemed more interested in doing photo ops than talking to Nun about the case"
            nun "Yeah, come to think of it he only asked me who else had arrived yet, nothing about his wife or finding out who killed her at all"
            chief "Did he mention Molly Stone?"
            "(Strudle and Nairda look at each other and shrug)"
            nun "No, he hasn't mentioned her at all. Does he assume she's been arrested for the murder?"
            hubby "He might do? She found the body, after escaping from the institution..."
            nun "But did she escape? She said she blacked out and was just there at the scene of the murder"
            nun "She claims she doesn't know the Beaks, and didn't know the location of the Beaks Mansion either"
            jump evidence3

# 3. Bad choice - links to possible Mistress? Has address and name noted down
        "I don't have anything else...":
            $ correct = solved -1 #Solved no choice!
            play sound "audio/no.mp3"
            hubby "Really Nairda? There's been loads of stuff!"
            hubby "What about that parcel?"
            nun "Oh, well there was a returned parcel that was addressed to a random woman by the door of the mansion"
            chief "Okay, and?"
            nun "It had 'refused delivery' stamps on it, also smelled like perfume."
            chief "So it wasn't accepted by this woman, and was returned to the Beaks Mansion?"
            hubby "Yeah it did seem a little odd"
            chief "Do you remember the name and address?"
            nun "I made a note of them, yes."
            chief "Go check it out... He might have had a jealous mistress"
            jump mistress

label evidence2:
# 1. Current evidence is only speculation about husband because he thrown the stuff away
    menu:
        "Mr Beaks had packed up all of his wife's things, he said he's getting rid of it all":
            $ correct = solved +1  #Solved yes choice!
            play sound "audio/yes.mp3"
            chief "All of it?"
            nun "Yeah, in the master bedroom everything was in boxes"
            nun "He said he is getting rid of it all so he can have a fresh start"
            chief "That seems a little quick, doesn't it? She's only been dead for a week..."
            nun "That's what I thought too"
            chief "Good catch, we should look into that a little more"
            jump evidence3

# 3. Bad choice - links to possible Mistress? Has address and name noted down
        "I don't have anything else...":
            $ correct = solved -1 #Solved no choice!
            play sound "audio/no.mp3"
            hubby "Really Nairda? There's been loads of stuff!"
            hubby "What about that parcel?"
            nun "Oh, well there was a returned parcel that was addressed to a random woman by the door of the mansion"
            chief "Okay, and?"
            nun "It had 'refused delivery' stamps on it, also smelled like perfume."
            chief "So it wasn't accepted by this woman, and was returned to the Beaks Mansion?"
            hubby "Yeah it did seem a little odd"
            chief "Do you remember the name and address?"
            nun "I made a note of them, yes."
            chief "Go check it out... He might have had a jealous mistress"
            jump mistress


label evidence3:
    # 3. Possible Mistress? Has address and name noted down
    hubby "What about the parcel at the Beaks Mansion with another woman's name and address on it"
    chief "The what?"
    nun "There was a returned parcel that was addressed to a random woman by the door of the mansion"
    chief "Okay, and?"
    nun "It had 'refused delivery' stamps on it, also smelled like perfume."
    chief "So it wasn't accepted by this woman, and was returned to the Beaks Mansion?"
    hubby "Yeah it did seem a little odd"
    chief "Do you remember the name and address?"
    nun "I made a note of them, yes."
    chief "Go check it out... He might have had a jealous mistress"
    jump mistress

# SCENE 07
label mistress:
# 1. Go to apartment of the parcel returnee

# 2. She says the man is insane and manipulative and she broke up with him but he keeps love bombing her
# #   Pretty much he's a controlling asshat and she's scared of him

# 3. Says she'd be happy to help if she isn't named directly and is kept from dangers as he's a dangerous man
#   Implications he killed his wife to finally be with her when she doesn't want this
    scene apartmentlongshot
    "(Nairda and Strudle go to the address he noted down)"
    "(In a disadvantaged part of town, the apartment building has several teens outside)"
    "(Nairda gets nervous around teenagers)"
    "(He's a very small frog and there's so many news stories about teenagers being 'thugs' that he's always a little on edge)"
    "(Strudle knows the news is mostly nonscence, but he did grow up in a safer environment to Nairda and most of their friends,)"
    "(and generally most of their day-to-day acquaintances, so he understands it isn't the most *outlandish* anxiety to have)"
    "(They go inside and make their way to the apartment door, knocking the handle lightly)"
    "(A shadow in the peep hole forms and disappears momentarily)"
    olive "Just a second!"
    "(The door opens and a frail rabbit peeking around the corner of the door)"
    "(She looks relieved that you were frogs, like she was expecting something else)"
    olive "I'm not interested in buying anything, I'm sorry..."
    nun "Ah! No! We're, well I'm a detective, this is my partner Strudle. He's like my assistant!"
    "(She looks at Strudle and nods knowingly)"
    olive "Is there an issue, err detective?"
    nun "I was wondering if we could ask you about someone in particular, regarding an open investigation?"
    "(Visibly shakey, as if she already knows who you're talking about, she ushers Nairda and Strudle to come inside quietly)"
    "(then closes and locks the door behind everyone)"
    olive "Oh dear..."
    hubby "Are you alright?"
    olive "Oh dear oh dear..."
    "(She ushers Nairda and Strudle to take a seat on the sofa, whiles she continues to pace around the room)"
    nun "Uhm, so! I'm detective Nairda, and this is my partner Strudle. I was wondering if you could tell me anything about Bea..."
    "(Before he could finish saying 'Beaks' Olivia lets out a small whimper and cuts him off)"
    olive "It'd be easier to tell you what I DON'T know about that penguin!"
    "(She pauses)"
    olive "I'm sorry he's just..."
    "(She pauses again)"

# QUESTION
    "What do you wish to ask about?"
    menu:
        "Were you two close...?":
            $ solved = solved +1  #Solved yes choice!
            play sound "audio/yes.mp3"
            olive "We were once, we used to date."
            nun "But he's married?"
            olive "I didn't know at first and then when I found out who he actually was I broke it off with him"
            hubby "How long were you dating before you found out he was married?"
            olive "It had been years..."
            "(Strudle and Nairda look shocked)"
            nun "Years?!?"
            olive "I know! I know! I feel like I must have had blinkers on!"
            olive "He used a fake name! A fake job! He always took me to the same fancy restaurant out of town!"
            olive "He was very controlling, but I'm not the most confident of people"
            olive "I would wear the dresses he got me, even if I didn't like them showing off so much fur"
            olive "Tie my ears back instead of being natural... the works!"
            olive "We always went to a hotel too... never to his place... and I never questioned it!"
            olive "He was paying some of my bills, I thought he loved me and maybe he'd pop the question and then... I saw the news..."
            olive "I only knew about him having a wife when I saw him as BEAKS on the news looking for his WIFE!"
            olive "I phoned him immediately afterwards and asked him what the hell was going on and he said not to worry about it and he'd explain it soon enough"
            olive "Then later on the news mentioned her body was found."
            olive "I phoned him again to give my condolences, even if he was a monster and an adulterer, his wife had been found dead and that'd be hard on anyone"
            "(She stops pacing and looks down, ears slumping towards the floor)"
            hubby "Are you ok?"
            olive "Y-yeah it's just... his reaction was that at least now we could be together..."
            nun "The same day his wife was found dead he reacted like that?!?"
            hubby "Did he sound in shock?"
            olive "No, he didn't. He sounded happy, excited even!"
            olive "I was creeped out and told him that isn't right"
            olive "And I said I wanted to break up with him"
            hubby "How did he react?"
            olive "He sounded angry. He's sounded angry before whenever I've challenged him on anything."
            "(Gesturing to her ears and clothes)"
            olive "Like not tieing my ears down, and maybe wearing something a little more comfortable to a dinner date"
            olive "I've had people knocking on the door in black suits, asking me to go see him, but I haven't opened the door and pretended I wasn't in"
            olive "I haven't been to work in 3 days! I don't want to lose my job but I'm scared of what might happen if I leave my apartment"
            olive "I don't even open the curtains so people can't see from inside"
            olive "I'm a mess..."
            "(Olivia sits on a small rocking chair and puts her hands on her face)"
            jump boxquestion

# 3. Bad choice - links to possible Mistress? Has address and name noted down
        "So he got you presents for... favours?":
            $ solved = solved -1 #Solved no choice!
            play sound "audio/no.mp3"
            olive "What are you implying?!?"
            "(There are expensive dresses thrown in the corner, and several expensive cosmetic items strewn around the apartment)"
            nun "Those dresses look to be worth something"
            hubby "And these cosmetics? It'd take me a month to buy that moisturising routine"
            "(Olivia looks closed off. Both offended at the implication, and ashamed at the amount of items in her posession that doesn't make the siuation she's in look good)"
            olive "He got me all of these. He tells me what to wear, and wants me to look 'young and fresh' for dinner dates where we'd be seen by his friends"
            "(She doesn't look like a criminal, she lives nowhere near any hills, and there isn't a single inkling of shoes being hidden anywhere in the tiny, barely furnished apartment)"
            olive "He'd of had me shaved bare if spotty ingrown hairs weren't a massive issue with rabbits!"
            nun "I'm sorry... I've had.. we've had a stressful few days ourselves"
            olive "Maybe don't jump to conclusions next time, you don't know what someone has been through."
            jump boxquestion

label boxquestion:
    "What do you wish to ask about?"
    menu:
        "There was an undelivered parcel at his home":
            $ solved = solved +1  #Solved yes choice!
            play sound "audio/yes.mp3"
            olive "..."
            "(She seems to be thinking)"
            hubby "It had your name and address on it, it was stamped with 'refused' on it, and was seemingly returned to sender"
            nun "It's honestly the only reason we knew about your existence in the first place"
            olive "Oh dear... He had started sending me presents since the break up, I stupidly accepted a parcel the first time"
            olive "I thought maybe I ordered something and forgot about it"
            olive "Since seeing it was a gift from him, I've refused every other parcel since"
            "(She points to a box of chocolates inside of a 'Rainforrest' delivery package in the corner)"
            olive "You can take that if you want to, I don't want it in my house but I don't want to be seen leaving the apartment at the moment"
            olive "I'm not sure what'll happen to me if him or one of his lackies see me outside"
            "(Nun puts the package into an evidence bag)"
            nun "Thanks, this could actually help a lot"
            olive "You're welcome... take the dresses too if you like. They've only been worn once each, he said he could not have 'his woman' wearing the same outfit to a date twice"
            "(The dresses are a very different style to the Olivia you see right now, in comfortable jogging bottoms and an oversized Hare State University hoody)"
            nun "I'm not sure if we need those, but maybe the reciepts if you have them? They might have some of his bank information on them"
            olive "Of course! He always left those in the boxes in case I could fit into a smaller size"
            "(She shuffles through the piles of dresses and packing material and pulls out several reciepts)"
            nun "Thank you!"
            "(He places them into another evidence bag)"
            jump helpher


        "Is perfume not good enough for the likes of you?":
            $ solved = solved -1  #Solved no choice!
            play sound "audio/no.mp3"
            olive "What are you implying?"
            nun "The undelivered box at Beaks Mansion. Smelled like expensive stuff."
            hubby "And it's not like you say no to expensive things"
            "(gesturing to the fancy cosmetics and dresses)"
            olive "Are you high? I hate this stuff! Don't you think I'd hang the dresses up in the wardrobe if I actually LIKED owning them!"
            "(A frustrated Olivia gives Nairda and Strudle a piece of her mind)"
            olive "Tight fitted dresses showing way TOO MUCH fur! Tieing my ears back so they didn't embarrass him!"
            olive "The beauty regimes to keep me 'young', those stupid diet pills and diet plans!"
            olive "He even wanted me to get plastic surgery! Ear shortening! Foot webbing?!?"
            olive "He was an intimidating man but I thought I could just handle it."
            "(Nairda and Strudle look at each other in mutual agreement and concern)"
            olive "I've spent my entire life with my head barely above water. A rich man wanted to date me. He helped with bills and all I had to do was..."
            "(Olivia looks down to the ground and mumbles)"
            olive "Whatever he said, I guess..."
            jump helpher



# SCENE 08
label helpher:
    "(It is clear she needs help)"
    nun "He sounds like a terrible person in real life but he hid it well when we were with him"
    hubby "It might be because we were associated with the police, so he was on good behaviour?"
    hubby "As we've only ever heard about him recently, we were told he was powerful... so a mistress in general isn't out of the realm of possibilities with rich folk"
    nun "But it sounded like he was trying to mold you into something you aren't comfortable with"
    nun "And it also seems like he doesn't like taking no for an answer"
    "(Olivia is visibly upset and stressed out)"
    "(Nairda whispers to Strudle)"
    nun "Does it sound like he... maybe had his wife killed to be with her in a more official setting?"
    "(Olivia looks even more on edge, she couldn't hear what he said but she felt like she knew what it was anyway and she steps in closer)"
    olive "With how he sounded on the phone recently, I'm almost certain that he did it so I could replace her"
    olive "He always went on about how his friends all had really young women hanging off their arms"
    olive "How he wished I would stop aging"
    olive "He even made jokes about replacing me with a 'younger model' whenever I admitted to skipping the beauty regimens he gave me, even for one day"
    hubby "That sounds awful"
    nun "I agree..."
    olive "I want to help you but you have to promise me I'll be safe!"
    olive "He said he has friends in the police force too, I don't want to be officially named in the reports"
    olive "I don't want anything to happen to me... I just want this to be over with"
    olive "I also heard that a woman from the institution had escaped... Maybe he paid her to kill Mrs Beaks?"
    nun "To be honest... I kind of get the feeling she was planted there on purpose to make it look like she did it"
    hubby "Or so someone other than him found the body!"
    "(Nairda stands up from the sofa)"
    nun "We'll get back to you! If you need anything here's my card and number! Do NOT hesitate to call!"
    "(Nairda and Strudle leave the apartment block and get back into the car)"
    scene apartmenthalls
    nun "We need to make a plan to keep her safe and have him admit to any crimes to do with his wife's death..."
    nun "And I think I need to talk to Molly Stone again to do it!"

# SCENE 09 - Back to the institute
# - get Molly to agree to pretending to be psychic and finding Molly's body in a similar place as Beaks' wife
# -
    scene hospital
    "(The Institute: A small brown building, with gold patterns painted meticulously on the roof)"
    "(If you didn't have claustrophobia before, you most certainly do now.)"
    "(Nobody wants to be in the institution.)"
    "(The inside feels like one long room wrapped in white fabric, shielding everyone from each other's gaze)"
    "(The air isn't thick)"
    "(It's just absent)"
    molly "You came back to this place? Why would anybody do that?"
    nun "I..."
    molly "Is it the reality? Because I don't know how to stop it once it's started"
    nun "No, it's not that."
    nun "I think we need your help"
    jump which_end

# SCENE XX - ENDINGS ENDINGS ENDINGS ENDINGS
# This checks which ending Nairda gets:
# - Tells truth about visions && solves the case - You tell the truth and take meds to stop it / solve case too
label which_end:
    if truth >= 2 and solved >= 3:
        jump truthsolved_end
# - Tells truth about visions && does not solve case - You tell the truth and take meds to stop it / don't solve case (due to this stress)
    elif truth >= 2 and solved < 3:
        jump truthnotsolved_end
# - Lies about visions && solves the case - You lie out of fear and don't take meds to stop it & you can see you're in a simulation type situation for the rest of
# your life/ but at least you solved the case (maybe visit Molly)
    elif truth < 2 and solved >= 3:
        jump liesolved_end
#- Lies about visions and does not solve the case - You lie out of fear & can see you're in a simulation type situation for the rest of your life / don't solve case (due to the stress) / Everyone is worried about you
    elif truth < 2 and solved < 3:
        jump lienotsolved_end


# SCENE 10 - The endings

label truthsolved_end:
    # Nairda tells the truth about seeing things, and the therapist helps with medication
    # The hands slowly disappear from existance
    # solved same way as other
    #"truth solved"
    "(A few days have passed)"
    "(Everyone goes down the hill towards the place where Mrs Beaks was found)"
    molly "Ohhhh it's getting stronger! I think her name is... Olive tree? That can't be right..."
    "(Molly holds her head then points one finger towards the bottom of the hill)"
    molly "It's Olive under the tree!"
    "(Down the hill next to a tree, Olivia's body is barely visible, laying still.)"
    "(In an expensive dress, red marks around her ears from being painfully tied back.)"
    "(Beaks sees her too, and runs to her side screaming in agony)"
    beaks "Noooo! It can't be!!!"
    "(The chief stops him from coming into close contact with the body)"
    beaks "Get off of me! I loved Olivia! I even got rid of my third wife so I could be with her!"
    chief "Wait a minute..."
    "(Beaks doesn't even realise what he's saying before the Chief remembers other details)"
    chief "Third...? That's right! You're last wife, Baabara the sheep? She went missing when she was only 25 years old!"
    chief "We never found the body... it was a cold case..."
    d "I thought his last wife was that actress? Betty Le Coo? That chick had legs for DAYS! What ever happened to her?"
    "(Nairda looks at Strudle and Strudle looks at him)"
    nun "It was a cold case."
    hubby "Nairda was helping to work on that case when he was fresh out of detective school... She was 26? 27 years old? Suddenly went missing..."
    hubby "Had a penguin husband... Was that Beaks?!?"
    "(At this point Beaks hears the commotion and puts together exactly what he had blurted out moments prior)"
    beaks "Well you see... I have very bad luck and... If you'd let me I can show you everything you need to know back in my house"
    "(Beaks starts to waddle slowly backwards towards his mansion)"
    nun "STOP RIGHT THERE!"
    "(Beaks flings around and makes a run for it...)"
    "(A run for his mansion...)"
    "(His mansion...)"
    "(on...)"
    "(a...)"
    "(HILL!)"
    chief "FREEZE!"
    "(The chief makes a run for Beaks, tackling him to the ground, and arresting him for the murder of Mrs Beaks,
    and as a suspected murderer in two other cold cases of murdered women under the age of 30 in their respected animal years.)"
    "(Once he was safely in the police car and out of view, Nairda went over to Olivia's body)"
    nun "You did amazingly, Olivia, it's safe to get up now"
    "(Olivia opens one eye slightly and whispers whiles still as still as the grave)"
    olive "Are his lackies still here?"
    nun "No no, it's just me, Strudle, and Molly Stone"
    olive "Thank the gods... My ears are killing me!"
    "(Olivia takes out her hair tie and stands up, dusting herself off, sighing a breath of relief)"
    "(Faking her own death with help from the police, means she'll be able to start a new identity)"
    "(Not that Beaks will be getting out of prison anytime soon.)"

    # Nairda tells the truth about seeing things, and the therapist helps with medication
    # The hands slowly disappear from existance
    scene emptygym
    "(Nairda tells his therapist all about 'the hands' and his flashes of the world looking plastic and full of giant doll house furniture)"
    drk "I'm happy you told me about this Nairda"
    nun "..."
    drk "There's been cases of this before, so we know how to treat it!"
    drk "It can return if you ever stop taking these..."
    "(Dr Krieger hands Nairda a prescription for 'handsbegoneapine')"
    drk "But the few patients I have prescribed this too said everything went back to normal on them, so I highly suggest trying them"
    drk "And we can have a few extra sessions over the next few weeks to see if they're working, and adjust the dosage as needed, and so on."
    "(Nairda is happy to take anything to make these 'hands' stop showing up in his daily life)"
    "(And to stop these unnerving flashes)"
    nun "Thank you, Dr Krieger."
    nun "See you on Wednesday for our usual session?"
    drk "I'm looking forward to it!"
    "(Nairda leaves the therapy office and Strudle drives him to the pharmacy to grab his new prescription)"
    "(As an extra treat, Strudle suggests fly pie for tea...)"
    "(Nairda would never turn down a fly pie...)"
    "(Everything is as it should be.)"

    # Ending line
    scene screenstart
    "(The End)"
    "(ENDING 1 of 4: You told the truth about seeing things and got help. You will no longer see the reality of the situation you are in.
    That you, and everyone you have ever loved, are toys being played with by an indie games dev a little too into crime TV shows.)"
    "(This is a good thing though, right? Ignorance is bliss! And those sudden flashes of reality were terribly unnerving so this really is for the best)"
    "(And hey! You solved the case! Beaks is arrested! Good job!)"
    return

label truthnotsolved_end:
    #"truth not solved"
    "(Molly refuses to help you)"
    "(You can't get her out of the Institute, as she would rather die than take what the orderlies offer her)"
    "(You only show up when you want something)"
    "(And she remembers how you treated her last time)"
    "(Nairda leaves empty handed, without the help of Molly Stone there is no way to prove Beaks is guilty)"

    # Nairda tells the truth about seeing things, and the therapist helps with medication
    # The hands slowly disappear from existance
    scene emptygym
    "(Nairda tells his therapist all about 'the hands' and his flashes of the world looking plastic and full of giant doll house furniture)"
    drk "I'm happy you told me about this Nairda"
    nun "..."
    drk "There's been cases of this before, so we know how to treat it!"
    drk "It can return if you ever stop taking these..."
    "(Dr Krieger hands Nairda a prescription for 'handsbegoneapine')"
    drk "But the few patients I have prescribed this too said everything went back to normal on them, so I highly suggest trying them"
    drk "And we can have a few extra sessions over the next few weeks to see if they're working, and adjust the dosage as needed, and so on."
    "(Nairda is happy to take anything to make these 'hands' stop showing up in his daily life)"
    "(And to stop these unnerving flashes)"
    nun "Thank you, Dr Krieger."
    nun "See you on Wednesday for our usual session?"
    drk "I'm looking forward to it!"
    "(Nairda leaves the therapy office and Strudle drives him to the pharmacy to grab his new prescription)"
    "(As an extra treat, Strudle suggests fly pie for tea...)"
    "(Nairda would never turn down a fly pie...)"
    "(Everything is as it should be.)"


    # 6 months later:
    # Beaks has a new wife, younger bird of some description
    # A woman went missing recently from her apartment, a rabbit called Olivia
    "(6 months later:)"
    "(The news shows the story of a missing person's case, a rabbit called Olivia from down town)"
    "(Her body was found with several botched plastic surgeries...)"
    "(Ear shortening, and foot webbing being only two of them...)"
    "(She was 20 years old...)"
    "(The news then switches to a happy story)"
    "(Of Beaks running for Mayor with his new wife, Tweetsy!)"
    "(A beautiful yellow canary whos modelling career is taking the world by storm!)"
    "(And Beaks' heart <3 )"
    "(The news wishes them a long and happy life)"
    "(He deserves it after the tragic death of his previous wife)"


# Ending line
    scene screenstart
    "(The End)"
    "(ENDING 2 of 4: You told the truth about seeing things and got help. You will no longer see the reality of the situation you are in.
    That you, and everyone you have ever loved, are toys being played with by an indie games dev a little too into crime TV shows.)"
    "(This is a good thing though, right? Ignorance is bliss! And those sudden flashes of reality were terribly unnerving so this really is for the best)"
    "(You didn't even solve the case... Beaks is free, and every several years when his current wife gets to the horrifyingly old age of....)"
    "(*cough* anything over 25...)"
    "(He'll have her killed, and remarry his newest mistress)"
    "(Rinse and repeat.)"
    "(Rinse and repeat.)"
    "(Rinse and repeat.)"
    return


label liesolved_end:
    # lie solved
    "(A few days have passed)"
    "(Everyone goes down the hill towards the place where Mrs Beaks was found)"
    molly "Ohhhh it's getting stronger! I think her name is... Olive tree? That can't be right..."
    "(Molly holds her head then points one finger towards the bottom of the hill)"
    molly "It's Olive under the tree!"
    "(Down the hill next to a tree, Olivia's body is barely visible, laying still.)"
    "(In an expensive dress, red marks around her ears from being painfully tied back.)"
    "(Beaks sees her too, and runs to her side screaming in agony)"
    beaks "Noooo! It can't be!!!"
    "(The chief stops him from coming into close contact with the body)"
    beaks "Get off of me! I loved Olivia! I even got rid of my third wife so I could be with her!"
    chief "Wait a minute..."
    "(Beaks doesn't even realise what he's saying before the Chief remembers other details)"
    chief "Third...? That's right! You're last wife, Baabara the sheep? She went missing when she was only 25 years old!"
    chief "We never found the body... it was a cold case..."
    d "I thought his last wife was that actress? Betty Le Coo? That chick had legs for DAYS! What ever happened to her?"
    "(Nairda looks at Strudle and Strudle looks at him)"
    nun "It was a cold case."
    hubby "Nairda was helping to work on that case when he was fresh out of detective school... She was 26? 27 years old? Suddenly went missing..."
    hubby "Had a penguin husband... Was that Beaks?!?"
    "(At this point Beaks hears the commotion and puts together exactly what he had blurted out moments prior)"
    beaks "Well you see... I have very bad luck and... If you'd let me I can show you everything you need to know back in my house"
    "(Beaks starts to waddle slowly backwards towards his mansion)"
    nun "STOP RIGHT THERE!"
    "(Beaks flings around and makes a run for it...)"
    "(A run for his mansion...)"
    "(His mansion...)"
    "(on...)"
    "(a...)"
    "(HILL!)"
    chief "FREEZE!"
    "(The chief makes a run for Beaks, tackling him to the ground, and arresting him for the murder of Mrs Beaks,
    and as a suspected murderer in two other cold cases of murdered women under the age of 30 in their respected animal years.)"
    "(Once he was safely in the police car and out of view, Nairda went over to Olivia's body)"
    nun "You did amazingly, Olivia, it's safe to get up now"
    "(Olivia opens one eye slightly and whispers whiles still as still as the grave)"
    olive "Are his lackies still here?"
    nun "No no, it's just me, Strudle, and Molly Stone"
    olive "Thank the gods... My ears are killing me!"
    "(Olivia takes out her hair tie and stands up, dusting herself off, sighing a breath of relief)"
    "(Faking her own death with help from the police, means she'll be able to start a new identity)"
    "(Not that Beaks will be getting out of prison anytime soon.)"


    # Scene where Nairda and Strudle are home and Strudle asks if Nairda is feeling ok as he's been weird lately
    # Nairda reassures Strudle he's ok, but he can see the hand holding Strudle whiles they're talking
    # He wants to live in blissful ignorance
    scene apartmentdoor
    hubby "Hey, Nairda?"
    nun "Hmm?"
    hubby "Are you sure you've been feeling ok?"
    "(Nairda watches as 'the hands' move Strudle around the apartment)"
    nun "Never been better! Why do you ask?"
    "(Strudle slides across the plastic floor as his stiff body smacks a table and hovers around a fake kitchen sink)"
    hubby "I feel like you've changed recently... You seem to be more anxious recently."
    hubby "You've been whimpering in your sleep..."
    hubby "What are the hands?"
    "(Nairda composes himself as best he can, walks over to his plastic husband, holds that solid resin hand and smiles)"
    nun "I have no idea what you're talking about. I must have been having a bad dream."
    nun "I love you, Strudle."
    "(Strudle smiles)"
    hubby "I love you too, Nairda!"

    # Ending line
    scene screenstart
    "(The End)"
    "(ENDING 3 of 4: You lied about seeing things and didn't get help. Now you will forever see the reality of the situation you are in.
    That you, and everyone you have ever loved, are toys being played with by an indie games dev a little too into crime TV shows.)"
    "(but hey! At least you solved the case! Beaks is arrested... so good for you!)"
    "(For you personally, seeing 'the hands' and the sudden flashes in your mind of actually being inside of giant plastic doll houses is
    terribly unnerving and out of your control, but you'll probably get used to it eventually...)"
    "(Probably...)"
    return

label lienotsolved_end:
    # "lied and not solved"
    "(Molly refuses to help you)"
    "(You can't get her out of the Institute, as she would rather die than take what the orderlies offer her)"
    "(You only show up when you want something)"
    "(And she remembers how you treated her last time)"
    "(Nairda leaves empty handed, without the help of Molly Stone there is no way to prove Beaks is guilty)"
# - Lies about visions && not solved the case
# - You lie out of fear and don't take meds to stop it & you can see you're in a simulation type situation for the rest of
    scene apartmentdoor
    hubby "Hey, Nairda?"
    nun "Hmm?"
    hubby "Are you sure you've been feeling ok?"
    "(Nairda watches as 'the hands' move Strudle around the apartment)"
    nun "Never been better! Why do you ask?"
    "(Strudle slides across the plastic floor as his stiff body smacks a table and hovers around a fake kitchen sink)"
    hubby "I feel like you've changed recently... You seem to be more anxious recently."
    hubby "You've been whimpering in your sleep..."
    hubby "What are the hands?"
    "(Nairda composes himself as best he can, walks over to his plastic husband, holds that solid resin hand and smiles)"
    nun "I have no idea what you're talking about. I must have been having a bad dream."
    nun "I love you, Strudle."
    "(Strudle smiles)"
    hubby "I love you too, Nairda!"

    # 6 months later:
    # Beaks has a new wife, younger bird of some description
    # A woman went missing recently from her apartment, a rabbit called Olivia
    "(6 months later:)"
    "(The news shows the story of a missing person's case, a rabbit called Olivia from down town)"
    "(Her body was found with several botched plastic surgeries...)"
    "(Ear shortening, and foot webbing being only two of them...)"
    "(She was 20 years old...)"
    "(The news then switches to a happy story)"
    "(Of Beaks running for Mayor with his new wife, Tweetsy!)"
    "(A beautiful yellow canary whos modelling career is taking the world by storm!)"
    "(And Beaks' heart <3 )"
    "(The news wishes them a long and happy life)"
    "(He deserves it after the tragic death of his previous wife)"

# Ending line
    scene screenstart
    "(The End)"
    "(ENDING 4 of 4: You lied about seeing things and didn't get help. Now you will forever see the reality of the situation you are in.
    That you, and everyone you have ever loved, are toys being played with by an indie games dev a little too into crime TV shows.)"
    "(You didn't even solve the case... Beaks is free, and every several years when his current wife gets to the horrifyingly old age of....)"
    "(*cough* anything over 25...)"
    "(He'll have her killed, and remarry his newest mistress)"
    "(Rinse and repeat.)"
    "(Rinse and repeat.)"
    "(Rinse and repeat.)"
    "(For you personally, seeing 'the hands' and the sudden flashes in your mind of actually being inside of giant plastic doll houses is
    terribly unnerving and out of your control, but you'll probably get used to it eventually...)"
    "(Probably...)"
    # This ends the game.
    return
