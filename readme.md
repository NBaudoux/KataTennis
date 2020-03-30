# Purpose
This project is about implementing a scoreboard for a tennis game.
There exists two versions of this scoreboard: A command line interface, and a graphical interface

## Description of the rules according Wikipedia ( http://en.wikipedia.org/wiki/Tennis#Scoring ):

1. A game is won by the first player to have won at least four points in total and at least two points more than the opponent.

2. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as “love”, “fifteen”, “thirty”, and “forty” respectively.

3. If at least three points have been scored by each player, and the scores are equal, the score is “deuce”.

4. If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is “advantage” for the player in the lead.

# How to execute
For windows: .exe files have been created and are available in folder `dist`
Otherwise: All source files are in `src`. If python3 has been installed first, those can be executed using commands:
* `python3 shell.py` for the command line interface
* `python3 GUI.py` for the graphical interface

# How to use
## Command line interface
1. Type 0 or 1 depending on which player has scored a point
2. Press Enter
3. When the game came to an end, press Enter to close the program

## Graphical interface
1. Press the + button corresponding to the player which has scored a point
2. The program notifies you if the game comes to an end and then resets the scoreboard. You may then begin a new game.
3. Click the upper right cross to close the program
