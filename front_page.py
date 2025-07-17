import tkinter as tk
from PIL import Image, ImageTk
import subprocess

class FrontPage:
    def __init__(self, root):
        self.root = root
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")
        self.root.geometry("1600x900+0+0")

        # === Background Image ===
        bg_img = Image.open("College_photo/what-is-FR.jpg")
        bg_img = bg_img.resize((1600, 900), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)

        bg_label = tk.Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=0, width=1600, height=900)

        # === WELCOME Text ===
        welcome_text = tk.Label(
            self.root,
            text="WELCOME TO FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Times New Roman", 24, "bold"),
            bg="#000000",
            fg="blue"
        )
        welcome_text.place(x=340, y=95)  

        # === START Button ===
        start_btn = tk.Button(
            self.root,
            text="START",
            font=("Times New Roman", 16, "bold"),
            bg="#007BFF",            
            fg="white",
            activebackground="#0056b3",
            activeforeground="white",
            bd=3,
            relief="ridge",
            command=self.open_login
        )
        start_btn.place(x=700, y=150, width=200, height=50)

    def open_login(self):
        subprocess.run(["python", "login.py"])  


if __name__ == "__main__":
    root = tk.Tk()
    app = FrontPage(root)
    root.mainloop()


