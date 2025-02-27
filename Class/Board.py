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
    
    def coupPossibleCavalier(self, piece, position):
        deplacements = piece.getPossibleMoves(position)
        listeCoups = []
        for deplacement in deplacements:
            if self.matrice.loc[deplacement[0], deplacement[1]] is None:
                listeCoups.append(deplacement)
            elif self.matrice.loc[deplacement[0], deplacement[1]].color != piece.color:
                listeCoups.append(deplacement)
        return listeCoups
    
    def coupPossibleFou(self, piece, position):
        listeCoups = []
        for direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for i in range(1, 8):
                x = ord(position[0]) + i * direction[0]
                y = int(position[1]) + i * direction[1]
                if chr(x) in self.listeLettreColonnes and str(y) in self.listeNumeroLignes:
                    if self.matrice.loc[chr(x), str(y)] is None:
                        listeCoups.append([chr(x), str(y)])
                    elif self.matrice.loc[chr(x), str(y)].color != piece.color:
                        listeCoups.append([chr(x), str(y)])
                    else:
                        return listeCoups
                else:
                    return listeCoups
        return listeCoups
    
    def coupPossibleTour(self, piece, position):
        listeCoups = []
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for i in range(1, 8):
                x = ord(position[0]) + i * direction[0]
                y = int(position[1]) + i * direction[1]
                if chr(x) in self.listeLettreColonnes and str(y) in self.listeNumeroLignes:
                    if self.matrice.loc[chr(x), str(y)] is None:
                        listeCoups.append([chr(x), str(y)])
                    elif self.matrice.loc[chr(x), str(y)].color != piece.color:
                        listeCoups.append([chr(x), str(y)])
                    else:
                        return listeCoups
                else:
                    return listeCoups
        return listeCoups
    
    def coupPossiblePion(self, piece, position):
        deplacements = piece.getPossibleMoves(position)
        listeCoups = []
        for deplacement in deplacements:
            if self.matrice.loc[deplacement[0], deplacement[1]] is None:
                listeCoups.append(deplacement)
            elif self.matrice.loc[deplacement[0], deplacement[1]].color != piece.color:
                listeCoups.append(deplacement)
                
        # Attaque en diagonale
        if piece.color == "blanc":
            x = ord(position[0]) + 1
            y = int(position[1]) + 1
            if chr(x) in self.listeLettreColonnes and str(y) in self.listeNumeroLignes:
                if self.matrice.loc[chr(x), str(y)] is not None and self.matrice.loc[chr(x), str(y)].color != piece.color:
                    listeCoups.append([(chr(x), str(y))])
            x = ord(position[0]) - 1
            y = int(position[1]) + 1
            if chr(x) in self.listeLettreColonnes and str(y) in self.listeNumeroLignes:
                if self.matrice.loc[chr(x), str(y)] is not None and self.matrice.loc[chr(x), str(y)].color != piece.color:
                    listeCoups.append([(chr(x), str(y))])
        else:
            x = ord(position[0]) + 1
            y = int(position[1]) - 1
            if chr(x) in self.listeLettreColonnes and str(y) in self.listeNumeroLignes:
                if self.matrice.loc[chr(x), str(y)] is not None and self.matrice.loc[chr(x), str(y)].color != piece.color:
                    listeCoups.append([(chr(x), str(y))])
            x = ord(position[0]) - 1
            y = int(position[1]) - 1
            if chr(x) in self.listeLettreColonnes and str(y) in self.listeNumeroLignes:
                if self.matrice.loc[chr(x), str(y)] is not None and self.matrice.loc[chr(x), str(y)].color != piece.color:
                    listeCoups.append([(chr(x), str(y))])
        
        return listeCoups
    
    def coupPossibleRoi(self, piece, position):
        listeCoups = []
        couleurAdverse = "noir" if piece.color == "blanc" else "blanc"        
        for direction in [(1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = ord(position[0]) + direction[0]
            y = int(position[1]) + direction[1]
            if [x, y] not in self.touslesCoupsPossibles(couleurAdverse):
                if chr(x) in self.listeLettreColonnes and str(y) in self.listeNumeroLignes:
                    if self.matrice.loc[chr(x), str(y)] is None:
                        listeCoups.append([chr(x), str(y)])
                    elif self.matrice.loc[chr(x), str(y)].color != piece.color:
                        listeCoups.append([chr(x), str(y)])
        return listeCoups

    def tousLesCoupsPossibles(self, couleur):
        listeCoups = []
        for col in self.listeNumeroLignes:
            for row in self.listeLettreColonnes:
                piece = self.matrice.loc[row, col]
                if piece and piece.color == couleur:
                    if isinstance(piece, Pion):
                        listeCoups.append(self.coupPossiblePion(piece, [row, col]))
                    elif isinstance(piece, Cavalier):
                        listeCoups.append(self.coupPossibleCavalier(piece, [row, col]))
                    elif isinstance(piece, Fou):
                        listeCoups.append(self.coupPossibleFou(piece, [row, col]))
                    elif isinstance(piece, Tour):
                        listeCoups.append(self.coupPossibleTour(piece, [row, col]))
                    elif isinstance(piece, Dame):
                        listeCoups.append(self.coupPossibleFou(piece, [row, col]))
                        listeCoups.append(self.coupPossibleTour(piece, [row, col]))
                    elif isinstance(piece, Roi):
                        listeCoups.append(self.coupPossibleRoi(piece, [row, col]))
        return listeCoups
        