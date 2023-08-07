import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime


video_capture = cv2.VideoCapture(0)

# Load Known Images

yugen_image = face_recognition.load_image_file("images/yugen.jpg")
yugen_encoding = face_recognition.face_encoding(yugen_image)[0]

susmita_image = face_recognition.load_image_file("images/susmita.jpg")
susmita_encoding = face_recognition.face_encoding(susmita_image)[0]

bimlendra_image = face_recognition.load_image_file("images/bimlendra.jpg")
bimlendra_encoding = face_recognition.face_encoding(bimlendra_image)[0]

known_face_encodings = [yugen_encoding, susmita_encoding, bimlendra_encoding]
known_face_names = ["Yugen", "Susmita", "Bimlendra"]


# list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get current time and date
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")