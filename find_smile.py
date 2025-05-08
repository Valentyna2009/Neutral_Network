import cv2

img = cv2.imread('ai/images/smile3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# in CascadeClassifier write file .xml (trained ai) 
smile = cv2.CascadeClassifier('ai/xml/smile.xml')

# scale factor is 
results = smile.detectMultiScale(gray, scaleFactor=1.85, minNeighbors=35)

# draw rechtangle around the smile
# thickness = толщина
for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness= 2)

cv2.imshow("Result", img)
cv2.waitKey(0)