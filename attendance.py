from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1540x850+0+0")
        self.root.title("Face Recognition System")
        
        #========variables==========
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # First image
        img = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\attendance-management-features.webp")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl = Label(self.root, image=self.photoimg)
        lbl.place(x=0, y=0, width=800, height=200)

      # Second image
        img1 = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\attendence-scaled.webp")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl1 = Label(self.root, image=self.photoimg1)
        lbl1.place(x=800, y=0, width=800, height=200)
        
        
         # Background Image
        bg_img = Image.open(r"College_photo/what-is-FR.jpg")
        bg_img = bg_img.resize((1530, 710), Image.LANCZOS)
        self.photoimg_bg = ImageTk.PhotoImage(bg_img)
        bg_label = Label(self.root, image=self.photoimg_bg)
        bg_label.place(x=0, y=200, width=1530, height=710)
        
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 32, "bold"),
                          bg="white", fg="skyblue")
        title_lbl.place(x=0, y=150, width=1540, height=50)      
        
        # ================Main Frame===================
        main_frame = Frame(self.root, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=0, y=210, width=1522, height=575)      
        
        # =================Left Label Frame====================
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=750, height=558) 
         
        img_left = Image.open(r"College_photo\may-2.png")
        img_left = img_left.resize((730, 135), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        left_label = Label(Left_frame, image=self.photoimg_left)  
        left_label.place(x=5, y=0, width=730, height=135)
        
        left_inside_frame= Label(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=745, height=400)    
        
        
        # Label and entry    
        attendanceID_label = Label(left_inside_frame, text="Attendance ID", font=("times new roman", 12, "bold"))
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        attendanceID_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_id, font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        # Roll
        rolllabel = Label(left_inside_frame, text="Roll:", bg="white", font="comicsansms 12 bold")
        rolllabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_roll, font="comicsansms 12 bold")
        atten_roll.grid(row=0, column=3, pady=8)

       # Name
        nameLabel = Label(left_inside_frame, text="Name:", bg="white", font="comicsansms 12 bold")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_name, font="comicsansms 12 bold")
        atten_name.grid(row=1, column=1, pady=8)
        
        # Date
        dateLabel = Label(left_inside_frame, text="Date:", bg="white", font="comicsansms 12 bold")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_date, font="comicsansms 12 bold")
        atten_date.grid(row=2, column=3, pady=8)  
        
        # Department
        depLabel = Label(left_inside_frame, text="Department:", bg="white", font="comicsansms 12 bold")
        depLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_dep, font="comicsansms 12 bold")
        atten_dep.grid(row=1, column=3, pady=8)
        
        # Time
        timeLabel = Label(left_inside_frame, text="Time:", bg="white", font="comicsansms 12 bold")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_time, font="comicsansms 12 bold")
        atten_time.grid(row=2, column=1, pady=8)
       

        # Attendance Status
        attendanceLabel = Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansms 12 bold")
        attendanceLabel.grid(row=3, column=0)
        
        self.atten_status = ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendance, font="comicsansms 12 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)
        
         # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=350, width=740, height=35)

        Button(btn_frame, text="Import csv",command=self.importCsv, width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export csv",command=self.exportCsv ,width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)

        Button(btn_frame, text="Update", width=18, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset",  width=18,command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)


         # ==================Right Label Frame====================
        Right_frame = LabelFrame(main_frame, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=765, y=10, width=740, height=558)      
        
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=724, height=480)        
        
        
        #============SCROLL BAR====
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)   
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)   
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance Id")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
        #=============fetch data==============
        
    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)
        
        
      #==========import csv============  
    def importCsv(self):
      global mydata
      mydata.clear()
      fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                 filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
      with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetchData(mydata)
        
       #===========export csv========== 
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data","No Data Found to export",parent=self.root)
          return False
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                 filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write=csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
            messagebox.showinfo("Data Export", "Your data exported to"+os.path.basename(fln)+"successfully")
      except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)      
             
      
    def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)  
      rows=content['values'] 
      self.var_atten_id.set(rows[0])        
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])       
        
        
    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")
          
        
        
        
        
        
        
        
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()        