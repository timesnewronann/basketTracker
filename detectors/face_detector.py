import cv2 as cv


def detect_faces(frame, face_cascade):
    # Convert the frame to grayscale so we can detect our face(player)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect the face
    faces = face_cascade.detectMultiScale(
        gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    return faces
