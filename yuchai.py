import gamePlay
from random import shuffle

INFINITY = 1000000000

#It's a board of weight of each position. Corners and most edges are important.
gradingStrategy = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0, 100, -10,  10,   3,   3,  10, -10, 100,   0,
    0, -10, -20,  -3,  -3,  -3,  -3, -20, -10,   0,
    0,  10,  -3,   8,   1,   1,   8,  -3,  10,   0,
    0,   3,  -3,   1,   1,   1,   1,  -3,   3,   0,
    0,   3,  -3,   1,   1,   1,   1,  -3,   3,   0,
    0,  10,  -3,   8,   1,   1,   8,  -3,  10,   0,
    0, -10, -20,  -3,  -3,  -3,  -3, -20, -10,   0,
    0, 100, -10,  10,   3,   3,  10, -10, 100,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
]
def eval_fn(board, color):
	# if the game is over, give a 100 point bonus to the winning player
    if gamePlay.gameOver(board):
        point = gamePlay.score(board)
        if point > 0:
            return 100
        elif point < 0:
            return -100
        else:
            return 0
    point = 0
    #find the color of the opponent
    opp = gamePlay.opponent(color)
    for row in range(8):
        for col in range(8):
            #calculate the point of current player
            if board[row][col] == color:
                point += gradingStrategy[(row+1)*10+1+col]
            #calculate the point of the opponent
            elif board[row][col] == opp:
                point -= gradingStrategy[(row+1)*10+1+col]
    return point

def minimax(board, color, depth):
  	#Find the best move in the game
  	#if depth = 0, we calculate the score
    if depth == 0:
    	return eval_fn(board, color)
    #if game is over, we calculate the score
    if gamePlay.gameOver(board):
        return gamePlay.score(board)

    best_val = None
    best_move = None
    opp = gamePlay.opponent(color)
    # valid moves
    moves = []
    for row in range(8):
    	for col in range(8):
    		if gamePlay.valid(board, color, (row,col)):
			 	moves.append((row,col))
	#shuffle the moves in case it places the same position in every game
	#shuffle(moves)
	if len(moves) == 0:
		return "pass"
	if move == "pass":
		return eval_fn(board, color)
	#try each move in valid moves
    #evaluate max's position and choose the best value
	if color == "B":
		for move in moves:
			newBoard = board[:]
    		gamePlay.doMove(newboard, color, move)
    		val = minimax(newBoard, opp, depth-1)
    		if best_val is None or val > (best_val, best_move)[0]:
				(best_val, best_move) = (val, move)
    #evaluate min's position and choose the best value
    if color == "W":
    	for move in moves:
			newBoard = board[:]
			gamePlay.doMove(newboard, color, move)
			val = minimax(newBoard, opp, depth-1)
			if best_val is None or val < (best_val, best_move)[0]:
				(best_val, best_move) = (val, move)
    return (best_val, best_move)[0]
def alpha_beta(board, color, depth, alpha, beta):
	"""Find the utility value of the game and the best_val move in the game."""
	
	if depth == 0:
		return eval_fn(board, color)
	if gamePlay.gameOver(board):
		return gamePlay.score(board)
	
	moves = []
	for row in range(8):
		for col in range(8):
			if gamePlay.valid(board, color, (row, col)):
				moves.append((row, col))
	#shuffle the moves in case it places the same position in every game
	#shuffle(moves)
	if len(moves) == 0:
		return "pass"
	if moves == "pass":
		return eval_fn(board, color)

	opp = gamePlay.opponent(color)
	# try each move
	#evaluate max's position and choose the best value
	if color == "B":
		for move in moves:
			newBoard = board[:]
			gamePlay.doMove(newBoard, color, move)
			#cut off the branches
			alpha = max(alpha, alpha_beta(newBoard, opp, depth-1, alpha, beta))
			if beta <= alpha:
				return
		return alpha
	#evaluate min's position and choose the best value
	if color == "W":
		for move in moves:
			newBoard = board[:]
			gamePlay.doMove(newBoard, color, move)
			#cut off the branches
			beta = min(beta, alpha_beta(newBoard, opp, depth-1, alpha, beta))
			if beta <= alpha:
				return
		return beta
def nextMove(board, color, time):
	best_val = None
	best_move = None
	moves = []
	for row in range(8):
		for col in range(8):
			if gamePlay.valid(board, color, (row, col)):
				moves.append((row, col))
	#shuffle the moves in case it places the same position in every game
	#shuffle(moves)
	if len(moves) == 0:
		return "pass"
	if moves == "pass":
		return "pass"
	opp = gamePlay.opponent(color)
	#evaluate max's position and choose the best value
	if color == "B":
		for move in moves:
			newBoard = board[:]
			gamePlay.doMove(newBoard, color, move)
			#alpha = - INFINITY beta = INFINITY
			#we want to choose the max one
			if best_val = max(best_val, alpha_beta(newBoard, opp, 3, -INFINITY, INFINITY)):
				#update best move
				best_move = move
	#evaluate min's position and choose the best value
	if color == "W":
		for move in moves:
			newBoard = board[:]
			gamePlay.doMove(newBoard, color, move)
			#alpha = - INFINITY beta = INFINITY
			#we want to choose the min one
			if best_val = min(best_val, alpha_beta(newBoard, opp, 3, -INFINITY, INFINITY)):
				#update best move
				best_move = move
	return best_move
		
			
	