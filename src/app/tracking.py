import numpy as np
import cv2


class TrackingWindow:
    def __init__(self, video_cap):
        self.cap = cv2.VideoCapture(0)

        self.feature_params = dict(
            maxCorners = 200,
            qualityLevel = 0.3,
            minDistance = 7,
            blockSize = 7
        )

        self.lk_params = dict(
            winSize = (15, 15),
            maxLevel = 2,
            criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
        )

        ret, old_frame = self.cap.read()
        old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
        p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **self.feature_params) 

        mask = np.zeros_like(old_frame)

        while True:
            ret, frame = self.cap.read()
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **self.lk_params)

            good_new = p1[st==1]
            good_old = p0[st==1]

            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()

                cv2.line(frame, (a,b), (c,d), (255, 0, 255), 2)
                cv2.circle(frame, (a,b), 5, (0, 255, 0), -1)
            
            #img = cv2.add(frame, mask)

            cv2.imshow('frame', frame)
            
            if cv2.waitKey(30) & 0xff == ord('q'):
                break

            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1, 1, 2)

        cv2.destroyAllWindows()
        self.cap.release()

    def set_point(self):
        pass

    def show(self):
        pass

c = TrackingWindow(0)
