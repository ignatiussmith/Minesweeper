#Author:		Ignatius Smith
#Date:		19-Aug-2020
#Description:	Minesweeper, will eventually make it chaotic

import random
#Game will probably be a class
#Board will probably be a class
def MakeBoard(size): 
	
	if size == 'B':
		#initialize the board, this prolly could be its own function
		board = initialize_board(10, 10)
		produce_minefield(10, board)	
	if size == 'I':
		board = initialize_board(20, 40)
		produce_minefield(100, board)
		
	return board;
	
def PrintBoard(board):
	for i in board:
		print(*i, sep = " ") #formatting can be better
		
def initialize_board(no_rows, no_columns):
	board = []
	for i in range(no_rows):
		new_list = [];
		for j in range(no_columns):
			new_list.append(0);
		board.append(new_list)
	return board
	
def produce_single_mine(p):
	if random.random() < p:
		return True
	else:
		return False

def iterate_neighbors(row, column, board):
	new_board = board;
	#if its a valid index, and doesn't touch a mine, we iterate
	if row + 1 < len(board):
		if column + 1 < len(new_board[row]):
			if new_board[row + 1][column + 1] != 'm':
				new_board[row + 1][column + 1] += 1
		if column - 1 >= 0:
			if new_board[row + 1][column - 1] != 'm':
				new_board[row + 1][column - 1] += 1
				
		if new_board[row + 1][column] != 'm':
				new_board[row + 1][column] += 1
			
	if row - 1 >= 0:
		if column + 1 < len(new_board[row]):
			if new_board[row - 1][column + 1] != 'm':
				new_board[row - 1][column + 1] += 1
		if column - 1 >= 0:
			if new_board[row - 1][column - 1] != 'm':
				new_board[row - 1][column - 1] += 1
		if new_board[row - 1][column] != 'm':
				new_board[row - 1][column] += 1
	if row == row:
		if column + 1 < len(new_board[row]):
			if new_board[row][column + 1] != 'm':
				new_board[row][column + 1] += 1
		if column - 1 >= 0:
			if new_board[row][column - 1] != 'm':
				new_board[row][column - 1] += 1
		
	return new_board
	
def produce_minefield(no_mines, board):
	board_avec_mines = board
	no_placed_mines = 0
	#iterate through squares, choose mine with probability mines/squares
	prob_mine = no_mines / (len(board) * len(board[1]))
	for i in range(len(board)):
		for j in range(len(board[i])):
			if produce_single_mine(prob_mine) and no_placed_mines < no_mines:
				board_avec_mines[i][j] = 'm'
				no_placed_mines += 1
				board_avec_mines = iterate_neighbors(i, j, board_avec_mines)
				
	#if we don't hit target no. mines, then yeet one in there
		#chance to be chaotic with lying about mine no.
	while no_placed_mines < no_mines:
		row = int(random.random() * len(board))
		column = int(random.random() * len(board[0]))
		if board_avec_mines[row][column] != 'm':
			board_avec_mines[row][column] = 'm'
			no_placed_mines += 1
			board_avec_mines = iterate_neighbors(row, column, board_avec_mines)

	#when a mine is placed, iterate all surround squares (excl. mines) up
	
	#check for spaces with zero mines touching, and mark as such	
	
for i in range(5):	
	PrintBoard(MakeBoard('B'))
	print(' ')
#PrintBoard(MakeBoard('I'))
