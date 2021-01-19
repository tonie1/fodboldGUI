# importing tkinter module
from tkinter import *
from tkinter.ttk import *

class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("200x200")

        Label(self.listWindow, text="Liste over indbetalinger")
        Label.pack()
