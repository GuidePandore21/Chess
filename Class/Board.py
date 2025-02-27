import pandas as pd

class Board:
    def __init__(self):
        self.listeLettreColonnes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.listeNumeroLignes = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.matrice = self.createBoard()
    
    def createBoard(self):
        grille = {col: [None for _ in range(8)] for col in self.listeNumeroLignes}
        return pd.DataFrame(grille, index=self.listeLettreColonnes)  
