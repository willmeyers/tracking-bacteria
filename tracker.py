import cv2
from datetime import datetime
from protozoa import Protozoa
from collections import deque
import time
import random


class Tracker:
    def __init__(self):
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        self.camera = cv2.VideoCapture(1)  
        grabbed, self.initial_frame = self.camera.read()
        
        g = cv2.cvtColor(self.initial_frame, cv2.COLOR_BGR2GRAY)
        g = cv2.GaussianBlur(g, (21, 21), 0)

        self.initial_frame = g

        if not grabbed:
            print('Could not grab initial frame!')

        self.points = deque()

        self.running = True

    def __del__(self):
        print('Exiting application.')
        self.camera.release()
        cv2.destroyAllWindows()
    
    def process_frame(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame, (21, 21), 0)

        return frame

    def run(self):
        start = time.time()
        while self.running:
            _, frame = self.camera.read()

            gray = self.process_frame(frame)

            frame_delta = cv2.absdiff(self.initial_frame, gray)
            thresh = cv2.threshold(frame_delta, 15, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.dilate(thresh, None, iterations=2)
            cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for c in cnts:
                if cv2.contourArea(c) < 0:
                    continue
               
                x, y, w, h = cv2.boundingRect(c)
                identifier = 'A1' 
                cv2.putText(frame, identifier, (x+w/2, y), self.font, 0.5, (0, 255, 0), 1)
                cv2.circle(frame, (x+w/2, y+h/2), 2, (0, 255, 0), -1)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255))

                self.points.appendleft(Protozoa('A1', (x, y, w, h)))    
            
            for p in self.points:
                cv2.circle(frame, (p.x+p.w/2, p.y+p.h/2), 2, (0, 255, 0), -1)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            if key == ord('u'):
                self.points = deque() 
                self.initial_frame = gray

            cv2.imshow('Thresh', frame_delta)
            cv2.imshow('Test', frame)
