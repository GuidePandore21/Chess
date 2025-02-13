from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        self.color = color
        self.listeLettreColonnes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.listeNumeroLignes = ['1', '2', '3', '4', '5', '6', '7', '8']

    @abstractmethod
    def getPossibleMoves(self, position):
        pass