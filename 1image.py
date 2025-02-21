import cv2
image = cv2.imread('Images/1.png')

cv2.imshow('My Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()