import cv2
import Tkinter as tk
from PIL import Image, ImageTk


class VideoCaptureFeed(tk.Frame):
    def __init__(self, parent, device, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.parent = parent
        self.image_frame = tk.Frame(self.parent, width=600, height=500)
        self.image_frame.pack()

        self.l = tk.Label(self.image_frame)
        self.l.pack()

        self.device = device

    def __del__(self):
        print('Ending video feed...')
        self.device.release()

    def capture_frame(self):
        _, frame = self.device.read()
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(im)
        im = ImageTk.PhotoImage(image=im)
        self.l.imgtk = im
        self.l.configure(image=im)
        self.l.after(10, self.capture_frame)


class VideoPlaybackFeed(tk.Frame):
    def __init__(self, parent, vstream, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.parent = parent
