import cv2 as cv
import numpy as np
liv_cam = cv.VideoCapture(0)
while True:
    true, frame = liv_cam.read()
    if true:
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        cv.imshow('live feed', rgb_frame)
    else:
        break
    if cv.waitKey(10) == ord('x'):
        break
liv_cam.release()
cv.destroyAllWindows