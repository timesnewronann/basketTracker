import cv2 as cv
import numpy as np

# Going to use openCV to get video from my webcam
capture = cv.VideoCapture(0, cv.CAP_AVFOUNDATION)

# cv.CascadeClassifier: a class from openCV to load pre-trained classifier
# cv.data.haarcascades gives us the path to the directory for the xml files
# we can use pre-trained face detection model (Haar Cascade)
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml")

if not capture.isOpened():
    print("Error: Could not open video capture.")
else:
    print("Video capture started successfully.")

# Establish a color range for our basketballs
# Basketballs can be multiple colors, going to test this out with a variety of colors
# For now we are testing an orange ball
lower_range_orange = np.array([5, 150, 150])
upper_range_orange = np.array([15, 255, 255])

# Capture loop
while True:
    ret, frame = capture.read()  # capture the frames
    if not ret:
        break  # end the loop

    # convert our frame to HSV color space because the space is better for detection than RGB
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Mask our basketball out depending on the color range
    mask = cv.inRange(hsv_frame, lower_range_orange, upper_range_orange)

    # Look for contours on the mask
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Draw contours on the OG frame
    for contour in contours:
        area = cv.contourArea(contour)
        # filter small contours
        if area > 500:
            # find the box for the contour
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Convert the frame to grayscale so we can detect our face(player)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect the face
    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces we detect
    for (x, y, w, h) in faces:
        # draw a blue box around detected faces
        cv.rectangle(frame, (x, y), (x+w, y + h), (255, 0, 0), 2)

    # show the frame with detected ball
    cv.imshow("Player & Basketball Detected", frame)
    cv.imshow("Mask", mask)  # we can show the mask for debugging

    # Q to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release and destroy captures
capture.release()
cv.destroyAllWindows()
