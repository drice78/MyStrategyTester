#Main program for testing Strategy board game layout against sample of random
#opponent boards

def build_board(board, player1_list, player2_list):
  print ('Building Board')
  
  #Randomly place player1 pieces onto board positions within (0,0-9) and (3,0-9)
  print ('Placeing pieces for player1')
  
  #Populate player2 special strategy locations first
  print ('Placing strategy pieces for player2')
  
  #Populate remaining player2 pieces into positions within (6,0-9) and (9,0-9)
  print ('Placing remaining player2 pieces')

def create_player(piece_list, player):
  print ("Creating Player")
  print (piece_list)
  for key, value in piece_list.items():
    for i in range(value):
      print ("Adding " + key)
      player.append(key)
  
def initiate_board(board):
  print ("Initiating Board")
    
  #Build a board of size 10 x 10
  
  #Mark Lakes at positions (4,2-3),(5,2-3) and (4,6-7),(5,6-7)
  
  return board

def print_board(board):
  print ("Displaying Board")

def get_game_status(board, player1_list, player2_list):
  print ("Getting status of game")
  return "Active"
  
board = []
player1 = []
player2 = []

#Initiate the turn number to 0
turn_number = 0

#Define piece names and quantity
pieces = {'marshal':1, 'general':1, 'colonel':2, 'major':3, 'captain':4, 
          'lieutenant':4, 'sergeant':4, 'minor':5, 'scout':8, 'bomb':6, 
          'spy':1, 'flag':1}

print (pieces['bomb'])
print ('Welcome to Strategy Tester')

# Create the Board
initiate_board(board)

#Display the board
print_board(board)

# Create the pieces lists for both players
create_player(pieces, player1)
create_player(pieces, player2)


#Populate the board with pieces from each player
build_board(board, player1, player2)

#Display initial board state
print_board(board)

#Determine who goes first randomly

#Move until game is over
while get_game_status(board, player1, player2):
  turn_number = turn_number + 1
  print ("Turn " + str(turn_number))
  #Pick random movable piece for active player
  
  #Move Piece
  
    #Battle or take empty space
  
  #Display board state
  print_board(board)
  
  #Check if game winning move was made
  if turn_number >= 20:
    break

