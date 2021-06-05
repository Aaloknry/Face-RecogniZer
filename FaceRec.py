import cv2
import numpy as np
import face_recognition
import os

path = "IMGD"
img_Prifix = []
chek = []
images = []
img_List = os.listdir(path)
for x in img_List:

    ImgP = cv2.imread(f'{path}/{x}')
    images.append(ImgP)
    img_Prifix.append(os.path.splitext(x)[0])

# Finding Arrays

def encode(imgenco):
    encode_list = []
    for imgs in imgenco:
        img2_bgr = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
        encoded = face_recognition.face_encodings(img2_bgr)[0]
        encode_list.append(encoded)
        return encode_list


encoded_L = encode(images)
print("Encoding Completed")

# RecogniZer
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSsize = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgSsize = cv2.cvtColor(imgSsize, cv2.COLOR_BGR2RGB)

    face_detection_Live = face_recognition.face_locations(imgSsize)
    encoded_Live_img = face_recognition.face_encodings(imgSsize, face_detection_Live)

    for encodeFace, faceLoc in zip(encoded_Live_img, face_detection_Live):

        matches = face_recognition.compare_faces(encoded_L, encodeFace)
        face_Dis = face_recognition.face_distance(encoded_L, encodeFace)
        print(face_Dis)
        matchIndex = np.argmin(face_Dis)

        if matches[matchIndex]:
            chek.append(1)
            name = img_Prifix[matchIndex].upper()[0]
            print(name)

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        else:
            chek.append(0)

    cv2.imshow('Recognising...', img)
    k = cv2.waitKey(1)
    # press ESC to exit the camera view

    if k % 256 == 27:
        break

    elif any(chek) == 1:
        os.system('Application root')
        print("App started")
        break
    elif len(chek) == 5:
        break

cap.release()
cv2.destroyAllWindows()

