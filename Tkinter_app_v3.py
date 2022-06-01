import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from detect_app import run, UploadAction, clean_output,clean_input
from detect_video_v2 import run_video
import cv2
import os
import sys
import shutil
output_path='./output_images'
input_path='./input_images'
save_path='./save_result'  
class App:
    def __init__(self, root=None):
        frameLogo.pack(side="left",fill='y')
        frameTitle.pack()
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        # tk.Label(self.frame, text='Main page').pack()
        tk.Button(self.frame, text='Detection by image',
                  command=self.make_page_1).pack()
        tk.Button(self.frame, text='Detection by live video',
                  command=self.make_page_2).pack()
        self.page_1 = Page_1(master=self.root, app=self)
        self.page_2 = Page_2(master=self.root, app=self)

    def main_page(self):
        self.frame.pack()
        

    def make_page_1(self):
        self.frame.pack_forget()
        self.page_1.start_page()
    def make_page_2(self):
        self.frame.pack_forget()
        self.page_2.start_page()


class Page_1:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frameBack = tk.Frame(self.master)
        self.frameTitlPage=tk.Frame(self.master)
        
        tk.Label(self.frameTitlPage, text='Detection by image').pack()
        tk.Button(self.frameBack, text='Go back', command=self.go_back).pack()
        #edemo new fram
        self.frameButton_P1 = tk.Frame(self.master,bd=1)
        self.frameImage=tk.Frame(self.master,bd=1)
        self.frameSource=tk.Frame(self.master,bd=1)
        btn_upload = Button(self.frameButton_P1, text="Upload Image",command=UploadAction).pack()
        btn_process = Button(self.frameButton_P1, text="Process",command=run).pack()
        btn_showRes = Button(self.frameButton_P1, text="Result",command=self.show_res).pack()
        # btn_saveRes= Button(self.frameBottom,text="Save your result",command=self.save_result).pack(anchor=N)
       
        
        
    def start_page(self):
        self.frameTitlPage.pack()
        #frameTitle.pack()
        self.frameBack.pack()
        self.frameButton_P1.pack()
        # self.frameImage.pack()
        

    def go_back(self):
        for widgets in self.frameImage.winfo_children():
          widgets.destroy()
        self.frameImage.pack_forget()
        self.frameTitlPage.pack_forget()
        self.frameButton_P1.pack_forget()
        self.frameBack.pack_forget()
        self.app.main_page()
        clean_output()
    
        self.frameImage.pack_forget()
        self.frameSource.pack_forget()
    def show_res(self):
        self.frameImage.pack(side=RIGHT)
        self.frameSource.pack(side=LEFT)
        self.show_source()
        list_file = os.listdir(output_path) # dir is your directory path
        file_count = len(list_file)
        for widgets in self.frameImage.winfo_children():
          widgets.destroy()
        label_titleImage = Label(self.frameImage, text="Your result", font=("Lato", 10))
        label_titleImage.pack()
        canvas = Canvas(self.frameImage, width = 350, height = 350)   
        canvas.pack()
        img= (Image.open(output_path+'/out%d.png'%(file_count-1)))
        resized_image= img.resize((340,330), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(20,20, anchor=NW, image=new_image)
        canvas.new_image=new_image
        
        clean_input()
        btn_saveRes= Button(self.frameButton_P1,text="Save your result",command=self.save_result).pack(side=BOTTOM)
    def save_result(self):
        list_file_sc = os.listdir(output_path) # dir is your directory path
        file_count_sc = len(list_file_sc)
        filename = output_path+'/out%d.png'%(file_count_sc-1)
        
        list_file_dst = os.listdir(save_path) # dir is your directory path
        file_count_dst = len(list_file_dst)
        shutil.copy(filename,save_path+'/save_result%d.png'%(file_count_dst))
        messagebox.showinfo("information","Save sucessfully as name "+" 'save_result%d.png' "%(file_count_dst)+ " !")
        
        
    def show_source(self):
        list_file = os.listdir(input_path) # dir is your directory path
        file_count = len(list_file)
        for widgets in self.frameSource.winfo_children():
          widgets.destroy()
        label_titleImage = Label(self.frameSource, text="Your Source", font=("Lato", 10))
        label_titleImage.pack()
        canvas = Canvas(self.frameSource, width = 330, height = 330)   
        canvas.pack()
        #img= (Image.open(input_path+'/out%d.png'%(file_count-1)))
        img=(Image.open(input_path+'/'+list_file[0]))
        
        
        resized_image= img.resize((340,330), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(20,20, anchor=NW, image=new_image)
        canvas.new_image=new_image
class Page_2:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        #new frame
        # self.frameVideo=tk.Frame(self.master,bd=1)
        self.frameButton_P2 = tk.Frame(self.master,bd=1)
        
        tk.Label(self.frame, text='detection by video').pack()
        tk.Button(self.frame, text='Go back', command=self.go_back).pack()
        
        tk.Button(self.frameButton_P2,text='start video',command=run_video).pack()
        

    def start_page(self):
        self.frame.pack()
        self.frameButton_P2.pack()
        
        # self.frameVideo.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()
        self.frameButton_P2.pack_forget()
        
    # def show_webcam(self):
    #     label_webcam=Label(self.frameVideo).pack
    #     cap= cv2.VideoCapture(0)
    #     # Get the latest frame and convert into Image
    #     cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    #     img = Image.fromarray(cv2image)
    #     # Convert image to PhotoImage
    #     imgtk = ImageTk.PhotoImage(image = img)
    #     # label_webcam.imgtk = imgtk
    #     label_webcam.configure(image=imgtk)
    #     # Repeat after an interval to capture continiously
    #     label_webcam.after(20, self.show_webcam)   


if __name__ == '__main__':
    #root
    root = tk.Tk()
    root.geometry("800x650")
    root.title("Détection de masque")
    # root.minsize(640, 480)
    root.iconbitmap("R.ico")
    
    #frameTitle
    frameTitle = Frame(root,bd=1)
    label_title = Label(frameTitle, text="Projet de Soutenance", font=("Lato", 15)).pack()
    label_subtitle = Label(frameTitle, text="Application de détection de masque ", font=("Lato", 15)).pack()
    #frameLogo
    frameLogo = Frame(root,bd=1)
    img = ImageTk.PhotoImage(Image.open("logo.png").resize((110,100)))
    panel = Label(frameLogo, image = img).pack()
    #frameImage
    # frameImage = Frame(root,bd=1)
    # frameImage.pack(side='bottom',fill='y')
    #from video
    frameVideo= Frame(root,bd=1)
    label_webcam=Label(frameVideo)
    # #label_webcam.grid(row=0,column=0)
    
    app = App(root)
    root.mainloop()