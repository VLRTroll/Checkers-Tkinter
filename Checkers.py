from tkinter import *


# Constants
BOARD_SIZE = 400
ROWS_FILLED = 3

DRAUGHTS_IN_ROW = 8
DRAUGHT_SIZE = BOARD_SIZE/DRAUGHTS_IN_ROW

PIECE_SIZE = int(0.8 * DRAUGHT_SIZE)
BORDER_SIZE = 5

DARK_DRAUGHT_COLOR = "black"
LIGHT_DRAUGHT_COLOR = "white"

DARK_PIECE_COLOR = "red"
LIGHT_PIECE_COLOR = "#cfaf50"


# Settings
game = Tk()
game.title("Checkers")
game.geometry(f'{BOARD_SIZE}x{BOARD_SIZE}+100+100')
game.resizable(0,0)

board = Frame(game)
board.pack()

draughts = Canvas(board, width = BOARD_SIZE, height = BOARD_SIZE)
draughts.pack(fill = 'both')


# Draw an 8×8 draughts board
DRAUGHT_COLOR = DARK_DRAUGHT_COLOR

for row in range(DRAUGHTS_IN_ROW + 1):
    for column in range(DRAUGHTS_IN_ROW + 1):
        DRAUGHT_COLOR = LIGHT_DRAUGHT_COLOR if DRAUGHT_COLOR == DARK_DRAUGHT_COLOR else DARK_DRAUGHT_COLOR
        
        draught = draughts.create_rectangle(row*DRAUGHT_SIZE,column*DRAUGHT_SIZE,\
                                            (row*DRAUGHT_SIZE)+DRAUGHT_SIZE,(column*DRAUGHT_SIZE)+DRAUGHT_SIZE,\
                                            fill = DRAUGHT_COLOR, outline = DRAUGHT_COLOR)


# Draw the pieces
'''
Piece coordinates on the canvas
O----------------------------------O
| CANVAS                           |
|                                  |
|   (x1,y1) x-----------O          |
|           |           |          |
|           |           |          |
|           |   PIECE   |          |
|           |           |          |
|           |           |          |
|           O-----------x (x0,y0)  |
|                                  |
O----------------------------------O
'''

draw_piece = lambda x0,y0,x1,y1,color:\
             draughts.create_oval(x0, y0, x1, y1, fill = color)

draw_dark_piece = lambda x0,y0,x1,y1:\
                  draw_piece(x0, y0, x1, y1, DARK_PIECE_COLOR)

dark_coords = lambda row,index,border: (
    (2*index + row%2)*DRAUGHT_SIZE + PIECE_SIZE - border*BORDER_SIZE,
                  row*DRAUGHT_SIZE + PIECE_SIZE - border*BORDER_SIZE,
    (2*i + 1 + row%2)*DRAUGHT_SIZE - PIECE_SIZE + border*BORDER_SIZE,
            (row + 1)*DRAUGHT_SIZE - PIECE_SIZE + border*BORDER_SIZE,
)

draw_light_piece = lambda x0,y0,x1,y1:\
                   draw_piece(x0, y0, x1, y1, LIGHT_PIECE_COLOR)

light_coords = lambda row,index,border: (
(2*index + 1 - row%2)*DRAUGHT_SIZE + PIECE_SIZE - border*BORDER_SIZE,
 BOARD_SIZE - (row+1)*DRAUGHT_SIZE + PIECE_SIZE - border*BORDER_SIZE,
    (2*i + 2 - row%2)*DRAUGHT_SIZE - PIECE_SIZE + border*BORDER_SIZE,
     BOARD_SIZE - row*DRAUGHT_SIZE - PIECE_SIZE + border*BORDER_SIZE,
)

for i in range(int(DRAUGHTS_IN_ROW/2)):
    for row in  range(ROWS_FILLED):
        ## --- Draw the dark pieces --- ##
        dark_piece = draw_dark_piece(*dark_coords(row,i,0))
        dark_border = draw_dark_piece(*dark_coords(row,i,1))

        ## --- Draw the light pieces --- ##
        light_piece = draw_light_piece(*light_coords(row,i,0))
        light_border = draw_light_piece(*light_coords(row,i,1))


# Open the window
game.mainloop()
