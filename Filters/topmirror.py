import cv2

img=cv2.imread("Person.jpeg")

hi,wi=img.shape[0:2]

h2=hi//2
newWidth=h2

for y in range(h2,hi):
  for x in range(wi):
    img[y,x]=img[newWidth,x]
  newWidth=newWidth-1
  

cv2.imshow("topmirror",img)
