# Tic Tac Toe Game (Using Python)

A simple console-based Tic Tac Toe game implemented in Python. Two players (X and O) take turns to place their mark on a 3x3 grid. The game ends when one player wins or the board is full (resulting in a draw).

# How to Play:
The board is represented by numbers 0–8 as shown below:

Welcome to Tic Tac Toe Game

<pre> ``` 0 | 1 | 2 --|---|--- 3 | 4 | 5 --|---|--- 6 | 7 | 8 ``` </pre>

Each player enters a number to mark that position with their symbol (X or O).
A move is invalid if the position is already occupied.

# The game continues until:
A player wins by placing 3 of their marks in a row (horizontal, vertical, or diagonal), or
All positions are filled (draw).

# Game Logic:
Board State: Maintained using two lists:
xState for X's moves
OState for O's moves

Win Conditions: Checked using all possible winning combinations:

wins = [[0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]]

# Running the Game:
1. Ensure you have Python 3 installed.
2. Save the code to a file, e.g., tic_tac_toe.py
3. Open a terminal or command prompt
4. Run the file:
python tic_tac_toe.py

# Features:
1. Turn-based 2-player gameplay
2. Input validation
3. Win and draw detection
4. Simple and readable code.
