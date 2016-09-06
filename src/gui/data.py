import Tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvas, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class GraphFrame(tk.Frame):
    def __init__(self, parent, matplot_graph, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.parent = parent
        
