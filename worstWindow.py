# importing tkinter module
from tkinter import *
from tkinter.ttk import *

class worstWindowClass:
    def __init__(self, master):
        self.master = master

        # Toplevel object which will
        # be treated as a new window
        self.worstWindow = Toplevel(self.master.root)

        # sets the title of the
        # Toplevel widget
        self.worstWindow.title("Bottom 3")

        # sets the geometry of toplevel
        self.worstWindow.geometry("200x200")

        # A Label widget to show in toplevel
        Label(self.worstWindow,
              text="De værste betalere").pack()
