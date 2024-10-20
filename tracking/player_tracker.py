import cv2 as cv

# Tracker using KCF or CSRT
tracker = cv.TrackerCSRT_create()


def initialize_tracker(frame, bbox):
    tracker.init(frame, bbox)


def track_player(frame):
    success, bbox = tracker.update(frame)
    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return (x, y, w, h)
    return None
