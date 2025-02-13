from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def getPossibleMoves(self, position):
        pass