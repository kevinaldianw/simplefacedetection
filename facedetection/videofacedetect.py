import cv2
import numpy as np
import imutils

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Get Video from Webcam
video = cv2.VideoCapture(0) 

while 1:
       
	_, img = video.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
    		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
 
	cv2.imshow('Haar Cascade Face Detection',img)
	
	if cv2.waitKey(1) == 27:
		break



