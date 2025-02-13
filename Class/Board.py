import pandas as pd
class Board:
    def __init__(self):
        self.matrice = self.createBoard()
    
    def createBoard(self):
        grille = {}
        listeLettreColonnes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        listeNumeroLignes = ['1', '2', '3', '4', '5', '6', '7', '8']
        for i in range(8):
            grille[listeLettreColonnes[i]] = [' ' for _ in range(8)]
        
        return pd.DataFrame(grille, index=listeNumeroLignes)    
    