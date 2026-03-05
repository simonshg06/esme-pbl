# **📦 \[Project Name]**

**MVP Status:** \[e.g., v1.0-Production]

**Group Members:** Yousef Abouturkia, Charlie Delecour, Simon Berger, Camy Merdji


## **🎯 Project Overview**

Our Tic-Tac-Toe application provides a flexible environment for experimenting with the Minimax algorithm through multiple game modes: human vs human, human vs AI, and AI vs AI. Users can adjust AI difficulty by modifying search depth. We built this tool to bridge the gap between theoretical algorithm instruction and practical implementation, allowing users to observe how decision trees, evaluation functions, and search depth directly influence an AI's strategic choices in real time.

## **🚀 Quick Start (Architect Level: < 60s Setup)**

Instructions on how to get this project running on a fresh machine.

1. **Clone the repo:**\
   git clone \[your-repo-link]\
   cd \[project-folder]

2. **Setup Virtual Environment:**\
   python -m venv .venv\
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install Dependencies:**\
   pip install -r requirements.txt

4. **Run Application:**\
   python main.py


## **🛠️ Technical Architecture**

Explain how your code is organized. An "Architect-level" README should describe the separation of concerns.

- **main.py**: Entry point of the application.

- **logic/**: Contains core algorithms and data processing.

- **ui/**: Handles user interactions (CLI/GUI).

- **utils/**: Helper functions and shared constants.




The project is in a single file split across two classes:


TicTacToe, pure game engine, no UI code:

   check_winner() : checks rows, columns, and diagonals for a winner
   is_full() : detects a draw
   evaluate() : scores a board position for the AI
   minimax() : recursive best-move search
   get_best_move() : returns the optimal move for standard mode
   get_best_move_infinite() : returns the optimal move for infinite mode
   get_all_scores() : collects all leaf node scores for display
   get_ideal_path() : reconstructs the optimal move sequence



TicTacToeGame, GUI and game controller:

   _build_ui() : constructs all tkinter widgets (board, buttons, labels, info box)
   _on_click() : handles human player input
   _place_piece() : updates board state, enforces infinite mode rules, checks end conditions
   _ai_turn() : triggers AI move in PvC and infinite PvC modes
   _cvc_turn() : runs the automated CvC loop with timed delays
   _show_scores() / _show_path() : display engine data in the info box
   reset_game() : resets board, move history, and restarts CvC if needed

__main__  entry point: launches the tkinter window.




## **🧪 Testing & Validation**

How can a user verify the code works?

1- Launch the code and confirm the window opens correctly
2- Try out each game mode (PvP, PvC, CvC, Infinite PvP, Infinite PvC)
3- Switch between Easy, Medium, and Hard difficulty levels
4- Play a few rounds and test the Reset Scores button
5- Click AI Ideal Path and Opponent Ideal Path mid-game to confirm move sequences appear in the info box


## **📦 Dependencies**

List the main third-party libraries used and _why_ they were chosen:

tkinter: desktop GUI (buttons, labels, layout)
math: provides math.inf for minimax value initialization
copy: deepcopy() for safely cloning board state without mutating the live game


## **🔮 Future Roadmap (v2.0)**

What features would you add if you had more time or a larger budget?

Undo button: let players step back one move, useful for learning and exploring alternate outcomes

Animated piece removal: add a brief flash or fade when the oldest piece vanishes in Infinite mode, making the mechanic clearer for new players

Save/load game state , especially for the score