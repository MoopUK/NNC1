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
# is sad and wanting any information about his wife.

# SCENE 02 - Molly Stone finds the wife / curses Nun
# 1. Molly Stone wakes up at murder scene with the dead wife there

# 2. Molly Stone doesn't like helping the police even if she knows where something is due
# to being seen as a "quack" and also being arrested and convicted of some crimes, due
# to knowing so much about the crime that only the perp would have known those details / etc.

# 3. An attack that'll cause the start of fourth wall breaking. He insults
# a Psychic, known as a "quack", but she's actually real. She curses Nun
# with the ability to break the fourth wall/see reality (they're all toys).

# 4. Molly Stone gets into her car to leave and adjusts her seat when she did, as if
# she wasn't driving it the last time.

# SCENE 04 - Funeral
# 1. Wife funeral, Nun has to go wash his hands and finds the husband has been
# throwing all of his wife's stuff into boxes to bin. When husband says Nun would understand
# wanting to have a fresh start asap after tradjedy, Nun mentions when his partner died he never threw anything
# out of theirs in the office.

# 2. Nun keeps seeing a weird ghost-like arm every so often holding the other characters in place

# 3.

# SCENE 05 -
# 1.

# 2.

# 3...

# SCENE 06 -
# 1.

# 2.

# 3...

# Scene XX - Ending/s
# 1. Win/Lose ending scene
# Game End.

# -----------------------------------------------------------------------------

# Movie / Cutscenes (where needed)
image officevideo1 movie = Movie(play="officevideo1.webm") # Placeholder of my cat
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
    "(*sigh* I don't think he's coming back, let's just start the game...)"
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
    beaks "My wife"
    beaks "If you hear this..."
    beaks "Don't give up!"
    # NOISE NEEDED crowds rabble rabble
    "(The reporters go wild, taking photos and shouting questions whiles Beaks leaves the stage)"
    scene messhall
    show nun sad at right
    show snun sad at left
    nun "That poor man"
    hubby "I know, I'd be besides myself if you ever went missing"
    "(Nairda goes to Beaks to offer his condolenses)"
    scene messhall
    show nun n at right
    show beaks n at left
    nun "Anything I can do, I'm available 24/7!"
    beaks "Ah, you must be Nairda Nun. I've heard great things about you."
    beaks "I'm sure you'll find my wife in no time at all"
    scene messhall
    show nun shy at right
    show beaks n at left
    nun "Thank you, sir."
    show hare happy
    d "Don't worry sir Beaks!"
    "(Detective Harry Hair nudges Nairda back and takes over the scene)"
    scene messhall
    show beaks n at left
    show hare happy at right
    d "We've got everything covered! We're searching the whole town! I guarantee she'll be home by tomorrow!"

    scene messhall
    "(Nairda goes back to his husband)"
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
    "(With the conference coming to a close)"
    scene stairs
    "(Nairda and Strudle grab a take away and head on home for the evening)"

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
    molly "Mrs Beaks...?"

    scene darkness5
    play sound "audio/thunderboom.mp3"
    play sound "audio/scream1.mp3"
    molly "MRS BEAKS!!?!!"

    scene morning3
    play sound "audio/scream2.mp3"
    "(Molly's scream echoes out in the distance)"



    scene morning3
    nun "I came here as fast as I could!"
    hubby "We heard Mrs Beaks had been found?"
    chief "Her body was discovered by Molly Stone at 7.43am this morning"
    "(Everyone looks around in confusion)"
    nun "I thought Molly Stone was in an institution?"
    chief "So did we... It seems she broke out and come across the body a mere 400 metres from Beak Mansion"
    chief "She claims she doesn't know how she got here, and was in histerics"
    chief "The doctors from the institution came shortly after to pick her up"
    "(An uneasy feeling circles in the air)"
    hubby "You don't think that...?"
    chief "I'm not sure what to think yet, but I had to break the news to Mr Beaks about his wife"
    chief "He said not to move the body until he got there"
    chief "Something about not believing it until he sees it for himself"




    play movie "officevideo1.webm" noloop
    nun "moop"

# Cursing Nun
    molly "Hocus pocus diddly dee"
    molly "You'll now see... the reality!"

#ENDINGS: This checks if Nairda gets the good ending or the bad ending
#    label which_end:
#        if correct >= 3:
#            jump good_end
#        elif correct < 3:
#            jump bad_end

    # This ends the game.

    return
