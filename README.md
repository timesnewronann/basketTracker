# basketTracker

Code file layout:
basketball_tracker/
│
├── detectors/
│ ├── face_detector.py # Face detection logic
│ ├── pose_detector.py # Pose estimation and body part detection
│ └── basketball_detector.py # Basketball detection logic (color-based, YOLO, etc.)
│
├── tracking/
│ ├── player_tracker.py # Tracking player (face/body) movement over time
│ └── ball_tracker.py # Tracking basketball movement
│
├── analysis/
│ ├── shot_analysis.py # Analyzing shot success, correlating movements to misses
│ └── stats_tracker.py # Tracking shot stats, shooting percentage
│
├── main.py # The main entry point to bring everything together
└── utils.py # Utility functions like configuration, helpers

I am currently learning how to detect objects
Camera 0 = iphone
Camera 1 = webcam
