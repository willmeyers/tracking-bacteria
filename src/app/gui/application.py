import cv2
import threading
from PIL import Image, ImageTk
import Tkinter as tk

from menubar import MenuBar

class MainApplicationFrame(tk.Frame):
    def __init__(self, parent, video_stream, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.video_stream = video_stream

        self.parent.title('Protozoa Tracking Software')

        self.menubar = MenuBar(self.parent)
