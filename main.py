from tkinter import *
from PIL import Image, ImageTk
from student import Student
import tkinter
import os
from train import Train
from detect_face import Detect_Face 
from attendance import Attendance
from developer import Developer
from help import Help

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root  
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg="white")

        # Background Image
        bg_img = Image.open(r"College_photo/what-is-FR.jpg")
        bg_img = bg_img.resize((1600, 900), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=0, width=1600, height=900)

        # Header Images
        header_images = [
            "FR-Scan-Featured-01-scaled-1.jpeg",
            "may-2-1.1-1024x536.png",
            "N-1.jpg",
            "biometric-scanning-system-control-protection-smart-phone-scan-user-face-facial-recognition-technology-concept_48369-14730.jpg"
        ]

        for i, img_name in enumerate(header_images):
            img = Image.open(f"College_photo/{img_name}")
            img = img.resize((400, 120), Image.LANCZOS)
            setattr(self, f"photoimg_header_{i}", ImageTk.PhotoImage(img))
            Label(self.root, image=getattr(self, f"photoimg_header_{i}")).place(x=i * 400, y=0, width=400, height=120)

        # Title
        Label(self.root, text="FACE RECOGNITION SYSTEM", font=("times new roman", 36, "bold"), bg="white", fg="darkblue").place(x=0, y=120, width=1600, height=50)


        # Features
        features = [
            ("attendance-management-features.webp", "Student Details", self.student_details),
            ("facial-recognition-attendance-service-500x500.webp", "Detect Face", self.detect_face),
            ("facial-recognition.webp", "Student Attendance", self.attendance),
            ("13.webp", "Help Desk", self.help),
            ("may-2-1.1-1024x536.png", "Train Data", self.train),
            ("44.jpg", "Photos", self.open_img),
            ("leave-mng-system.webp", "Developer", self.developer),
            ("How-Does-Face-Recognition-Door-Access-Control-System-Works.webp", "Exit", self.iExit),
        ]

        x_positions = [180, 460, 740, 1020]
        y_positions = [200, 500]

        index = 0
        for y in y_positions:
            for x in x_positions:
                if index >= len(features):
                    break
                img_path, label_text, command = features[index]

                img = Image.open(f"College_photo/{img_path}")
                img = img.resize((220, 220), Image.LANCZOS)
                photo_img = ImageTk.PhotoImage(img)
                setattr(self, f"photoimg_{index}", photo_img)

                Button(self.root, image=photo_img, cursor="hand2", bg="white", command=command if command else None).place(x=x, y=y, width=220, height=220)
                Button(self.root, text=label_text, cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white", command=command if command else None).place(x=x, y=y+220, width=220, height=40)

                index += 1
                
                
                
    def iExit(self):
        exit_confirmation = tkinter.messagebox.askyesno("Face Recognition", "Do you want to exit this project?", parent=self.root)
        if exit_confirmation:
           self.root.destroy()
           

    def open_img(self):
        os.startfile("data")  

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def detect_face (self):
        self.new_window = Toplevel(self.root)
        self.app = Detect_Face (self.new_window)

    def attendance (self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer (self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
        
    def help (self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)         

# Main Program Run
if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()








