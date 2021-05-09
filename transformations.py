import cv2 as cv 
import numpy as np

img = cv.imread("Resources/Photos/park.jpg")
cv.imshow("Park", img)

# #Translation
# def translate(img, x, y):
#     transMatrix = np.float32([[1,0,x],[0,1,y]])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, transMatrix, dimensions)

# # -x --> left
# # -y --> Up
# # x --> Right
# # y --> Down

# translated = translate(img,100,100)
# cv.imshow("Translated", translated)

# #Rotation
# def rotate(img, angle, rotPoint = None):
#     (height,width) = img.shape[:2]

#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
    
#     rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)

#     return cv.warpAffine(img, rotMatrix, dimensions)

# rotated = rotate(img, 45)
# cv.imshow("Rotated", rotated)

# def duit(number):
#     rotated_pic = img
#     for i in range(0,360,number):
#         rotated_pic = rotate(rotated_pic, number)
#     cv.imshow("UltimateRotationof"+str(number), rotated_pic)


# duit(1)
# duit(5)
# duit(10)
# duit(45)
# duit(90)

# #Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow("resized",resized)

# #Flipping
# flip = cv.flip(img, -1)
# cv.imshow("Flip",flip)

cropped = img[200:400, 300:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)