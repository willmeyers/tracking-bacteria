import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import style
from collections import deque


class GraphWindow:
    def __init__(self):
        style.use('ggplot')
        plt.ion()

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(211)
        self.ax2 = self.fig.add_subplot(212, projection='3d')
        self.ax2.set_xlabel('X')
        self.ax2.set_ylabel('Y')
        self.ax2.set_zlabel('Z')
        
        self.velocity_data = deque()
        self.position_data = deque()

        self.posx = []
        self.posy = []
        self.posz = []

    def push_data(self, buf, data):
        pass 

    def show(self, i):
        x=i
        z=i**2
        y=i
        self.ax2.scatter(x, y, z)

v = GraphWindow()
animation.FuncAnimation(v.fig, v.show, blit=True, interval=50, repeat=True) 
plt.show()
