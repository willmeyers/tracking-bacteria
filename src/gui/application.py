import cv2
from PIL import Image, ImageTk
import Tkinter as tk

from menubar import MenuBar
from media import VideoCaptureFeed


class MainApplicationFrame(tk.Frame):
    def __init__(self, parent, video_stream, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.video_stream = video_stream

        self.parent.title('Protozoa Tracking Software')

        self.menubar = MenuBar(self.parent)
        self.feed = VideoCaptureFeed(self.parent, self.video_stream)

        self.feed.capture_frame()

        self.feed.pack()

root = tk.Tk()
MainApplicationFrame(root).pack()
root.mainloop()
