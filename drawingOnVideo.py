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
        cv.rectangle(mask, rect_pt1, rect_pt2, (0, 255, 0), 3)
        return
    #circle controls with R mouse buttons
    elif event == cv.EVENT_RBUTTONDOWN:
        c_pt1 = (x, y)
        return
    elif event == cv.EVENT_RBUTTONUP:
        c_pt2 = (x, y)
        radius = math.sqrt((c_pt2[0] - c_pt1[0])**2 + (c_pt2[1] - c_pt1[1])**2)
        cv.circle(mask, c_pt1, int(radius), (0, 255, 0), 3)
        return
    return

capture = cv.VideoCapture(0)
mask = np.ones((480, 640, 3), dtype=np.uint8)
width = capture.get(3)
height = capture.get(4)

print((width, height))
cv.namedWindow("video")
cv.setMouseCallback("video", mouseEvents)


fourcc = cv.VideoWriter_fourcc(*"XVID")
writer = cv.VideoWriter("drawingVideo.avi", fourcc=fourcc, fps=20.0, frameSize=(int(width), int(height)))

while capture.isOpened():
    cv.imshow("video", mask)
    ret, frame = capture.read()
    if ret:
        frame = cv.flip(frame, 1)
        frame = frame * mask
        writer.write(frame)
        cv.imshow("video", frame)
        if cv.waitKey(1) & 0xff == ord("p"):
            break

capture.release()
writer.release()
cv.destroyAllWindows()