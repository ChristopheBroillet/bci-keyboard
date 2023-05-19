import cv2
import mediapipe as mp
import numpy as np
import time
import signal

# Custom SIGINT when CTRL + C is pressed to close everything properly
def SignalHandler_SIGINT(SignalNumber,Frame):
    webcam.release()
    cv2.destroyAllWindows()
    print("Correctly closed")
    exit()

# Register the signal with SignalHandler
signal.signal(signal.SIGINT, SignalHandler_SIGINT)


mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

webcam = cv2.VideoCapture(0)

# #calculate the Eye Aspect Ratio (EAR)
# def eye_aspect_ratio(eye_points, facial_landmarks):
#     # Compute the euclidean distances between the two sets of vertical eye landmarks
#     A = np.linalg.norm(facial_landmarks[eye_points[1]] - facial_landmarks[eye_points[5]])
#     B = np.linalg.norm(facial_landmarks[eye_points[2]] - facial_landmarks[eye_points[4]])
#
#     # Compute the euclidean distance between the two horizontal eye landmarks
#     C = np.linalg.norm(facial_landmarks[eye_points[0]] - facial_landmarks[eye_points[3]])
#
#     # Calculate the EAR
#     ear = (A + B) / (2.0 * C)
#     return ear
# #-------------------------------------
#
# #landmarks for the left and right eyes
# RIGHT_EYE_INDICES = [33, 161, 160, 159, 158, 157, 173]
# LEFT_EYE_INDICES = [263, 249, 390, 373, 374, 380, 362]
#-------------------------------------
#threshold for EAR
# EAR_THRESHOLD = 1.12
with mp_face_mesh.FaceMesh(
    max_num_faces=2,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    blinked = False
    start_time = None
    blink_counter = 0

    while webcam.isOpened():
        success, img = webcam.read()

        if not success:
            print("Failed to capture frame from webcam. Ignoring process")
            break

        # applying face mesh model using mediapipe
        # convert to process
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(img)
        # draw annotations on the image
        # reconvert back to display on the screen
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                # Border around Face, eyes, lips
                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style()
                )

                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
                )

                mp_drawing.draw_landmarks(
                    image=img,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style()
                )

                # mp_drawing.draw_landmarks(
                #     image=img,
                #     landmark_list=face_landmarks,
                #     connections=mp_face_mesh.FACEMESH_MOUTH,
                #     landmark_drawing_spec=None,
                #     connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_mouth_connections_style()
                # )

        # if results.multi_face_landmarks:
        #     for face_landmarks in results.multi_face_landmarks:

                # Extract landmarks
                # landmarks = face_landmarks.landmark
                # print(len(landmarks))
                # landmarks = np.array([(landmark.x, landmark.y, landmark.z) for landmark in landmarks])

                # calculate eye aspect ratio (EAR) to detect blink
                RIGHT_EYE = [33, 246, 161, 160, 159, 158, 157, 173, 133, 155, 154, 153, 145]
                MOUTH = [312, 57, 82, 315, 85, 287]
                right_eye = [face_landmarks.landmark[idx] for idx in MOUTH]
                right_eye_h = np.linalg.norm(right_eye[1].x - right_eye[5].x)
                right_eye_v1 = np.linalg.norm(right_eye[2].y - right_eye[4].y)
                right_eye_v2 = np.linalg.norm(right_eye[0].y - right_eye[3].y)
                EAR_right = (right_eye_v1 + right_eye_v2) / (2 * right_eye_h)

                # Here blink is detected
                if EAR_right > 0.3:
                    print("Blink")
                    # webcam.release()
                    # # cv2.destroyAllWindows()
                    # return True



        # display frame
        cv2.imshow('BCI keyboard', img)
        if cv2.waitKey(5) & 0xFF == 27:
            break

webcam.release()
cv2.destroyAllWindows()
