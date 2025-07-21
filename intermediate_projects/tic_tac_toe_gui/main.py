import tkinter as tk
from tkinter import messagebox
import random

#CONSTANTS
PLAYER_X = 'X'
PLAYER_X_COLOR = '#FF5555'
PLAYER_O = 'O'
PLAYER_O_COLOR = '#55FFFF'
BACKGROUND_COLOR = '#121212'
GRID_COLOR = '#1F1F1F'
WIN_COLOR = '#FFD700'
BUTTON_COLOR = '#1A1A1A'
GRID_FONT = ('consolas', 40, 'bold')
BUTTON_FONT = ('consolas', 10, 'bold')


#VARIABLES
board=[[0,0,0],[0,0,0],[0,0,0]]
current_player = PLAYER_X
ai_thinking = False
game_over = False
vs_ai = True
current_difficulty = 'Easy'


#FUNCTIONS
#Win check
def win_check():
	global game_over, current_player
	
	
	#Checking row
	for row in range(3):
		if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != '':
			for column in range(3):
				winner = board[row][0]['text']
				label.config(text=f'{winner} won!', fg=WIN_COLOR)
				board[row][column].config(bg=BACKGROUND_COLOR, fg=WIN_COLOR)
			game_over = True
			messagebox.showinfo(title='Tic Tac Tie', message=f'Player {winner} won!')
			restart_game()
			return
	#Checking column			
	for column in range(3):
		if board[0][column]['text'] == board[1][column]['text'] == board[2][column]['text'] != '':
			for row in range(3):
				winner = board[0][column]['text']
				label.config(text=f'{winner} won!', fg=WIN_COLOR)
				board[row][column].config(bg=BACKGROUND_COLOR, fg=WIN_COLOR)
			game_over = True
			messagebox.showinfo(title='Tic Tac Tie', message=f'Player {winner} won!')
			restart_game()
			return
	#Checking diagonal \
	if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
		winner = board[0][0]['text']
		label.config(text=f'{winner} won!', fg=WIN_COLOR)
		for diagonal in range(3):
			board[diagonal][diagonal].config(bg=BACKGROUND_COLOR, fg=WIN_COLOR)
		game_over = True
		messagebox.showinfo(title='Tic Tac Tie', message=f'Player {winner} won!')
		restart_game()
		return	
	#Checking Diagonal /
	elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
		winner = board[0][2]['text']
		label.config(text=f'{winner} won!', fg=WIN_COLOR)
		board[0][2].config(bg=BACKGROUND_COLOR, fg=WIN_COLOR)
		board[1][1].config(bg=BACKGROUND_COLOR, fg=WIN_COLOR)
		board[2][0].config(bg=BACKGROUND_COLOR, fg=WIN_COLOR)
		game_over = True
		messagebox.showinfo(title='Tic Tac Tie', message=f'Player {winner} won!')
		restart_game()
		return
	#Checking Draw
	if all(board[r][c]['text'] != '' for r in range(3) for c in range(3)):
		label.config(text='It\'s a draw!', fg=WIN_COLOR)
		game_over = True
		messagebox.showinfo(title='Tic Tac Tie', message='It\'s a draw!')
		restart_game()
		return

#Updating grid according to current player
def place_mark(row, column):
	global ai_thinking, current_player
	
	if ai_thinking or game_over:
		return
	
	if board[row][column]['text'] != '':
		return

		
	if current_player == PLAYER_X:
		board[row][column].config(text=PLAYER_X, fg=PLAYER_X_COLOR) 
		current_player = PLAYER_O
		label['text'] = f'{PLAYER_O}\'s turn'
		win_check()
		if vs_ai and not game_over:
			root.after(600, ai_mode)
			return
	else:
		board[row][column].config(text=PLAYER_O, fg=PLAYER_O_COLOR)
		current_player = PLAYER_X
		label['text'] = f'{PLAYER_X}\'s turn'
		win_check()
		return
		

#Helper function
def is_winner(player):
	for i in range(3):
		#Rows
		if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] == player:
			return True
		#Columns
		elif board[0][i]['text'] == board[1][i]['text'] == board[2][i]['text'] == player:
			return True
	#Diagonal \
	if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] == player:
		return True
	#Diagonal /
	elif board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] == player:
		return True
	
	return False
		
			

#Find winning players
def find_winning_move(player):
	for r in range(3):
		for c in range(3):
			if board[r][c]['text'] == '':
				board[r][c]['text'] = player
				if is_winner(player):
					board[r][c]['text'] = ''
					return r,c
				board[r][c]['text'] = '' 
	return None
			

			
#AI mode
def ai_mode():
	global ai_thinking, current_player
	
	if game_over:
		return
	
	ai_thinking = True
	
	if current_difficulty == 'Hard':
		move = find_winning_move(PLAYER_O)
		
		if not move:
			move = find_winning_move(PLAYER_X)
			
		if not move:
			empty_cell = [(r,c) for r in range(3) for c in range(3) if board[r][c]['text'] == '']
			if not empty_cell:
				return
			move = random.choice(empty_cell)
			
		row, col = move
	else:
		empty_cell = [(r,c) for r in range(3) for c in range(3) if board[r][c]['text'] == '']
		if not empty_cell:
			return
		move = random.choice(empty_cell)
		row, col = move
		
	board[row][col].config(text=PLAYER_O, fg=PLAYER_O_COLOR)
	current_player = PLAYER_X
	label['text'] = f'{current_player}\'s turn'
		
	root.after(200, ai_thinking_false)
	
	win_check()
	

#Setting AI thinking to false
def ai_thinking_false():
	global ai_thinking
	ai_thinking = False
	return
	
	
def restart_game():
	global ai_thinking, current_player, game_over, turns
	
	turns = 0
	game_over = False
	ai_thinking = False
	current_player = PLAYER_X
	
	label.config(text=f'{current_player}\'s turn', fg='white')
	for row in range(3):
		for column in range(3):
			board[row][column].config(text='', bg=GRID_COLOR)
		

#Toggle mode
def toggle_mode():
	global vs_ai
	
	vs_ai = not vs_ai
	
	if vs_ai:
		mode_button['text'] = 'Mode: Single Player'
	else:
		mode_button['text'] = 'Mode: Multiplayer'
		
	restart_game()


#Difficulty mode
def difficulty_mode():
	global current_difficulty
	if current_difficulty == 'Easy':
		current_difficulty = 'Hard'
		difficulty_button['text'] = f'Difficulty: {current_difficulty}'
	else:
		current_difficulty = 'Easy'
		difficulty_button['text'] = f'Difficulty: {current_difficulty}'
	if vs_ai:
		restart_game()

#TKINTER SETUP
root = tk.Tk()
root.resizable(False, False)
root.title('Tic Tac Toe')

#FRAME
frame = tk.Frame(root, bg=BACKGROUND_COLOR)
frame.pack()

#WIDGETS
#Player's turn label
label = tk.Label(frame,text=current_player+'\'s turn', fg='white', bg=BUTTON_COLOR, font=('consolas', 20, 'bold'))

#Grid
for row in range(3):
	for column in range(3):
		board[row][column] = tk.Button(frame, font=GRID_FONT, width=4, height=2, bg=GRID_COLOR, bd=2, command=lambda row=row, column=column: place_mark(row, column))
		
		board[row][column].grid(row=row+1, column=column)

#Restart Button
restart_button = tk.Button(frame, text='Restart', font=BUTTON_FONT, bg=BUTTON_COLOR, fg='white', command=restart_game)

#Mode Button
mode_button = tk.Button(frame, text='Mode: Single Player', font=BUTTON_FONT, bg=BUTTON_COLOR, fg='white', command=toggle_mode)

#Difficulty Button
difficulty_button = tk.Button(frame, text=f'Difficulty: {current_difficulty}', font=BUTTON_FONT, bg=BUTTON_COLOR, fg='white', command=difficulty_mode)

#PLACING WIDGETS
label.grid(row=0, column=0, columnspan=3, sticky='ew')
restart_button.grid(row=4, column=0, columnspan=3, sticky='ew')
mode_button.grid(row=5, column=0, columnspan=3, sticky='ew')
difficulty_button.grid(row=6, column=0, columnspan=3, sticky='ew')

root.mainloop()

