from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x850+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)

        # ===================Variables=====================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
        self.var_search = StringVar()
        self.var_search_txt = StringVar()

        # ==================Background Image==================
        bg_img = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\what-is-FR.jpg")
        bg_img = bg_img.resize((1540, 850), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=0, width=1540, height=850)

        # ==================Top Images=======================
        img_paths = [
            r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\acad126a7cc5046a4990c65a11e55f8d.jpg",
            r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\may-2.png",
            r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\attendence-scaled.webp",
            r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\e87febcf993bdf5687501b2bb724dedb.jpg"
        ]

        for i, path in enumerate(img_paths):
            img = Image.open(path).resize((385, 120), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            setattr(self, f"photoimg{i+1}", img_tk)
            Label(self.root, image=img_tk).place(x=385 * i, y=0, width=385, height=120)

        # ================Title Label==================
        title_lbl = Label(self.root, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 32, "bold"), bg="white", fg="skyblue")
        title_lbl.place(x=0, y=120, width=1540, height=50)

        # ================Main Frame===================
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=10, y=180, width=1520, height=660)

        # =================Left Label Frame====================
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=750, height=640)

        img_left = Image.open(img_paths[0]).resize((730, 140), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=730, height=140)

        # ==============Current Course=================
        current_course_frame = LabelFrame(Left_frame, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=10, y=150, width=730, height=104)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2022-23", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Sem-1", "Sem-3", "Sem-5", "Sem-7")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # ==================Class Student Information====================
        student_info_frame = LabelFrame(Left_frame, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        student_info_frame.place(x=10, y=260, width=730, height=340)

        # Student info fields
        fields = [("Student ID", self.var_std_id),
                  ("Student Name", self.var_std_name),
                  ("Class Division", self.var_div),
                  ("Roll No", self.var_roll),
                  ("Gender", self.var_gender),
                  ("DOB", self.var_dob),
                  ("Email", self.var_email),
                  ("Phone No", self.var_phone),
                  ("Address", self.var_address),
                  ("Teacher Name", self.var_teacher)]

        for idx, (label_text, var) in enumerate(fields):
            Label(student_info_frame, text=label_text + ":", font=("times new roman", 13, "bold"), bg="white").grid(row=idx//2, column=(idx%2)*2, padx=10, pady=5, sticky=W)
            ttk.Entry(student_info_frame, textvariable=var, width=22, font=("times new roman", 13, "bold")).grid(row=idx//2, column=(idx%2)*2+1, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1.set("No")
        Radiobutton(student_info_frame, command=self.generate_dataset, text="Take Photo Sample", variable=self.var_radio1, value="Yes", font=("times new roman", 13, "bold"), bg="white").grid(row=5, column=0)
        Radiobutton(student_info_frame, text="No Photo Sample", variable=self.var_radio1, value="No", font=("times new roman", 13, "bold"), bg="white").grid(row=5, column=1)

        # Button Frame
        btn_frame = Frame(student_info_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=724, height=40)

        Button(btn_frame, text="Save", command=self.add_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Update", command=self.update_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Delete", command=self.delete_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        # Photo Sample Button Frame
        btn_frame1 = Frame(student_info_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=250, width=724, height=40)

        Button(btn_frame1, text="Take Photo Sample", width=36, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame1, text="Update Photo Sample", width=36, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)

        # ==================Right Label Frame====================
        Right_frame = LabelFrame(main_frame, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=765, y=10, width=740, height=640)

        img_right = Image.open(img_paths[3]).resize((723, 140), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(Right_frame, image=self.photoimg_right).place(x=5, y=0, width=723, height=140)

        # ================Search System=================
        search_frame = LabelFrame(Right_frame, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=150, width=723, height=70)

        search_combo = ttk.Combobox(search_frame, textvariable=self.var_search, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll No", "Student Id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, textvariable=self.var_search_txt, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", command=self.search_data, width=10, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_frame, text="Show All", command=self.show_all_data, width=10, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # ==================Table Frame====================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=220, width=723, height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"
        ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSample")

        self.student_table["show"] = "headings"

        # Set column widths
        for col in (
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
            "dob", "email", "phone", "address", "teacher", "photo"
        ):
            self.student_table.column(col, width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ================Function to add data=================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ruchika@123", database="face_recognisor")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # =====Function to fetch data=====
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ruchika@123",
                database="face_recognisor"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            if data:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {str(e)}", parent=self.root)

    # ==========get cursor==========
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # ==== Update Function ====
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if update:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="ruchika@123", database="face_recognisor"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET 
                            dep=%s, course=%s, year=%s, semester=%s, name=%s, division=%s, roll=%s,
                            gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s 
                        WHERE student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                else:
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

    # delete function=====
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="ruchika@123", database="face_recognisor")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)

    # Reset function=====
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ========== SEARCH STUDENT ==========
    def search_data(self):
        if self.var_search.get() == "Select" or self.var_search_txt.get() == "":
            messagebox.showerror("Error", "Please select a search criteria and enter search text", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="ruchika@123",
                    database="face_recognisor"
                )
                my_cursor = conn.cursor()

                # Mapping display text to actual DB fields
                field_map = {
                    "Roll No": "roll",
                    "Student Id": "student_id"
                }
                selected_field = field_map.get(self.var_search.get())

                if not selected_field:
                    messagebox.showerror("Error", "Invalid search criteria", parent=self.root)
                    return

                query = f"SELECT * FROM student WHERE {selected_field} LIKE '%{self.var_search_txt.get()}%'"
                my_cursor.execute(query)
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in data:
                        self.student_table.insert("", END, values=row)
                else:
                    messagebox.showinfo("Info", "No matching record found.", parent=self.root)

                conn.close()

            except Exception as e:
                messagebox.showerror("Error", f"Error searching data: {str(e)}", parent=self.root)

    # ========== SHOW ALL STUDENTS ==========
    def show_all_data(self):
        self.fetch_data()

    # =========== Generate data set or Take photo sample ==========
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if update:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="ruchika@123", database="face_recognisor")
                    my_cursor = conn.cursor()

                    my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, name=%s, division=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s WHERE student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        "Yes",
                        self.var_std_id.get()
                    ))

                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # ======== Load pre-defined data on face frontals from OpenCV ========
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            return img[y:y+h, x:x+w]
                        return None

                    cap = cv2.VideoCapture(0)
                    img_id = 0

                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or img_id == 100:  # Enter key or 100 images
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data set completed!")

            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()



