# first step, OpenCV library is imported
import cv2 as cv
import sys

# Read in stary night image sample
img = cv.imread(cv.samples.findFile("starry_night.jpg"))

# Check if we were able to properly load in the photo
if img is None:
    sys.exit("Could not read the image.")

# We can show the photo with .imshow
cv.imshow("Display window", img)
k = cv.waitKey(0)

# Write our file to starry_night.png
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
