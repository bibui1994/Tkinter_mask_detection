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
    label_titleImage.pack()
    canvas = Canvas(frameImage, width = 500, height = 500)   
    canvas.pack()
    img= (Image.open(output_path+'/out%d.png'%(file_count-1)))
    resized_image= img.resize((460,450), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    canvas.create_image(20,20, anchor=NW, image=new_image)
    canvas.new_image=new_image
def sel():
   selection = "You selected the option(comming soon!) " + str(var.get())

   label_cb.config(text = selection)
    
    
    
    
    


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
frameLogo.pack(side="left",fill='y')


img = ImageTk.PhotoImage(Image.open("logo.png").resize((110,100)))
panel = Label(frameLogo, image = img)
panel.pack()

# titre
frameTitle = Frame(app,bg='#41B77F',bd=1,relief=SUNKEN)
frameTitle.pack(side='top',fill='y')


#affichier res
frameImage = Frame(app,bg='blue',bd=1,relief=SUNKEN)
frameImage.pack(side='bottom',fill='y')


#nom etudiant
frameEtudiant = Frame(app,bg='blue',bd=1,relief=SUNKEN)
frameEtudiant.pack(side='left',fill='y')


#menu
var = StringVar()
frameMenu= Frame(app,bg='blue',bd=1,relief=SUNKEN)
frameMenu.pack(side='left',fill='y')
# cb_image = Checkbutton(frameMenu, text='Image',variable=var1, onvalue=1, offvalue=0, command=print_selection)
cb_image = Radiobutton(frameMenu, text='Image',variable=var, value='detect by image',
                  command=sel)
cb_image.pack(anchor = W )
cb_live = Radiobutton(frameMenu, text='live video',variable=var, value='detect by live video',
                  command=sel)
cb_live.pack(anchor = W )
label_cb=Label(frameMenu)
label_cb.pack()

#button upload, process, resultat
frameButton=Frame(app,bg='blue',bd=1,relief=SUNKEN)
frameButton.pack(expand=1)

#up
btn_upload = Button(frameButton, text="Upload Image",command=UploadAction)
btn_upload.pack(expand=YES)
#process
btn_process = Button(frameButton, text="Process Image",command=run)
btn_process.pack(expand=YES)
#show res
btn_res= Button(frameButton, text="show resultat",command=show_res)
btn_res.pack(expand=YES) 




# label_titleImage = Label(frameImage, text="your result", font=("Lato", 40))
# label_titleImage.grid()

label_title = Label(frameTitle, text="Projet de Soutenance", font=("Lato", 40))
label_title.pack()



label_subtitle = Label(frameTitle, text="Application de détection de masque ", font=("Lato", 20))
label_subtitle.pack()








# afficher la fenêtre
app.mainloop()
