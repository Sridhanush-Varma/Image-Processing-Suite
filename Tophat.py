import cv2
import numpy as np

image = cv2.imread('Images/Circle.png', 0)
cv2.imshow('Original', image)

kernel = np.ones((3,3), np.uint8)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()