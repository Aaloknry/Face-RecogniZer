from tkinter import *
import os
from PIL import ImageTk, Image
def saveimg():
    global val
    val = name.get()
    print(val)
    id.destroy()


id = Tk()
id.title("Enter Your Name")
name = StringVar()

img = Image.open("face.png")

img = ImageTk.PhotoImage(img)


Label(id, text ='Password Manager', font = ("Century Gothic", 20)).grid(row=0, sticky=N, pady=10)
Label(id, text ='equiped with--Face ReconiZer', font = ("Century Gothic", 10)).grid(row=1, sticky=N)
Label(id, image= img).grid(row=2, sticky=N, pady=15)

Label(id, text ='Enter Your Name:', font= ("Century Gothic", 14)).grid(row=3,column=0, pady=10)
Entry(id, textvariable= name).grid(row=4, column=0, pady=10)
Button(id, text="Done", font =('Century Gothic', 14), width=10, command =saveimg).grid(row=5, sticky=N)


id.mainloop()




