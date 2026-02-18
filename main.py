import math
import tkinter as tk
from tkinter import ttk

class TicTacToe:
    def __init__(self,depth=9) #initialize the game and set the maximum depth
     self.max_depth = depth