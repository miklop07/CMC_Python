import tkinter as tk

class Redirect:
    def __init__(self, function, button):
        self.function = function
        self.button = button

    def __call__(self):
        self.function(self.button)


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.elements = [[None for i in range(4)] for j in range(4)]
        self.none_position = (0, 0)

        self.CreateWidgets()
        self.CreateGame()

    def CreateWidgets(self):
        self.new_button = tk.Button(self, text="new", command=self.CreateGame)
        self.quit_button = tk.Button(self, text="quit", command=self.quit)

        self.new_button.grid(row=0, column=0, columnspan=2)
        self.quit_button.grid(row=0, column=2, columnspan=2)

    def CreateGame(self):
        for i in range(1, 4):
            for j in range(4):
                self.elements[i - 1][j] = tk.Button(self, text=f"{4 * (i - 1) + j + 1}")
                self.elements[i - 1][j]["command"] = Redirect(self.Shift, self.elements[i - 1][j])
                self.elements[i - 1][j].grid(row=i, column=j, sticky="NEWS")

        for j in range(3):
            self.elements[3][j] = tk.Button(self, text=f"{13 + j}")
            self.elements[3][j]["command"] = Redirect(self.Shift, self.elements[3][j])
            self.elements[3][j].grid(row=4, column=j, sticky="NEWS")

        for i in range(1, 5):
            self.rowconfigure(i, weight=1)

        for i in range(4):
            self.columnconfigure(i, weight=1)

        self.none_position = (4, 3)

    def Shift(self, button):
        info = button.grid_info()
        col = info["column"]
        row = info["row"]

        np_0 = self.none_position[0]
        np_1 = self.none_position[1]
        if abs(row - np_0) == 1 and col == np_1 or abs(col - np_1) == 1 and row == np_0:
            print(button["text"])
            self.elements[np_0 - 1][np_1] = tk.Button(self, text=button["text"])
            self.elements[np_0 - 1][np_1]["command"] = Redirect(self.Shift, self.elements[np_0 - 1][np_1])
            self.elements[np_0 - 1][np_1].grid(row=np_0, column=np_1, sticky="NEWS")
            self.elements[row - 1][col].grid_remove()
            self.elements[row - 1][col] = None
            self.none_position = (row, col)

game = Game()
game.title("15")
game.geometry("320x240")
game.mainloop()
