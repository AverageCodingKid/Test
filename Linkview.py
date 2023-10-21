# Link Viewer Code 🔗
import webbrowser
from webbrowser import *
import os
from os import *
from tkinter import *

def linksave():
    value = l
    copied = Label(root, text="Sending to link ⌛")
    copied.place(x=15, y=75)
    link = l.get("1.0", "end-1c")
    webbrowser.open(link)
    # Close the window
    copied.after(300, root.destroy)

#Develop root
root = Tk()

#Window Size
root.geometry("500x500")

#No fullscreen or Resize
root.resizable(width=False, height=False)

#Window Name
root.title("Link Viewer 🔗")


#Text
l = Text(root)
l.place(x=0, y=150)

#Button
nav = Button(root, text="Navigate to site 🔗", command=linksave)
nav.place(y=0, x=0)
nav.place(width=500)
root.mainloop()