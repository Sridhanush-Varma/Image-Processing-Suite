import cv2

image = cv2.imread('Images/cat.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Binary Thresholding
#All pixel valus above 127 will be converted to 255 (white), and below to 0 (black)
_, thresholded_image = cv2.threshold(gray_image, 127 , 255, cv2.THRESH_BINARY)
_, thresholded_image2 = cv2.threshold(gray_image, 175 , 255, cv2.THRESH_BINARY)
_, thresholded_image3 = cv2.threshold(gray_image, 200, 100, cv2.THRESH_BINARY)
_, thresholded_image4 = cv2.threshold(gray_image, 220 , 25, cv2.THRESH_BINARY)

cv2.imshow('Grayscale Image', gray_image)

cv2.imshow('Thresholded Image', thresholded_image)
cv2.imshow('Thresholded Image 2', thresholded_image2)
cv2.imshow('Thresholded Image 3', thresholded_image3)
cv2.imshow('Thresholded Image 4', thresholded_image4)

cv2.waitKey(0)

cv2.destroyAllWindows()