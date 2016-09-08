import cv2
from video.display import VideoDisplay


class Controller:
    def __init__(self):
        self.vstream = cv2.VideoCapture(0)
        
        self.stream = VideoDisplay(self.vstream)

    def __del__(self):
        cv2.destroyAllWindows()
        self.vstream.release()

    def run(self):
        self.stream.run()

