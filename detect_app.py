import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.preprocessing.image import smart_resize
from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
import glob
import cv2
from os.path import exists


output_path='./output_images'
input_path='./input_images'
def clean_input():
    dir = input_path
    for file in os.scandir(dir):
        os.remove(file.path)
    print("clean input sucessfully")

def clean_output():
    dir = output_path
    for file in os.scandir(dir):
        os.remove(file.path)
    print("clean output sucessfully")      



def check_input_exist():
    list_file = os.listdir(input_path) # dir is your directory path
    file_count = len(list_file)
    if file_count >0:
        return True
    return False



global file_count
def mask_detect(img):
  list_file = os.listdir(output_path) # dir is your directory path
  file_count = len(list_file)
  model = keras.models.load_model("1_MTCNN_Face_Mask_Detection/Outputs/cnn_model.h5")
  sns.set_theme(style="white", palette=None)
  img_ary = img_to_array(img)
  detector = MTCNN()
  faces = detector.detect_faces(img_ary)
  plt.figure(figsize=(15, 12))
  plt.imshow(img)
  ax = plt.gca()
  for face in faces:
    x1, y1, width, height = face['box']
    x2, y2 = x1+width, y1+height

    pred = model.predict(smart_resize(img_ary[y1:y2, x1:x2], (256, 256)).reshape(1, 256, 256, 3));
    # print("prediction")
    # print(pred)
    if pred[0][0] >= pred[0][1]:
      txt = 'Without Mask'
      color = 'red'
    else:
      txt = 'With Mask'
      color = 'lime'
    
    rect = Rectangle((x1, y1), width, height, fill=False, color=color, linewidth=2)
    ax.add_patch(rect)
    ax.text(x1, y1-2, txt, fontsize=14, fontweight='bold', color=color)
  
  plt.savefig(output_path+'/out%d.png'%(file_count), dpi=300,bbox_inches='tight')
  print("process sucessfully")
  messagebox.showinfo("information","Process sucessfully !")
  clean_input()
  
  # plt.show()
  
  
def run():
    if not check_input_exist():
        messagebox.showwarning("Warning", "Image is not selected")
    test_path = "./input_images"
    images = [cv2.imread(file) for file in glob.glob(test_path+"/*")]
    # print('There are {} test images'.format(len(images)))
    # print(test_path)
    # print(images)
    scaled_images =[]
    for img in images:
      dim = (256,256)
      if img.shape<(256, 256):
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        print('resized')
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      scaled_images.append(img)

    for image in scaled_images:
      mask_detect(image)

def UploadAction(event=None):
    list_file = os.listdir(input_path) # dir is your directory path
    file_count = len(list_file)
    #print(number_files)
    filename = filedialog.askopenfilename()
    split=filename.split('.')
    file_extension=split[-1]
    #shutil.copy(filename)
    if file_extension=="jpg":          
        shutil.copy(filename,input_path+'./in.jpg')
        print("saved file jpg")
        messagebox.showinfo("information","Upload sucessfully !")
    elif file_extension=="png":
        shutil.copy(filename,input_path+'./in.png')
        print("saved file png")
        messagebox.showinfo("information","Upload sucessfully !")
    else:
        print("file error !!!")
    # print('Selected:', filename)
    # print('extension:', file_extension)   
    

    
    


