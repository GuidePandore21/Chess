from Class.Pièces.Pieces import Piece

class Roi(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def getPossibleMoves(self, position):
        listeCoups = []
        listeCoupsTemp = []
        
        listeCoupsTemp.append((self.listeLettreColonnes.index(position[0]) + 1, self.listeNumeroLignes.index(position[1]) + 1))
        listeCoupsTemp.append((self.listeLettreColonnes.index(position[0]) + 1, self.listeNumeroLignes.index(position[1])))
        listeCoupsTemp.append((self.listeLettreColonnes.index(position[0]) + 1, self.listeNumeroLignes.index(position[1]) - 1))
        listeCoupsTemp.append((self.listeLettreColonnes.index(position[0]), self.listeNumeroLignes.index(position[1]) + 1))
        listeCoupsTemp.append((self.listeLettreColonnes.index(position[0]), self.listeNumeroLignes.index(position[1]) - 1))
        listeCoupsTemp.append((self.listeLettreColonnes.index(position[0]) - 1, self.listeNumeroLignes.index(position[1]) + 1))
        listeCoupsTemp.append((self.listeLettreColonnes.index(position[0]) - 1, self.listeNumeroLignes.index(position[1])))
        listeCoupsTemp.append((self.listeLettreColonnes.index(position[0]) - 1, self.listeNumeroLignes.index(position[1]) - 1))
        
        for coup in listeCoupsTemp:
            if coup[0] >= 0 and coup[0] <= 7 and coup[1] >= 0 and coup[1] <= 7:
                listeCoups.append((self.listeLettreColonnes[coup[0]], self.listeNumeroLignes[coup[1]]))

        return listeCoups