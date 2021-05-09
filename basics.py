import cv2 as cv 

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow("Park", img)

# #Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# #Blur
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# #Edge Cascade
# canny = cv.Canny(blur,125, 175)
# cv.imshow("Canny", canny)

# #dilating the image
# dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow("Dilated",dilated)

# #Eroding 
# eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow("Eroded",eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#cropped
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)