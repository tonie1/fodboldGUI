# importing tkinter module
import pickle
from tkinter import *
filename = 'assets/betalinger.pk'

test = False

# Directory til betalinger.pk filen...
fodboldtur ={"./assets/betalinger.pk"}

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

if test is True:
    print("Opened pk file")

class worstWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("Bottom 3")
        self.worstWindow.geometry("450x600")
        canvas= Canvas(self.worstWindow, width= 450, height= 600, bg="SpringGreen2")
        Label(self.worstWindow, text="De værste betalere")

        yCoord = 1

        #TODO Fix pickle load / label merge
        top = sorted(fodboldtur.items(), key=lambda item: item[1], reverse=True)
        for pair in top[:3]:
            canvas.create_text(150, (100 * yCoord), text=f"{pair[0]} har indbetalt {pair[1]}", fill="black", font=('Helvetica 15 bold'))
            yCoord += 1

            if test is True:
                print('Attempted to make text in the Canvas')
        canvas.pack()

