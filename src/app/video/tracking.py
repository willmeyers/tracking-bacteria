import numpy as np
import cv2


class Tracker:
    def __init__(self, video_stream):
        self.vstream = video_stream
        self.running = True

        self.lk_params = dict(
            winSize = (21, 21),
            maxLevel = 2,
            criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
        )

        self.mask = None

        self.init_frame = None
        self.init_gray = None
        self.p0 = None

        self.capture_initial_frame()

    def capture_initial_frame(self):
        _, self.init_frame = self.vstream.read()
        self.mask = np.zeros_like(self.init_frame)
        self.init_gray = cv2.cvtColor(self.init_frame, cv2.COLOR_BGR2GRAY)
        
    def process_frame(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
        if self.p0 is not None:
            p1, st, err = cv2.calcOpticalFlowPyrLK(self.init_gray, frame_gray, self.p0, None, **self.lk_params)

            if st == 1:
                good_new = p1[st==1]
                good_old = self.p0[st==1]

                for i, (new, old) in enumerate(zip(good_new, good_old)):
                    a, b = new.ravel()
                    c, d = old.ravel()
                
                    cv2.line(self.mask, (a,b), (c,d),(255, 0, 255), 2)
                    cv2.circle(frame, (a,b), 5, (0, 255, 0), -1)
        
            self.init_gray = frame_gray.copy()
            if st==1:
                self.p0 = good_new.reshape(-1, 1, 2)
        
        complete_frame = cv2.add(frame, self.mask)
        
        return complete_frame

    def set_point(self, x, y):
        self.p0 = [[(x, y)]]
        self.p0 = np.float32(np.asarray(self.p0))

    def get_point(self):
        return self.p0

    def reset(self):
        self.mask = np.zeros_like(self.init_frame)
