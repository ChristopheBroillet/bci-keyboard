#facemesh with detection of blinking eye, works but needs improvement regarding
import cv2
import mediapipe as mp
import numpy as np
import time

# part is either "blink" or "mouth"
def validation_move(interval_time, part):
    webcam = cv2.VideoCapture(0)
    mp_face_mesh = mp.solutions.face_mesh

    if part == "blink":
        landmark_points = [33, 246, 161, 160, 159, 158, 157, 173, 133, 155, 154, 153, 145]
        # Blink is when eye is closing so use smaller than
        test_aspect_ratio = lambda x: x < 0.1
    elif part == "mouth":
        landmark_points = [312, 57, 82, 315, 85, 287]
        # Opening mouth so use greater than
        test_aspect_ratio = lambda x: x > 0.3

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
                        # Calculate aspect ratio
                        used_landmarks = [face_landmarks.landmark[idx] for idx in landmark_points]
                        horizontal_line = np.linalg.norm(used_landmarks[1].x - used_landmarks[5].x)
                        vertical_line_1 = np.linalg.norm(used_landmarks[2].y - used_landmarks[4].y)
                        vertical_line_2 = np.linalg.norm(used_landmarks[0].y - used_landmarks[3].y)
                        aspect_ratio = (vertical_line_1 + vertical_line_2) / (2 * horizontal_line)

                        # Test if blink/mouth opening is detected
                        if test_aspect_ratio(aspect_ratio):
                            webcam.release()
                            return True

                # Update current time
                current_time = time.time()

            # Time has passed and no detection
            webcam.release()
            return False
