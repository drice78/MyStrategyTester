#Main program for testing Strategy board game layout against sample of random
#opponent boards
import random 


#Things to Do
#1) Mark if a piece is known to the other player
#2) If piece is known to player then don't purposely attack with guaranteed loss, unless there are no other moves
#3) Target miners towards bombs?
#4) check for stalemate scenarios, such as no miners to clear remaining bombs
#5) check for player with no moveable pieces at all, i.e. bombs and flags only





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
	board[5][3] = ['lake', 'lake', False]
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

def is_right_clear(row, column):
	if column == 9:
		return False
	elif board[row][column + 1][1] == 'lake' or board[row][column + 1][1] == board[row][column][1]:
		return False
	else:
		return True

def is_left_clear(row, column):
	if column == 0:
		return False
	elif board[row][column - 1][1] == 'lake' or board[row][column - 1][1] == board[row][column][1]:
		return False
	else:
		return True

def is_below_clear(row, column):
	if row == 9:
		return False
	elif board[row + 1][column][1] == 'lake' or board[row + 1][column][1] == board[row][column][1]:
		return False
	else:
		return True

def is_above_clear(row, column):
	if row == 0:
		return False
	elif board[row - 1][column][1] == 'lake' or board[row - 1][column][1] == board[row][column][1]:
		return False
	else:
		return True


def moves_left(board, player1_list, player2_list):
	print ("Getting status of game")

	moves = False # assume no move until one is found
	#loop through board and update whether a piece is movable or not based on its neighboars
	for r in range(10):
		for c in range(10):
			#check movement possibilities for player pieces
			if board[r][c][1] == "player1" or board[r][c][1] == "player2":
				#check nearby locations and mark if movable
				if board[r][c][0] == 'flag' or board[r][c][0] == 'bomb':
					board[r][c][2] = False
				elif is_right_clear(r, c) or is_left_clear(r, c) or is_above_clear(r, c) or is_below_clear(r, c):
					board[r][c][2] = True
					moves = True
				else:
					board[r][c][2] = False
	return moves

def piece_value(piecename):
	value = pieces.get(piecename)[0]
	return value

def battle(att_r, att_c, def_r, def_c):
		#battle royale
	print ("Battle is beginning")
	attacker = board[att_r][att_c][0]
	defender = board[def_r][def_c][0]

	print ("{} is attacking {}").format(attacker, defender)

	if defender == "flag":
		#Game Over!!!a
		print ("{}'s flag has been captured!").format(board[def_r][def_c][1])
		flag_captured = True
	elif defender == "empty":
		#move piece
		board[def_r][def_c] = board[att_r][att_c]
		board[att_r][att_c] = ["empty", "empty", False]
		print ("{} moved").format(attacker)
	elif defender == "bomb":
		if attacker == "miner":
			board[def_r][def_c] = board[att_r][att_c]
			board[att_r][att_c] = ["empty", "empty", False]
			print ("{} defeated {}").format(attacker, defender)
		else:
			board[att_r][att_c] = ["empty", "empty", False]
			print ("{}, lost to {}").format(attacker, defender)
	elif attacker == "spy":
		if defender == "marshal":
			board[def_r][def_c] = board[att_r][att_c]
			board[att_r][att_c] = ["empty", "empty", False]
			print ("{} defeated {}").format(attacker, defender)
		else:
			board[att_r][att_c] = ["empty", "empty", False]
			print ("{}, lost to {}").format(attacker, defender)
	else:
		if piece_value(attacker) <= piece_value(defender):
			board[def_r][def_c] = board[att_r][att_c]
			board[att_r][att_c] = ["empty", "empty", False]
			print ("{} defeated {}").format(attacker, defender)
		else:
			print ("{}, lost to {}").format(attacker, defender)
			board[att_r][att_c] = ["empty", "empty", False]


def move_piece(row, column):
	checkcount = 0
	battlecount = 0

	#pick a random direction
	direction = random.randint(0,3)

	while checkcount < 4 and battlecount < 1:
		#check if direction is free, if not iterate(for 3 times) to find first available move
		if  direction == 0: 
			#check up
			if is_above_clear(row, column):
				#move up
				battle(row, column, row - 1, column)
				battlecount = battlecount + 1
		elif direction == 1:
			#check right
			if is_right_clear(row, column):
				#move right
				battle(row, column, row, column + 1)
				battlecount = battlecount + 1
		elif direction == 2:
			#check down
			if is_below_clear(row, column):
				#move down
				battle(row, column, row + 1, column)
				battlecount = battlecount + 1
		elif direction == 3:
			#check left
			if is_left_clear(row, column):
				#move left
				battle(row, column, row, column -1)
				battlecount = battlecount + 1

		if battlecount == 0:
			if direction == 3:
				direction = 0
			else:
				direction = direction + 1
		checkcount = checkcount + 1

	#if space is free, just move

	#if space is occupied by opponent, then lets battle




#Initialize board and player lists
board = []
player1 = []
player2 = []
moveable = []
#Initiate the turn number to 0
turn_number = 0
flag_captured = False

#Define piece names and quantity {name : [value, quantity]}
pieces = {'marshal' : [1, 1], 'general' : [2, 1], 'colonel' : [3, 2], 'major' : [4, 3], 'captain' : [5, 4],
				'lieutenant' : [6, 4], 'sergeant' : [7, 4], 'miner' : [8, 5], 'scout' : [9, 8], 'bomb' : [10, 6],
          'spy' : [11, 1], 'flag' : [12, 1]}

print ('Welcome to Strategy Tester')
MAX_TURNS = raw_input("Enter the max number of turns: ")
print ("You entered: {}").format(MAX_TURNS)
isCorrect = raw_input("Is that correct?")

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
	curPlayer = "player1"
	#move_piece(player1)
else:
	curPlayer = "player2"
	print ("Player 2 goes first")
		#move_piece(player2)
#Move until game is over
while moves_left(board, player1, player2) and flag_captured != True:
	turn_number = turn_number + 1
	print ("Turn {}").format(turn_number)
	moveable[:] = []
	moveable_count = 0
	#Pick random movable piece for active player
	#Lets first try to print out pieces that are moveable and reduce our list of random picking.
	for r in range(10):
		for c in range(10):
			if board[r][c][2] and board[r][c][1] == curPlayer:
				moveable.append([r, c])
				moveable_count = moveable_count + 1
	print ("{} has {} moveable pieces").format(curPlayer, moveable_count)

	#pick random from moveable
	if	moveable_count > 0:
		random.shuffle(moveable)
		print ("Moving {},{}").format(moveable[0][0], moveable[0][1])

		#Move Piece
		move_piece(moveable[0][0], moveable[0][1])
	else:
		print("Cannot move for {}").format(curPlayer)

	#Display board state
	#print_board(board)
	#Check if game winning move was made
	if turn_number >= int(MAX_TURNS):
		print ("Ran out of turns")
		break

	#Change player
	if curPlayer == 'player1':
		curPlayer = 'player2'
		print ("Player 2 moved next")
	else:
		curPlayer = 'player1'
		print ("Player 1 moves next")

	#Print the pieces owned by current player
	for pr in range(10):
		for pc in range(10):
			if board[pr][pc][1] == curPlayer:
				print ("{}, - {}").format(board[pr][pc][0], board[pr][pc][2])

if flag_captured:
	print ("Game ended in flag capture")
else:
	print ("Game ended in stale mate due to lack of moving pieces left")
