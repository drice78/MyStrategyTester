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
				board[r][c] = [player1_list.pop(), "player1"]

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
				board[r][c] = [player2_list.pop(), "player2"]


def create_player(piece_list, player):
  for key, value in piece_list.items():
    for i in range(value[1]):
      player.append(key)

def initiate_board(board):
	print ("Initiating Board")

  #Build a board of size 10 x 10
	for r in range(10):
		#for c in range(10):
			#Mark Lakes at positions on rows 4 and 5
			if r == 4 or r == 5:
				board.append([["empty", "none"]] * 2)
				board[r].append([["lake", "lake"]] * 2)
				board[r].append([["empty", "none"]] * 2)
				board[r].append([["lake", "lake"]] * 2)
				board[r].append([["empty", "none"]] * 2)
			else:
				#Put empty list into all other positions
				board.append([["empty", "none"]] * 10)
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
	return "Active"

def move_piece(board, player_pieces)
	#find a random movable piece
	random.shuffle(player_pieces)

	#move piece in random direction
	direction = random.randint(1,4)
	if direction == 1:
		#Check north
	elif direction == 2:
		#check south
	elif direction == 3:
		#check east
	else:
		#go west

	#if other player piece occupies new position, then battle
	if board[player_piece[1]][player_piece[2]] == 'lake' or playername
		valid_move = False
	else:
		valid_move = True

	if valid_move:
		if board


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
#print_board(board)

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

