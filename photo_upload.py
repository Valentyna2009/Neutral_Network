import cv2
import numpy as np

# upload the image
img = cv2.imread('ai/images/smile1.jpg')

# lets halve the picture because it doesnt fit (не помещается) on the display
half_width = img.shape[0] // 2
half_height = img.shape[1] // 2

# resize with new num of height and width
img = cv2.resize(img, (half_height, half_width), interpolation= cv2.INTER_LINEAR)

# photo to gray
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 

# cut the photo img[height, width]
#cv2.imshow('Result', img[0:300, 0:200])

# outline along the contour (обвезти по контуру). the SMALLER the number, the better
img = cv2.Canny(img, 200, 200)

# increase the boldness of the lines (увеличить жирность линий)
kernel = np.ones((4, 4), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

# show the resized photo 
cv2.imshow('Result', img)

# it will be open until we press x
cv2.waitKey(0) 