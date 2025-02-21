import cv2

#pre-trained model used by OPencv for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread('Images/faces.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.1, minNeighbors = 6, minSize = (100,100))

#Draw rectangles around the detected faces
for(x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0))

cv2.imshow('Faces Detected', image)

cv2.waitKey(0)
cv2.destroyAllWindows()