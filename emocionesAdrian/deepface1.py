#emotion_detection.py
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import numpy as np  #this will be used later in the process

imgpath = 'sad1.jpeg'  #put the image where this file is located and put its name here
image = cv2.imread(imgpath)
#plt.imshow(image[:,:,::-1])
#analyze = DeepFace.analyze(image,actions=['emotions'])  #here the first parameter is the image we want to 
analyze = DeepFace.analyze(image)  #here the first parameter is the image we want to 
#analyze #the second one there is the action
print(analyze)
input("Enter para salir")
