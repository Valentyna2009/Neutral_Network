import cv2

# '0' means camera of laptop
cap = cv2.VideoCapture('ai/videos/car_video1.mp4')

#because the video consits of many pictures. it should be take WHILE
while True:
    # success is true or false. true is when it can read the video
    # img means a lot of photos which make a video
    success, img = cap.read()
    cv2.imshow("My camera", img)

    # the speed of translating the pictures. the less time there is, the faster they will be translated
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break