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
    def create_widgets(self):
        self.input_label = InputLabel(self)
        self.quit_button = tk.Button(self, text="Quit", command=self.master.quit)

        self.quit_button.grid(row=1, sticky="SE")

class InputLabel(tk.Label):
    def __init__(self, master=None):
        self.text = tk.StringVar(value="")
        self.font_size = 15
        super().__init__(master, textvariable=self.text, font=("Consolas", self.font_size), highlightthickness=1, relief='sunken')

        self.cursor_position = 0
        self.cursor = tk.Frame(self, height=24, width=1, background="black")
        self.bind("<Key>", func=self.KeyboardHandler)
        self.bind("<Button-1>", func=self.LeftClickHandler)
        self.grid(row=0, sticky="WE")

    def KeyboardHandler(self, event):
        if event.keysym == "Left":
            self.SetCursor(self.cursor_position - 1)
        elif event.keysym == "Right":
            self.SetCursor(self.cursor_position + 1)
        elif event.keysym == "Home":
            self.SetCursor(0)
        elif event.keysym == "End":
            self.SetCursor(len(self.text.get()))
        elif event.keysym == "BackSpace":
            self.DeleteChar()
        elif event.char and event.char.isprintable():
            self.InsertChar(event.char)

    def InsertChar(self, char):
        current_text = self.text.get()
        self.text.set(current_text[:self.cursor_position] + char + current_text[self.cursor_position:])
        self.SetCursor(self.cursor_position + 1)

    def DeleteChar(self):
        current_text = self.text.get()
        self.text.set(current_text[:self.cursor_position] + current_text[self.cursor_position + 1:])
        self.SetCursor(self.cursor_position - 1)

    def LeftClickHandler(self, event):
        self.focus()
        self.SetCursor(event.x // 12)

    def SetCursor(self, position):
        if position >= 0 and position <= len(self.text.get()):
            self.cursor_position = position
        self.cursor.place(x=self.cursor_position * 12, y=1)

app = App(title="InputLabel")
app.mainloop()
