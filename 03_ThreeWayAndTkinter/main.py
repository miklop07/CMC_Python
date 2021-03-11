import tkinter as tk

class Game(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.CreateWidgets()

    def CreateWidgets(self):
        self.new_button = tk.Button(self, text="new", command=self.CreateGame)
        self.quit_button = tk.Button(self, text="quit", command=self.quit)

        self.new_button.grid(row=0, column=0, columnspan=2)
        self.quit_button.grid(row=0, column=2, columnspan=2)

        for i in range(1, 5):
            for j in range(4):
                self.tmp_but = tk.Button(self, text=f"{4 * (i - 1) + j + 1}", command=self.Shift)
                self.tmp_but.grid(row=i, column=j, sticky="NEWS")

        for i in range(1, 5):
            self.rowconfigure(i, weight=1)

        for i in range(4):
            self.columnconfigure(i, weight=1)

    def CreateGame(self):
        pass

    def Shift(self):
        pass

game = Game()
game.title("15")
game.geometry("800x600")
game.mainloop()
