import cv2
image  = cv2.imread('Images//cat.jpg')
width, height = 400,100

resized_image = cv2.resize(image, (width, height))

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

flipped_image = cv2.flip(image, 0)

cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Grey Image', grey_image)
cv2.imshow('Flipped Image', flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()