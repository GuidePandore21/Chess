import tkinter as tk
from PIL import Image, ImageTk
from Class.Board import Board

class ChessGame:
    def __init__(self, squareSize):
        self.window = tk.Tk()
        self.window.title("Jeu d'échecs avec Tkinter")
        
        self.square_size = squareSize
        self.canvas = tk.Canvas(self.window, width=self.square_size * 8, height=self.square_size * 8)
        self.canvas.pack()
        
        self.board = Board()
        
        self.piece_images = {}  # Dictionnaire pour stocker les images
        
        self.load_images()
        self.createChessboardInterface()
        self.board.placementPiecesInitiales()
        self.displayPieces()

    def load_images(self):
        pieces = ["pion", "tour", "cavalier", "fou", "dame", "roi"]
        colors = ["blanc", "noir"]

        for color in colors:
            for piece in pieces:
                image_path = f"sprites/{piece}_{color}.png"
                try:
                    image = Image.open(image_path)
                    image = image.resize((self.square_size, self.square_size), Image.Resampling.LANCZOS)
                    self.piece_images[f"{piece}_{color}"] = ImageTk.PhotoImage(image)
                except FileNotFoundError:
                    print(f"Image introuvable : {image_path}")

    def displayPieces(self):
        self.canvas.delete("piece")  # Efface les pièces existantes
        
        for col in self.board.listeNumeroLignes:  # Colonnes 1-8
            for row in self.board.listeLettreColonnes:  # Lignes A-H
                piece = self.board.matrice.loc[row, col]
                if piece:
                    piece_name = f"{piece.__class__.__name__.lower()}_{piece.color}"
                    if piece_name in self.piece_images:
                        x = self.board.listeLettreColonnes.index(row) * self.square_size + self.square_size // 2
                        y = (7 - self.board.listeNumeroLignes.index(col)) * self.square_size + self.square_size // 2
                        self.canvas.create_image(x, y, image=self.piece_images[piece_name], tags="piece")

    def createChessboardInterface(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                x1 = row * self.square_size
                y1 = (7 - col) * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                color = colors[(row + col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def run(self):
        self.window.mainloop()