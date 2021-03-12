import tkinter as tk
import random

from tkinter import messagebox as msgbox

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
        self.title("15")
        self.geometry("320x240")

        self.CreateWidgets()
        self.CreateGame()

    def CreateWidgets(self):
        self.new_button = tk.Button(self, text="New", command=self.RestartGame)
        self.quit_button = tk.Button(self, text="Exit", command=self.quit)

        self.new_button.grid(row=0, column=0, columnspan=2)
        self.quit_button.grid(row=0, column=2, columnspan=2)

        for i in range(1, 5):
            self.rowconfigure(i, weight=1)

        for i in range(4):
            self.columnconfigure(i, weight=1)

    def RestartGame(self):
        for row in self.elements:
            for but in row:
                if but != None:
                    but.grid_remove()

        self.CreateGame()

    def CreateGame(self):
        numbers = [i for i in range(1, 16)]
        for i in range(1, 4):
            for j in range(4):
                rand_num = random.choice(numbers)
                numbers.remove(rand_num)
                if rand_num <= 9:
                    self.elements[i - 1][j] = tk.Button(self, text=f" {rand_num}")
                else:
                    self.elements[i - 1][j] = tk.Button(self, text=f"{rand_num}")
                self.elements[i - 1][j]["command"] = Redirect(self.Shift, self.elements[i - 1][j])
                self.elements[i - 1][j].grid(row=i, column=j, sticky="NEWS")

        for j in range(3):
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            if rand_num <= 9:
                self.elements[3][j] = tk.Button(self, text=f" {rand_num}")
            else:
                self.elements[3][j] = tk.Button(self, text=f"{rand_num}")
            self.elements[3][j]["command"] = Redirect(self.Shift, self.elements[3][j])
            self.elements[3][j].grid(row=4, column=j, sticky="NEWS")

        self.none_position = (random.randrange(1, 5), random.randrange(0, 4))

        np_0 = self.none_position[0]
        np_1 = self.none_position[1]
        if self.none_position != (4, 3):
            self.elements[3][3] = tk.Button(self, text=self.elements[np_0 - 1][np_1]["text"])
            self.elements[3][3]["command"] = Redirect(self.Shift, self.elements[3][3])
            self.elements[3][3].grid(row=4, column=3, sticky="NEWS")
            self.elements[np_0 - 1][np_1].grid_remove()
            self.elements[np_0 - 1][np_1] = None

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

        if self.GameIsOver():
            msgbox.showinfo(message = "You win!")
            self.RestartGame()

    def GameIsOver(self):
        for row_num in range(3):
            for col_num in range(4):
                if self.elements[row_num][col_num] == None:
                    print("droppedNone", row_num, col_num)
                    return False
                if int(self.elements[row_num][col_num]["text"]) != row_num * 4 + col_num + 1:
                    print(row_num * 4 + col_num + 1)
                    print(self.elements[row_num][col_num]["text"])
                    print("dropped", row_num, col_num)
                    return False

        for col_num in range(3):
            if self.elements[3][col_num] == None:
                print("droppedNone", 3, col_num)
                return False
            if int(self.elements[3][col_num]["text"]) != 13 + col_num:
                print("dropped", 3, col_num)
                return False

        return True

game = Game()
game.mainloop()
