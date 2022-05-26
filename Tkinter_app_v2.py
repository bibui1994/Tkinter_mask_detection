import sys
from tkinter import *
import cv2
import os
from PIL import ImageTk, Image
from detect_app import run, UploadAction
from detect_video_v2 import run_video_demo


output_path='./output_images'
input_path='./input_images'

def clear_frame():
    #frameImage,frameWebcam, frameButton
    return 0

def show_webcam():
    # Get the latest frame and convert into Image
    # run_video_demo(cap)
    # cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    cv2image = run_video_demo(cap)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label_webcam.imgtk = imgtk
    label_webcam.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label_webcam.after(20, show_webcam)
    
def frame_webcam():
    for widgets in frameWebcam.winfo_children():
      widgets.destroy()
    btn_process_webcam = Button(frameWebcam, text="Open webcam",command=show_webcam_2)
    btn_process_webcam.pack(expand=YES)
    

def show_webcam_2():
    # Get the latest frame and convert into Image
    
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label_webcam.imgtk = imgtk
    label_webcam.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label_webcam.after(20, show_webcam_2)    
    
    
def show_res():
    list_file = os.listdir(output_path) # dir is your directory path
    file_count = len(list_file)
    for widgets in frameImage.winfo_children():
      widgets.destroy()
    label_titleImage = Label(frameImage, text="your result", font=("Lato", 40))
    label_titleImage.pack()
    canvas = Canvas(frameImage, width = 500, height = 500)   
    canvas.pack()
    img= (Image.open(output_path+'/out%d.png'%(file_count-1)))
    resized_image= img.resize((460,450), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    canvas.create_image(20,20, anchor=NW, image=new_image)
    canvas.new_image=new_image


def detect_img():
    for widgets in frameButton.winfo_children():
      widgets.destroy()
    for widgets in frameWebcam.winfo_children():
      widgets.destroy()  
    #up
    btn_upload = Button(frameButton, text="Upload Image",command=UploadAction)
    btn_upload.pack(expand=YES)

    #process
    btn_process = Button(frameButton, text="Process Image",command=run)
    btn_process.pack(expand=YES)

    #show res
    btn_res= Button(frameButton, text="show resultat",command=show_res)
    btn_res.pack(expand=YES) 

    
def detect_webcam():
    #code here
    a =0    
    
    

app = Tk()


# personnaliser la fenêtre
app.title("Détection de masque")
app.geometry("720x830")
app.minsize(640, 480)
app.iconbitmap("R.ico")


# logo de univ
frameLogo = Frame(app)
frameLogo.pack(side="left",fill='y')


img = ImageTk.PhotoImage(Image.open("logo.png").resize((110,100)))
panel = Label(frameLogo, image = img)
panel.pack()

# titre
frameTitle = Frame(app,bd=1,relief=SUNKEN)
frameTitle.pack(side='top',fill='y')


#affichier res
frameImage = Frame(app,bd=1,relief=SUNKEN)
frameImage.pack(side='bottom',fill='y')


#nom etudiant
frameEtudiant = Frame(app,bd=1,relief=SUNKEN)
frameEtudiant.pack(side='left',fill='y')
#button upload, process, resultat
frameButton=Frame(app,bd=1,relief=SUNKEN)
frameButton.pack(expand=1)
#frame webcam
frameWebcam = Frame(app,bd=1,relief=SUNKEN)
frameWebcam.pack()
label_webcam=Label(frameImage)
label_webcam.pack()
cap= cv2.VideoCapture(0)


#menu
var = StringVar()
frameMenu= Frame(app,bd=1,relief=SUNKEN)
frameMenu.pack(side='left',fill='y')
#detect by image
cb_image = Radiobutton(frameMenu, text='Image',variable=var, value='detect by image',command=detect_img)
cb_image.pack(anchor = W )
#detect by webcam
cb_live = Radiobutton(frameMenu, text='live video',variable=var, value='detect by live video',command=frame_webcam)
cb_live.pack(anchor = W )


# #up
# btn_upload = Button(frameButton, text="Upload Image",command=UploadAction)
# btn_upload.pack(expand=YES)
# #process
# btn_process = Button(frameButton, text="Process Image",command=run)
# btn_process.pack(expand=YES)
# #show res
# btn_res= Button(frameButton, text="show resultat",command=show_res)
# btn_res.pack(expand=YES) 




# label_titleImage = Label(frameImage, text="your result", font=("Lato", 40))
# label_titleImage.grid()

label_title = Label(frameTitle, text="Projet de Soutenance", font=("Lato", 40))
label_title.pack()



label_subtitle = Label(frameTitle, text="Application de détection de masque ", font=("Lato", 20))
label_subtitle.pack()








# afficher la fenêtre
app.mainloop()
