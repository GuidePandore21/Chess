import tkinter as tk
from Class.Board import Board
from Class.Pièces.Cavalier import Cavalier
from Class.Pièces.Fou import Fou
from Class.Pièces.Pion import Pion
from Class.Pièces.Dame import Dame
from Class.Pièces.Roi import Roi
from Class.Pièces.Tour import Tour

class ChessGame:
    def __init__(self, squareSize):
        self.window = tk.Tk()
        self.window.title("Jeu d'échecs avec Tkinter")
        self.createChessboardInterface(squareSize)
        self.board = Board()
        self.placementPiecesInitiales()
    
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
                
    def placementPiecesInitiales(self):
        # Placement des pions
        self.board.matrice.loc['A', '2'] = Pion("blanc")
        self.board.matrice.loc['A', '7'] = Pion("noir")
        self.board.matrice.loc['B', '2'] = Pion("blanc")
        self.board.matrice.loc['B', '7'] = Pion("noir")
        self.board.matrice.loc['C', '2'] = Pion("blanc")
        self.board.matrice.loc['C', '7'] = Pion("noir")
        self.board.matrice.loc['D', '2'] = Pion("blanc")
        self.board.matrice.loc['D', '7'] = Pion("noir")
        self.board.matrice.loc['E', '2'] = Pion("blanc")
        self.board.matrice.loc['E', '7'] = Pion("noir")
        self.board.matrice.loc['F', '2'] = Pion("blanc")
        self.board.matrice.loc['F', '7'] = Pion("noir")
        self.board.matrice.loc['G', '2'] = Pion("blanc")
        self.board.matrice.loc['G', '7'] = Pion("noir")
        self.board.matrice.loc['H', '2'] = Pion("blanc")    
        self.board.matrice.loc['H', '7'] = Pion("noir")
            
        
        # Placement des tours
        self.board.matrice.loc['A', '1'] = Tour("blanc")
        self.board.matrice.loc['H', '1'] = Tour("blanc")
        self.board.matrice.loc['A', '8'] = Tour("noir")
        self.board.matrice.loc['H', '8'] = Tour("noir")
        
        # Placement des cavaliers
        self.board.matrice.loc['B', '1'] = Cavalier("blanc")
        self.board.matrice.loc['G', '1'] = Cavalier("blanc")
        self.board.matrice.loc['B', '8'] = Cavalier("noir")
        self.board.matrice.loc['G', '8'] = Cavalier("noir")
        
        # Placement des fous
        self.board.matrice.loc['C', '1'] = Fou("blanc")
        self.board.matrice.loc['F', '1'] = Fou("blanc")
        self.board.matrice.loc['C', '8'] = Fou("noir")
        self.board.matrice.loc['F', '8'] = Fou("noir")
        
        # Placement des dames
        self.board.matrice.loc['D', '1'] = Dame("blanc")
        self.board.matrice.loc['D', '8'] = Dame("noir")
        
        # Placement des rois
        self.board.matrice.loc['E', '1'] = Roi("blanc")
        self.board.matrice.loc['E', '8'] = Roi("noir")

      
    def run(self):
        self.window.mainloop()