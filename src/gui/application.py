import Tkinter as tk

from menubar import MenuBar


class MainApplicationFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.parent.title("Protozoa Tracking Software")
        self._center_window(tk.Toplevel(self.parent))

        self.menubar = MenuBar(self.parent)

        self.menubar.pack(side)

    def _center_window(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

root = tk.Tk()
MainApplicationFrame(root).pack(side='top', fill='both', expand=True)
root.mainloop()
