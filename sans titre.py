#opening the webcam

import cv2

import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing=mp.solutions.drawing_utils
webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    success,img=webcam.read()
    #face detection using mediapipe
    img = cv2.cvtcolor(img,cv2.COLOR_BGR2RGB)
    results=mp_face_detection.process(img)
    
    #draw the face dtection annotations on the image
    img=cv2.cvtcolor(img,cv2.COLOR_RGB2BGR)
    if results.detections:#if there are faces in the image then draw rectangles on the face,etc
        for detection in results.detections:
            mp_drawing.draw_detection(img,detection)#we pass the image and the detection
    
    if success:
        cv2.imshow("Webcam",img)
    else:
        print("error reading frame from webcam")              
        break
    if cv2.waitKey(5) & 0xFF ==ord("q"):
              break
webcam.release()
cv2.destroyAllWindows
