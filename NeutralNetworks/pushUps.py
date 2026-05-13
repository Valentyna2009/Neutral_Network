import cv2
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

while True:
    cv2.imshow('Push ups recognize', img_bg)
    
    #project the bg image for infinite time
    key = cv2.waitKey(0)

    key_ord = ['L', 'l', 'R', 'r', 'F', 'f']

    for i in key_ord:
        if key == ord(i):
            print(key)

        elif key == ord('S') or key == ord('s'):
            break


cv2.destroyAllWindows()