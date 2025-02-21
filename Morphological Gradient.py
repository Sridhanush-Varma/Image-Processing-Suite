import cv2
import numpy as np

image = cv2.imread('Images/Circle.png', 0)
cv2.imshow('Original', image)

kernel = np.ones((3,3), np.uint8)
Gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", Gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()