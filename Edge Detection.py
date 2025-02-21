import cv2
image = cv2.imread('Images//cat.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Gaussion blur to reduce noise and improve edge detection
blurred_image = cv2.GaussianBlur(gray_image, (5,1), 0)
blurred_image2 = cv2.GaussianBlur(gray_image, (7,7), 0)
blurred_image3 = cv2.GaussianBlur(gray_image, (1,1), 0)
blurred_image4 = cv2.GaussianBlur(gray_image, (99,99), 0)

#Performing cannoy edge detection
edges = cv2.Canny(blurred_image, 200, 200)
edges2 = cv2.Canny(blurred_image2, 200, 200)
edges3 = cv2.Canny(blurred_image3, 200, 200)
edges4 = cv2.Canny(blurred_image4, 200, 200)

cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.imshow('Edges 2', edges2)
cv2.imshow('Edges 3', edges3)
cv2.imshow('Edges 4', edges4)

cv2.waitKey(2000)
cv2.destroyAllWindows()