import cv2

img = cv2.imread('ai/images/car1.jpg')

half_height = img.shape[1] // 2
half_width = img.shape[0] // 2

img = cv2.resize(img, (half_height, half_width))
 
# flip the img to vertical(0), horizontal(1) and both(-1) 
# img = cv2.flip(img, 0)

# rotating the img
def rotate(img, angle):
    height = img.shape[1]
    width = img.shape[0]
    #get the central point of img
    point = (width // 2, height // 2)

    # lets rotate
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img, mat, (width, height))



img = rotate(img, 180)

cv2.imshow('Flipped image', img)

cv2.waitKey(0)