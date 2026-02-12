# the bare min code that is required to run hand tracking

import cv2
import mediapipe as mp
import time

# start video from camera
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if success:
        cv2.imshow("Image", img)
        cv2.waitKey(1)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()