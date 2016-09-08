import cv2
import threading
import numpy as np

from tracking import Tracker


class VideoDisplay:
    def __init__(self, vstream):
        cv2.namedWindow('Video')
        self.vstream = vstream 

        self.tracker = Tracker(self.vstream)

        cv2.setMouseCallback('Video', self.handle_mouse_events)

        self.mask = np.zeros_like(self.tracker.init_frame)
        cv2.rectangle(self.mask, (0, 0), (150, 25), (255, 255, 255), -1)
        #cv2.rectangle(self.mask, (150, 25), (150, 50), (255, 255, 255), -1)

        self.cropping = False
        self.box_start = None
        self.box_end = None
        self.roi = None

        self.running = True

    def __del__(self):
        self.running = False
        self.vstream.release()
        cv2.destroyAllWindows()

    def handle_mouse_events(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            mouse_pos = 'x:'+str(x)+' y:'+str(y) 
            cv2.rectangle(self.mask, (0, 0), (150, 25), (255, 255, 255), -1)
            cv2.putText(self.mask, mouse_pos, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, .65, (0, 0, 0), 1)

        if event == cv2.EVENT_LBUTTONDOWN:
            self.box_start = (x, y)
            self.cropping = True
        
        if event == cv2.EVENT_MOUSEMOVE and self.cropping:
            self.box_end = (x, y)
            cv2.rectangle(self.mask, self.box_start, self.box_end, (0, 155, 0), -1)
        
        if event == cv2.EVENT_LBUTTONUP:
            self.box_end = (x, y)
            self.cropping = False
            self.roi = self.frame[self.box_start[1]:self.box_end[1], self.box_start[0]:self.box_end[0]]
            
            points = self.tracker.get_points_to_track(self.roi)
            for p in points:
                p[0][0] = p[0][0]+self.box_start[0]
                p[0][1] = p[0][1]+self.box_start[1]

            self.tracker.set_points_to_track(points)
            self.mask = np.zeros_like(self.frame)


    def run(self):
        while self.running:
            _, f = self.vstream.read()
            self.frame = self.tracker.process_frame(f)
            self.frame = cv2.add(self.frame, self.mask)
            cv2.imshow('Video', self.frame)

            cv2.waitKey(30)

d = VideoDisplay(cv2.VideoCapture(1))
d.run()
