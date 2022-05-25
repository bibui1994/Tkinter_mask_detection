import sys
from tkinter import *
import os
from PIL import ImageTk, Image
from detect_app import run
from detect_app import UploadAction

output_path='./output_images'

def show_res():
    def reset_frame():
        canvas.destroy()
        
    # if bool_canvas==True:
    #     reset_frame()
    #     bool_canvas= False
    
    list_file = os.listdir(output_path) # dir is your directory path
    file_count = len(list_file)
    for widgets in frameImage.winfo_children():
      widgets.destroy()
    label_titleImage = Label(frameImage, text="your result", font=("Lato", 40))
    label_titleImage.grid()
    canvas = Canvas(frameImage, width = 500, height = 500)   
    canvas.grid()
    img= (Image.open(output_path+'/out%d.png'%(file_count-1)))
    resized_image= img.resize((460,450), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    canvas.create_image(20,20, anchor=NW, image=new_image)
    canvas.new_image=new_image

    
    
    
    
    


# output_path='./output_images'
# input_path='./input_images'
# def UploadAction(event=None):
#     #print(number_files)
#     filename = filedialog.askopenfilename()
#     split=filename.split('.')
#     file_extension=split[-1]
#     #shutil.copy(filename)
#     if file_extension=="jpg":          
#         shutil.copy(filename,input_path+'./in.jpg')
#         print("saved file jpg")
#     elif file_extension=="png":
#         shutil.copy(filename,input_path+'./ind.png')
#         print("saved file png")
#     else:
#         print("file error !!!")
#     # print('Selected:', filename)
#     # print('extension:', file_extension)
    

#créer une première fenêtre
app = Tk()


# personnaliser la fenêtre
app.title("Détection de masque")
app.geometry("720x960")
app.minsize(640, 480)
app.iconbitmap("R.ico")


# logo de univ
frameLogo = Frame(app)
frameLogo.grid(row=1, column=1, columnspan=2)


img = ImageTk.PhotoImage(Image.open("logo.png").resize((110,100)))
panel = Label(frameLogo, image = img)
panel.grid(row=1, column=1, columnspan=2)

# titre
frameTitle = Frame(app,bg='#41B77F',bd=1,relief=SUNKEN)
frameTitle.grid(row=10, column=5, columnspan=10)
#affichier res
frameImage = Frame(app,bg='blue',bd=1,relief=SUNKEN)
frameImage.grid(row=15, column=5, columnspan=10)
#nom etudiant
frameEtudiant = Frame(app,bg='blue',bd=1,relief=SUNKEN)
frameEtudiant.grid(row=15, column=5, columnspan=10)
#menu
frameMenu= Frame(app,bg='blue',bd=1,relief=SUNKEN)
frameMenu.grid(row=15, column=5, columnspan=10)
#button upload, process, resultat
frameButton = Frame(app,bg='blue',bd=1,relief=SUNKEN)
frameButton.grid(row=15, column=5, columnspan=10)


# label_titleImage = Label(frameImage, text="your result", font=("Lato", 40))
# label_titleImage.grid()

label_title = Label(frameTitle, text="Projet de Soutenance", font=("Lato", 40))
label_title.grid()



label_subtitle = Label(frameTitle, text="Application de détection de masque ", font=("Lato", 20))
label_subtitle.grid()



btn_upload = Button(frameTitle, text="Upload Image",command=UploadAction)
# btn_upload.pack(expand=YES)
btn_upload.grid()



btn_process = Button(frameTitle, text="Process Image",command=run)
# btn_process.pack(expand=YES)
btn_process.grid()

btn_res= Button(frameTitle, text="show resultat",command=show_res)
# btn_process.pack(expand=YES) 
btn_res.grid()




# afficher la fenêtre
app.mainloop()