import tkinter as tk
import inspect

class Application(tk.Frame):
    def __init__(self, master=None, title="<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        # self.master.geometry("800x600")
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        pass

class App(Application):
    def create_widgets(self):
        self.text = tk.Text(self, undo=True)
        self.text.grid(row=0, column=0, sticky="NEWS")

        self.graphics = tk.Canvas(self)
        self.graphics.grid(row=0, column=1, sticky="NEWS")

    

app = App(title="Graph Edit")
app.mainloop()