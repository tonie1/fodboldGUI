# importing tkinter module
import pickle
from tkinter import *
from tkinter.ttk import * #progressbar
from tkinter import messagebox

from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass

##open file
from tkinter import Frame, Tk, BOTH, Text, Menu, END
##import tkFileDialog

##login
import login


##TODO: ændre navnet på tkinter vinduet (også login vinduet)


class thewayin: ##https://stackoverflow.com/questions/63867798/how-to-call-one-window-to-another-using-python-tkinter
    login.everything()
#TODO: få login knappen ind på det andet tkinter vindue (Dette vil også fikse problemet med at man skal trykke
# luk på login knappen

class mainWindow:
    def __init__(self):


        self.total = 0
        self.target = 4500

        # creating tkinter window
        self.root = Tk()

        #load filen:
        self.filename = 'betalinger.pk'
        self.fodboldtur = {}
        try: #FILEN FINDES :)
            infile = open(self.filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()
        except: #FILEN FINDES IKKE.
##TODO: open file?? (Jeg prøvede, men kunne ikke finde ud af hente tkFileDialog)

            class Example(Frame):

                def __init__(self, parent):
                    Frame.__init__(self, parent)

                    self.parent = parent
                    self.initUI()

                def initUI(self):
                    self.parent.title("File dialog")
                    self.pack(fill=BOTH, expand=1)

                    menubar = Menu(self.parent)
                    self.parent.config(menu=menubar)

                    fileMenu = Menu(menubar)
                    fileMenu.add_command(label="Open", command=self.onOpen)
                    menubar.add_cascade(label="File", menu=fileMenu)

                    self.txt = Text(self)
                    self.txt.pack(fill=BOTH, expand=1)

                def onOpen(self):
                    ftypes = [('Python files', '*.py'), ('All files', '*')]
                    dlg = tkFileDialog.Open(self, filetypes=ftypes)
                    fl = dlg.show()

                    if fl != '':
                        text = self.readFile(fl)
                        self.txt.insert(END, text)

                def readFile(self, filename):
                    f = open(filename, "r")
                    text = f.read()
                    return text

            def mainOpenFile():

                root = Tk()
                ex = Example(root)
                root.geometry("300x250+300+300")
                root.mainloop()

            if __name__ == '__main__':
                mainOpenFile()


                ##TODONE: warn a brother
            messagebox.showerror(parent=self.root, title="GWAAAAAAA", message="FILEN ER IKKE FUNDET!!")
        print(self.fodboldtur)
        self.total = sum(self.fodboldtur.values())
        print(f"TOTAL: {self.total}")


        #TEXT:
        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        # Progress bar widget
        #TODO: Gøre så man ikke kan betale efter man har ramt 4500/4500 kroner; måske endda også tilføje en nice besked

        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")

        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient = HORIZONTAL,
                    length = 250, mode = 'determinate')
        self.progress['value'] = self.total/self.target*100
        #print(self.progress['length'])
        #print(self.progress['value'])
        #BUTTONS
        self.progress.pack(padx= 20)

        listButton = Button(self.root,text ="Liste over indbetalinger",command = lambda: listWindowClass(self))
        listButton.pack(padx = 20, pady = 10,side=LEFT)

        #TODO liste af betalinger, og hvor meget hver har betalt (note: er lidt trist over jeg ikke fik dette til
        # at virke da jeg fik det gjordt i det sidste fodboldtur projekt lmao
        ##TODO (mere en maybe-do): Tilføje et nice billed af London ;)

        payButton = Button(self.root,text ="Indbetal",command = lambda: payWindowClass(self))
        payButton.pack(padx = 20, pady = 10,side=LEFT)

        bottom3Button = Button(self.root,text ="Bund 3",command = lambda: worstWindowClass(self))
        bottom3Button.pack(padx = 20, pady = 10,side=LEFT)

        #TODO The bottom 3 missing

        # infinite loop
        mainloop()

    def gemFilen(self):
        outfile = open(self.filename, 'wb')
        pickle.dump(self.fodboldtur, outfile)
        outfile.close()
        print("GEMT")

if __name__ == '__main__':
    main = mainWindow()
