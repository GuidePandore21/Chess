from Class.ChessGame import ChessGame

game = ChessGame(50)
print(game.board.coupPossiblePion(game.board.matrice.loc['E', '2'], ['E', '2']))
game.run()