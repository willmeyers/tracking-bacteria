import Tkinter as tk


class MenuBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.parent = parent

        self.menubar = tk.Menu(self.parent)
    
        self.file_menu = tk.Menu(self.parent)
        self.project_menu = tk.Menu(self.parent)
        self.help_menu = tk.Menu(self.parent)
   
        self.build_file_menu()
        self.build_project_menu()
        self.build_help_menu()

        self.menubar.add_cascade(label='File', menu=self.file_menu)
        self.menubar.add_cascade(label='Project', menu=self.project_menu)
        self.menubar.add_cascade(label='Help', menu=self.help_menu)

        self.parent.configure(menu=self.menubar)
    
    def build_file_menu(self):
        self.file_menu.add_command(label='Import video', command=None)
        self.file_menu.add_command(label='Import camera', command=None)
        self.file_menu.add_command(label='Export', command=None)

    def build_project_menu(self):
        self.project_menu.add_command(label='New', command=None)
        self.project_menu.add_command(label='Save', command=None)
        self.project_menu.add_command(label='Open', command=None)

    def build_help_menu(self):
        self.help_menu.add_command(label='Readme', command=None)
        self.help_menu.add_command(label='Online', command=None)

    def goto_file(self):
        pass

    def goto_project(self):
        pass

    def goto_help(self):
        pass
