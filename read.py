import cv2 as cv

#reading pictures
"""
img = cv.imread('Resources/Photos/cat_large.jpg')
cv.imshow("Cat", img)
"""

#reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)