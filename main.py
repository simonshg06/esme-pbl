import math
import tkinter as tk
from tkinter import ttk

class TicTacToe:
    def __init__(self,depth=9): #initialize the game and set the maximum depth
        self.max_depth = depth

    def check_winner(self, board, player):
        for i in range(3):
            if all([board[i][j] == player for j in range(3)]): return True # Check rows
            if all([board[j][i] == player for j in range(3)]): return True #Check clumns
        if board[0][0] == board[1][1] == board[2][2] == player: return True #Check the main diagonal
        if board[0][2] == board[1][1] == board[2][0] == player: return True
        return False # No winner

    def is_full(self, board):
        return all(board[r][c] != ' ' for r in range(3) for c in range(3))


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
        for line in lines: # Evaluate each line for potential winning or loosing conditions
             if ai_piece in line and opponent in line: continue 
             if line.count(ai_piece) == 2: score += 30  
             elif line.count(ai_piece) == 1: score += 10 
             if line.count(opponent) == 2: score -= 30
             elif line.count(opponent) == 1: score -= 10
        return score # Return the calculated score
    def minimax(self, board, depth, is_maximizing, ai_piece, collect_scores=None):
        opponent = 'X' if ai_piece == 'O' else 'O'
        if self.check_winner(board, ai_piece): return 1000
        if self.check_winner(board, opponent): return -1000
        if self.is_full(board) or depth == 0:
            score = self.evaluate(board, ai_piece)
            if collect_scores is not None:
                collect_scores.append(score)
            return score
        if is_maximizing:
            best = -math.inf
            for r in range(3):
                for c in range(3):
                    if board[r][c] == ' ':
                        board[r][c] = ai_piece
                        val = self.minimax(board, depth - 1, False, ai_piece,collect_scores)
                        board[r][c] = ' '
                        best = max(best,val)
            return best
        else:
            best = math.inf
            for r in range(3):
                for c in range(3):
                    if board[r][c] == ' ':
                        board[r][c] = opponent
                        val = self.minimax(board, depth - 1, True, ai_piece, collect_scores)
                        board[r][c] = ' '
                        best = min(best,val)
            return best
    def get_best_move(self, board, ai_piece):
        best_val = -math.inf
        best_move = None
        opponent = 'X' if ai_piece == 'O' else 'O'

        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = ai_piece
                    val = self.minimax(board, self.max_depth_max - 1, False, ai_piece)
                    board[r][c] = ' '
                    if val > best_val:
                        best_val = val
                        best_move = (r, c)
        return best_move
    def get_all_scores(self, board, ai_piece):
        scores = []
        self.minimax(board, self.max_depth, True, ai_piece, collect_scores=scores)
        return scores
    def get_ideal_path(self, board, ai_piece, maximizing):
        opponent = 'X' if ai_piece == 'O' else 'O'
        current_piece = ai_piece if maximizing else opponent

        if self.check_winner(board, ai_piece) or self.check_winner(board, opponent) or self.is_full(board):
            return []
        best_val = -math.inf if maximizing else math.inf
        best_move = None

        for r in range(3):
            for c in range(3):
                if board[r][c] == ' ':
                    board[r][c] = current_piece
                    val = self.minimax(board, self.max_depth - 1, not maximizing, ai_piece)
                    board[r][c] = ' '
                    if (maximizing and val > best_val) or (not maximizing and val < best_val):
                        best_val = val
                        best_move = (r, c)
        if best_move is None:
            return []
        
        r,c = best_move
        board[r][c] = current_piece
        rest = self.get_ideal_path(board, ai_piece, not maximizing)
        board[r][c] = ' '
        return [best_move] + rest
    
class TicTacToeApp:
    def __init__(self, root):
       self.root = root
       self.root.title("Tic-Tac-Toe")
       self.root.geometry("600x750")
       self.root.resizable(False, False)
       self.engine = TicTacToe()
       self.board = [[' '] * 3 for _ in range(3)]
       self.buttons = [[None] * 3 for _ in range(3)]
       self.current_player = 'X'  # X always starts
       self.game_over = False
       self.game_mode = tk.StringVar(value="pvc")
       self._build_ui()
       self.reset_game()
    
    def _build_ui(self):
       tk.Label(self.root, text="Tic-Tac-Toe", font=("Arial", 20, "bold")).pack(pady=10)
       mode_frame = tk.LabelFrame(self.root, text="Game Mode", padx=10, pady=5)
       mode_frame.pack(fill="x", padx=20, pady=5)
       for text, val in [("Player vs Computer", "pvc"), ("Player vs Player", "pvp"), ("Computer vs Computer", "cvc")]:
           tk.Radiobutton(mode_frame, text=text, variable=self.game_mode, value=val).pack(side="left", padx=10)

       diff_frame = tk.LabelFrame(self.root, text="Difficulty (AI depth)", padx=10, pady=5)
       diff_frame.pack(fill="x", padx=20, pady=5)
       self.depth_var = tk.IntVar(value=9)
       for text, val in [("Easy (1)", 1), ("Medium (3)", 3), ("Hard (9)", 9)]:
           tk.Radiobutton(diff_frame, text=text, variable=self.depth_var, value=val, command=self._update_depth).pack(side="left", padx=10)

       board_frame = tk.Frame(self.root, bg="#333")
       board_frame.pack(pady=10)
       for r in range(3):
           for c in range(3):
            btn = tk.Button(board_frame, text="", font=("Arial", 28, "bold"), width=4, height=2,bg="white", command=lambda row=r, col=c: self._on_click(row, col))
            btn.grid(row=r, column=c, padx=3, pady=3)
            self.buttons[r][c] = btn