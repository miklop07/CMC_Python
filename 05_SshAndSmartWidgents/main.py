import tkinter as tk
import re

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
        self.busy = False
        self.current_string = ""
        self.true_string_regexpr = r"<\d+\s+\d+\s+\d+\s+\d+>\s+\d+\.\d+\s+#[0-9A-F]{6}\s+[a-zA-Z]+"
        self.true_string_regexpr_params = r"<(\d+)\s+(\d+)\s+(\d+)\s+(\d+)>\s+(\d+\.\d+)\s+(#[0-9A-F]{6})\s+([a-zA-Z]+)"


        self.www = 1

    def create_widgets(self):
        self.text = tk.Text(self, undo=True)
        self.text.bind('<<Modified>>', func=self.CheckText)
        self.text.tag_configure("WrongString", background="red")
        self.text.grid(row=0, column=0, sticky="NEWS")

        self.graphics = tk.Canvas(self)
        self.graphics.bind("<Button-1>", func=self.MouseButtonOn)
        self.graphics.bind("<ButtonRelease-1>", func=self.MouseButtonOff)
        self.graphics.bind("<Motion>", func=self.Draw)

        self.graphics.tag_bind(tagOrId="obj", sequence="<Button-1>", func=self.MoveBegin)
        self.graphics.tag_bind(tagOrId="obj", sequence="<ButtonRelease-1>", func=self.MoveEnd)
        self.graphics.tag_bind(tagOrId="obj", sequence="<Motion>", func=self.Move)

        self.graphics.grid(row=0, column=1, sticky="NEWS")

    def CheckText(self, event):
        self.text.tag_remove("WrongString", 1.0, "end")
        figures = self.graphics.find_all()
        for oval in figures:
            self.graphics.delete(oval)
        lines = self.text.get("1.0", "end").split("\n")
        for line_num in range(len(lines)):
            if lines[line_num] != "":
                parsed_str = re.findall(self.true_string_regexpr, lines[line_num])
                if parsed_str == []:
                    self.text.tag_add("WrongString", f"{line_num + 1}.0", f"{line_num + 1}.end")
                elif lines[line_num] != parsed_str[0]:
                    self.text.tag_add("WrongString", f"{line_num + 1}.0", f"{line_num + 1}.end")
                else:
                    params = re.findall(self.true_string_regexpr_params, lines[line_num])
                    print(params)
                    self.graphics.create_oval(
                        *params[0][:4],
                        tags="obj",
                        width=params[0][4],
                        fill=params[0][5],
                        outline=params[0][6]
                    )
                    # coords = re.findall(r"<(\d+)\s+(\d+)\s+(\d+)\s+(\d+)>", lines[line_num])
                    # fill = 
                    # print(coords)
                    # print(fill)
                    # print(width)
                    # self.graphics.create_oval(
                    #     *coords[0],
                    #     tags="obj",
                    #     fill="#FFFFFF",
                    #     width=self.www
                    # )
        self.text.edit_modified(False)

    def MoveBegin(self, event):
        self.busy = True

    def Move(self, event):
        pass
        # if self.busy:
        #     self.graphics.move(self.save, 1, 1)

    def MoveEnd(self, event):
        self.busy = False

    def MouseButtonOn(self, event):
        # print(self.busy)
        if not self.busy:
            self.begin_pos = (event.x, event.y)
            self.is_drawing = True

    def MouseButtonOff(self, event):
        self.www += 1
        if self.current_string != "":
            params = self.graphics.itemconfigure(self.current_oval)
            self.current_string += " " + str(params["width"][-1])
            self.current_string += " " + str(params["fill"][-1])
            self.current_string += " " + str(params["outline"][-1])
            self.text.insert("end", self.current_string + "\n")
            self.current_string = ""

        self.begin_pos = (None, None)
        self.is_drawing = False
        self.current_oval = None

    def Draw(self, event):
        if self.is_drawing:
            if self.current_oval:
                self.graphics.delete(self.current_oval)
            self.current_oval = self.graphics.create_oval(*self.begin_pos, event.x, event.y, tags="obj", fill="#FFFFFF", width=self.www)
            self.current_string = f"<{self.begin_pos[0]} {self.begin_pos[1]} {event.x} {event.y}>"
            # self.save = self.current_oval

app = App(title="Graph Edit")
app.mainloop()