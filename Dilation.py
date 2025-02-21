import cv2
import numpy as np

image = cv2.imread('Images/Circle.png')

kernel = np.ones((3,3), np.uint8)

dilation = cv2.dilate(image, kernel, iterations=1)
dilation2 = cv2.dilate(image, kernel, iterations=2)
dilation3 = cv2.dilate(image, kernel, iterations=3)
dilation4 = cv2.dilate(image, kernel, iterations=4)

cv2.imshow('Original Image', image)
cv2.imshow("Dilated Image", dilation)
cv2.imshow("Dilated Image 2", dilation2)
cv2.imshow("Dilated Image 3", dilation3)
cv2.imshow("Dilated Image 4", dilation4)
cv2.waitKey(0)
cv2.destroyAllWindows()