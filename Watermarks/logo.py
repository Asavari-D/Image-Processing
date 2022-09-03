import cv2

img=cv2.imread("lion.jpeg")
img2=cv2.imread("pylogo.jpeg")
img2=cv2.resize(img2,(200,200))
hi,wi=img2.shape[0:2]

for y in range(hi):
  for x in range(wi):
    pix=img2[y,x]
    if not(pix[0]>240 and pix[1]>240 and pix[2]>240):
      img[y,440+x]=pix


cv2.imshow("logo2.jpg",img)
