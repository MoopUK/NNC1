# The script of the game goes in this file.

# Movie / Cutscenes (where needed)
image example movie = Movie(play="examplemovie2.webm")
init:
    image movie = Movie(size=(1280, 720), xalign=0.5, yalign=0.5)

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show nun happy

    # These display lines of dialogue.

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
