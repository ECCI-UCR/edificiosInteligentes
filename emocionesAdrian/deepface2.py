#emotion_detection.py
import cv2
from deepface import DeepFace
import numpy as np  #this will be used later in the process

verification = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
print(verification)
