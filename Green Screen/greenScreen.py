import cv2

img=cv2.imread("panda.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

bg=cv2.imread("background.jpeg")
bg=cv2.cvtColor(bg,cv2.COLOR_BGR2RGB)

img=cv2.resize(img,(450,450))
bg=cv2.resize(bg,(450,450))

hi,wi=img.shape[0:2]

for i in range(hi):
  for j in range(wi):
    if img[i,j,1]<240:
      bg[i,j]=img[i,j]
  
bg=cv2.cvtColor(bg,cv2.COLOR_RGB2BGR)
cv2.imshow("greenScreen.jpg",bg)
print("Program done")
