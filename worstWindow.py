# importing tkinter module
import pickle
from tkinter import *
filename = 'betalinger.pk'

# Directory til betalinger.pk filen...
fodboldtur ={"assets/"}

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("200x200")



        Label(self.worstWindow, text="De værste betalere")
        #TODO Fix pickle load / label merge
        top = sorted(fodboldtur.items(), key=lambda item: item[1])
        for pair in top[:3]:
            Label(self.worstWindow, text=f"{pair[0]} Mangler {pair[1]}").pack

