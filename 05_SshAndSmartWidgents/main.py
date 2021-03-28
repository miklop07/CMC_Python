import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None, title="<application>", **kwargs):
        super().__init__(master, **kwargs)
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_drawing = False
        self.begin_pos = (None, None)
        self.current_oval = None

    def create_widgets(self):
        self.text = tk.Text(self, undo=True)
        self.text.grid(row=0, column=0, sticky="NEWS")

        self.graphics = tk.Canvas(self)
        self.graphics.bind("<Button-1>", func=self.MouseButtonOn)
        self.graphics.bind("<ButtonRelease-1>", func=self.MouseButtonOff)
        self.graphics.bind("<Motion>", func=self.Draw)
        self.graphics.tag_bind(tagOrId="obj",  sequence="<Button-1>", func=lambda x: print("asd"))
        self.graphics.grid(row=0, column=1, sticky="NEWS")

    def MouseButtonOn(self, event):
        self.begin_pos = (event.x, event.y)
        self.is_drawing = True

    def MouseButtonOff(self, event):
        self.begin_pos = (None, None)
        self.is_drawing = False
        print(self.graphics.find_all())
        # self.current_oval.bind("<Button-1>", func=lambda e: print("!"))
        self.current_oval = None

    def Draw(self, event):
        if self.is_drawing:
            if self.current_oval:
                self.graphics.delete(self.current_oval)
            self.current_oval = self.graphics.create_oval(*self.begin_pos, event.x, event.y, tags="obj", fill="#FFFFFF")
    

app = App(title="Graph Edit")
app.mainloop()