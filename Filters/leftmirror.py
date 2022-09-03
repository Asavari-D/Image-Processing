import cv2

img=cv2.imread("Person.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hi,wi=img.shape[0:2]

hw=wi//2
newWidth=hw

for y in range(hi):
  for x in range(hw,wi):
    img[y,x]=img[y,newWidth]
    newWidth=newWidth-1
  newWidth=hw

img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imshow("leftmirror",img)
