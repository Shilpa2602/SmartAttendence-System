import cv2
import time

path='bks'
camera = cv2.VideoCapture(0)
i=108
#for i in range(105):
while(i<=1100):
    return_value, image = camera.read()
    #while(True):
    cv2.imshow('image',image)
    #cv2.imwrite('image/bhushan/'+str(i)+'.jpg', image)
    time.sleep(50)
    i+=1
    
del(camera)
