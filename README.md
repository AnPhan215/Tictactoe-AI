# Tictactoe-AI
 *This is my final project for CS50x*  

This is tic-tac-toe game that let human play with AI

UNDERSTANDING:

Tic-tac-toe, noughts and crosses, or Xs and Os is a paper-and-pencil game for two players who take turns marking the spaces in a three-by-three grid with X or O. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.[Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe)

In this program, I coded an AI to fight against players by using heuristic evaluation approaching method, minimax and alpha-beta pruning algorithm.

EXPLAINING:

For this game application, I have used ``` pygame``` library from python. Accredit to [TechVidvan](https://techvidvan.com/tutorials/python-game-project-tic-tac-toe/) that helps me understand more about ```pygame``` and [Rohit Agrawal](https://towardsdatascience.com/lets-beat-games-using-a-bunch-of-code-part-1-tic-tac-toe-1543e981fec1) to helps me understand more about minimax.

A first few step like:
- Initializing pygame window

- Load the images

- Resizing images

are the things we must do to get the desired visual.

In the ```game_opening()``` function, I displayed the intro picture for the game then draw the lines for the board and shows whose turn it is to play.

After that, the game will go into a while loop until it finds a winner or a draw result.

If it is the player's turn, the game will listen to the user's mouse event, it will go to ```userClick``` function if it get a ```MOUSEBUTTONDOWN``` event then will draw an 'X' if that slot is available.

If it is the AI's turn, the game will run the ```get_best_move``` function to to choose a best move to go then will draw an 'O' on the selected slot.

After each drawing, the program will check the game's status by ```check_win``` function. If it finds a winner or the game gets to a tie result, it will display the result the result by ```draw_status``` function and reset the game by ```reset_game``` function. Otherwise, it will continue the while loop.

The core thing in this program is within the ```get_best_move``` function which helps the AI decides the best move to go. This is where the heuristic approach, minimax and alpha-beta pruning algorithm are applied.

***get_best_move FUNCTION:***

The ```get_best_move``` function will take 5 variable: board (the layout of the board), player (X or O), turn (the number of turn left, there's 9 in the beginning), alpha, beta (for the alpha-beta pruning algorithm)

At the beginning of the function, it will always check the status of the board by:

```win, finish = AI_check_win(board)```

The ```win``` variable will be either None, "X" or "O" and the ```finish``` variable will be either "Done" or "Not Done"

The heuristic approach is shown as below:

> When the AI win, it will get a positive score corresponding to the number of turns remaining.

```
if finish == "Done" and win == 'o':
        return (turn, 0)
```

> And when the Player win, it will get a negative score corresponding to the number of turns remaining.
```
elif finish == "Done" and win == 'x':
        return (-turn, 0)
```

> When there is a draw, a score of 0 will be return
```
elif finish == "Draw":
        return (0, 0)
```

If ```win``` is None and ```finish``` is "Not Done" then an ```empty_cells``` is created to give the AI available option to decide, or generate the available branches in this concept. It also update the ```turn``` variable after everytime the ```empty_cells``` is made.
```
for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                empty_cells.append(i*3 + (j+1))
    turn = len(empty_cells)
```

**The minimax with alpha-beta pruning algorithm is shown as below:**

For each turn, the AI's turn and player's turn will call the ```get_best_move``` function recursively until a score is returned.

> For AI's turn, it will maximize its score and update alpha, then check if beta <= alpha, if it is, the program will prune that branch or *break the loop*, if it's not then it will return the best *max* score with the move

```
    # Max for AI
    if move['score'] > maxbest:
        maxbest = move['score']
        maxbest_move = move['index']
    
    # Max for alpha
    alpha = max(alpha, move['score'])
    
    # Prune branch if needed
    if beta <= alpha:
        break
return (maxbest, maxbest_move)
```

> For Player's turn, it will minimize AI's score and update beta, then check if beta <= alpha, if it is, the program will prune that branch or *break the loop*, if it's not then it will return the best *min* score with the move

```
    # Create new branch for human's turn
    score,_ = get_best_move(new_board, 'o', turn, alpha, beta)
    move['score'] = scor
    # Min for Human
    if move['score'] < minbest:
        minbest = move['score']
        minbest_move = move['index'
    # Min for beta
    beta = min(beta, move['score'])
    
    # Prune branch if needed
    if beta <= alpha:
        break
return (minbest, minbest_move)
```
