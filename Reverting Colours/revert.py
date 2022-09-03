import cv2

img=cv2.imread("blacknwhite.jpeg",cv2.IMREAD_GRAYSCALE)

x,y=img.shape

for i in range(x):
  for j in range(y):
    if img[i,j]<120:
      img[i,j]=255
    else:
      img[i,j]=0

cv2.imwrite("blacknwhite_edit.jpeg",img)

cv2.imshow('image', img)
cv2.waitKey(0)