from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ================== Variables ==================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background Image
        bg_img = Image.open(r"College_photo/what-is-FR.jpg")
        bg_img = bg_img.resize((1600, 900), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=0, width=1600, height=900)

        # Left image
        bg_img1 = Image.open(r"College_photo/sign-in-page-flat-design-concept-illustration-icon-account-login-user-login-abstract-metaphor-can-use-for-landing-page-mobile-app-ui-posters-free-vector.jpg")
        bg_img1 = bg_img1.resize((470, 550), Image.LANCZOS)
        self.photoimg_bg1 = ImageTk.PhotoImage(bg_img1)
        bg_label1 = Label(self.root, image=self.photoimg_bg1)
        bg_label1.place(x=50, y=100, width=470, height=550)

        # Main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        register_lbl.place(x=20, y=20)

        # ===================== Labels and Entries =====================
        # Row 1
        Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15)).place(x=50, y=130, width=250)

        Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=100)
        ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15)).place(x=370, y=130, width=250)

        # Row 2
        Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=170)
        ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15)).place(x=50, y=200, width=250)

        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=170)
        ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15)).place(x=370, y=200, width=250)

        # Row 3
        Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Friend Name", "Your Teacher Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50, y=270, width=250)

        Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=240)
        ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15)).place(x=370, y=270, width=250)

        # Row 4
        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=310)
        ttk.Entry(frame, textvariable=self.var_pass, show="*", font=("times new roman", 15)).place(x=50, y=340, width=250)

        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=310)
        ttk.Entry(frame, textvariable=self.var_confpass, show="*", font=("times new roman", 15)).place(x=370, y=340, width=250)

        # Checkbutton
        self.var_check = IntVar()
        Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0, bg="white").place(x=50, y=380)

        # Buttons
        img = Image.open(r"College_photo/360_F_30978872_yJeUVjMx99CU0qIwz0pC7ge5PReOOyKC.jpg")
        img = img.resize((200, 70), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2").place(x=30, y=420, width=190)

        img1 = Image.open(r"College_photo/360_F_31331324_bqXgqwmlnnXaOeXwFv8CrO6oMHpAKPum.jpg")
        img1 = img1.resize((200, 70), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2").place(x=375, y=420, width=190)

    # ================== Function Declaration ==================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the Terms & Conditions")
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
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    my_cursor.execute(
                        "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get()
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Success", "Registered Successfully")
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")

# ================== Run Application ==================
if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()

