from tkinter import *
from tkinter import messagebox

def everything():
    def a(e=''):
        uname = e1.get()
        password = e2.get()

        if(uname == "" and password == "") :
            messagebox.showinfo("", "Please Enter Details")

        elif(uname == "username" and password == "password"):

            messagebox.showinfo("","Login Success")
            top.destroy()
            main.destroy()

        else :
            messagebox.showinfo("","Incorrent Username and Password")
            exit("Incorrect Username and Password")

    main = Tk()
    root = Tk()
    main.withdraw()
    top = Toplevel()
    top.title("Login")
    top.geometry("300x200")

    Label(top, text="Username").place(x=10, y=10)
    Label(top, text="Password").place(x=10, y=40)
    Button(root, text="Login", command=a, height=3, width=13).place(x=10, y=100)
    top.bind('<Return>', a)

    e1 = Entry(top)
    e1.place(x=140, y=10)

    e2 = Entry(top)
    e2.place(x=140, y=40)
    e2.config(show="*")

    root.mainloop()