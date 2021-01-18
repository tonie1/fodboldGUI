# importing tkinter module
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class payWindowClass:

    def __init__(self, master):
        self.master = master

        # Toplevel object which will
        # be treated as a new window
        self.payWindow = Toplevel(self.master.root)

        # sets the title of the
        # Toplevel widget
        self.payWindow.title("Pay Window")

        # sets the geometry of toplevel
        self.payWindow.geometry("200x200")

        # A Label widget to show in toplevel
        Label(self.payWindow,
              text="Indbetal").pack()

        self.money = Entry(self.payWindow)
        self.money.pack()


        self.button = Button(self.payWindow,
                               text="betal",
                               command= self.addMoney).pack()

    def addMoney(self):
        try:
            amount = int(self.money.get()) #HUSK AT VALIDERE INPUT!
        except:
            messagebox.showerror(title="Beløb fejl!", message="Prøv igen.\nKun hele tal!")
            return

        self.master.total+=amount
        self.master.progressLabelText.set(f"Indsamlet: {self.master.total} af {self.master.target} kroner:")
        print(f"Indsamlet: {self.master.total} af {self.master.target} kroner!")
        self.master.progress['value'] = self.master.total / self.master.target * 100
