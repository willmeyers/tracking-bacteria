class Protozoa: 
    def __init__(self, identifier, rect):
        self.identifier = identifier
        self.prev_positions = []
   
        self.x = rect[0]
        self.y = rect[1]
        self.w = rect[2]
        self.h = rect[3]
