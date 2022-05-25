#Transfer learning - resnet152V2 .ipynb
 
# import packages
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from mtcnn.mtcnn import MTCNN

import os

model = load_model('1_MTCNN_Face_Mask_Detection/Outputs/cnn_model.h5') 
# model = load_model('1_MTCNN_Face_Mask_Detection/Outputs/mask_detector_vgg19.h5') 
# model accept below hight and width of the image
img_width, img_hight = 256, 256
 

detector = MTCNN() 
#startt  web cam
cap = cv2.VideoCapture(0) # for webcam
video_path='./test/video/'
#cap = cv2.VideoCapture(video_path+'testvideo_01.mp4') # for video
 
img_count_full = 0
 
#parameters for text
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
# org 
org = (1, 1) 
# fontScale 
fontScale = 1 #0.5
# Blue color in BGR 
color = (255, 0, 0) 
# Line thickness of 2 px 
thickness = 2 
 
while True:
    img_count_full += 1
     
    #read image from webcam
    responce, color_img = cap.read()
     
    #if respoce False the break the loop
    if responce == False:
        break    
     
    # Convert to grayscale
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

    faces = detector.detect_faces(gray_img)
    img_count = 0
    for face in faces:
        x, y, w, h = face['box']

        org = (x-10,y-10)
        img_count +=1 
        color_face = color_img[y:y+h,x:x+w] # color face
        cv2.imwrite('faces/input/%d%dface.jpg'%(img_count_full,img_count),color_face)
        img = load_img('faces/input/%d%dface.jpg'%(img_count_full,img_count), target_size=(img_width,img_hight))
         
        img = img_to_array(img)
        img = np.expand_dims(img,axis=0)
        pred_prob = model.predict(img)
        pred=np.argmax(pred_prob)
        if pred==0:
          print("User with mask - predic = ",pred_prob[0][0])  
          txt = 'Without Mask'
          color = (0,0,255)
          cv2.imwrite('faces/with_mask/%d%dface.jpg'%(img_count_full,img_count),color_face)
        else:
          print('user not wearing mask - prob = ',pred_prob[0][1])
          txt = 'With Mask'
          color = (0,255,0)
          cv2.imwrite('faces/without_mask/%d%dface.jpg'%(img_count_full,img_count),color_face)             
        cv2.rectangle(color_img, (x, y), (x+w, y+h), color, 3)
        cv2.putText(color_img, txt, org, font,  
                                   fontScale, color, thickness, cv2.LINE_AA) 
     
    # display image
    cv2.imshow('LIVE face mask detection', color_img)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
#delete all images
for f in os.listdir('./faces/input/'):
    os.remove(os.path.join('./faces/input/', f))
    print("deteted ", str(f))
