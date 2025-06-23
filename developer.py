from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1540x850+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)
        
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 32, "bold"),
                          bg="white", fg="skyblue")
        title_lbl.place(x=0, y=10, width=1540, height=45)

        
        top_img = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\1576061014235.jpeg")
        top_img = top_img.resize((1540, 765), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(top_img)

        top_label = Label(self.root, image=self.photoimg_top)
        top_label.place(x=0, y=60, width=1540, height=765)        
        
        
        # ================Main Frame===================
        main_frame = Frame(top_label, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=1000, y=0, width=500, height=600) 
        
        top_img1 = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\ruchika.jpeg")
        top_img1 = top_img1.resize((200, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(top_img1)

        top_label1 = Label(main_frame, image=self.photoimg_top1)
        top_label1.place(x=300, y=0, width=200, height=200)                

        # Developer info
        dev_label = Label(main_frame, text="Hello! my name is Ruchika Jaiswal", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        dev_label.place(x=0,y=5)   
        
        dev_label = Label(main_frame, text="I am full stack developer", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        dev_label.place(x=0,y=40)  
        
        img1 = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\4745b4cea8eaec3fe5010ef7e5052685.jpg")
        img1 = img1.resize((500, 390), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl1 = Label(main_frame, image=self.photoimg1)
        lbl1.place(x=0, y=210, width=500, height=390)                    
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()        
        