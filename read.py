import cv2 as cv

#reading pictures
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow("Cat", img)

#reading videos
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) and 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# Create a VideoCapture object and read from input file
capture = cv.VideoCapture('tree.mp4')
   
# Check if camera opened successfully
if (capture.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
while(capture.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = capture.read()
  if ret == True:
   
    # Display the resulting frame
    cv.imshow('Frame', frame)
   
    # Press Q on keyboard to  exit
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
capture.release()
   
# Closes all the frames
cv.destroyAllWindows()



cv.waitKey(0)