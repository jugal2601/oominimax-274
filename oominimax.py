# ---------------------------------
#  Course: CMPUT 274
#  Name: Jugal Sadhnani
#  ccid: sadhnani
#  Assignment: Weekly #06 oominimax
#  Aknowledgements: Most of this code has just been copy pasted using Paul lu's minimax
# ----------------------------------

from math import inf as infinity
from random import choice
from random import seed as randomseed       # Paul Lu
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)


Jugal Sadhnani
CCID:  sadhnani
"""

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

class state:
	def __init__(self):
		return

	def __repr__(self):
		return

	def __str__(self):
		return

	def game_over(self,current_state):
		self.current_state=current_state
		"""
	    This function test if the human or computer wins
	    :param state: the state of the current board
	    :return: True if the human or computer wins
	    """
		return self.wins(current_state, HUMAN) or self.wins(current_state, COMP)

	def wins(self,current_state,player):
		win_state = [
	        [current_state[0][0], current_state[0][1], current_state[0][2]],
	        [current_state[1][0], current_state[1][1], current_state[1][2]],
	        [current_state[2][0], current_state[2][1], current_state[2][2]],
	        [current_state[0][0], current_state[1][0], current_state[2][0]],
	        [current_state[0][1], current_state[1][1], current_state[2][1]],
	        [current_state[0][2], current_state[1][2], current_state[2][2]],
	        [current_state[0][0], current_state[1][1], current_state[2][2]],
	        [current_state[2][0], current_state[1][1], current_state[0][2]],
	    ]
		if [player, player, player] in win_state:
			return True
		else:
			return False

	def evaluate(self,current_state):
	    """
	    Function to heuristic evaluation of state.
	    :param state: the state of the current board
	    :return: +1 if the computer wins; -1 if the human wins; 0 draw
	    """
	    if self.wins(current_state, COMP):
	        score = +1
	    elif self.wins(current_state, HUMAN):
	        score = -1
	    else:
	        score = 0

	    return score


	def empty_cells(self,current_state):
	    """
	    Each empty cell will be added into cells' list
	    :param state: the state of the current board
	    :return: a list of empty cells
	    """
	    cells = []

	    for x, row in enumerate(current_state):
	        for y, cell in enumerate(row):
	            if cell == 0:
	                cells.append([x, y])

	    return cells

	def render(self,current_state,c_choice, h_choice):
	    """
	    Print the board on console
	    :param state: current state of the board
	    """

	    chars = {
	        -1: h_choice,
	        +1: c_choice,
	        0: ' '
	    }
	    str_line = '---------------'

	    print('\n' + str_line)
	    for row in current_state:
	        for cell in row:
	            symbol = chars[cell]
	            print(f'| {symbol} |', end='')
	        print('\n' + str_line)


class oominimax:

	def __init__(self):
		return
	def __str__(self):
		return
	def __repr__(self):
		return
	def minimax(self,current_state, depth, player):
	    """
	    AI function that choice the best move
	    :param state: current state of the board
	    :param depth: node index in the tree (0 <= depth <= 9),
	    but never nine in this case (see iaturn() function)
	    :param player: an human or a computer
	    :return: a list with [the best row, best col, best score]
	    """
	    if player == COMP:
	        best = [-1, -1, -infinity]
	    else:
	        best = [-1, -1, +infinity]

	    if depth == 0 or state().game_over(current_state):
	        score = state().evaluate(current_state)
	        return [-1, -1, score]

	    for cell in state().empty_cells(current_state):
	        x, y = cell[0], cell[1]
	        current_state[x][y] = player
	        score = self.minimax(current_state, depth - 1, -player)
	        current_state[x][y] = 0
	        score[0], score[1] = x, y

	        if player == COMP:
	            if score[2] > best[2]:
	                best = score  # max value
	        else:
	            if score[2] < best[2]:
	                best = score  # min value

	    return best





class Board:
	def __init__(self):
		return

	def __repr__(self):
		return

	def __str__(self):
		return


	def valid_move(self,x, y,current_state):
	    """
	    A move is valid if the chosen cell is empty
	    :param x: X coordinate
	    :param y: Y coordinate
	    :return: True if the board[x][y] is empty
	    """
	    if [x, y] in state().empty_cells(current_state):
	        return True
	    else:
	        return False


	def set_move(self,x, y, player,current_state):
	    """
	    Set the move on board, if the coordinates are valid
	    :param x: X coordinate
	    :param y: Y coordinate
	    :param player: the current player
	    """
	    if self.valid_move(x, y,current_state):
	        current_state[x][y] = player
	        return True
	    else:
	        return False


def clean():
    """
    Clears the console
    """
    # Paul Lu.  Do not clear screen to keep output human readable.
    print()
    return

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def ai_turn(c_choice, h_choice,current_state):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(state().empty_cells(current_state))
    if depth == 0 or state().game_over(current_state):
        return

    #clean()
    print(f'Computer turn [{c_choice}]')
    state().render(current_state, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = oominimax().minimax(current_state, depth, COMP)
        x, y = move[0], move[1]

    Board().set_move(x, y, COMP,current_state)
    # Paul Lu.  Go full speed.
    # time.sleep(1)


def human_turn(c_choice, h_choice,current_state):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(state().empty_cells(current_state))
    if depth == 0 or state().game_over(current_state):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    #clean()
    print(f'Human turn [{h_choice}]')
    state().render(current_state, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            clean()
            coord = moves[move]
            can_move = Board().set_move(coord[0], coord[1], HUMAN,current_state)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    # Paul Lu.  Set the seed to get deterministic behaviour for each run.
    #       Makes it easier for testing and tracing for understanding.
    randomseed(274 + 2020)
    State01=state()

    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
            clean()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
    #clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
            clean()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(State01.empty_cells(board)) > 0 and not State01.game_over(board):
        if first == 'Y':
            human_turn(c_choice, h_choice,board)
            first = '' 
        #clean()
        ai_turn(c_choice, h_choice,board)
        clean()
        human_turn(c_choice, h_choice,board)

    # Game over message
    if State01.wins(board,HUMAN):
        #clean()
        print(f'Human turn [{h_choice}]')
        State01.render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif State01.wins(board, COMP):
        #clean()
        print(f'Computer turn [{c_choice}]')
        State01.render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        #clean()
        State01.render(board, c_choice, h_choice)
        print('DRAW!')

    exit()



if __name__=='__main__':
	main()