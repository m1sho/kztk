import tkinter
import customtkinter
import tkinter.messagebox
from tkinter import *
import random
import translators as ts
kz= str(random.choice(open("kz.txt").read().split()))
translation=(ts.google(kz, from_language='kk',to_language='en'))

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


root_tk = customtkinter.CTk()  # create CTk window like the Tk window
root_tk.geometry("300x200")
root_tk.title("Kazakh Word of the Day")


def onClick():
    print(tkinter.messagebox.showinfo("Translation", translation))
def exportClick():
    f=open("KazakhWords.txt","w+")
    for i in range(1):
        f.write(kz +"\n" )

# Use CTkButton instead of tkinter Button



l = Label(text=kz)
l.config(font=("Roboto", 26))
#l.config(background='Yellow')

l.pack()
button1 = customtkinter.CTkButton(master=root_tk, text="Translation",command=onClick)
button1.pack()
#button = customtkinter.CTkButton(master=root_tk, text="Export to Excel",command=exportClick())
#button.pack()
root_tk.configure(background='grey')
root_tk.mainloop()







