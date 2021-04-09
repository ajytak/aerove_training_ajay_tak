import cv2 as cv
import numpy as np 
image = cv.imread('spidy.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.medianBlur(gray, 3)
canny = cv.Canny(gray, 75, 75)
cv.imshow('drawing', canny)
cv.waitKey(0)