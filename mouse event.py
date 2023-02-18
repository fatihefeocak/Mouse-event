import cv2

cap = cv2.VideoCapture('line.mp4')

rectangles = []


def mouse(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        rectangles.append((x,y))


cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',mouse)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    for center in rectangles:
        cv2.rectangle(frame,center,(center[0]+10,center[1]+10),(255,0,0),1)

    cv2.imshow('Frame',frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('h'):
        rectangles = []

cap.release()
cv2.destroyAllWindows()