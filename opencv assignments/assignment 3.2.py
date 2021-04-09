import cv2 as cv
import numpy as np 
live = cv.VideoCapture(0)
while True:
    _, frame = live.read()
    if _:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blur = cv.medianBlur(gray, 5)
        canny = cv.Canny(blur, 75, 75)
        cv.imshow('live', canny)
    else:
        break
    if cv.waitKey(10) == ord('x'):
        break
live.release()
cv.destroyAllWindows()
