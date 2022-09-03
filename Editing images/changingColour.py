import cv2

img=cv2.imread("cube.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img[34:101, 33:104]=img[34:101, 194:265]

img=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imshow("cubeW2B.jpg",img)
print("Program over")