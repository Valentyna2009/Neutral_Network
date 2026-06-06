import cv2
import sys
import os
import numpy as np
import random
from ultralytics import YOLO
from utils import (
   align_points_to_fixed_reference_line,
   getAngle,
   draw_pts,
   draw_connection,
   draw_pushup_bar,
   draw_counter
)

#set background image
img_bg_path = 'NeutralNetworks/bg.png'

#read background image
img_bg = cv2.imread(img_bg_path)
cv2.imshow('Push ups recognize', img_bg)

#Load YOLO model
model = YOLO('NeutralNetworks/yolov8n.pt')
print('Model service:', model.info())

# function to get video depending on side L/R/F the user chooses
def get_video(folder_name):

    #get path to folder names Video
    folder_path = os.path.join('Videos', folder_name)

    #list all video files
    video_files = os.listdir(folder_path)

    #pick randomly one
    selected_video = random.choise(video_files)

    # get full path of video
    video_path = os.path.join(folder_path, selected_video)
    return video_path

# pose detection function
def run_pose_detection(video_path):
    global counter, stage

    #open video
    cap = cv2.VideoCapture(video_path)

    # error if video is not found
    if not cap.isOpened():
        print('Video is not found', video_path)
        return
    
    while cap.isOpened():
        #ret - bool (true) if frame is worked. frame - array (set) of vector images that changes with default frames per second
        ret, frame = cap.read()
        #end of video
        if not ret: # == false
            # push ups count is 0
            counter = 0
            break

        frame = cv2.resize(frame, (1280, 720))
        results = model.predict(frame, conf=0.5, verbose = False)
        keypoints = results[0].keypoints.xy[0]
        p = keypoints.cpu().numpy()
        frame = draw_pts(frame, p)

        #show the video
        cv2.imshow('Push ups counter', frame)
        #display video until it ends
        key = cv2.waitKey(10)
        if key == 'S' or key == 's':
            counter = 0
            sys.exit()
    
    
while True:
    cv2.imshow('Push ups recognize', img_bg)
    
    #project the bg image for infinite time
    key = cv2.waitKey(0)

    if key == ord('F') or key == ord('f'):
        run_pose_detection("NeutralNetworks/F/front_side.mp4")

    elif key == ord('L') or key == ord('l'):
        run_pose_detection("NeutralNetworks/L/left_side.mp4")

    elif key == ord('R') or key == ord('r'):
        run_pose_detection("NeutralNetworks/R/right_side.mp4")
            
    elif key == ord('S') or key == ord('s'):
        sys.exit()

cap.release()
cv2.destroyAllWindows()