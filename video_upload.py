import cv2
import numpy as np

# '0' means camera of laptop
cap = cv2.VideoCapture('ai/videos/car_video1.mp4')

#because the video consits of many pictures. it should be take WHILE
while True:
    # success is true or false. true is when it can read the video
    # img means a lot of photos which make a video
    success, img = cap.read()

    double_width = int(img.shape[0] * 2)
    double_height = int(img.shape[1] * 2)

    img = cv2.resize(img, (double_height, double_width), interpolation= cv2.INTER_LINEAR)

    # photo to gray
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 


# outline along the contour (обвезти по контуру). the SMALLER the number, the better
    img = cv2.Canny(img, 100, 100)

    # increase the boldness of the lines (увеличить жирность линий)
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    img = cv2.erode(img, kernel, iterations=1)

    cv2.imshow("Car", img)

    # the speed of translating the pictures. the less time there is, the faster they will be translated
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break