from Class.Pièces.Pieces import Piece

class Tour(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def getPossibleMoves(self, position):
        listeCoups = []
        for i in range(8):
            listeCoups.append((position[0], self.listeNumeroLignes[i + 1]))
            listeCoups.append((self.listeLettreColonnes[i + 1], position[1]))
        return listeCoups