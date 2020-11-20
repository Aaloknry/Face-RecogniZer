import cv2
import os

cam = cv2.VideoCapture(0)


while True:
    ret, frame = cam.read()
# If Unable to fetch the Camera then msg
    if not ret:
        print("Fail in retriving Img")
        break

    cv2.imshow("Test", frame)

    k = cv2.waitKey(1)
    # press ESC to exit the camera view
    if k % 256 == 27:

        break
    # Press SPACE to capture the Image
    # Remember to add the Name of Your Image to save it
    elif k % 256 == 32:
        val = input("Enter your Name to be Displayed:")
        print("Snap")
        img_name = val + ".png"
        path = "E:\CS Poject\Face RecogniZer\IMGD"
        cv2.imwrite(os.path.join(path, img_name), frame)
        print("Captured")

cam.release()
cv2.destroyAllWindows()
