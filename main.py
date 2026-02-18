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

diagonal
        if board[0][2] == board[1][1] == board[2][0] == player: return True
anti-diagonal
        return False # No winner
