import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while True:
    true, frame = video.read()
    if true:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blur = cv.medianBlur(gray, 9)
        canny = cv.Canny(blur, 30, 30)
        contours, _ = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
        cv.drawContours(frame, [contour], 0, (0, 255, 0), thickness=3)
        cv.imshow('video', frame)
    if cv.waitKey(10) == ord('x'):
        break
video.release()
cv.destroyAllWindows()