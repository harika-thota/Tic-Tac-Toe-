"""Building a tic tac toe game 
requirments: 
	-board
	-display board
	-setting positions
	-play game 
	-shifting turns
	-taking input from user and displaying it in board 
	-check win 
		+check rows, columns, diaognal
	-check tie
"""
#----Global Variables----
#if game is still going
game_goingon = True
current_player = "X"
winner = None

board =["_", "_", "_", 
		"_", "_", "_", 
		"_", "_", "_" ]
		
#displaying a board
def display_board():
	print(board[0] +"|"+ board[1] +"|"+ board[2])
	print(board[3] +"|"+ board[4] +"|"+ board[5])
	print(board[6] +"|"+ board[7] +"|"+ board[8])

#shows who turn to play
def handle_turns(player):

	#shows who's turn
	print(player, "'s turn:")
	#asks for input from players
	user = input("choose from position 1-9: ")

    #prevents overwritting by players
	valid = False
	while not valid:
		#shows error if players enter invalid input
		while user not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			user = input("invalid input given!!!. choose a position from 1-9:")        

		#coverting user input to int
		user = int(user) - 1

		#now checking weather that particular position is avialable or not. prevents player to overwrite 
		if board[user] == "_":
			valid = True
		else:
			print("Already Occupied by other player. Kindly choose another position:") 


	#marks X or O at user input
	board[user] = player 
	#displays board after updating
	display_board()
	

#shows weather game is over or not 
def check_if_game_over():
	check_winner()
	check_tie()

#shows who wins the game
def check_winner():

	#overwriting global varibale inside a function  
	global winner
	#cehck rows 
	row_winner = check_rows()
	#check columns
	column_winner = check_columns()
	#check diagonals
	diaognal_winner = check_diagonals()
	
	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diaognal_winner:
		winner = diaognal_winner
	else:
		winner = None

	return 


#checking rows equal or not 
def check_rows():

	#setting up global variables
	global game_goingon
	r1 = board[0] == board[1] == board[2] !="_"
	r2 = board[3] == board[4] == board[5] !="_"
	r3 = board[6] == board[7] == board[8] !="_"
	#if the condition satisfies it stores true in r1 if not false  
	#if any row does have a match, flag that there is a win and should stop the game
	if r1 or r2 or r3:
		game_goingon = False
	#returns winner is X or O
	if r1 :
		return board[0]
	elif r2 :
		return board[3]
	elif r3 :
		return board[6]


	return

#checking columns equal or not 
def check_columns():

	global game_goingon
	c1 =  board[0] == board[3] == board[6] !="_"
	c2 =  board[1] == board[4] == board[7] !="_"
	c3 =  board[2] == board[5] == board[8] !="_"
	if c1 or c2 or c3 :
		game_goingon = False
	if c1:
		return board[0]
	elif c2:
		return board[1]
	elif c3:
		return board[2] 

	return

#checking diagonals equal or not 
def check_diagonals():

	global game_goingon
	d1 =  board[0] == board[4] == board[8] !="_"
	d2 =  board[2] == board[4] == board[6] !="_"
	
	if d1 or d2:
		game_goingon = False
	if d1:
		return board[0]
	elif d2:
		return board[2]

	return


#checks if game is draw
def check_tie():

	#set up global variables
	global game_goingon
	#if there is no _ in the board and no one wins; 
	#then game should be terminated and declared as tie.
	if "_" not in board:
		game_goingon = False

	return 


#shows who's turn to play game 
def flip_player():

	#set global variables
	global current_player
	#if current player is X, then it changes to O
	if current_player == "X" :
		current_player = "O"
	#if current player is O, then it changes to X
	elif current_player == "O" :
		current_player = "X"

	return


#game starts here
def play_game():

	#display intial board
	display_board()

#Allow player1 to play -->Checks if he wins, if not -->flip player
	while game_goingon: 
		handle_turns(current_player)
		check_if_game_over()
		flip_player()

	#The game has ended
	#if loop to decide and show who is the final winner 
	if winner == "X" or winner == "O":
		print(winner, "won the TIC TAC TOE game. HURRAY!!!")

	elif winner == None:
		print("Tie.")

play_game()	






