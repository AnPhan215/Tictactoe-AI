from math import inf as infinity
import pygame as pg, sys
from pygame.locals import *
import time

# Global variables
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)

# Tictactoe 3x3 board
TTT = [[None]*3, [None]*3, [None]*3]

# Initializing pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# Load the images
opening = pg.image.load('tic tac opening.png')
x_image = pg.image.load('X.png')
o_img = pg.image.load('o.png')

# Resizing images
x_image = pg.transform.scale(x_image, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))

def game_opening():
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    # Drawing vertical lines
    pg.draw.line(screen, line_color, (width/3, 0), (width/3, height), 5)
    pg.draw.line(screen, line_color, (width*2/3, 0), (width*2/3, height), 5)

    # Drawing horizontal lines
    pg.draw.line(screen, line_color, (0,height/3), (width, height/3), 5)
    pg.draw.line(screen, line_color, (0, height*2/3), (width, height*2/3), 5)
    # pg.draw.rect(screen, line_color, (10, 50, 100, 80))
    draw_status()

def copy_game_board(TTT):
    new_board = [[None]*3, [None]*3, [None]*3]
    for i in range(3):
        for j in range(3):
            new_board[i][j] = TTT[i][j]
    return new_board

def draw_status():
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " Won!"
    if draw:
        message = 'Game Draw!'

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # Copy the render message to the board

    screen.fill ((0,0,0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win(AI, board):
    if not AI:
        global TTT, winner, draw

    # Check for winning rows
    for row in range (0,3):
        if not AI:
            if (((TTT[row][0] == TTT[row][1] == TTT[row][2])) and (TTT[row][0] is not None)):
                # This row won
                winner = TTT[row][0]
                pg.draw.line(screen, (250,0,0), (0,(row+1)*height/3 - height/6),\
                    (width, (row+1)*height/3 - height/6), 3)
                break
        else:
            if (((board[row][0] == board[row][1] == board[row][2])) and (board[row][0] is not None)):
                # This row won
                winner = board[row][0]
                pg.draw.line(screen, (250,0,0), (0,(row+1)*height/3 - height/6),\
                    (width, (row+1)*height/3 - height/6), 3)
                return winner, "Done"

    # Check for winning columns
    for column in range(0,3):
        if not AI:
            if (((TTT[0][column] == TTT[1][column] == TTT[2][column])) and (TTT[0][column] is not None)):
                # This column won
                winner = TTT[0][column]
                pg.draw.line(screen, (250,0,0), ((column+1)*width/3 - width/6, 0),\
                     ((column+1)*width/3 - width/6, height), 3)
                break
        else:
            if (((board[0][column] == board[1][column] == board[2][column])) and (board[0][column] is not None)):
                # This column won
                winner = board[0][column]
                pg.draw.line(screen, (250,0,0), ((column+1)*width/3 - width/6, 0),\
                     ((column+1)*width/3 - width/6, height), 3)
                return winner, "Done"

        
    
    # Check for diagnoal winners
        
    # Diagonal from the left to right
    if not AI:
        if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
            winner = TTT[0][0]
            pg.draw.line(screen, (250,0,0),(50, 50), (350, 350), 3)
    else:
        if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
            winner = board[0][0]
            pg.draw.line(screen, (250,0,0),(50, 50), (350, 350), 3)
            return winner, "Done"
    
    # Diagonal from the right to left
    if not AI:
        if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
            winner = TTT[0][2]
            pg.draw.line(screen, (250,0,0), (350, 50), (50, 350), 3)
    else:
        if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
            winner = board[0][2]
            pg.draw.line(screen, (250,0,0), (350, 50), (50, 350), 3)
            return winner, "Done"
        
    # Check for draw
    if not AI:
        if (all([all(row) for row in TTT]) and winner is None):
            draw = True
    else:
        if (all([all(row) for row in board]) and winner is None):
            draw = True
            return None, "Draw"
    
    draw_status()
    

def drawXO(row, col):
    global TTT, XO
    
    # Get x position 
    if row == 1:
        posx = 30
    if row == 2:
        posx = width/3 + 30
    if row == 3:
        posx = width*2/3 +30
    
    # Get y position
    if col == 1:
        posy = 30
    if col == 2:
        posy = height/3 + 30
    if col == 3:
        posy = height*2/3 +30
    
    TTT[row-1][col-1] = XO
    # Switch turn
    if(XO == 'x'):
        screen.blit(x_image, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'
    pg.display.update()

def userClick():
    
    # Get cordinates of mouse click
    x,y = pg.mouse.get_pos()

    # Get clicked column (1-3)
    if (x < width/3):
        col = 1
    elif (x < width*2/3):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None

    # Get clicked row
    if ( y < height/3):
        row = 1
    elif (y < height*2/3):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None
    
    if(row and col and TTT[row-1][col-1] is None):
        drawXO(row, col)
        check_win(False, TTT)

def get_best_move(board, player):
    ''' Minimax Algorithm '''

    winner, finish = check_win(True,board)
    
    # Check match status
    # If AI won
    if finish == "Done" and winner == 'o':
        # Score 1 if AI won
        return 1
    # If Human won
    elif finish == "Done" and winner == 'x':
        # Score -1 if Human won
        return -1
    # If Draw
    elif finish == "Draw":
        # Draw 0 if Draw
        return 0

    moves = []
    empty_cells = []

    # If match continues, create array of empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                empty_cells.append(i*3 + (j+1))

    # Create recursive for loop untill no more empty cell
    for empty_cell in empty_cells:
        move = {}

        # AI choose the each empty cells 
        move['index'] = empty_cell

        # Generate new board with the new selection
        new_board = copy_game_board(board)
        new_board[int((empty_cell-1)/3)][(empty_cell-1)%3] = player

        # If AI turn
        if player == 'o':
            # Create new branch for human's turn
            score,_ = get_best_move(new_board, 'x')
            move['score'] = score
        else:
            # Create new branch for AI's turn
            score,_ = get_best_move(new_board, 'o')
            move['score'] = score
        
        # Add the cell and score to moves[]
        moves.append(move)
    
    # Find best move
    bestMove = None

    # Max for AI
    if player == 'o':
        best = -infinity

        # Select the max score for parent branch
        for move in moves:
            if move['score'] > best:
                best = move['score']
                bestMove = move['index']
    
    # Min for Human
    else:
        best = infinity

        # Select the min score for parent branch
        for move in moves:
            if move['score'] < best:
                best = move['score']
                bestMove = move['index']

    return (best, bestMove)
    


def reset_game():
    global TTT, winner, XO, draw
    time.sleep(1)
    XO = 'x'
    winner = None
    draw = False
    TTT = [[None]*3,[None]*3,[None]*3]
    game_opening()


game_opening()

# Run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type ==  MOUSEBUTTONDOWN:
            # Draw X,O if you user clicked
            userClick()
            if(winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)