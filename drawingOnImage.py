import cv2 as cv
import numpy as np
import math

rect_pt1 = None
rect_pt2 = None
c_pt1 = None
c_pt2 = None
def mouseEvents(event, x, y, flags, param):
    global rect_pt1, rect_pt2, c_pt1, c_pt2
    # rectangle controls with L mouse buttons
    if event == cv.EVENT_LBUTTONDOWN:
        rect_pt1 = (x, y)
        return
    elif event == cv.EVENT_LBUTTONUP:
        rect_pt2 = (x, y)
        cv.rectangle(img, rect_pt1, rect_pt2, (255, 255, 255), 3)
        return
    #circle controls with R mouse buttons
    elif event == cv.EVENT_RBUTTONDOWN:
        c_pt1 = (x, y)
        return
    elif event == cv.EVENT_RBUTTONUP:
        c_pt2 = (x, y)
        radius = math.sqrt((c_pt2[0] - c_pt1[0])**2 + (c_pt2[1] - c_pt1[1])**2)
        cv.circle(img, c_pt1, int(radius), (255, 255, 255), 3)
        return
    return

cv.namedWindow("result")

img = np.zeros((500, 1000, 3))
cv.setMouseCallback("result", mouseEvents)

while True:
    cv.imshow("result", img)
    if cv.waitKey(1) == ord("p"):
        cv.imwrite("drawing.png", img)
        break