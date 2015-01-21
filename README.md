# Othello
Python code for Othello, using minimax with alpha-beta pruning, and developing a reasonable evaluation function.  
1. Board state. This is a nested list which represents the state of the board. Initially the Board state is as follows:
[
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', 'W', 'B', '.', '.', '.'],
['.', '.', '.', 'B', 'W', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.']
]
2. Color: is either the string "B" or the string "W", representing the color to play.
3. Remaining time: Remaining time in seconds.

How to run the code.
gamePlay.py: Plays two agents against each other. From the command line, this function is invoked with:
% python gameplay.py [-t<timelimit>] [-v] player1 player2
