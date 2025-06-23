from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import mysql.connector
from register import Register
from main import FaceRecognitionSystem

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1600x900+0+0")

        # Background Image
        bg_img = Image.open("College_photo/what-is-FR.jpg")
        bg_img = bg_img.resize((1600, 900), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=0, width=1600, height=900)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open("College_photo/9.webp")
        img1 = img1.resize((200, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimg1, bg="black", borderwidth=0)
        lblimg1.place(x=680, y=185, width=200, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=110)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        img2 = Image.open("College_photo/6681204.png").resize((25, 25), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("College_photo/6542954.png").resize((25, 25), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, bg="blue", fg="white")
        loginbtn.place(x=100, y=300, width=160)

        registerbtn = Button(frame, command=self.register_window, text="New User Register",
                             font=("times new roman", 10, "bold"), borderwidth=0, bg="black", fg="white")
        registerbtn.place(x=24, y=360, width=120)

        forgetbtn = Button(frame,command=self.forgot_password_window, text="Forget Password", font=("times new roman", 10, "bold"),
                           borderwidth=0, bg="black", fg="white")
        forgetbtn.place(x=20, y=380, width=120)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "pointer" and self.txtpass.get() == "point":
            messagebox.showinfo("Success", "Welcome to Face Recognition Attendance System")
            self.new_window = Toplevel(self.root)
            self.app = FaceRecognitionSystem(self.new_window)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="ruchika@123",
                    database="face_recognisor"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "SELECT * FROM register WHERE email=%s AND password=%s",
                    (self.txtuser.get(), self.txtpass.get())
                )
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username & Password")
                else:
                    open_main = messagebox.askyesno("Access", "Access only admin?")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = FaceRecognitionSystem(self.new_window)

                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")
                
       #====reset password===========
       
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select security Question",parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="ruchika@123", database="face_recognisor")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s and securityQ=%s and securityA=%s"
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
        if row is None:
            messagebox.showerror("Error", "Please enter correct Answer",parent=self.root2)
        else:
           query = "update register set password=%s where email=%s"
           value = (self.txt_newpass.get(), self.txtuser.get())
           my_cursor.execute(query, value)

           conn.commit()
           conn.close()
           messagebox.showinfo("Info", "Your password has been reset, please login new password",parent=self.root2)
           self.root2.destroy()
     
                
     #===forget password window==============
                
    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the Email address to reset password")
        else:
           try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ruchika@123",
                database="face_recognisor"
            )
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
           # print(row)  

            conn.close()
           except Exception as e:
            messagebox.showerror("Error", f"Database connection failed due to: {str(e)}")
           if row is None:
            messagebox.showerror("My Error", "Please enter a valid user name")
           else:
            conn.close()
            self.root2 = Toplevel()
            self.root2.title("Forget Password")
            self.root2.geometry("340x450+610+170")

            l1 = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="blue", bg="white")
            l1.place(x=0, y=10, relwidth=1)

            security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
            security_Q.place(x=50, y=80)

            self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
            self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Friend Name", "Your Teacher Name")
            self.combo_security_Q.place(x=50, y=110, width=250)
            self.combo_security_Q.current(0)

            security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
            security_A.place(x=50, y=150)

            self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
            self.txt_security.place(x=50, y=180, width=250)
            
            new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
            new_password.place(x=50, y=220)

            self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
            self.txt_newpass.place(x=50, y=250, width=250)

            btn = Button(self.root2, text="Reset",command=self.reset_pass, font=("times new roman", 15, "bold"), fg="white", bg="blue")
            btn.place(x=150, y=290)



           


if __name__ == "__main__":
    main()


