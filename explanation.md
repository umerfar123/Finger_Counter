## Explanation

This program capture your video from your video capture frame by frame. Each frame which is a numpy array is passed to function findHands which is inside a class handDetector,
which uses model from mediapipe that detects the keypoint localization of 21 hand-knuckle coordinates within the detected hand regions.

<img align="center" alt="Coding" width="100%" height='200px' src="joints.jpeg">
