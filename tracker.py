import cv2
from datetime import datetime


class Tracker:
    def __init__(self):
        self.record_video = False
        self.record_pos = False

        self.camera = cv2.VideoCapture(0)   
        self.initial_frame = cv2.Query

        self.running = False

    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()

    def run(self):
        while self.running:
            pass

    def _process_frame(self, frame):
        pass
