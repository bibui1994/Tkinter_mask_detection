import tkinter
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
import customtkinter
import tkinter as tk
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
