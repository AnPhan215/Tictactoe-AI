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
    

game_opening()

# Run the game loop forever
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    CLOCK.tick(fps)