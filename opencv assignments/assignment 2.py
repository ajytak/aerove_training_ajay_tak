import cv2 as cv
import numpy as np

def tranlate_image(image, x_translate, y_translate):
    dimensions = (image.shape[1], image.shape[0])
    translation_matrix = np.float32([[1, 0, x_translate], [0, 1, y_translate]])
    return cv.warpAffine(image, translation_matrix, dimensions)
def rotate_image(image, angle, scale=None, point=None):
    dimensions = (image.shape[1], image.shape[0])
    if scale==None:
        scale=1
    if point==None:
        point = (image.shape[0]//2, image.shape[1]//2)
    rotation_matrix = cv.getRotationMatrix2D(point, angle, scale)
    return cv.warpAffine(image, rotation_matrix, dimensions)

img = cv.imread('T.png')
img1 = tranlate_image(img, 50, 100)
cv.imshow('image1', img1)
cv.waitKey(0)
img2 = tranlate_image(img, 100, 50)
cv.imshow('image2', img2)
cv.waitKey(0)
img3 = tranlate_image(img, 150, 150)
cv.imshow('image3', img3)
cv.waitKey(0)
img4 = tranlate_image(img, -150, -150)
cv.imshow('image4', img4)
cv.waitKey(0)
img5 = rotate_image(img, 45, 1.0)
cv.imshow('image5', img5)
cv.waitKey(0)
img6 = rotate_image(img, -45, 1.25)
cv.imshow('image6', img6)
cv.waitKey(0)
img7 = rotate_image(img, 120, point = (img.shape[0]*5//8, img.shape[1]*5//8))
cv.imshow('image7', img7)
cv.waitKey(0)
img8 = rotate_image(img, 270)
cv.imshow('image8', img8)
cv.waitKey(0)
img9 = cv.blur(img, (7, 7))
cv.imshow('image9', img9)
cv.waitKey(0)
img10 = cv.medianBlur(img, 9)
cv.imshow('image10', img10)
cv.waitKey(0)

