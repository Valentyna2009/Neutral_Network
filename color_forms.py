import cv2

img = cv2.imread('ai/images/car1.jpg')

half_width = img.shape[0] // 2
half_height = img.shape[1] // 2

img = cv2.resize(img, (half_height, half_width), interpolation=cv2.INTER_LINEAR)

# img = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# show the different lays of img
r, g, b = cv2.split(img)

img = cv2.merge([b, g, b])

cv2.imshow('Car', img)

cv2.waitKey(0)