import cv2
import numpy as np

image = cv2.imread('Images/Circle.png', 0)

#Kernel for erosion
kernel = np.ones((3,3), np.uint8)

erosion = cv2.erode(image, kernel, iterations=1)
erosion2 = cv2.erode(erosion, kernel, iterations=2)
erosion3 = cv2.erode(erosion2, kernel, iterations=3)

cv2.imshow('Original Image', image)
cv2.imshow('Erroded Image', erosion)
cv2.imshow('Erroded Image 2', erosion2)
cv2.imshow('Erroded Image 3', erosion3)
cv2.waitKey(0)
cv2.destroyAllWindows()
