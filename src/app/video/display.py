import cv2
import threading
import numpy as np

from tracking import Tracker


class VideoDisplay:
    """ The VideoDisplay class is the main object for displaying the application.
    When initializing, a tracker object is created and the created video stream
    `vstream` is passed into the constructor.

    """
    def __init__(self, vstream):
        cv2.namedWindow('Video')
        
        self.vstream = vstream 
        _, init_frame = vstream.read()

        self.tracker = Tracker(init_frame)

        cv2.setMouseCallback('Video', self.handle_mouse_events)

        self.mask = np.zeros_like(self.tracker.init_frame)
        cv2.rectangle(self.mask, (0, 0), (150, 25), (255, 255, 255), -1)

        # For defining region of interest 
        self.cropping = False
        self.box_start = None
        self.box_end = None
        self.roi = None

        self.running = True

    def handle_mouse_events(self, event, x, y, flags, param):
        """ Handles OpenCV mouse events.

        """

        # Displays the current mouse cursor postion.
        if event == cv2.EVENT_MOUSEMOVE:
            mouse_pos = 'x:'+str(x)+' y:'+str(y) 
            cv2.rectangle(self.mask, (0, 0), (150, 25), (255, 255, 255), -1)
            cv2.putText(self.mask, mouse_pos, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, .65, (0, 0, 0), 1)

        # On click, start cropping area and set start point
        if event == cv2.EVENT_LBUTTONDOWN:
            self.box_start = (x, y)
            self.cropping = True
        
        # While clicking and moving mouse, draw a rectangle and set the end point
        if event == cv2.EVENT_MOUSEMOVE and self.cropping:
            self.box_end = (x, y)
            cv2.rectangle(self.mask, self.box_start, self.box_end, (0, 155, 0), -1)
        
        # On click up, set end point and create region of interest, set points to track
        if event == cv2.EVENT_LBUTTONUP:
            self.box_end = (x, y)
            self.cropping = False
            self.roi = self.frame[self.box_start[1]:self.box_end[1], self.box_start[0]:self.box_end[0]]
            
            points = self.tracker.get_points_to_track(self.roi)
            for p in points:
                p[0][0] = p[0][0]+self.box_start[0]
                p[0][1] = p[0][1]+self.box_start[1]

            self.tracker.set_mean_point(points)
            self.mask = np.zeros_like(self.frame)
            self.tracker.clear_paths()


    def run(self):
        """ The main loop of the display window. While the application is running,
        read a frame from the video stream `vstream` and send it to the tracker.
        The tracker returns the processed frame, add the drawing mask and render the
        frame.

        """
        while self.running:
            _, f = self.vstream.read()
            self.frame = self.tracker.process_frame(f)
            self.frame = cv2.add(self.frame, self.mask)
            cv2.imshow('Video', self.frame)

            cv2.waitKey(30)
