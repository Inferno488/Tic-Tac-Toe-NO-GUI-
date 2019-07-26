# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:11:59 2019

@author: Prabhleen
"""

from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
    pass

def player_input():
    marker = ''
    while not ((marker == 'X') or (marker =='O')):
        marker = input("Player1: Select input")
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    

def place_marker(board, marker, position):
    board[position] = marker
    pass

def win_check(board, mark):
        
    return((board[7] == board[8]==board[9] == mark) or 
           (board[4] == board[5] == board[6] == mark) or
           (board[1] == board[2] == board[3] == mark) or
           (board[7] == board[4] == board[1] == mark) or
           (board[8] == board[5] == board[2] == mark) or
           (board[9] == board[6] == board[3] == mark) or
           (board[7]== board[5]== board[3] == mark) or
           (board[1] == board[5] == board[9] == mark))
    

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player1'
    else:
        return 'Player2'
    pass

def space_check(board, position):
    return board[position] == ' '
    pass

def full_board_check(board):
    for i in range(len(board)):
        if(space_check(board,i) == True):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+ "will go first")
    
    play_game = input("Are you ready to play Y/N")
    if play_game == 'Y':
        gameon = True
    else:
        gameon = False

    while gameon:
        if(turn == 'Player1'):
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            
            if(win_check(theBoard,player1_marker)):
                display_board(theBoard)
                print("Congratz u win")
                gameon = False
                break
            else:
                if(full_board_check(theBoard)):
                    display_board(theBoard)
                    print("Game is draw")
                    gameon = False
                    break
                else:
                    turn = 'Player2'
    
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            
            if(win_check(theBoard,player2_marker)):
                display_board(theBoard)
                print("Congratz u win")
                gameon = False
                break
            else:
                if(full_board_check(theBoard)):
                    display_board(theBoard)
                    print("Game is draw")
                    gameon = False
                    break
                else:
                    turn = 'Player1'
    if not replay():
        break
