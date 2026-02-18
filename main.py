import math
import tkinter as tk
from tkinter import ttk

class TicTacToe:
    def __init__(self,depth=9) #initialize the game and set the maximum depth
     self.max_depth = depth

    def check_winner(self, board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]): return True # Check rows
        if all([board[j][i] == player for j in range(3)]): return True #Check clumns
        if board[0][0] == board[1][1] == board[2][2] == player: return True #Check the main diagonal

        if board[0][2] == board[1][1] == board[2][0] == player: return True
        return False # No winner
def evaluate(self, board, ai_piece):
    opponent = 'X' if ai_piece == 'O' else 'O'
     if self.check_winner(board, ai_piece): return 1000 # AI wins
    if self.check_winner(board, opponent): return -1000 #Opponent wins
    score = 0   
        lines = []  # Create a list to hold all possible lines (rows, cols, diags)
        for i in range(3):  
            lines.append(board[i])  # Add rows to the list
            lines.append([board[j][i] for j in range(3)])  # Add columns to the list
        lines.append([board[i][i] for i in range(3)])  #Add
        lines.append([board[i][2-i] for i in range(3)])  #Add
