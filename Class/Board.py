class Board:
    def __init__(self):
        matrice = self.buildBoard()
    
    def createBoard(self):
        self.matrice = []
        for i in range(8):
            self.matrice.append([])
            for j in range(8):
                self.matrice[i].append(' ')
        return self.matrice