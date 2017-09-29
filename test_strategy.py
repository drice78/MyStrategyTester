#Main program for testing Strategy board game layout against sample of random
#opponent boards
import random 

def build_board(board, player1_list, player2_list):
	print ('Building Board')

	#Randomly place player1 pieces onto board positions within (0,0-9) and (3,0-9)
	print ('Placing pieces for player1')
	#Pop a single piece from the players list as long as the list is not empty

	#lets shuffle our list
	random.shuffle(player1_list)

	#Start adding pieces until we run out
	for r in range(4):
		for c in range(10):
			if not player1_list:
				print "We ran out of pieces"
				break
			else:
				board[r][c] = [player1_list.pop(), "player1", False]

	#Populate player2 special strategy locations first
	print ('Placing strategy pieces for player2')

	#Populate remaining player2 pieces into positions within (6,0-9) and (9,0-9)

	#Shuffle the list first
	random.shuffle(player2_list)

	print ('Placing remaining player2 pieces')
	for r in range(6,10):
		for c in range(10):
			if not player2_list:
				print "We ran out of pieces"
			else:
				print ("{}, {}").format(r, c)
				board[r][c] = [player2_list.pop(), "player2", False]


def create_player(piece_list, player):
  for key, value in piece_list.items():
    for i in range(value[1]):
      player.append(key)

def initiate_board(board):
	print ("Initiating Board")

  #Build a board of size 10 x 10
	for r in range(10):
		#Put empty list into all other positions
		board.append([["empty", "none", False]] * 10)
	#Add lakes
	board[4][2] = ['lake', 'lake', False]
	board[4][3] = ['lake', 'lake', False]
	board[5][2] = ['lake', 'lake', False]
	board[4][3] = ['lake', 'lake', False]
	board[4][6] = ['lake', 'lake', False]
	board[4][7] = ['lake', 'lake', False]
	board[5][6] = ['lake', 'lake', False]
	board[5][7] = ['lake', 'lake', False]

	return board

def print_board(board, player="NONE"):
	print ("Displaying Board")
	if player == "NONE":
		for r in board:
			print (r)
	else:
		#print board showing where pieces exist, but hiding value if piece is owned by the other player
		print ("Cannot display for a single player....yet")

def get_game_status(board, player1_list, player2_list):
	print ("Getting status of game")

	moves = False # assume no move until one is found
	#loop through board and update whether a piece is movable or not based on its neighboars
	for r in range(10):
		for c in range(10):
			#check for empty or opposing player pieces
			print ("{},{}: {}").format(r,c,board[r][c])
			if board[r][c][1] == "player1" or board[r][c][1] == "player2":
				#check nearby locations and mark if movable
#
#
#
# Need to check if it is on the top row, then check for right or left, then check final direcitons. Repeat for bottom row. 
#
#
#


				print ("We found a player piece at {},{}").format(r,c)
				if c < 9:
					if board[r][c+1][1] == "empty" or board[r][c+1][1] != board[r][c+1][1] and board[r][c+1][1] != 'lake':
					print ("Clear in the right")
					board[r][c][2] = False
					moves = True
				elif board[r][c-1][1] == "empty" or board[r][c-1][1] != board[r][c-1][1] and board[r][c-1][1] != 'lake':
					print ("Clearn on the left")
					board[r][c][2] = False
					moves = True
				elif board[r+1][c][1] == "empty" or board[r+1][c][1] != board[r+1][c][1] and board[r+1][c][1] != 'lake':
					print ("Clear down below")
					board[r][c][2] = False
					moves = True
				elif board[r-1][c][1] == "empty" or board[r-1][c][1] != board[r-1][c][1] and board[r-1][c][1] != 'lake':
					print ("Clear up above")
					board[r][c][2] = False
					moves = True
				print ("Moveable is {}").format(moves)
	return "Active"

def move_piece(board, player_pieces, playername):
	#find a random movable piece
	random.shuffle(player_pieces)

	#move piece in random direction

	#if other player piece occupies new position, then battle
	if board[player_piece[1]][player_piece[2]]  == 'lake':
		valid_move = False
	else:
		valid_move = True



#Initialize board and player lists
board = []
player1 = []
player2 = []

#Initiate the turn number to 0
turn_number = 0

#Define piece names and quantity {name : [value, quantity]}
pieces = {'marshal' : [1, 1], 'general' : [2, 1], 'colonel' : [3, 2], 'major' : [4, 3], 'captain' : [5, 4],
				'lieutenant' : [6, 4], 'sergeant' : [7, 4], 'miner' : [8, 5], 'scout' : [9, 8], 'bomb' : [10, 6],
          'spy' : [11, 1], 'flag' : [12, 1]}

print ('Welcome to Strategy Tester')

# Create the Board
initiate_board(board)

#Display the board

# Create the pieces lists for both players
create_player(pieces, player1)
create_player(pieces, player2)

#Populate the board with pieces from each player
build_board(board, player1, player2)

#Display initial board state
print_board(board)

#Determine who goes first randomly
if random.randint(1,2) == 1:
	print ("Player 1 goes first")
	#move_piece(player1)
else:
	print ("Player 2 goes first")
		#move_piece(player2)
#Move until game is over
while get_game_status(board, player1, player2):
  turn_number = turn_number + 1
  print ("Turn " + str(turn_number))
  #Pick random movable piece for active player

  #Move Piece

    #Battle or take empty space

  #Display board state
  #print_board(board)

  #Check if game winning move was made
  if turn_number >= 2:
    break

