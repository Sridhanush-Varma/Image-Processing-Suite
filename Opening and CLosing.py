import cv2
import numpy as np

image = cv2.imread('Images/Circle.png', 0)

kernel = np.ones((10,10), np.uint8)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Open and closed Image', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()