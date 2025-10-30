# Characters premade from Chapter 00, and others added for this story
# Script for all characters.

# Defaulting player as answering correctly in the investigation to 0,
# Find all the clues to win the case
default truth = 0
default solved = 0

# Character List

# Narrator / The Game Developer (fourth-wall breaking character)
define GameDev = Character("Game Dev")

# Main Character, Nairda Nun
define nun = Character("Nairda Nun", color="#99C68E") #nun, frog green

# Main Characters, Beaks (man with missing wife)
define beaks = Character("Beaks", color="FFFF00")

# Side Character, Beaks Ex-Mistress
define olive = Character("Olivia", color="808000") # Olive colour

# Main Characters, Molly Stone (Psychic)
define molly = Character("Molly Stone", color="FF69B4")

# Side Character, Institute nurse
define nurse = Character("Institute Nurse", color="49535A") # Dark grey colour

# Main Character, Husband of Nun
define hubby = Character("Strudle", color="#FF0000")#Red

# Sice Character, Fry the Pizza Guy
define fry = Character("Fry", color="#DBA87F") #Pizza crust colour

# Apartment neighbours
define tony = Character("Tony", color="#FF0000")#Red

# Misc characters
define d = Character("Detective Harry Hare", color="#FFCC33")#yellow # Angry police detective
define mor = Character("Mortician", color="#800000")#maroon # Mortician
define drk = Character("Dr Krieger", color="FFCCAA") # Psychologist
define chief = Character("Chief", color="135DD8") # Police blue, chief of police

# images for characters and facial expressions
# General expressions:
# - neutral face
# - sad/crying
# - happy
# - angry
# - confused
# - embarrassed/shy
# EXTRA: For fourth-wall breaking, some models will have hand variants

# Hand (fourth wall breaker)
image hand r:
    "righthand1"
    zoom 0.5
image tester hand:
    "testerhand"
    zoom 0.5

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
# EXTRA HANDS
image nun hand1:
    "nunhand40percent"

# Olivia
image olive n:
    "oliven"
    zoom 0.5
image olive sad:
    "olivesad"
    zoom 0.5
image olive happy:
    "olivehappy"
    zoom 0.5
image olive angry:
    "oliveangry"
    zoom 0.5
image olive confused:
    "oliveconfused"
    zoom 0.5
image olive shy:
    "oliveshy"
    zoom 0.5

# Beaks (man with missing wife)
image beaks n:
    "beaks"
    zoom 0.5
image beaks truesad:
    "beakstruesad "
    zoom 0.5
image beaks sad:
    "beakssad "
    zoom 0.5
image beaks happy:
    "beakshappy"
    zoom 0.5
image beaks angry:
    "beaksangry"
    zoom 0.5
image beaks confused:
    "beaksconfused"
    zoom 0.5
image beaks shy:
    "beaksshy"
    zoom 0.5

# Molly Stone (psychic)
image molly n:
    "mollyn"
    zoom 0.5
image molly sad:
    "mollysad"
    zoom 0.5
image molly happy:
    "mollystone"
    zoom 0.5
image molly angry:
    "mollyangry"
    zoom 0.5
image molly confused:
    "mollyconfused"
    zoom 0.5
image molly shy:
    "mollyshy"
    zoom 0.5

# Institute Nurse (only need neutral face)
image nurse n:
    "nursen"
    zoom 0.5

# Strudle Nun (Nairda's husband)
image snun n:
    "snunneutral"
    zoom 0.5
image snun sad:
    "snunsad"
    zoom 0.5
image snun happy:
    "snunhappy"
    zoom 0.5
image snun angry:
    "snunangry"
    zoom 0.5
image snun confused:
    "snunconfused"
    zoom 0.5
image snun shy:
    "snunshy"
    zoom 0.5

# EXTRA HANDS
image snun hand1:
    "snunhandtest"
    zoom 0.8

# Dr Krieger (Therapist)
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

# Tony (apartment neighbour)
image tony n:
    "tonyneutral"
    zoom 0.5
image tony sad:
    "tonysad"
    zoom 0.5
image tony happy:
    "tonyhappy"
    zoom 0.5
image tony angry:
    "tonyangry"
    zoom 0.5
image tony confused:
    "tonyconfused"
    zoom 0.5
image tony shy:
    "tonyshy"
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

# Chief (Police chief)
image chief n:
    "chiefn"
    zoom 0.5
image chief sad:
    "chiefsad"
    zoom 0.5
image chief happy:
    "chiefhappy"
    zoom 0.5
image chief angry:
    "chiefangry"
    zoom 0.5
image chief confused:
    "chiefconfused"
    zoom 0.5
image chief shy:
    "chiefshy"
    zoom 0.5

# Harry Hare (arrogant police detective)
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

# Fry (Pizza guy)
image fry n:
    "fryn"
    zoom 0.5
image fry sad:
    "frysad"
    zoom 0.5
image fry happy:
    "fryhappy"
    zoom 0.5
image fry angry:
    "fryangry"
    zoom 0.5
image fry confused:
    "fryconfused"
    zoom 0.5
image fry shy:
    "fryshy"
    zoom 0.5

# MISC ITEMS - All game scenes are in 1280 x 720, resize accordingly
image boot boot:
    "boot"
    zoom 0.5
image news news:
    "news"
    zoom 0.7

image stalking1:
    "stalking1"
    zoom 0.7
image stalking2:
    "stalking2"
    zoom 0.7
