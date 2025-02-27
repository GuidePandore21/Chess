import pandas as pd
from Class.Pièces.Cavalier import Cavalier
from Class.Pièces.Fou import Fou
from Class.Pièces.Pion import Pion
from Class.Pièces.Dame import Dame
from Class.Pièces.Roi import Roi
from Class.Pièces.Tour import Tour

class Board:
    def __init__(self):
        self.listeLettreColonnes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.listeNumeroLignes = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.matrice = self.createBoard()
    
    def createBoard(self):
        grille = {col: [None for _ in range(8)] for col in self.listeNumeroLignes}
        return pd.DataFrame(grille, index=self.listeLettreColonnes)  
    
    def placementPiecesInitiales(self):
        for col in self.listeLettreColonnes:
            self.matrice.loc[col, '2'] = Pion("blanc")
            self.matrice.loc[col, '7'] = Pion("noir")

        self.matrice.loc['A', '1'] = Tour("blanc")
        self.matrice.loc['H', '1'] = Tour("blanc")
        self.matrice.loc['A', '8'] = Tour("noir")
        self.matrice.loc['H', '8'] = Tour("noir")
        
        self.matrice.loc['B', '1'] = Cavalier("blanc")
        self.matrice.loc['G', '1'] = Cavalier("blanc")
        self.matrice.loc['B', '8'] = Cavalier("noir")
        self.matrice.loc['G', '8'] = Cavalier("noir")
        
        self.matrice.loc['C', '1'] = Fou("blanc")
        self.matrice.loc['F', '1'] = Fou("blanc")
        self.matrice.loc['C', '8'] = Fou("noir")
        self.matrice.loc['F', '8'] = Fou("noir")
        
        self.matrice.loc['D', '1'] = Dame("blanc")
        self.matrice.loc['D', '8'] = Dame("noir")
        
        self.matrice.loc['E', '1'] = Roi("blanc")
        self.matrice.loc['E', '8'] = Roi("noir")
