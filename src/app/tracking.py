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

        self.init_frame = None
        self.init_gray = None
        self.p0 = None

    def capture_initial_frame(self):
        _, self.init_frame = self.vstream.read()
        self.init_gray = cv2.cvtColor(self.init_frame, cv2.COLOR_BGR2GRAY)
        
    def process_frame(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        p1, st, err = cv2.calcOpticalFlowPyrLK(self.init_gray, frame_gray, self.p0, None, **self.lk_params)

        if st == 1:
            good_new = p1[st==1]
            good_old = self.p0[st==1]

            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()

                cv2.circle(frame, (a,b), 5, (0, 255, 0), -1)
        
        self.init_gray = frame_gray.copy()
        if st==1:
            self.p0 = good_new.reshape(-1, 1, 2)

        return frame

    def run(self):
        self.capture_initial_frame()
        self.set_point(120, 120)
        while True:
            _, f = self.vstream.read()
            cv2.imshow('hey', self.process_frame(f))
            cv2.waitKey(30)

    def set_point(self, x, y):
        self.p0 = [[(x, y)]]
        self.p0 = np.float32(np.asarray(self.p0))

t = Tracker(cv2.VideoCapture(0))
t.run()


class TrackerDisplay:
    def __init__(self):
        self.draw_states = {
            'NONE': 0,
            'LINE': 1,
            'POINT': 2
        }

        self.selected_draw_state = self.draw_states['NONE']

        self.mask = None
        self.display_frame = None

    def show_frame(self):
        pass

    def draw_line(self):
        pass

    def draw_point(self):
        pass
