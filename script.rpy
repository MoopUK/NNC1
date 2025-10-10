# Game by: Moop Open-source Games
# Nairda Nun: Chapter 1 (*The Halloween Episode* - For LGBTQ+ Horror Jam 2025)

# Game summary: Nairda Nun, the private detective.
# Based in the 90's, general crime type genre, all characters are animal-based,
# proportions and style similar to Sylvanian Families.

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

## To Do List / Needs
# - Arm photo and edit, opaque, to use for showing a human is holding the characters
# at random intervals.
# - Audio of human in "real world" for different immersion / fourth wall
# breaking.


# SCENE 01 - Nairda Nun normal day
# 1. Nun having a normal day of work
# 2. An attack that'll cause the start of fourth wall breaking

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
image example movie = Movie(play="examplemovie2.webm") # Placeholder of my cat
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

# CRIME SCENE: First choice of investigation
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
    t "Am I on?"
    t "Welcome to..."
    t "Lore!"
    t "In our world, you don't wear shoes. Shoes hide your footprints, and
    only criminals would purposefully hide their footprints!"
    t "Have you ever heard of someone running for the hills?"
    t "Well it comes from an old law that has never been rectified!"
    t "If you stand on a hill, you're above the law, and thus, you can not be
    charged with any crime whiles on that hill."
    t "Crazy I know!"
    t "And lastly..."
    play sound "audio/toiletnoise.mp3"
    "(a toilet flushes above)"
    scene apartmenthalls
    show tony angry
    t "Dammit Ezekiel! I'm trying to!"
    t "I'm sorry everyone, I have to stop the water!"
    scene apartmenthalls
    "(Tony runs back into his apartment, you hear a broom hitting on the ceiling
    and a faint 'Fuck you, Tony!' coming from above)"
    GameDev "(I don't think he's coming back, let's just start the game...)"
    jump GameStart

# SCENE: Game Start
label GameStart:
    scene apartmentlongshot
    # Character sprites (name, expression)
    show nun happy
    # These display lines of dialogue (name "dialogue")
    nun "You've created a new Ren'Py game."

    show example movie

    nun "Once you add a story, pictures, and music, you can release it to the world!"
    hide example
    nun "moop moop"

    nun "no loop film but it'll skip text in background whiles we are watching this"

    play movie "examplemovie2.webm" noloop

    nun "moop again"
    nun "background text working"
    nun "background text working2"
    nun "again background text working3"


#ENDINGS: This checks if Nairda gets the good ending or the bad ending
#    label which_end:
#        if correct >= 3:
#            jump good_end
#        elif correct < 3:
#            jump bad_end

    # This ends the game.

    return
