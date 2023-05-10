#facemesh with detection of blinking eye, works but needs improvement regarding
import cv2
import mediapipe as mp
import numpy as np
import time

def blink_detected(interval_time):
    webcam = cv2.VideoCapture(0)
    mp_face_mesh = mp.solutions.face_mesh

    with mp_face_mesh.FaceMesh(
        max_num_faces=2,
        refine_landmarks=True,
        #min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face_mesh:

        start_time = time.time()
        current_time = time.time()

        while webcam.isOpened():
            while(current_time - start_time < interval_time):
                success, img = webcam.read()

                if not success:
                    print("Failed to capture frame from webcam. Ignoring process")
                    break

                # applying face mesh model using mediapipe
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(img)

                # draw annotations on the image
                # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        # calculate eye aspect ratio (EAR) to detect blink
                        RIGHT_EYE = [33, 246, 161, 160, 159, 158, 157, 173, 133, 155, 154, 153, 145]
                        right_eye = [face_landmarks.landmark[idx] for idx in RIGHT_EYE]
                        right_eye_h = np.linalg.norm(right_eye[1].x - right_eye[5].x)
                        right_eye_v1 = np.linalg.norm(right_eye[2].y - right_eye[4].y)
                        right_eye_v2 = np.linalg.norm(right_eye[0].y - right_eye[3].y)
                        EAR_right = (right_eye_v1 + right_eye_v2) / (2 * right_eye_h)

                        # Here blink is detected
                        if EAR_right < 0.1:
                            print("Blink")
                            webcam.release()
                            # cv2.destroyAllWindows()
                            return True

                # Update current time
                current_time = time.time()

            # Time has passed and no blink detected
            webcam.release()
            # cv2.destroyAllWindows()
            print("No blink")
            return False
