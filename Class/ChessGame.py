import tkinter as tk
from Class.Board import Board

class ChessGame:
    def __init__(self, squareSize):
        self.window = tk.Tk()
        self.window.title("Jeu d'échecs avec Tkinter")
        self.createChessboardInterface(squareSize)
        self.board = Board()
    
    def createChessboardInterface(self, squareSize):
        colors = ["white", "gray"]
        SQUARE_SIZE = squareSize
        HEIGHT = SQUARE_SIZE * 8
        WIDTH = SQUARE_SIZE * 8
        
        canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT)
        canvas.pack()

        for row in range(8):
            for col in range(8):
                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                color = colors[(row + col) % 2]
                canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    
    def run(self):
        self.window.mainloop()