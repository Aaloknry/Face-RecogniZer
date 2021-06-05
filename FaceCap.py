import cv2
from tkinter import *
import os
from PIL import ImageTk, Image

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    # If Unable to fetch the Camera then msg
    if not ret:
        print("Fail in retrieving Img")
        break

    cv2.imshow("Position Your face Close to camera", frame)

    k = cv2.waitKey(1)
    # press ESC to exit the camera view
    if k % 256 == 27:

        break
    # Press SPACE to capture the Image and ask for Name
    # Remember to add the Name of Your Image to save it

    elif k % 256 == 32:
        def saveimg():
            global val
            val = name.get()
            print(val)
            id.destroy()

        # Saving New User and Asking Name by GUI

        id = Tk()
        id.title("Enter Your Name")
        name = StringVar()

        img = Image.open("./resource/face.png")

        img = ImageTk.PhotoImage(img)

        Label(id, text='Password Manager', font=("Century Gothic", 20)).grid(row=0, sticky=N, pady=10)
        Label(id, text='equiped with--Face ReconiZer', font=("Century Gothic", 10)).grid(row=1, sticky=N)
        Label(id, image=img).grid(row=2, sticky=N, pady=15)

        Label(id, text='Enter Your Name:', font=("Century Gothic", 14, 'bold')).grid(row=3, column=0, pady=10)
        Entry(id, textvariable=name, font=('Century Gothic', 14)).grid(row=4, column=0, pady=10)
        Button(id, text="Done", fg= 'white',font=('Century Gothic', 20, 'bold'), command=saveimg, bg='SlateBlue2').grid(row=5, sticky=N, pady=5)

        id.mainloop()

        # Saving in IMGD

        img_name = val + ".jpg"
        path = "./IMGD"
        cv2.imwrite(os.path.join(path, img_name), frame)
        print("Captured")

cam.release()
cv2.destroyAllWindows()
