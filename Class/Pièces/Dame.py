from Class.Pièces.Pieces import Piece

class Dame(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def getPossibleMoves(self, position):
        pass