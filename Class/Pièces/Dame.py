from Pièces.Pieces import Piece

class Dame(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def getPossibleMoves(self, position):
        listeCoups = []
        for i in range(8):
            listeCoups.append((position[0], self.listeNumeroLignes[i + 1]))
            listeCoups.append((self.listeLettreColonnes[i + 1], position[1]))
            
        for i in range(8):
            if self.listeLettreColonnes.index(position[0]) + i + 1 < 8 and self.listeNumeroLignes.index(position[1]) + i + 1 < 8:
                listeCoups.append((self.listeLettreColonnes[self.listeLettreColonnes.index(position[0]) + i + 1], self.listeNumeroLignes[self.listeNumeroLignes.index(position[1]) + i + 1]))
            
            if self.listeLettreColonnes.index(position[0]) - i - 1 >= 0 and self.listeNumeroLignes.index(position[1]) - i - 1 >= 0:
                listeCoups.append((self.listeLettreColonnes[self.listeLettreColonnes.index(position[0]) - i - 1], self.listeNumeroLignes[self.listeNumeroLignes.index(position[1]) - i - 1]))
            
            if self.listeLettreColonnes.index(position[0]) + i + 1 < 8 and self.listeNumeroLignes.index(position[1]) - i - 1 >= 0:
                listeCoups.append((self.listeLettreColonnes[self.listeLettreColonnes.index(position[0]) + i + 1], self.listeNumeroLignes[self.listeNumeroLignes.index(position[1]) - i - 1]))
           
            if self.listeLettreColonnes.index(position[0]) - i - 1 >= 0 and self.listeNumeroLignes.index(position[1]) + i + 1 < 8:
                listeCoups.append((self.listeLettreColonnes[self.listeLettreColonnes.index(position[0]) - i - 1], self.listeNumeroLignes[self.listeNumeroLignes.index(position[1]) + i + 1]))
        
        return listeCoups