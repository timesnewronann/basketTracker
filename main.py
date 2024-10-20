import cv2 as cv
from detectors.face_detector import detect_faces
from detectors.basketball_detector import detect_basketball
from tracking.player_tracker import initialize_tracker, track_player
from analysis.stats_tracker import PlayerStats


# cv.CascadeClassifier: a class from openCV to load pre-trained classifier
# cv.data.haarcascades gives us the path to the directory for the xml files
# we can use pre-trained face detection model (Haar Cascade)
# Initialize objects
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
stats = PlayerStats()

# Initialize video capture
cap = cv.VideoCapture(1)

# Initialize player tracking (we’ll set this after detecting the face)
init_tracking = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect faces
    faces = detect_faces(frame, face_cascade)
    if not init_tracking and len(faces) > 0:
        # Start tracking the first detected face
        x, y, w, h = faces[0]
        initialize_tracker(frame, (x, y, w, h))
        init_tracking = True

    # Track the player if tracking is initialized
    if init_tracking:
        tracked_player = track_player(frame)

    # Detect basketballs
    basketballs, basketball_masks = detect_basketball(frame)
    for (x, y, w, h) in basketballs:
        cv.rectangle(frame, (x, y), (x + w, y + h),
                     (0, 0, 255), 2)  # Red box for basketball

    # Display the frame
    cv.imshow("Basketball Shot Tracker", frame)

    # show basketball mask
    #cv.imshow("Basketball Mask", basketball_masks)

    # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv.destroyAllWindows()
