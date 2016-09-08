import numpy as np
import cv2


class Tracker:
    """ The Tracker class main purpose is to take in frames via the `process frame`
    method and return a new, processed frame. The Tracker class takes an initial
    frame from the video stream. The initial frame is converted to grayscale and 
    ready to be incorporated into Lucas-Kanade algorithm. The `draw_mask` is also
    initialized and is there for drawing paths, later added on top of the outputted
    frame.

    OpenCV's implementations of Lucas-Kanade and Shi Feature detection take parameters,
    which are supplied via dictionaries. These can be set via the `set_lk_params` or 
    `set_fd_params` methods.

    init_frame: OpenCV Mat
    """
    def __init__(self, init_frame):
        self.init_frame = init_frame
        self.init_gray = cv2.cvtColor(self.init_frame, cv2.COLOR_BGR2GRAY)
        self.draw_mask = np.zeros_like(self.init_frame)

        # Feature detection params
        self.feature_params = dict(
            maxCorners = 10,
            qualityLevel = 0.3,
            minDistance = 7,
            blockSize = 7
        )

        # Lucas-Kanade parameters
        self.lk_params = dict(
            winSize = (21, 21),
            maxLevel = 2,
            criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
        )
        
        # Initializing points to be tracked
        self.p0 = None

    def process_frame(self, frame):
        """ Takes a frame (Mat) as input and outputs a processed frame (Mat).
        
        This method applies Lucas-Kanade on the given frame and appies `draw_mask`
        to the completed frame.

        """
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
        """ Takes an image as input and outputs an array of points outputted by
        FEATDECT. The inputted image is a cropped section of a frame made by the
        user.

        """
        mat = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
        points = cv2.goodFeaturesToTrack(mat, mask=None, **self.feature_params)
        return points

    def set_points_to_track(self, points):
        """ Given an array of points (x, y), set the points to be tracked to them.
        """
        self.p0 = points

    def clear_paths(self):
        """ Clears drawn paths from the `draw_mask`. Just zeros an array the size
        of the initial frame.

        """
        self.draw_mask = np.zeros_like(self.init_frame)
