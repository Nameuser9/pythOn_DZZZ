from tkinter import *
import emoji
import isOdd
import random
import time

def field():
    root = Tk()
    global Label
    global buttons
    Label = Label(width = 55, text='КРЕСТИКИ-НОЛИКИ(СО СМАЙЛИКАМИ)', font=('Times New Roman',20))
    buttons =[Button(width = 15,height = 4,font=('Times New Roman',28),bg='red',command=lambda x=i:button_push(x)) for i in range (9)]
    Label.grid(row = 0,column = 0,columnspan=3)
    row = 1; col = 0
    for i in range(9):
        buttons[i].grid(row=row,column=col)
        col += 1
        if col == 3:
            row += 1
            col = 0
    root.mainloop()

def button_push(x):#x это номер поля(от 0 до 8)
    global move
    global move_left
    global turn
    
    
    
    move[x] =(emoji.emojize(':thumbs_up:'))
    buttons[x].config(text=(emoji.emojize(':thumbs_up:')),bg='white',state='disabled')
    move_left.remove(x)
    print (x)
    
    if x == 4 and turn == 0:
        t = random.choice(move_left)
    elif x != 4 and turn == 0:
        t = 4
    if turn > 0:
        t = 8 - x 
        if (len(move_left)) == 0:
                print('игра окончена')
                if t not in move_left:
                    t +=1
    print(t) 
    print(turn)
    
    move[t]=(emoji.emojize(':thumbs_down:'))
    time.sleep(0.5)
    buttons[t].config(text=(emoji.emojize(':thumbs_down:')),bg='white',state='disabled')
    move_left.remove(t)
    print(move_left)
    turn +=1
    win_condition()
    

def win_condition(n):
    if (move[0] == n and move[1] == n and move[2] == n) or (move[3] == n and move[4] == n and move[5] == n) or (move[6] == n and move[7] == n and move[8] == n) or (move[0] == n and move[4] == n and move[8] == n) or (move[0] == n and move[3] == n and move[6] == n) or (move[1] == n and move[4] == n and move[7] == n) or (move[2] == n and move[5] == n and move[8] == n) or (move[2] == n and move[4] == n and move[6] == n):
        for i in move_left:
            buttons[i].config(emoji.emojizeconfig(text=(emoji.emojize(":red_heart:")),bg='white',state='disabled'))
        if n== (emoji.emojize(':thumbs_down:')):
            Label['text'] ='ты проиграл, мы играли на миллион денег'
        else:
            Label['text'] ='ты выиграл, загадай желание и посмотри под подушку'


turn = 0 
move = [None] * 9
move_left = list(range (9))      
field()
button_push()
