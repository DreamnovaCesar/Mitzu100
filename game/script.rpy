# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Eileen = Character("Eileen")
define Dave = Character("Dave")

image picture_1 = im.Scale("Background_1.jpg", 1920, 1080)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show picture_1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    Eileen "Hi!, how are you?"

    menu:

        "I am fine, thank you":
            call Good
        "My day was not too good":
            call Bad

    return

label Good:

    Eileen  "I love to hear that"

    return

label Bad:

    Eileen "Oh sorry, what happend?"

    return