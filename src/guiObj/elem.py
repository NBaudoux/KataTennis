from toolTip import *

class Elem:
    def __init__(self):
        """
        Generic Constructor
        """
        self.elem =""

    def pos(self, row, col, pos="N"):
        """
        Position on grid
        """
        self.elem.grid(row=row, column=col, sticky=pos)

    def hovering(self, msg):
        """
        Enable message on hovering
        """
        self.msg = msg
        self.toolTip = ToolTip(self.elem)
        self.elem.bind('<Enter>', self.enter)
        self.elem.bind('<Leave>', self.leave)

    def enter(self, event):
        self.toolTip.showtip(self.msg)
    def leave(self, event):
        self.toolTip.hidetip()
