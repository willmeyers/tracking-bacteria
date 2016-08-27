import cv2
from datetime import datetime
import time

class Tracker:
    def __init__(self):
        self.record_video = False
        self.record_pos = False

        self.camera = cv2.VideoCapture(1)  
        grabbed, self.initial_frame = self.camera.read()
        
        g = cv2.cvtColor(self.initial_frame, cv2.COLOR_BGR2GRAY)
        g = cv2.GaussianBlur(g, (11, 11), 0)

        self.initial_frame = g

        if not grabbed:
            print('Could not grab initial frame!')

        self.running = True

    def __del__(self):
        self.camera.release()
        cv2.destroyAllWindows()
    
    def process_frame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame, (11, 11), 0)

        return frame

    def run(self):
        while self.running:
            _, frame = self.camera.read()

            gray = self.process_frame(frame)

            frame_delta = cv2.absdiff(self.initial_frame, gray)
            thresh = cv2.threshold(frame_delta, 15, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in cnts:
                if cv2.contourArea(c) < 50:
                    continue

                (x, y, w, h) = cv2.boundingRect(c)
                cv2.circle(frame, (x+w/2, y+h/2), 5, (255, 0, 0), -1)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            cv2.imshow('Thresh', frame_delta)
            cv2.imshow('Test', frame)
