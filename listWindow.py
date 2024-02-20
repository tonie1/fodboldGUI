# importing tkinter module

#TODO Notér jeg ikke kunne få dette til at virke

from tkinter import *
import pickle
filename = 'betalinger.pk'

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()

from PIL import ImageTk,Image #image stuff - install package: Pil

class listWindowClass:
    def __init__(self, master):
        self.master = master #reference til main window objektet
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List Window")
        self.listWindow.geometry("500x500")

        Label(self.listWindow, text="Liste over indbetalinger").pack()

        def liste():
            for item in fodboldtur.items():
                print(item, '/ 562,5kr')
            liste()

        #img = ImageTk.PhotoImage(Image.open("assets/img/cyl.png"))
        #panel = Label(self.listWindow, image=img)
        #panel.image = img
        #panel.pack(side="bottom", fill="both", expand="yes")