from tkinter import *

# Constants
BOARD_SIZE = 400
DRAUGHTS_COUNT = 8
DRAUGHT_SIZE = BOARD_SIZE/DRAUGHTS_COUNT

# Settings
game = Tk()
game.title("Checkers")
game.geometry('400x400+100+100')
game.resizable(0,0)

board = Frame(game)
board.pack()

draughts = Canvas(board, width = BOARD_SIZE, height = BOARD_SIZE)
draughts.pack(fill = 'both')

# Draw an 8×8 draughts board

DRAUGHT_COLOR = 'black'

for row in range(DRAUGHTS_COUNT + 1):
    for column in range(DRAUGHTS_COUNT + 1):
        DRAUGHT_COLOR = 'white' if DRAUGHT_COLOR == 'black' else 'black'
        
        draught = draughts.create_rectangle(row*DRAUGHT_SIZE,column*DRAUGHT_SIZE,\
                                            (row*DRAUGHT_SIZE)+DRAUGHT_SIZE,(column*DRAUGHT_SIZE)+DRAUGHT_SIZE,\
                                            fill = DRAUGHT_COLOR, outline = DRAUGHT_COLOR)

# Impressão das Peças Vermelhas
for i in range(0,4):
    #Dimensão da imagem e distância entre a borda da imagem e o inicio da mesma
    row1 = draughts.create_oval(40+100*i,40,10+100*i,10,fill="red")
    borda1 = draughts.create_oval(35+100*i,35,15+100*i,15)
    row2 = draughts.create_oval(90+100*i,90,60+100*i,60,outline=None,fill="red")
    borda1 = draughts.create_oval(85+100*i,85,65+100*i,65)
    row3 = draughts.create_oval(40+100*i,140,10+100*i,110,outline=None,fill="red")
    borda1 = draughts.create_oval(35+100*i,135,15+100*i,115)

# Impressão das Peças Marrons
for i in range(0,4):
    #Dimensão da imagem e distância entre a borda da imagem e o inicio da mesma
    row1 = draughts.create_oval(90+100*i,390,60+100*i,360,fill="#cfaf50")
    borda1 = draughts.create_oval(85+100*i,385,65+100*i,365)
    row2 = draughts.create_oval(40+100*i,340,10+100*i,310,fill="#cfaf50")
    borda2 = draughts.create_oval(35+100*i,335,15+100*i,315)
    row3 = draughts.create_oval(90+100*i,290,60+100*i,260,fill="#cfaf50")
    borda3 = draughts.create_oval(85+100*i,285,65+100*i,265)

game.mainloop()
