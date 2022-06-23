# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:10:17 2022

@author: habib
"""

import tkinter as tk
from tkinter import *
# import tkinter.font as font
import customtkinter
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from detect_img import run, clean_output,clean_input
from detect_video import run_video
import cv2
import os
# import sys
import shutil





output_path='./output_images'
input_path='./input_images'




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
        self.page_2 = Page_2(master=self.root, app=self)

    def main_page(self):
        self.frame.grid()
        self.frameButton_home.grid()
    def make_page_1(self):
        self.page_1.start_page()
        self.frameButton_home.grid_forget()
    def make_page_2(self):
        # self.frame.grid_forget()
        self.frameButton_home.grid_forget()
        self.page_2.start_page()


class Page_1:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        
        tk.Label(self.frame, text='Détection par image', font=("Roboto Medium", 14)).grid()
        #tk.Button(self.frameBack, text='Go back', command=self.go_back).grid()
        
        #edemo new fram
        self.frameButton_P1 = tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        # self.frameOutput=tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        # self.frameSource=tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        
        btn_upload = customtkinter.CTkButton(self.frameButton_P1, text="Choirsir Image",
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white",command=self.UploadAction).grid(row=2,column=3, padx=50, pady=5)
        
        btn_process = customtkinter.CTkButton(self.frameButton_P1, text="Détection",
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white",command=lambda:[run(), self.result()]).grid(row=3,column=3, padx=50)
        
        # btn_showRes = customtkinter.CTkButton(self.frameButton_P1, text="Résultat",
        # fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white", command=self.result).grid(row=4,column=3, padx=50, pady=5)
        
        btn_back = customtkinter.CTkButton(self.frameButton_P1, text="Retour",
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white", command=self.go_back).grid(row=7,column=3, padx=50, pady=5)


    def start_page(self):
       
        self.frame.grid(sticky=S)
        self.frameButton_P1.grid()
        
    def go_back(self):
     
          

        self.frameButton_P1.grid_forget()
        self.frame.grid_forget()
        self.app.main_page()
        clean_output()
     
    
    def UploadAction(self):
        # list_file = os.listdir(input_path) # dir is your directory path
        # file_count = len(list_file)

        filename = filedialog.askopenfilename()
        split=filename.split('.')
        file_extension=split[-1]
        #shutil.copy(filename)
        if file_extension=="jpg":          
            shutil.copy(filename,input_path+'./in.jpg')
            print("saved file jpg")
            messagebox.showinfo("information","Upload sucessfully !")
            #anglais
        elif file_extension=="png":
            shutil.copy(filename,input_path+'./in.png')
            print("saved file png")
            messagebox.showinfo("information","Upload sucessfully !")
            #anglais

        else:
            print("file error !!!")

        # btn_saveRes= Button(self.frameButton_P1,text="Save your result",command=self.save_result).pack(side=BOTTOM)
        
    def result(self):
        
        list_file_input = os.listdir(input_path) # dir is your directory path
        file_count_input = len(list_file_input)
        
        list_file_output = os.listdir(output_path) # dir is your directory path
        file_count_output = len(list_file_output)
        if file_count_input == 0:
            tk.messagebox.showerror(title="Error", message="no input, no output")
            #anglais
            
        elif file_count_output==0:
            tk.messagebox.showerror(title="Error", message="click button traitement to show output")
            #anglais
        else:
            win = Toplevel(root)
            win.title("Résultat")
            win.geometry("800x450")
            win.maxsize(800,450)
            win.minsize(800,450)
            self.frame_left = customtkinter.CTkFrame(win,fg_color=None)
            self.frame_left.set_appearance_mode("light")
            self.frame_left.grid(row=0, column=0,padx=20, pady=20)
            
            self.frame_right = customtkinter.CTkFrame(win,fg_color=None)
            self.frame_right.set_appearance_mode("light")
            self.frame_right.grid(row=0, column=1, padx=20, pady=20)
            
            self.show_input()
            self.show_res()
            #bouton saugarder
            # clean_output()
            
            btn_back = customtkinter.CTkButton(win, text="Saugarder Résultat ",
            fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white",command=self.saugarder)
            # btn_back.grid(sticky=SE)
            btn_back.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
            

        
    def show_input(self):
        list_file = os.listdir(input_path) # dir is your directory path
        file_count = len(list_file)
        for widgets in self.frame_left.winfo_children():
          widgets.destroy()
        label_titleImage = Label(self.frame_left, text="Votre image", font=("Roboto Medium", 10))
        label_titleImage.grid()
        canvas = Canvas(self.frame_left, width = 350, height = 350)   
        canvas.grid()
        print(list_file[0])
        #img= (Image.open(input_path+'/out%d.png'%(file_count-1)))
        img=(Image.open(input_path+'/'+list_file[0]))
        
        resized_image= img.resize((340,330), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(20,20, anchor=NW, image=new_image)
        canvas.new_image=new_image
        
    def show_res(self):
    
        list_file = os.listdir(output_path) # dir is your directory path
        file_count = len(list_file)
        for widgets in self.frame_right.winfo_children():
          widgets.destroy()
        label_titleImage = Label(self.frame_right, text="Le Résultat", font=("Roboto Medium", 10))
        label_titleImage.grid()
        canvas = Canvas(self.frame_right, width = 350, height = 350)   
        canvas.grid()
        img= (Image.open(output_path+'/out%d.png'%(file_count-1)))
        resized_image= img.resize((340,330), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(20,20, anchor=NW, image=new_image)
        canvas.new_image=new_image
        
        clean_input()
    def saugarder(self):
        list_file = os.listdir(output_path) # dir is your directory path
        im=(Image.open(output_path+'/'+list_file[0]))
        file = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
        if file:
            abs_path = os.path.abspath(file.name)

            im.save(abs_path) # saves the image to the input file name. 
        clean_output()
        messagebox.showinfo("information","Save sucessfully !")
        #anglais
class Page_2:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        tk.Label(self.frame, text='Détection par vidéo', font=("Roboto Medium", 14)).grid()
        
        self.frameButton_home = tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        self.frameButton_home.grid(sticky="nswe", padx= 100, pady=30)
   
        self.frameButton_P2 = tk.Frame(frame_right,padx=10, pady=10, bg="#d1d5d8")
        
        btn_start = customtkinter.CTkButton(self.frameButton_P2, text="Start video",#anglais
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white",command=run_video).grid(row=0,column=3, padx=50, pady=5)
        btn_retour = customtkinter.CTkButton(self.frameButton_P2, text="Retour",
        fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white",command=self.go_back).grid(row=2,column=3, padx=50, pady=5)

    def start_page(self):
        self.frame.grid()
        self.frameButton_home.grid()
        self.frameButton_P2.grid()
        
        # self.frameVideo.pack()

    def go_back(self):
        
        self.frame.grid_forget()
        self.app.main_page()
        self.frameButton_P2.grid_forget()

if __name__ == '__main__':
    
    
    #Fenêtre principale
    root = Tk()

    # personnaliser la fenêtre
    root.title("Détection de masque")
    root.geometry("1080x720")
    root.maxsize(1080, 720)
    root.minsize(1080, 720)
    root.iconbitmap("img_GUI/R.ico")
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    
    # Frame de gauche
    frame_left = customtkinter.CTkFrame(root, bg="#d0ced0")
    frame_left.set_appearance_mode("light")
    frame_left.grid(row=0, column=0, sticky="nswe")
    
    # logo de univ
    img = ImageTk.PhotoImage(Image.open("img_GUI/logo.png").resize((200,160)))
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
    
    frame_supervisor = LabelFrame(frame_left, text="Sous la supervision de :", 
                               bg="#d1d5d8", fg="#005DA4", font=("Roboto Medium", 10), padx=20, pady=15)
    frame_supervisor.grid(padx=20, pady=30)
    
    label_nom1 = Label(frame_supervisor, text="Mme Imane YOUKANA", bg="#d1d5d8", font=("Roboto Medium", 10))
    label_nom1.grid()
    
    
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


    #from video
    frameVideo= Frame(root,bd=1)
    label_webcam=Label(frameVideo)
    # #label_webcam.grid(row=0,column=0)
    
    app = App(root)
    root.mainloop()
    
