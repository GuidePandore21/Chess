from Class.Pièces.Pieces import Piece

class Tour(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def getPossibleMoves(self, position):
        pass