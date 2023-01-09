from tkinter import *


root = Tk()
Label = Label(width = 30, text='КРЕСТИКИ-НОЛИКИ(СО СМАЙЛИКАМИ)', font=('Times New Roman',20))
buttons =[Button(width = 10,height = 4,font=('Times New Roman',28),bg='red') for i in range (9)]
Label.grid(row = 0,column = 0,columnspan=3)
row = 1; col = 0
for i in range(9):
    buttons[1].grid(row=row,column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0
root.mainloop()