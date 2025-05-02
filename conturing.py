import cv2
import numpy as np

img = cv2.imread('ai/images/car1.jpg')

half_width = img.shape[0] // 2
half_height = img.shape[1] // 2

new_img = np.zeros(img.shape, dtype='uint8')

# resize with new num of height and width
img = cv2.resize(img, (half_height, half_width), interpolation= cv2.INTER_LINEAR)

# photo to gray
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 

# blur (размыть изображение)
img = cv2.GaussianBlur(img, (5, 5), 0)


img = cv2.Canny(img, 100, 140)

# con meams the coordinate of all the contours, like angles etc.
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(new_img, con, -1, (234, 123, 233), 2)

cv2.imshow('Result', new_img)

cv2.waitKey(0)