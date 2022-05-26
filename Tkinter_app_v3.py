import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from detect_app import run, UploadAction
import cv2
import os
import sys
output_path='./output_images'
input_path='./input_images'
# def show_res():
#     list_file = os.listdir(output_path) # dir is your directory path
#     file_count = len(list_file)
#     for widgets in frameImage.winfo_children():
#       widgets.destroy()
#     label_titleImage = Label(frameImage, text="your result", font=("Lato", 10))
#     label_titleImage.pack()
#     canvas = Canvas(frameImage, width = 350, height = 350)   
#     canvas.pack()
#     img= (Image.open(output_path+'/out%d.png'%(file_count-1)))
#     resized_image= img.resize((340,330), Image.ANTIALIAS)
#     new_image= ImageTk.PhotoImage(resized_image)
#     canvas.create_image(20,20, anchor=NW, image=new_image)
#     canvas.new_image=new_image
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
        btn_upload = Button(self.frameButton_P1, text="Upload Image",command=UploadAction).pack()
        btn_process = Button(self.frameButton_P1, text="Process",command=run).pack()
        btn_showRes = Button(self.frameButton_P1, text="Resultat",command=self.show_res).pack()


    def start_page(self):
        self.frameTitlPage.pack()
        #frameTitle.pack()
        self.frameBack.pack()
        self.frameButton_P1.pack()
        frameImage.pack()

    def go_back(self):
        self.frameTitlPage.pack_forget()
        self.frameButton_P1.pack_forget()
        self.frameBack.pack_forget()
        self.app.main_page()
        
        frameImage.pack_forget()
    def show_res(self):
        list_file = os.listdir(output_path) # dir is your directory path
        file_count = len(list_file)
        for widgets in frameImage.winfo_children():
          widgets.destroy()
        label_titleImage = Label(frameImage, text="your result", font=("Lato", 10))
        label_titleImage.pack()
        canvas = Canvas(frameImage, width = 350, height = 350)   
        canvas.pack()
        img= (Image.open(output_path+'/out%d.png'%(file_count-1)))
        resized_image= img.resize((340,330), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        canvas.create_image(20,20, anchor=NW, image=new_image)
        canvas.new_image=new_image    
        

class Page_2:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master)
        tk.Label(self.frame, text='Page 2').pack()
        tk.Button(self.frame, text='Go back', command=self.go_back).pack()

    def start_page(self):
        #frameTitle.pack()
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()        


if __name__ == '__main__':
    #root
    root = tk.Tk()
    root.geometry("480x640")
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
    frameImage = Frame(root,bd=1)
    # frameImage.pack(side='bottom',fill='y')
    
    
    app = App(root)
    root.mainloop()