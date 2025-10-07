# Game by: Moop Open-source Games
# Nairda Nun: Chapter 1 (*The Halloween Episode* - For LGBTQ+ Horror Jam 2025)

# Game summary: Nairda Nun, the private detective.
# Based in the 90's, general crime type genre, all characters are animal-based,
# proportions and style similar to Sylvanian Families.

# -----------------------------------------------------------------------------
# Game Contents:

# SCENE 00 - Introduction
# 1. Previously on Nairda Nun:
# - Murder and Giant Opal stolen from the Museum of Frogs and Fancies.
# - It was the care takers, using a mace, due to bullet proof glass, etc.

# 2. Discuss the silly world lore again:
# - Such as hills being a crime zone as old laws say you can't
# arrest people standing on hills.
# - How only criminals wear shoes/footware because it conceals their
# foot prints and thus their species.

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
    "No real animals were dressed in tiny suits and forced to solve crimes in the making of this videogame."
    # PHOTO OF THE MODELS IN A CRIME SCENE SETTING
    scene screenstart1
    "Only fake ones."
    scene apartmenthalls

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


    # This ends the game.

    return
