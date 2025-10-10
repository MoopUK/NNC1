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

## Game Story draft / thoughts
# Wanting a story where there is horror dream world alongside real life
# going to a suspects house Nun is attacked and something happens to break
# his fourth wall, realising he's a toy being controlled by a human.

# SCENE 01 - Nairda Nun normal day
# 1. Nun having a normal day of work
# 2. An attack that'll cause the start of fourth wall breaking. He insults
# a Psychic, known as a "quack", but she's actually real. She curses Nun
# with the ability to break the fourth wall/see reality (they're all toys),
#

# SCENE 02 -
# 1.
# 2.

# SCENE 03 -
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
    # Background image/s
    scene screenstart
    "Any similarities to real events are purely coincidental."
    # can't really put this bit as it's kind of the entire storyline for this horror game version?
    "No real animals were dressed in tiny suits and forced to solve crimes in the making of this videogame."
    # PHOTO OF THE MODELS IN A CRIME SCENE SETTING
    scene screenstart1
    "Only fake ones."

    scene classroom

# QUESTION: Do you want a lore refresher?
    "Would you like a quick refresher on the world lore?"
    menu:
        "Sure!":
            jump Lore
        "No thanks, let's just start the game":
            jump GameStart

# SCENE: Lore
label Lore:
    scene apartmenthalls
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
    scene apartmenthalls
    show tony confused
    t "I'm not sure why they need to know this? It's common knowledge isn't it?"
    "(Tony see's the cameraman pointing to the teleprompter and mouthing to please just read from that)"
    scene apartmenthalls
    show tony n
    t "Ah, ok! and last but not least you should never..."
    play sound "audio/toiletnoise.mp3"
    "(a toilet flushes above)"
    scene apartmenthalls
    show tony angry
    t "Dammit Ezekiel! I'm trying to!"
    t "I'm sorry everyone, I have to stop the water!"
    scene apartmenthalls
    "(Tony runs back into his apartment, you hear a broom hitting on the ceiling
    and a faint 'Fuck you, Tony!' coming from above)"
    "(*sigh* I don't think he's coming back, let's just start the game...)"
    jump GameStart

# SCENE: Game Start
label GameStart:
    scene screenstart1
    "(Previously on Nairda Nun:)"
    "(There was a murder robbery at the Museum of Frogs and Fancies.)"
    "(It was the care takers, killing a guard, using a mace to open the opal case,
    and stealing it! Nairda solved the case and they were caught before they made a run for the hills...)"
    scene apartmentlongshot
    "(And now the story continues...)"

    show nun happy
    nun "You've created a new Ren'Py game."
    play movie "officevideo1.webm" noloop
    nun "........"
    nun "moop moop"
    nun "moop again"

#ENDINGS: This checks if Nairda gets the good ending or the bad ending
#    label which_end:
#        if correct >= 3:
#            jump good_end
#        elif correct < 3:
#            jump bad_end

    # This ends the game.

    return
