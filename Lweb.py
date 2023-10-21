import webbrowser
from webbrowser import *
import os
from os import *
from tkinter import *

def linksave():
  value = l
  copied = Label(root, text="Please Wait ⌛")
  copied.place(x=210, y=170)
  link = l.get("1.0", "end-1c")
  webbrowser.open(link)

  copied.after(300, copied.destroy)


def yt():
  webbrowser.open("youtube.com")


#Develop root
root = Tk()

#Window Size
root.geometry("500x500")

#No fullscreen or Resize
root.resizable(width=False, height=False)

#Window Name
root.title("Webby 🔎")

#Text
l = Text(root, font=("TkDefaultFont", 10), width=50, height=0)

l.place(x=70, y=79)

#Button
nav = Button(root, text="Search 🔎", command=linksave)
nav.place(y=110, x=205)
nav.place(width=75)

#Title
ex = Label(root, text="Browse 🔗")
ex.place(x=210, y=0)

#shortcut data 1
# Shortcuts
youtube = Button(root, text="YouTube", command=yt)
youtube.place(x=195, y=400)
youtube.place(width=100)

#Extra Tips
notify = Label(root, text="Common Shortcuts 💡")
notify.place(x=190, y=350)

#Close logic
def rem():
  root.destroy()

#close
closebutton = Button(root, text="Close 🔒", command=rem)
closebutton.place(x=195, y=240)
closebutton.place(width=100)

#------------------------------------------------------------
def mystery():
  print("Nothing to see here 👀")

#History
history = Button(root, text="History 🗝", command=mystery)
history.place(x=0)

#Credit
cred = Button(root, text="Credits 📄", command=mystery)
cred.place(x=440, y=0)
#disc
def disc():
  webbrowser.open("https://docs.google.com/forms/d/1Rvs2soR8MPTmdqNArjI2bBy3LFto4BpxAskz_rP5bDU/edit")
  
#Request
dis2 = Button(root, text="Status ✉", command=disc)
dis2.place(x=0, y=474)
# log
def info():
  display = 3
  display.after(300000, display.destroy)
  display.place(x=250, y=420)
#Tutorial
how = Button(root, text="Press for more information", command=info)
how.place(x=347, y=474)
root.mainloop()