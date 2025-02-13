from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def move(self, start_pos, end_pos):
        pass

    @abstractmethod
    def getPossibleMoves(self, position):
        pass