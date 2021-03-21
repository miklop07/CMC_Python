import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None, title="<application>", **kwargs):
        super().__init__(master, **kwargs)
        self.master.geometry("320x240")
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
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
        self.input_label = InputLabel(self)
        self.quit_button = tk.Button(self, text="Quit", command=self.master.quit)

        self.input_label.grid()
        self.quit_button.grid(row=1, sticky="SE")

class InputLabel(tk.Label):
    def __init__(self, master=None):
        pass

    def grid(self):
        pass

app = App(title="InputLabel")
app.mainloop()
