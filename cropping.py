import cv2

img2=cv2.imread("thanos.jpeg")

img2=img2[42:154,150:256]

cv2.imshow('cropped gauntlet', img2)
print("Program Done")