import numpy as np
import cv2


class Tracker:
    def __init__(self, video_stream):
        self.vstream = video_stream
        self.running = True

        self.feature_params = dict(
            maxCorners = 10,
            qualityLevel = 0.3,
            minDistance = 7,
            blockSize = 7
        )

        self.lk_params = dict(
            winSize = (21, 21),
            maxLevel = 2,
            criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
        )

        self.draw_mask = None

        self.init_frame = None
        self.init_gray = None
        self.p0 = None

        self.capture_initial_frame()

    def capture_initial_frame(self):
        _, self.init_frame = self.vstream.read()
        self.draw_mask = np.zeros_like(self.init_frame)
        self.init_gray = cv2.cvtColor(self.init_frame, cv2.COLOR_BGR2GRAY)
        
    def process_frame(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
        if self.p0 is not None:
            p1, st, err = cv2.calcOpticalFlowPyrLK(self.init_gray, frame_gray, self.p0, None, **self.lk_params)

            if st.any():
                good_new = p1[st==1]
                good_old = self.p0[st==1]

                for i, (new, old) in enumerate(zip(good_new, good_old)):
                    a, b = new.ravel()
                    c, d = old.ravel()
                
                    cv2.line(self.draw_mask, (a,b), (c,d),(255, 0, 255), 2)
                    cv2.circle(frame, (a,b), 5, (0, 255, 0), -1)
        
            self.init_gray = frame_gray.copy()
            if st.any():
                self.p0 = good_new.reshape(-1, 1, 2)
        
        complete_frame = cv2.add(frame, self.draw_mask)
        
        return complete_frame
    
    def get_points_to_track(self, mat):
        mat = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
        points = cv2.goodFeaturesToTrack(mat, mask=None, **self.feature_params)
        return points

    def set_points_to_track(self, points):
        self.p0 = points

    def total_reset(self):
        pass
