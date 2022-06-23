#Transfer learning - resnet152V2 .ipynb
 
# import packages
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from mtcnn.mtcnn import MTCNN
from tkinter import messagebox

import os
def clean():
    for f in os.listdir('./faces'):
        os.remove(os.path.join('./faces', f))
        print("deteted ", str(f))
    print("clean faces successfully! ")
    #anglais
    
def run_video():
    #cnn_model.h5
    model = load_model('model/Outputs/cnn_model_30_313.h5') 
    # model = load_model('1_MTCNN_Face_Mask_Detection/Outputs/mask_detector_vgg19.h5') 
    # model accept below hight and width of the image
    img_width, img_hight = 256, 256
     

    detector = MTCNN() 
    #startt  web cam
    cap = cv2.VideoCapture(0) # for webcam
    # video_path='./test/video/'
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
    if not cap.isOpened():
        print("webcam error")
        messagebox.showwarning("Warning", "Can not access webcam")
        #anglais
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
            cv2.imwrite('faces/%d%dface.jpg'%(img_count_full,img_count),color_face)
            img = load_img('faces/%d%dface.jpg'%(img_count_full,img_count), target_size=(img_width,img_hight))
             
            img = img_to_array(img)
            img = np.expand_dims(img,axis=0)
            pred_prob = model.predict(img)
            pred=np.argmax(pred_prob)
            if pred==0:
              print("user not wearing mask - predic = ",pred_prob[0][0])  
              txt = 'Without Mask'
              color = (0,0,255)
              cv2.imwrite('faces/%d%dface.jpg'%(img_count_full,img_count),color_face)
            else:
              print(' User with mask- prob = ',pred_prob[0][1])
              txt = 'With Mask'
              color = (0,255,0)
              cv2.imwrite('faces/%d%dface.jpg'%(img_count_full,img_count),color_face)             
            cv2.rectangle(color_img, (x, y), (x+w, y+h), color, 3)
            cv2.putText(color_img, txt, org, font,  
                                       fontScale, color, thickness, cv2.LINE_AA) 
         
        # display image
        #anglais
        cv2.imshow('LIVE face mask detection', color_img)
        # if cv2.getWindowProperty('LIVE face mask detection', cv2.WND_PROP_VISIBLE) <1:
        #     break 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
     
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
    #delete all images
    clean()

    


