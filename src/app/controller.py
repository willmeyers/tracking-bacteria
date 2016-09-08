import cv2
import threading
import Tkinter as tk

from video.display import VideoDisplay
from gui.application import MainApplicationFrame


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.vstream = cv2.VideoCapture(0)
        
        self.display = VideoDisplay(self.vstream)
        self.display.start()

        self.application = MainApplicationFrame(self.root, self.display)
        self.application.pack()

        self.running = True

    def __del__(self):
        self.running = False

    def start(self):
        t = threading.Thread(target=self.run, args=())
        t.start()

    def run(self):
        self.root.mainloop()


c = Controller()
c.run()
