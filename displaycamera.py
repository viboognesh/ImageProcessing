# importing libraries
import cv2 as cv
import numpy as np

# Create a VideoCapture object and read from input file
capture = cv.VideoCapture(0, cv.CAP_DSHOW)
   
# Check if camera opened successfully
if (capture.isOpened()== False): 
  print("Error opening video  file")

   
# Read until video is completed
while(capture.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = capture.read()
  if ret == True:
   
    # Display the resulting frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Video', frame)
   
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
