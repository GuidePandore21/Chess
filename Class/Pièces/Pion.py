from Class.Pièces.Pieces import Piece

class Pion(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.isFirstMove = True
    
    def getPossibleMoves(self, position):
        listeCoups = []
        if self.color == "blanc":
            if self.isFirstMove:
                listeCoups.append((position[0], str(int(position[1]) + 2)))
            listeCoups.append((position[0], str(int(position[1]) + 1)))
        else:
            if self.isFirstMove:
                listeCoups.append((position[0], str(int(position[1]) - 2)))
            listeCoups.append((position[0], str(int(position[1]) - 1)))