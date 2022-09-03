import cv2

img=cv2.imread("backdrop.jpeg")
watermark=cv2.imread("openCVlogo.jpeg")

mark=cv2.addWeighted(img,0.8,watermark,0.2,0)

cv2.imshow("watermark.jpg",mark)
