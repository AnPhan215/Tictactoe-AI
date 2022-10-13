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

def check_win():
    global TTT, winner, draw

    # Check for winning rows
    for row in range (0,3):
        if (((TTT[row][0] == TTT[row][1] == TTT[row][2])) and (TTT[row][0] is not None)):
            # This row won
            winner = TTT[row][0]
            pg.draw.line(screen, (250,0,0), (0,(row+1)*height/3 - height/6),\
                (width, (row+1)*height/3 - height/6), 3)
            break

    # Check for winning columns
    for column in range(0,3):
        if (((TTT[0][column] == TTT[1][column] == TTT[2][column])) and (TTT[0][column] is not None)):
            # This column won
            winner = TTT[0][column]
            pg.draw.line(screen, (250,0,0), ((column+1)*width/3 - width/6, 0),\
                 ((column+1)*width/3 - width/6, height), 3)
            break
    
    # Check for diagnoal winners
        
        # Diagonal from the left to right
        if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
            winner = TTT[0][0]
            pg.draw.line(screen, (250,0,0),(50, 50), (350, 350), 3)
        
        # Diagonal from the right to left
        if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
            winner = TTT[0][2]
            pg.draw.line(screen, (250,0,0), (350, 50), (50, 350), 3)
        
    # Check for draw
        if (all([all(row) for row in TTT]) and winner is None):
            draw = True
    
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

    
    

game_opening()

# Run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    CLOCK.tick(fps)