from tkinter import *
import os
from PIL import ImageTk, Image

FaceGui = Tk()
FaceGui.title("Password Manager")

img = Image.open("./resource/bgStart.jpg")

img = ImageTk.PhotoImage(img)

Label(FaceGui, text='Password Manager', font=("Century Gothic", 26)).grid(row=0, sticky=N, pady=10)
Label(FaceGui, text='equipped with--Face RecogiZer', font=("Century Gothic", 14)).grid(row=1, sticky=N)
Label(FaceGui, image=img).grid(row=2, sticky=N, pady=15)


def facerec():
    os.system('python FaceRec.py')
    FaceGui.destroy()


def facecap():
    os.system('python FaceCap.py')
    FaceGui.destroy()


Button(FaceGui, text="Go to Password Manager", fg='white', bg='deep sky blue', font=('Century Gothic', 15, 'bold'),
       width=25, command=facerec, ).grid(row=3, sticky=N)
Label(FaceGui, text='Press "ESC" to exit the Face Recognition', font=("Century Gothic", 8)).grid(row=4, sticky=N,
                                                                                                 pady=2)
Button(FaceGui, text="Add new User", fg='white', bg='cyan4', font=('Century Gothic', 14, 'bold'), width=20,
       command=facecap).grid(row=5, sticky=N)
Label(FaceGui, text='Note:- To feed your Face press "SPACE"', font=("Century Gothic", 8)).grid(row=6, sticky=N)

FaceGui.mainloop()
