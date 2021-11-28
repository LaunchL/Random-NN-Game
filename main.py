import numpy as np
import numpy.random as rand
import random
from tkinter import *
import sys
import os


#Neural Network
def sigmoid(x, der=False):
    if der:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


x = np.array([[1, 0, 1],
            [1, 0, 1],
            [0, 1, 0],
            [0, 1, 0]])

y = np.array([[0, 0, 1, 1]]).T

np.random.seed(1)

syn0 = 2 * np.random.random((3, 1)) - 1

l1 = []

for iter in range(10000):
    l0 = x
    l1 = sigmoid(np.dot(l0, syn0))

    l1_error = y - l1

    l1_delta = l1_error * sigmoid(l1, True)

    syn0 += np.dot(l0.T, l1_delta)

#Game
r1 = random.randint(0, 1)
r2 = random.randint(0, 1)
r3 = random.randint(0, 1)

z = np.array([[r1,r2,r3]])
l2 = z
l3 = sigmoid(np.dot(l2, syn0))
def txt():
    if(l3 >= 0.8):
        print("Неиронная сеть сделала выбор: ")
        print(l3)
        print("Извините, но вы проиграли!")
    else:
        print("Неиронная сеть сделала выбор: ")
        print(l3)
        print("Поздравляем вы, выйграли!")

#Interfaces
window = Tk()
window.title("NN Game Random")
window.geometry('400x250')

def quit():
    sys.exit()

def game():
    if(l3 >= 0.8):
        text.configure(text="Извините, но вы проиграли!") 
        restart1 = Button(window, text="Заново.", command=game)  
        restart1.grid(column=0, row=2)
        return
    else:
        text.configure(text="Поздравляем вы, выйграли!") 
        restart = Button(window, text="Заново", command=game)  
        restart.grid(column=0, row=2)
        return 

gamen = Label(window, text="Neural Network Game: Random!")  
gamen.grid(column=0, row=0) 

text = Label(window, text="Game")  
text.grid(column=0, row=1) 

play = Button(window, text="Играть!", command=game)  
play.grid(column=0, row=2)

quit = Button(window, text="Quit", command=quit)
quit.grid(column=0, row=3)

window.mainloop()