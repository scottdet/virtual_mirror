from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import datetime
import argparse
import imutils
import math
import time
import dlib
import cv2
import os

# -------------------------------------------------------------------------------------------
# 	Input arguments, dlib face detector initilization, start webcam, load hat
# -------------------------------------------------------------------------------------------

# initialize dlib's face detector (HOG-based) and then create the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

hat_dict = {}

# load our overlay images
hats = os.listdir('hats') 	# returns a list of directory items
for i in hats:
	hat_dict[i] = cv2.imread('hats/' + i, cv2.IMREAD_UNCHANGED)

# -------------------------------------------------------------------------------------------
# 	Helper function
# -------------------------------------------------------------------------------------------

def add_img(img1, img2):
    for i in range(img1.shape[0]):
        for j in range(img1.shape[1]):
            if img2[i][j][0] != 0:
                img1[i][j] = img2[i][j][0:3]
    return img1

# -------------------------------------------------------------------------------------------
# 	Main program loop
# -------------------------------------------------------------------------------------------

def getFrame(frame):
	# detect faces in the grayscale frame
	frame = imutils.resize(frame, width = 500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 0)

	# loop over the face detections
	for (i, rect) in enumerate(rects):

		# ---------------------------------------------------------------------------
		#	Distances and angles calculate for later use
		# ---------------------------------------------------------------------------
	
		shape = predictor(gray, rect)
		dY = shape.part(39).y - shape.part(42).y
       	 	dX = shape.part(39).x - shape.part(42).x
        	angle = int(np.degrees(np.arctan2(dX, dY)) + 90)
		center = ((shape.part(39).x + shape.part(42).x) // 2, (shape.part(39).y + shape.part(42).y) // 2)
		
		rot_hat = hat_dict['hat' + str(-1*angle) + '.png']
		
		jaw_x = math.pow((shape.part(16).x - shape.part(0).x), 2)
		jaw_y = math.pow((shape.part(16).y - shape.part(0).y), 2)
		jaw_dist = int(math.sqrt(jaw_x + jaw_y))
		
		# ---------------------------------------------------------------------------
		#	Hat placement based on angle
		# ---------------------------------------------------------------------------

		w_2 = int(1.15*jaw_dist)
		h_2 = int(1.15*jaw_dist)

		coord_1 = int(center[0] + (0.5*(w_2/1.1)) - (1.6*angle))
		coord_2 = int(center[1] - (0.1*(h_2/1.1)) + (0.3*angle))

        	# resize and place hat
		final_hat = cv2.resize(rot_hat, (w_2, h_2))
		roi = frame[coord_2-h_2:coord_2, coord_1-w_2:coord_1]
		dst = add_img(roi, final_hat)
		frame[coord_2-h_2:coord_2, coord_1-w_2:coord_1] = dst

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	return frame

