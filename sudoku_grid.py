# Task - 04 sudoku solver
import tkinter as tk
from sudoku_solver import solve_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PRODIGY INFOTECH - Sudoku Solver")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for row in range(9):
            for col in range(9):
                entry = tk.Entry(frame, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=row, column=col)
                self.entries[row][col] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.pack()

    def get_board(self):
        for row in range(9):
            for col in range(9):
                val = self.entries[row][col].get()
                self.board[row][col] = int(val) if val.isdigit() else 0

    def set_board(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(self.board[row][col]))

    def solve(self):
        self.get_board()
        if solve_sudoku(self.board):
            self.set_board()
        else:
            print("No solution exists")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
