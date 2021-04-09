import cv2 as cv
import numpy as np
img = cv.imread('spidy.jpg')
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray scale', gray_img)
cv.waitKey(0)
_, BW_img = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
cv.imshow("bW image", BW_img)
cv.waitKey(0)