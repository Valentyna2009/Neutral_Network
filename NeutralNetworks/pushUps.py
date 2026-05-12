import cv2
import numpy as np
import cvzone
from cvzone.PoseModule import PoseDetector
import math 
import mediapipe as mp


# load the video
cap = cv2.VideoCapture('Neutral Networks/vid1(2).mp4')

# show connected arms lines
pd = PoseDetector(trackCon=0.70,detectionCon=0.70)


while 1:
    ret,img = cap.read()
    if not ret:
        cap = cv2.VideoCapture('vid1.mp4')
        continue

    pd.findPose(img,draw=0)


    cv2.imshow('frame',img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()