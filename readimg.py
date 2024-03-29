import cv2
import numpy as np
import pickle
from PIL import Image
import urllib.request

face_cascade=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

recognizer= cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainner.yml")
labels={"name":"1"}
try:
    with open("labels.pickle", 'rb') as f:
    	og_labels = pickle.load(f)
    	labels = {v:k for k,v in og_labels.items()}
except EOFError:
    print("n")

img=cv2.imread("test.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face=face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 5);

print('Faces found: ', len(face))
#img1=[]
i=0;
for (x,y,w,h) in face:
	roi=gray[y:y+h,x:x+w]
	cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 2)
	roi = cv2.resize(roi, (220, 220))
	id_,conf=recognizer.predict(roi)
	name=labels[id_]
	#API_ENDPOINT = "http://localhost:2020/AttendenceSystem/Receive?name="
	#API_ENDPOINT=API_ENDPOINT+name
	#urllib.request.urlopen(API_ENDPOINT)
	print(name)
	'''if conf>60:
		name="Unknown"'''
	print(conf)

        #img1.append(roi)
	i+=1
	font = cv2.FONT_HERSHEY_SIMPLEX
	color = (255, 0, 0)
	stroke=2
	cv2.putText(img, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
	cv2.imwrite('bkss/sss'+str(i)+'.png',roi)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('1.jpg',img)
#cv2.imwrite('bhushan.png',img)
#cv2.imshow('imgage',img)
#img=cv2.imread("bks.jpg",0)
#print(img)
