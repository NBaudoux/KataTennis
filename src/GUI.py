#   --- Imports ---
import sys
import os
source = os.path.dirname(__file__) + "\guiObj"
sys.path.append(source)

from tennisGame import *
from lang import *

from tkinter import *
from tkinter.messagebox import showerror, showinfo
from button import *

#   --- Local constants ---
FONT = ('Arial', 20)

#   --- GUI Class ---
class GUI:
    def __init__(self):
        """
        GUI class constructor
        """
        self.lang = Lang().current
        self.game = TennisGame()
        #GUI initialisation
        self.root=Tk(self.lang["KATATEN"])
        self.root.title("")
        self.root.minsize(200,200)

        self.displayTopFrame()

    def displayTopFrame(self):
        """
        Display top frame
        """
        self.topFrame = Frame(self.root)
        self.topFrame.grid(row=0, sticky=N+S+W+E)

        self.frames = []
        self.labels = []
        self.labelPoints = []
        self.labelNames  = []
        self.incrButtons = []
        for i in range(2):
            self.frames.append(Frame(self.topFrame))
            self.frames[i].grid(row=0,column=i)
            score = self.game.getPoints(i)
            self.labels.append(Label(self.frames[i], text=self.lang["PLAYER"]+" "+str(i), font=FONT))
            self.labels[i].grid(row=0)
            self.labelPoints.append(Label(self.frames[i], text=str(score[0]), font=FONT))
            self.labelPoints[i].grid(row=1)
            self.labelNames.append(Label(self.frames[i], text=str(score[1]), font=FONT))
            self.labelNames[i].grid(row=2)
        #Score button
        self.incrButtons.append(ImgButton(self.frames[0], "logo/add.png", lambda: self.process(0), 1.5))
        self.incrButtons[0].pos(3,0)
        self.incrButtons[0].hovering(self.lang["SCORE"])
        self.incrButtons.append(ImgButton(self.frames[1], "logo/add.png", lambda: self.process(1), 1.5))
        self.incrButtons[1].pos(3,0)
        self.incrButtons[1].hovering(self.lang["SCORE"])

    def update(self):
        """
        Update information displayed
        """
        for i in range(2):
            score = self.game.getPoints(i)
            self.labelPoints[i].config(text=str(score[0]))
            self.labelNames[i].config(text=str(score[1]))

    def process(self, player):
        """
        Processing score
        Args: (int) player - player identifier (0 or 1)
        """
        self.game.incr(player)
        if(self.game.gameWon(player)):
            finalText = self.lang["WINNER"]+" "
            finalText += self.lang["PLAYER"]+" "
            finalText += str(player)
            showinfo(self.lang["WON"],finalText)
            self.topFrame.destroy()
            self.game.reset()
            self.displayTopFrame()
        else:
            self.update()

if __name__ == "__main__":
    main=GUI()
    main.root.mainloop()
