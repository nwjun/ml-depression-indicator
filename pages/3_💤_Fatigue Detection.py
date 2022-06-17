import streamlit as st
import numpy as np
import cv2
import time
import mediapipe as mp  # for facemesh and landmarks
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks

def get_landmark(face_landmarks):
        # extract landmarks for both eyes
        left_eyes = []
        right_eyes = []

        for i in [33, 173, 160, 158, 144, 153]:
            result = face_landmarks.landmark[i]
            right_eyes.append(np.array([result.x, result.y]))
        for i in [263, 398, 385, 387, 380, 373]:
            result = face_landmarks.landmark[i]
            left_eyes.append(np.array([result.x, result.y]))

        return left_eyes, right_eyes
    
def manhattan_distance(a, b):
    # distance between two points
    return np.abs(a - b).sum()

def count_ear(eyes_arr):
    # calculate the EAR for one eyes
    hori = eyes_arr[:2]
    top = eyes_arr[2:4]
    bot = eyes_arr[4:]
    ear = (manhattan_distance(top[0], bot[0]) + manhattan_distance(top[1], bot[1])) / (2 * manhattan_distance(hori[0], hori[1]))
    return ear

def average(arr):
    return sum(arr) / len(arr)

def calculatePeaks(np_arr, noise_removal=True, window_length=9, polyorder=5):
    if noise_removal:
        arr = savgol_filter(np_arr, window_length, polyorder)
    else:
        arr = np_arr
    # flip horizontally
    peaks = find_peaks(-arr, prominence=0.009)

    return arr, peaks

# Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# index of eyes landmarks from Mediapipe FaceMesh 
LEFT_EYES = [263, 398, 385, 387, 380, 373]
RIGHT_EYES = [33, 173, 160, 158, 144, 153]

# variables
startTime = 0
fig, ax = plt.subplots()
numBlinks = 0
fatigue = False
arr = []

st.header("Fatigue Detection")
st.write("Use your device normally for 1 minute to detect your fatigue. Before you start, please ensure the surrounding has adequate lighting.")
source = st.slider('Video source', min_value=-1, max_value=3, value=0)
st.caption("*Try changing the video source if it fails to start the webcam*")

SHOW_FACE_MESH = st.checkbox("Show face mesh")
SHOW_EYES_LANDMARKS = st.checkbox("Show eyes landmarks")
SHOW_LANDMARKS_NUM = st.checkbox("Show number of index of eyes landmarks")
run = st.checkbox('Start recording')

cap = cv2.VideoCapture(source)

# show video stuff
FRAME_WINDOW = st.image([])
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

reset = st.button("Reset")
st.caption("*To reset, please uncheck *Start recording* first then press \"Reset\" Button*")

if reset:
    startTime = 0
    fig, ax = plt.subplots()
    numBlinks = 0
    fatigue = False
    arr = []
    run = False
    cap.release()

with mp_face_mesh.FaceMesh(
max_num_faces=1,  # only one face is processed
refine_landmarks=True,
min_detection_confidence=0.5,  # can play with the confidence here
min_tracking_confidence=0.5
) as face_mesh:
    while run:
        ret, frame = cap.read()

        if ret == False: break

        frame = cv2.flip(frame, 1)
        if startTime == 0:
            startTime = time.time()
            

        showFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = face_mesh.process(showFrame)

        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0]

            if (SHOW_FACE_MESH):
                mp_drawing.draw_landmarks(
                image=showFrame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_tesselation_style())

                mp_drawing.draw_landmarks(
                    image=showFrame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_contours_style())

            if SHOW_EYES_LANDMARKS:
                mp_drawing.draw_landmarks(
                    image=showFrame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_RIGHT_EYE,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_contours_style()
                )

                mp_drawing.draw_landmarks(
                    image=showFrame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_LEFT_EYE,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles
                    .get_default_face_mesh_contours_style()
                )
                
            if SHOW_LANDMARKS_NUM:
                landmarks = face_landmarks.landmark

                for i in LEFT_EYES:
                    landmark = landmarks[i]
                    origin = (int(landmark.x * w), int(landmark.y * h))
                    color = (255, 255,0) # BGR
                    cv2.circle(showFrame, origin, 2, color)
                    cv2.putText(showFrame, str(i+1), origin, cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                for i in RIGHT_EYES:
                    landmark = landmarks[i]
                    origin = (int(landmark.x * w), int(landmark.y * h))
                    color = (0,255,0)# BGR
                    cv2.circle(showFrame, origin, 2, color)
                    cv2.putText(showFrame, str(i+1), origin, cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            left_eyes, right_eyes = get_landmark(face_landmarks)
            
            for i in left_eyes:
                x, y = i
                # coordinates from Mediapipe are normalised,
                # so we will unnormalised them
                x, y = int(x*w), int(y*h) 

            for i in right_eyes:
                # same goes to the right eyes
                x, y = i
                x, y = int(x*w), int(y*h)

            ear_left = count_ear(left_eyes)
            ear_right = count_ear(right_eyes)
            avgEAR = (ear_left+ear_right) / 2
            arr.append(avgEAR)
            
            cv2.putText(showFrame, "Average EAR: " + str(avgEAR),(50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
        passedTime = time.time() - startTime
        cv2.putText(showFrame, "Passed Time(s): " + str(int(passedTime)),(50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        FRAME_WINDOW.image(showFrame)
        

        if passedTime >= 10:
            arr = np.array(arr)
            arr = arr/np.linalg.norm(arr)
            arr, peaks = calculatePeaks(arr) 
            numBlinks = peaks[0].shape[0]
            fatigue = True if numBlinks <= 6 else False
            ax.plot(arr)
            ax.scatter(peaks[0], arr[peaks[0]],color="red")
            ax.set_title("Peak Detection")
            ax.set_xlabel("Video Frames per Second")
            ax.set_ylabel("EAR Values")
            cap.release()
            break
            
    # Showing Result
    st.header('Result')

    if len(arr) != 0:    
        st.pyplot(fig)
        st.write("Number of blinks per minute: "+ str(numBlinks))
        st.write("**Fatigue: "+ str(fatigue) + "**")
           