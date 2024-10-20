import cv2 as cv
import numpy as np


# Establish a color range for our basketballs
# Basketballs can be multiple colors, going to test this out with a variety of colors
# For now we are testing an orange ball
lower_range_orange = np.array([5, 150, 150])
upper_range_orange = np.array([15, 255, 255])


def detect_basketball(frame):
    # convert our frame to HSV color space because the space is better for detection than RGB
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Mask our basketball out depending on the color range
    mask = cv.inRange(hsv_frame, lower_range_orange, upper_range_orange)

    # Look for contours on the mask
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Return the detected basketball position
    basketballs = []
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 500:  # Filter small contours
            x, y, w, h = cv.boundingRect(contour)
            basketballs.append((x, y, w, h))

    return basketballs
