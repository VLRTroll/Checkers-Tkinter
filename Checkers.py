from tkinter import *

jogo = Tk()
jogo.title("Damas")
jogo.geometry('400x400+100+100')

tabuleiro = Frame(jogo)
tabuleiro.pack()

casas = Canvas(tabuleiro, width = 400, height = 400)
casas.pack(fill = 'both')

#Desenho das casas do tabuleiro
for linha in range(0,8):
    for coluna in range(0,8):
        if (linha + coluna)%2 == 0:
            casa = casas.create_rectangle(linha*50,coluna*50,\
                                          (linha*50)+50,(coluna*50)+50,\
                                          fill = "white", outline = 'white')
        else:
            casa = casas.create_rectangle(linha*50,coluna*50,\
                                          (linha*50)+50,(coluna*50)+50,\
                                          fill = "black", outline = 'black')

#Impressão das Peças Vermelhas
for i in range(0,4):
    #Dimensão da imagem e distância entre a borda da imagem e o inicio da mesma
    linha1 = casas.create_oval(40+100*i,40,10+100*i,10,fill="red")
    borda1 = casas.create_oval(35+100*i,35,15+100*i,15)
    linha2 = casas.create_oval(90+100*i,90,60+100*i,60,outline=None,fill="red")
    borda1 = casas.create_oval(85+100*i,85,65+100*i,65)
    linha3 = casas.create_oval(40+100*i,140,10+100*i,110,outline=None,fill="red")
    borda1 = casas.create_oval(35+100*i,135,15+100*i,115)

#Impressão das Peças Marrons
for i in range(0,4):
    #Dimensão da imagem e distância entre a borda da imagem e o inicio da mesma
    linha1 = casas.create_oval(90+100*i,390,60+100*i,360,fill="#cfaf50")
    borda1 = casas.create_oval(85+100*i,385,65+100*i,365)
    linha2 = casas.create_oval(40+100*i,340,10+100*i,310,fill="#cfaf50")
    borda2 = casas.create_oval(35+100*i,335,15+100*i,315)
    linha3 = casas.create_oval(90+100*i,290,60+100*i,260,fill="#cfaf50")
    borda3 = casas.create_oval(85+100*i,285,65+100*i,265)

jogo.mainloop()
