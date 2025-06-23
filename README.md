
#  Face Recognition Attendance System

A Python-based attendance system that uses real-time face recognition to mark student attendance automatically. This project integrates computer vision, a GUI interface, and MySQL database management for a smooth and efficient experience.

---

##  Features

- ✅ Real-time face detection and recognition using OpenCV
- ✅ Student data entry with photo capture
- ✅ Attendance logging with date and time
- ✅ MySQL database integration
- ✅ Clean and interactive GUI using Tkinter
- ✅ Automatic saving of attendance to CSV

---

##  Technologies Used

| Component        | Library / Tool               |
|------------------|------------------------------|
| Face Detection   | OpenCV                       |
| Hand Detection   | cvzone, MediaPipe (optional) |
| GUI Interface    | Tkinter                      |
| Image Handling   | PIL (Pillow)                 |
| Database         | MySQL + mysql-connector-python |
| Virtual Keyboard | pynput, cvzone               |

---

##  How to Run

###  Prerequisites

- Python 3.9+ recommended  
- Install required packages:

```bash
pip install opencv-python
pip install pillow
pip install mysql-connector-python
pip install cvzone
pip install mediapipe
pip install pynput
---

## Screenshots




![image](https://github.com/user-attachments/assets/df860093-ed93-474a-bfd9-16c49816667c)
---

##  Project Structure

Face_recognition_AttendanceSystem/
│
├── main.py                  # Main application
├── student.py               # Student data management
├── training.py              # Model training script
├── attendance.csv           # Auto-generated attendance
├── data/                    # Face images
├── icons/                   # GUI icons/images
└── README.md                # Project documentation
---

##  License
This project is open-source and available under the MIT License.

---

### ✅ What to do next:

1. **Create a file named** `README.md` in your project folder.
2. Paste the above content.
3. Save the file.
4. Then push to GitHub:

```bash
git add README.md
git commit -m "Added project README"
git push


