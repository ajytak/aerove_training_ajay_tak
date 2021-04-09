import cv2 as cv
import numpy as np 
img = cv.imread('T.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(gray, 15)
_, threshold = cv.threshold(blur, 127, 255, cv.THRESH_BINARY)
contours, i = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
for contour in contours:
    approx = cv.approxPolyDP(contour, 0.1*cv.arcLength(contour, True), True)
    cv.drawContours(img, [contour], 0, (0, 255, 0), 3)
    l = len(approx)
    M = cv.moments(contour)
    if l == 3:
        cv.putText(img, 'Triangle', (int(M['m10']/M['m00']), int(M['m01']/M['m00'])), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    elif l == 4:
        cv.putText(img, 'Square', (int(M['m10']/M['m00']), int(M['m01']/M['m00'])), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    elif l >= 9:
        cv.putText(img, 'Circle', (int(M['m10']/M['m00']), int(M['m01']/M['m00'])), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
cv.imshow('final image', img)
cv.waitKey(0)