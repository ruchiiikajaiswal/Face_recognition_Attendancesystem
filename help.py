from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1540x850+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)
        
        title_lbl = Label(self.root, text="HELP  DESK", font=("times new roman", 32, "bold"),
                          bg="white", fg="skyblue")
        title_lbl.place(x=0, y=10, width=1540, height=45)

        
        top_img = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\13.webp")
        top_img = top_img.resize((1540, 765), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(top_img)

        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=60, width=1540, height=765) 
        
        
        # help desk
        dev_label = Label(top_label, text="Email : ruchika.cse22@satyug.edu.in", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        dev_label.place(x=686,y=290)   
        
          
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()           