from tkinter import *

# Constants
BOARD_SIZE = 400
ROWS_FILLED = 3

DRAUGHTS_IN_ROW = 8
DRAUGHT_SIZE = BOARD_SIZE/DRAUGHTS_IN_ROW
PIECE_SIZE = int(0.8 * DRAUGHT_SIZE)

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

draw_light_piece = lambda x0,y0,x1,y1:\
                   draw_piece(x0, y0, x1, y1, LIGHT_PIECE_COLOR)


for i in range(ROWS_FILLED + 1):
    ## --- Draw the dark pieces --- ##
    row1 = draw_dark_piece(40+100*i,40,10+100*i,10)
    borda1 = draw_dark_piece(35+100*i,35,15+100*i,15)
    
    row2 = draw_dark_piece(90+100*i,90,60+100*i,60)
    borda1 = draw_dark_piece(85+100*i,85,65+100*i,65)
    
    row3 = draw_dark_piece(40+100*i,140,10+100*i,110)
    borda1 = draw_dark_piece(35+100*i,135,15+100*i,115)

    ## --- Draw the light pieces --- ##
    row1 = draw_light_piece(90+100*i,390,60+100*i,360)
    borda1 = draw_light_piece(85+100*i,385,65+100*i,365)
    
    row2 = draw_light_piece(40+100*i,340,10+100*i,310)
    borda2 = draw_light_piece(35+100*i,335,15+100*i,315)
    
    row3 = draw_light_piece(90+100*i,290,60+100*i,260)
    borda3 = draw_light_piece(85+100*i,285,65+100*i,265)

game.mainloop()
