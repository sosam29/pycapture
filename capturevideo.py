import cv2 as cv
import shutil
import os


cap = cv.VideoCapture(0)

while (True):
    _, fr= cap.read()
    if not fr.any():
        print("NO stream available")
    file="image.png"
    cv.imwrite(file, fr)
    if cv.waitKey(1) &  0xFF ==ord('q'):
        break
cap.release()
cv.distroyAllwindows()
