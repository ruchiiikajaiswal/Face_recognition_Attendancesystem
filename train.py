from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
import re

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x850+0+0")
        self.root.title("Face Recognition System")
        self.root.resizable(False, False)

        title_lbl = Label(self.root, text="TRAIN  DATA  SET", font=("times new roman", 32, "bold"),
                          bg="white", fg="skyblue")
        title_lbl.place(x=0, y=10, width=1540, height=45)

        # Top image
        try:
            top_img = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\attendence-scaled.webp")
            top_img = top_img.resize((1540, 350), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(top_img)

            top_label = Label(self.root, image=self.photoimg_top)
            top_label.place(x=0, y=60, width=1540, height=350)
        except Exception as e:
            messagebox.showerror("Error", f"Top image not found:\n{e}")

        # Train Button
        train_btn = Button(self.root, text="TRAIN  DATA", command=self.train_classifier, cursor="hand2",
                           font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        train_btn.place(x=400, y=380, width=785, height=60)

        # Bottom image
        try:
            bottom_img = Image.open(r"C:\Users\Redmi\OneDrive\Desktop\Face_recorgnition_system\College_photo\may-2.png")
            bottom_img = bottom_img.resize((1540, 400), Image.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(bottom_img)

            bottom_label = Label(self.root, image=self.photoimg_bottom)
            bottom_label.place(x=0, y=440, width=1540, height=400)
        except Exception as e:
            messagebox.showerror("Error", f"Bottom image not found:\n{e}")

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Data directory '{data_dir}' not found.")
            return

        image_paths = [os.path.join(data_dir, file) for file in os.listdir(data_dir)
                       if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

        faces = []
        ids = []

        for image_path in image_paths:
            try:
                img = Image.open(image_path).convert('L')  # Convert to grayscale
                image_np = np.array(img, 'uint8')

                filename = os.path.split(image_path)[1]
                match = re.search(r"user\.\.(\d+)", filename)


                if match:
                    id = int(match.group(1))
                    faces.append(image_np)
                    ids.append(id)

                    # Optional: preview training image
                    # cv2.imshow("Training", image_np)
                    cv2.waitKey(1)
                else:
                    print(f"Skipping invalid filename format: {filename}")
            except Exception as e:
                print(f"Error processing file {image_path}: {e}")

        if not faces:
            messagebox.showerror("Error", "No valid training images found in the 'data' folder.")
            return

        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            messagebox.showerror("Error", "OpenCV is missing the 'face' module.\nInstall it using:\n\npip install opencv-contrib-python")
            return

        clf.train(faces, np.array(ids))
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed successfully!")


if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()

