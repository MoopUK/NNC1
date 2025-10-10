# Carbon copy of NNC0 characters.rpy, with edits/extras.
# Using the same character models/images in every Nairda Nun game,
# so it makes sense not to redraw them all for the second game/this one.

# Script for all characters.
# Defaulting player as answering correctly in the investigation to 0,
# Find all the clues to win the case
default correct = 0
# How to put yes or no answer into game:
#            $ correct = correct +1  #GOOD choice!
#            play sound "audio/yes.mp3"

#            $ correct = correct -1  #BAD choice!
#            play sound "audio/no.mp3"

# Here you can give the info and colour of name tag for each character

# Narrator / The Game Developer (fourth-wall breaking character)
define GameDev = Character("Game Dev")

# Main Character, Nairda Nun
define nun = Character("Nairda Nun", color="#99C68E") #nun, frog green

# Husband of Nun - placeholder until physical character model received for editing
define hubby = Character("Strudle", color="#FF0000")#Red

# Late Police Detective Partner of Nun
define np = Character("Nun's Partner", color="#99C55E")

# Apartment neighbours
define t = Character("Tony", color="#FF0000")#Red
define e = Character("Ezekiel", color="#FFE4E1")#MistRose

# Misc characters
define a = Character("Alice", color="#33FFCC")#light blue # Museum Owner?
define d = Character("Detective", color="#FFCC33")#yellow # Angry police detective
define mor = Character("Mortician", color="#800000")#maroon # Mortician
define r = Character("Receptionist", color="AABBCC")
define drk = Character("Dr Krieger", color="FFCCAA")
define ch = Character("Chief", color="FFFFFF")

# images for characters and facial expressions
# General expressions:
# - neutral face
# - sad/crying
# - happy
# - angry
# - confused
# - embarrassed/shy

# Nun (Main Character)
image nun n:
    "nunneutral"
    zoom 0.5
image nun sad:
    "nunsad"
    zoom 0.5
image nun happy:
    "nunhappy"
    zoom 0.5
image nun angry:
    "nunangry"
    zoom 0.5
image nun confused:
    "nunconfused"
    zoom 0.5
image nun shy:
    "nunshy"
    zoom 0.5

# Strudle Nun (Nairda's husband) PLACEHOLDERS REPLACEMENT NEEDED
image snun n:
    "snunneutral"
    zoom 0.2
image snun sad:
    "snunsad"
    zoom 0.2
image snun happy:
    "snunhappy"
    zoom 0.2
image snun angry:
    "snunangry"
    zoom 0.2
image snun confused:
    "snunconfused"
    zoom 0.2
image snun shy:
    "snunshy"
    zoom 0.2

# Dr Krieger (Therapist) PLACEHOLDERS REPLACEMENT NEEDED
image drk n:
    "drkn"
    zoom 0.5
image drk sad:
    "drksad"
    zoom 0.5
image drk happy:
    "drkhappy"
    zoom 0.5
image drk angry:
    "drkangry"
    zoom 0.5
image drk confused:
    "drkconfused"
    zoom 0.5
image drk shy:
    "drkshy"
    zoom 0.5

# Therapy Receptionist
image rec n:
    "receptionistn"
    zoom 0.5
image rec sad:
    "receptionistsad"
    zoom 0.5
image rec happy:
    "receptionisthappy"
    zoom 0.5
image rec angry:
    "receptionistangry"
    zoom 0.5
image rec confused:
    "receptionistconfused"
    zoom 0.5
image rec shy:
    "receptionistshy"
    zoom 0.5

# Tony (apartment neighbour)
image tony n:
    "tonyneutral"
    zoom 0.5
image tony sad:
    "tonysad"
    zoom 0.5
image tony happy: #NEEDED
    "tonyhappy"
    zoom 0.5
image tony angry:
    "tonyangry"
    zoom 0.5
image tony confused: #NEEDED
    "tonyconfused"
    zoom 0.5
image tony shy:
    "tonyshy"
    zoom 0.5

# Ezekiel (Tony's nemesis and vice versa at apartments) PLACEHOLDERS REPLACEMENTS NEEDED
image ez n:
    "tonyneutral"
    zoom 0.5
image ez sad:
    "nunsad"
    zoom 0.5
image ez happy:
    "nunhappy"
    zoom 0.5
image ez angry:
    "nunangry"
    zoom 0.5
image ez confused:
    "nunneutral"
    zoom 0.5
image ez shy:
    "nunshy"
    zoom 0.5

# Dr Wolfe (Mortician)
image drwolfe n:
    "drwolfeneutral"
    zoom 0.5
image drwolfe sad:
    "drwolfesad"
    zoom 0.5
image drwolfe happy:
    "drwolfehappy"
    zoom 0.5
image drwolfe angry:
    "drwolfeangry"
    zoom 0.5
image drwolfe confused:
    "drwolfeconfused"
    zoom 0.5
image drwolfe shy:
    "drwolfeshy"
    zoom 0.5

# Chief (Police chief) placeholder, might be entirely unneeded, might not show chief
image chief n:
    "placeholder"
    zoom 0.5
image chief sad:
    "placeholder"
    zoom 0.5
image chief happy:
    "placeholder"
    zoom 0.5
image chief angry:
    "placeholder"
    zoom 0.5
image chief confused:
    "placeholder"
    zoom 0.5
image chief shy:
    "placeholder"
    zoom 0.5

# Harry Hare (arrogant police detective) PLACEHOLDER NEEDS REPLACING
image hare n:
    "haren"
    zoom 0.5
image hare sad:
    "haresad"
    zoom 0.5
image hare happy:
    "harehappy"
    zoom 0.5
image hare angry:
    "hareangry"
    zoom 0.5
image hare confused:
    "hareneutral"
    zoom 0.5
image hare shy:
    "hareshy"
    zoom 0.5

# Bruce (Nairda's nemesis at therapy) placeholder, might be entirely unneeded, might not show Bruce
image bruce n:
    "nunneutral"
    zoom 0.5
image bruce sad:
    "nunsad"
    zoom 0.5
image bruce happy:
    "nunhappy"
    zoom 0.5
image bruce angry:
    "nunangry"
    zoom 0.5
image bruce confused:
    "nunneutral"
    zoom 0.5
image bruce shy:
    "nunshy"
    zoom 0.5

# MISC ITEMS - All game scenes are in 1280 x 720, resize accordingly
image gun gun:
    "gun"
    zoom 0.5

image opencab opencab:
    "opencabinet"
    zoom 0.5

image boot boot:
    "boot"
    zoom 0.5

image doorlock doorlock:
    "doorlock"
    zoom 0.65

image mace mace:
    "mace"
    zoom 0.6

image body body:
    "body"
