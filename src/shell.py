#   --- Imports ---
from tennisGame import *
from lang import *

#   --- Local Constants ---
TXT_WIDTH = 50

#   --- Class ---
class ShellInterface:
    def __init__ (self):
        """
        Class constructor
        """
        self.game = TennisGame()
        self.lang = Lang().current

        self.printAligned(self.lang["WELCOME"])
        while(not self.game.done):
            self.displayScore()
            self.askScore()
        input(self.lang["EXIT"])

    def printAligned(self, text, endText="\n"):
        """
        Adding space in order to align
        Args: (str) text     - original text
              (str) endText  - endline text
        """
        res = ""
        toBeAdded = (TXT_WIDTH - len(text)) // 2 #Euclidian division
        for i in range(toBeAdded):
            res += " "
        res += text
        for i in range(toBeAdded):
            res += " "
        print(res, end=endText)

    def displayScore(self):
        """
        Displaying current score
        """
        score0 = self.game.getPoints(0)
        score1 = self.game.getPoints(1)
        self.printAligned(self.lang["PLAYER"]+" 0 - "+self.lang["PLAYER"]+" 1")
        for i in range(2):
            self.printAligned(score0[i]+" - "+score1[i])

    def askScore(self):
        """
        Asking who has scored
        """
        notCorrect = True
        while(notCorrect):
            self.printAligned(self.lang["WHO"]+" ", "")
            player = input()
            if player in ["0","1"]:
                notCorrect = False
            else:
                self.printAligned(self.lang["NOTCORR"])

        self.process(int(player))

    def process(self, player):
        """
        Processing score
        Args: (int) player - player identifier (0 or 1)
        """
        self.game.incr(player)
        if(self.game.done):
            finalText = self.lang["WINNER"]+" "
            finalText += self.lang["PLAYER"]+" "
            finalText += str(player)
            self.printAligned(finalText)

if __name__ == "__main__":
    ShellInterface()
