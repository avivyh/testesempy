# Game Ping-Pong

# importando bibliotecas
from tkinter import *
import random
import time

# variável recebendo o valor digitado pelo usuário
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))

# variável
length = 500/level

# instância do Objeto Tk
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# variável recebendo o resultado da função Canvas
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()
root.update()

# variável
count = 0

# variável
lost = False

# classe
class Bola:
    def __init__(self, canvas, Barra, color):

        # variáveis
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        # lista
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        # variáveis
        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # função
    def draw(self):

        # variáveis
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # condicional if
        if pos[1] <= 0:

            # variável
            self.y = 3

        # condicional if
        if pos[3] >= self.canvas_height:

            # variável
            self.y = -3

        # condicional if
        if pos[0] <= 0:

            # variável
            self.x = 3
            
        # condicional if
        if pos[2] >= self.canvas_width:

            # variável
            self.x = -3

        # variável
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # condicional if aninhado
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:

                # variáveis
                self.y = -3
                global count
                count +=1

                # chamada à função
                score()

        # condicional if 
        if pos[3] <= self.canvas_height:

            # variável
            self.canvas.after(10, self.draw)
        else:

            # chamada à função
            game_over()

            # variáveis
            global lost
            lost = True

# classe
class Barra:
    def __init__(self, canvas, color):

        # variáveis
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    # função
    def draw(self):

        # chamada ao método
        self.canvas.move(self.id, self.x, 0)

        # variável
        self.pos = self.canvas.coords(self.id)

        # condicional if 
        if self.pos[0] <= 0:

            # variável
            self.x = 0
        
        # condicional if 
        if self.pos[2] >= self.canvas_width:

            # variável
            self.x = 0
        
        global lost
        
        # condicional if 
        if lost == False:
            self.canvas.after(10, self.draw)

    # função
    def move_left(self, event):

        # condicional if 
        if self.pos[0] >= 0:

            # variável
            self.x = -3

    # função
    def move_right(self, event):

        # condicional if 
        if self.pos[2] <= self.canvas_width:

            # variável
            self.x = 3

# função
def start_game(event):

    # variáveis
    global lost, count
    lost = False
    count = 0

    # chamando a função
    score()

    # variável que recebe o resultado da função
    canvas.itemconfig(game, text=" ")

    # metodos dos objetos
    time.sleep(1)
    Barra.draw()
    Bola.draw()

# função
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

# função
def game_over():
    canvas.itemconfig(game, text="Game over!")

# instancias dos objetos Barra e Bola
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

# variáveis que recebem o resultado das funções
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))
canvas.bind_all("<Button-1>", start_game)

# executando o programa
root.mainloop()


