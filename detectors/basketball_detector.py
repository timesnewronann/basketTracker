import cv2 as cv
import numpy as np


# Establish a color range for our basketballs
# Basketballs can be multiple colors, going to test this out with a variety of colors
# For now we are testing an orange ball
lower_range_orange = np.array([5, 150, 150])
upper_range_orange = np.array([15, 255, 255])

# let's try to add a silent basketball that's black
lower_range_black = np.array([0, 0, 0])
upper_range_black = np.array([180, 255, 50])


def detect_basketball(frame):
    # convert our frame to HSV color space because the space is better for detection than RGB
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Mask our basketball out depending on the color range
    orange_mask = cv.inRange(hsv_frame, lower_range_orange, upper_range_orange)

    black_mask = cv.inRange(hsv_frame, lower_range_black, upper_range_black)

    # create a variable that will store all potential ball masks
    basketball_masks = cv.bitwise_or(black_mask, orange_mask)
    # Look for contours on the mask
    contours, _ = cv.findContours(
        basketball_masks, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Return the detected basketball position
    basketballs = []
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 500:  # Filter small contours
            x, y, w, h = cv.boundingRect(contour)
            basketballs.append((x, y, w, h))

    return basketballs, basketball_masks
