
from string import ascii_lowercase
import random
import string
import tkinter
from tkinter import*
from tkinter import messagebox



def generatePassword():
    if choices.get() == 1:
        return messagebox.showinfo(message="".join(random.choices(string.hexdigits, k=8)))
        
    elif choices.get() == 2:
        messagebox.showinfo(message= "".join(random.choices(string.ascii_letters, k=8)))
    elif choices.get() == 3:
        messagebox.showinfo(message= "".join(list(filter(lambda z: ' ' not in z ,(random.choices(string.printable, k=8))))))
# filter and lambda z to avoid empty space

       

window = Tk()
# window.geometry("700x350")
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.title("Password Generator")



choices = IntVar()
choices.set(0)    
    


Checkbutton(window, text= "Lettres et chiffres", variable= choices, onvalue=1).grid(sticky=W, row=0)
Checkbutton(window, text= "Lettres", variable= choices, onvalue=2).grid(sticky=W, row=1)

Checkbutton(window, text= "Lettres, chiffre, punctuation", variable= choices, onvalue=3).grid(sticky=W, row=2)







Button(window, text="Generate password", command= generatePassword).grid(sticky=W, row=3)




window.mainloop()

