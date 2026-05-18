import cv2
import sys
import os
import numpy as np
import random
#from ultralytics import YOLO
#from utils import (
#    align_points_to_fixed_reference_line,
#    getAngle,
#    draw_pts,
#    draw_connection,
#    draw_pushup_bar,
#    draw_counter
#)

#set background image
img_bg_path = 'NeutralNetworks/bg.png'

#read background image
img_bg = cv2.imread(img_bg_path)
cv2.imshow('Push ups recognize', img_bg)

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
# def run_pose_detection(video_path, side):
#     global counter, stage

#     #open video
#     cap = cv2.VideoCapture(video_path)

#     # error if video is not found
#     if not cap.isOpened():
#         print('Video is not found', video_path)
#         return
    
#     while cap.isOpened():
#         #ret - bool (true) if frame is worked. frame - array (set) of vector images that changes with default frames per second
#         ret, frame = cap.read()
#         #end of video
#         if not ret: # == false
#             counter = 0
#             break

#         #show the video
#         cv2.imshow('Push ups counter', frame)
#         #display video until it ends
#         key = cv2.waitKey(1)
#         if key == 'S' or key == 's':
#             counter = 0
#             sys.exit()
    
    
while True:
    cv2.imshow('Push ups recognize', img_bg)
    
    #project the bg image for infinite time
    key = cv2.waitKey(0)

    key_ord = ['L', 'l', 'R', 'r', 'F', 'f']

    for i in key_ord:
        if key == ord(i):
            print(key)

        elif key == ord('S') or key == ord('s'):
            sys.exit()

        elif key == key_ord[-2:]:
            print('very good')
            


cv2.destroyAllWindows()