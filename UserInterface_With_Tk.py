# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:30:28 2022

@author: habib
"""

# Utilisation de tkinter pour interface graphique en python

import tkinter
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
import customtkinter

#créer une première fenêtre
app = Tk()

# personnaliser la fenêtre
app.title("Détection de masque")
app.geometry("1080x720")
#app.maxsize(1080, 720)
app.minsize(640, 480)
app.iconbitmap("R.ico")
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# ajouter du contenu

# Frame de gauche
frame_left = customtkinter.CTkFrame(app, bg="#d0ced0", corner_radius=0)
frame_left.set_appearance_mode("light")
frame_left.grid(row=0, column=0, sticky="nswe")

# logo de univ
img = ImageTk.PhotoImage(Image.open("logo_2.png").resize((200,160)))
panel = Label(frame_left, image = img)
panel.grid(padx=30, pady=30)

frame_membres = LabelFrame(frame_left, text="Membres du l'équipe", 
                           bg="#e5e5e6", fg="#005DA4", font=("Roboto Medium", 10), padx=20, pady=15)
frame_membres.grid(padx=20, pady=30)

label_nom1 = Label(frame_membres, text="TRAN Minh Thang", bg="#e5e5e6", font=("Roboto Medium", 10))
label_nom1.grid()
label_nom2 = Label(frame_membres, text="KHERFI Bahia", bg="#e5e5e6", font=("Roboto Medium", 10))
label_nom2.grid()
label_nom3 = Label(frame_membres, text="LEWHE Habib", bg="#e5e5e6", font=("Roboto Medium", 10))
label_nom3.grid()

#frame de droite
#b3bbf7
#eaecfa
#005da4
#767476
frame_right = customtkinter.CTkFrame(app)
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

frameMenu = Frame(frame_right, padx=10, pady=10, bg="#e5e5e6")
frameMenu.grid(sticky="nswe", padx= 100, pady=30)

b1 = customtkinter.CTkButton(frameMenu, text='Détection par image', 
fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white").grid(padx=50)

b2 = customtkinter.CTkButton(frameMenu, text='Détection par vidéo',
fg_color= "#005DA4", text_font=(("Roboto Medium"), 10), text_color="white").grid(row=0, column=3, padx=50)


frame_result = LabelFrame(frame_right, text="Résultat", bg="#cffbe4", padx= 30, pady=30)
frame_result.grid(sticky="nswe",padx= 100, pady=30)


# afficher la fenêtre 
app.mainloop()