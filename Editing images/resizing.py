import cv2

img=cv2.imread("green.jpg")
img=cv2.resize(img,(400,200))

cv2.line(img,(0,0),(399,0),(0,0,0),15)
cv2.line(img,(0,0),(0,199),(0,0,0),15)
cv2.line(img,(399,0),(399,199),(0,0,0),15)
cv2.line(img,(0,199),(399,199),(0,0,0),15)

cv2.imshow('resized', img)
cv2.waitKey(0)
