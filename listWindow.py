# importing tkinter module
from tkinter import *
from tkinter.ttk import *

class listWindowClass:
    def __init__(self, master):
        self.master = master

        # Toplevel object which will
        # be treated as a new window
        self.listWindow = Toplevel(self.master.root)

        # sets the title of the
        # Toplevel widget
        self.listWindow.title("List Window")

        # sets the geometry of toplevel
        self.listWindow.geometry("200x200")

        # A Label widget to show in toplevel
        Label(self.listWindow,
              text="Liste over indbetalinger").pack()
