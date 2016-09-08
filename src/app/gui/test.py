import cv2
import Tkinter as tk
import numpy as np
from PIL import Image, ImageTk

window = tk.Tk()

image_frame = tk.Frame(window, width=600, height=500)
image_frame.pack()

cap = cv2.VideoCapture(0)

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image=image)
    d1.imgtk = image
    d1.configure(image=image)

    window.after(10, show_frame)

d1 = tk.Label(image_frame)
d1.pack()

show_frame()
window.mainloop()
