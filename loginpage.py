import tkinter
from tkinter import messagebox 
root = tkinter.Tk()  
root.geometry("500x500")
root.config(bg='skyblue')
def new_window():
    messagebox.showinfo("Success", "Login successful")

label1 = tkinter.Label(root, text="Enter Username", font=('Arial 18')) 
label1.place(x=160, y=20)

uname = tkinter.StringVar() 
t1 = tkinter.Entry(root, textvariable=uname, font=("Arial 18"))
t1.place(x=120, y=80)

label2 = tkinter.Label(root, text="Enter Password", font=('Arial 18')) 
label2.place(x=160, y=150)

passvar = tkinter.StringVar()
t2 = tkinter.Entry(root, textvariable=passvar, font=("Arial 18"), show="*")  
t2.place(x=120, y=200)

button = tkinter.Button(root, 
                        font=('Times New Roman', 10), 
                        text='Login', 
                        width=15, 
                        height=2, 
                        bg='orangered',
                        command = new_window,
                        )
button.place(x=190, y=300)

root.mainloop()
