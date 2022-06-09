from PIL import ImageGrab
import tkinter as tk
from tkinter import filedialog
import os
from PIL import ImageTk, Image
output_path='./output_images'
input_path='./input_images'
save_path='./save_result' 
root = tk.Tk()
tk.Entry(root).pack()

def save_pic():
    # file = filedialog.asksaveasfile(defaultextension='.png',filetypes=[
    #     ("file image",".png")])
    # list_file = os.listdir(input_path) # dir is your directory path
    # file_count = len(list_file)
    # img=(Image.open(input_path+'/'+list_file[0]))  
    # file.save(img)
    # file.close()
    
    
    list_file = os.listdir(input_path) # dir is your directory path
    file_count = len(list_file)
    im=(Image.open(input_path+'/'+list_file[0]))
    file = filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=(("PNG file", "*.png"),("All Files", "*.*") ))
    if file:
        abs_path = os.path.abspath(file.name)

        im.save(abs_path) # saves the image to the input file name. 

tk.Button(root,text="Click me",command=save_pic).pack()

root.mainloop()