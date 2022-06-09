# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:10:17 2022

@author: habib
"""

import tkinter as tk
from tkinter import *
import tkinter.font as font
import customtkinter
from tkinter import filedialog
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
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.grid()
        
        self.frameButton_home = tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        self.frameButton_home.grid(sticky="nswe", padx= 100, pady=30)
        customtkinter.CTkButton(self.frameButton_home, text='Détection par image', 
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), 
        text_color="white", command=self.make_page_1).grid(padx=50)
        
        customtkinter.CTkButton(self.frameButton_home, text='Détection par vidéo',
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), 
        text_color="white", command=self.make_page_2).grid(row=0, column=3, padx=50)
        
        self.page_1 = Page_1(master=self.root, app=self)
        # self.page_2 = Page_2(master=self.root, app=self)

    def main_page(self):
        self.frame.grid()
        self.frameButton_home.grid()
    def make_page_1(self):
        self.page_1.start_page()
        self.frameButton_home.grid_forget()
    def make_page_2(self):
        self.frame.grid_forget()
        # self.page_2.start_page() 


class Page_1:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        #self.frameBack = tk.Frame(self.master)
        self.frameBack = tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        
        tk.Label(self.frameBack, text='Detection by image', font=("Roboto Medium", 14)).grid()
        #tk.Button(self.frameBack, text='Go back', command=self.go_back).grid()
        
        #edemo new fram
        self.frameButton_P1 = tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        self.frameOutput=tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        self.frameSource=tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        
        btn_upload = customtkinter.CTkButton(self.frameButton_P1, text="Choirsir Image",
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white",command=self.UploadAction).grid(row=2,column=3, padx=50)
        
        btn_process = customtkinter.CTkButton(self.frameButton_P1, text="Traitement",
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white",command=run).grid(row=3,column=3, padx=50)
        
        btn_showRes = customtkinter.CTkButton(self.frameButton_P1, text="Résultat",
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white")#.grid(row=4,column=3, padx=50)
        # btn_showRes= Button(self.frameButton_P1, text="Resultat")
        btn_showRes.bind("<Button>",
             lambda e: Resultat(root))
        btn_showRes.grid(row=4,column=3, padx=50)
        
        btn_back = customtkinter.CTkButton(self.frameButton_P1, text="Back",
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white", command=self.go_back).grid(row=7,column=3, padx=50)


    def start_page(self):
       
        self.frameBack.grid(sticky=S)
        self.frameButton_P1.grid()
        
    def go_back(self):
        for widgets in self.frameOutput.winfo_children():
          widgets.destroy()
          

        self.frameButton_P1.grid_forget()
        self.frameBack.grid_forget()
        self.app.main_page()
        clean_output()
        self.frameSource.grid_forget()
    
    def UploadAction(self):
        list_file = os.listdir(input_path) # dir is your directory path
        file_count = len(list_file)

        filename = filedialog.askopenfilename()

        split=filename.split('.')
        file_extension=split[-1]
        #shutil.copy(filename)
        if file_extension=="jpg":          
            shutil.copy(filename,input_path+'./in.jpg')
            print("saved file jpg")
            messagebox.showinfo("information","Upload sucessfully !")
            self.frameSource.grid()
            self.show_input()
        elif file_extension=="png":
            shutil.copy(filename,input_path+'./in.png')
            print("saved file png")
            messagebox.showinfo("information","Upload sucessfully !")
            self.frameSource.grid()
            self.show_input()
        else:
            print("file error !!!")

    
    def show_input(self):
        list_file = os.listdir(input_path) # dir is your directory path
        file_count = len(list_file)
        for widgets in self.frameSource.winfo_children():
          widgets.destroy()
        label_titleImage = Label(self.frameSource, text="Your input", font=("Lato", 10))
        label_titleImage.grid()
        canvas = Canvas(self.frameSource, width = 330, height = 330)   
        canvas.grid()
        print(list_file[0])
        #img= (Image.open(input_path+'/out%d.png'%(file_count-1)))
        img=(Image.open(input_path+'/'+list_file[0]))
        
        resized_image= img.resize((340,330), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(20,20, anchor=NW, image=new_image)
        canvas.new_image=new_image
    
    def show_res(self):
        self.frameOutput.grid()
        list_file = os.listdir(output_path) # dir is your directory path
        file_count = len(list_file)
        for widgets in self.frameOutput.winfo_children():
          widgets.destroy()
        label_titleImage = Label(self.frameOutput, text="Your result", font=("Lato", 10))
        label_titleImage.grid()
        canvas = Canvas(self.frameOutput, width = 350, height = 350)   
        canvas.grid()
        img= (Image.open(output_path+'/out%d.png'%(file_count-1)))
        resized_image= img.resize((340,330), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(20,20, anchor=NW, image=new_image)
        canvas.new_image=new_image
        
        clean_input()
        # btn_saveRes= Button(self.frameButton_P1,text="Save your result",command=self.save_result).pack(side=BOTTOM)
class Resultat(Toplevel):
     
    def __init__(self, master = None):
         
        super().__init__(master = master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text ="This is a new Window")
        label.pack()
    def start_page(self):
        a=1        
if __name__ == '__main__':
    
    
    #Fenêtre principale
    root = Tk()

    # personnaliser la fenêtre
    root.title("Détection de masque")
    root.geometry("1080x720")
    #app.maxsize(1080, 720)
    root.minsize(640, 480)
    root.iconbitmap("R.ico")
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    # Frame de gauche
    frame_left = customtkinter.CTkFrame(root, bg="#d0ced0")
    frame_left.set_appearance_mode("light")
    frame_left.grid(row=0, column=0, sticky="nswe")
    
    # logo de univ
    img = ImageTk.PhotoImage(Image.open("logo_2.png").resize((200,160)))
    panel = Label(frame_left, image = img)
    panel.grid(padx=30, pady=30)

    frame_membres = LabelFrame(frame_left, text="Membres du l'équipe", 
                               bg="#d1d5d8", fg="#005DA4", font=("Roboto Medium", 10), padx=20, pady=15)
    frame_membres.grid(padx=20, pady=30)

    label_nom1 = Label(frame_membres, text="TRAN Minh Thang", bg="#d1d5d8", font=("Roboto Medium", 10))
    label_nom1.grid()
    label_nom2 = Label(frame_membres, text="KHERFI Bahia", bg="#d1d5d8", font=("Roboto Medium", 10))
    label_nom2.grid()
    label_nom3 = Label(frame_membres, text="LEWHE Habib", bg="#d1d5d8", font=("Roboto Medium", 10))
    label_nom3.grid()
    
    
    #frame de droite
    frame_right = customtkinter.CTkFrame(root)
    frame_right.set_appearance_mode("light")
    frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)


    # titre 
    frameTitle = Frame(frame_right, bg = "#ffffff", padx=10, pady=10, borderwidth= 1, relief="ridge")
    frameTitle.grid(sticky="nswe", padx= 100, pady=30)

    label_title = Label(frameTitle, text="Projet de Soutenance", font=("Roboto Medium", 35),
                        bg = "#ffffff", fg = "#005DA4")
    label_title.grid()

    label_subtitle = Label(frameTitle, text="Détection de masque avec Deep Learning",
                           font=("Roboto Medium",12), bg = "#ffffff", fg = "#005DA4", justify="center")
    label_subtitle.grid(pady=10)
    
    # frame menu
    # frameMenu = Frame(frame_right, padx=10, pady=10, bg="#d1d5d8") #d1d5d8
    # frameMenu.grid(sticky="nswe", padx= 100, pady=30)
    
    # frame résultat
    frame_result = LabelFrame(frame_right, text="Résultat", bg="#cffbe4", padx= 30, pady=30)
    frame_result.grid(sticky="nswe",padx= 100, pady=30)

    #from video
    frameVideo= Frame(root,bd=1)
    label_webcam=Label(frameVideo)
    # #label_webcam.grid(row=0,column=0)
    
    
    btn = Button(root,
             text ="Click to open a new window")
 

    btn.bind("<Button>",
         lambda e: Resultat(root))
 
    btn.grid(pady = 10)
    
    app = App(root)
    root.mainloop()