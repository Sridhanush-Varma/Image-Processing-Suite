import cv2
face_cacade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Open webcam
cap =cv2.VideoCapture(0)

while True:
    #Read a farme foem the video stream
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cacade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=5, minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

    #Display the frame with detected faces
    cv2.imshow('Face Recognition', frame)

    #Break the loop if 'g' is pressed
    if cv2.waitKey(2)& 0xFF == ord('a'):
        break
cap.release()
cv2.destroyAllWindows()