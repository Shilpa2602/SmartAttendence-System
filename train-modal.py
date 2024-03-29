import cv2
import numpy as np
import os
from PIL import Image
import pickle

base_dir=os.path.dirname(os.path.abspath(__file__))
image_dir=os.path.join(base_dir,"image")
face_cascade=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

#recognizer=cv2.readimg.LBPHFaceRecognizer_create()
recognizer= cv2.face.LBPHFaceRecognizer_create()

current_id=0
label_ids={}

y_label=[]
x_train=[]
i=0
for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path=os.path.join(root,file)
			label=os.path.basename(root).replace(" ","-").lower()
			#print(label,path)
			if not label in label_ids:
				label_ids[label]=current_id
				current_id+=1
			id_=label_ids[label]
			#print(label_ids)

			pil_image=Image.open(path).convert("L")
			'''size=(450,450)
			final_image=pil_image.resize(size,Image.ANTIALIAS)'''
			image_array=np.array(pil_image,"uint8")
			#print(image_array)
			face=face_cascade.detectMultiScale(image_array, scaleFactor = 1.3, minNeighbors = 5);
			for(x,y,w,h) in face:
				roi=image_array[y:y+h,x:x+w]
				'''cv2.imwrite('tmp/17223018/sss'+str(i)+'.png',roi)
				img1=cv2.imread('tmp/17223018/sss'+str(i)+'.png')
				'''
				 
				'''scale_percent = 60 # percent of original size
				width = int(img1.shape[1] * scale_percent / 100)
				height = int(img1.shape[0] * scale_percent / 100)
				dim = (width, height)
				# resize image
				resized = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)
				'''
				'''cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
				resized_image = cv2.resize(img1, (220, 220)) 
				cv2.imwrite('tmp/17223018/sss'+str(i)+'.png',resized_image)
				i=i+1'''
				x_train.append(roi)
				y_label.append(id_)

#print(y_label)
#print(x_train)
with open("labels.pickle",'wb') as f:
	pickle.dump(label_ids,f)
recognizer.train(x_train,np.array(y_label))
recognizer.save("trainner.yml")

