import cv2
import numpy as np
from deepface import DeepFace
import time

cap = cv2.VideoCapture(0)
time.sleep(5)
while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    #while True:
    #try:
    analyze = DeepFace.analyze(frame)
    print(analyze)
    #except:
    #   print("No face")

    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

cap.release()
cv2.destroyAllWindows()
