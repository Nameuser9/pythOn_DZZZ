from random import randint
candy = 2021
firstBank , secondBank ,hands , = 0 ,0 ,0 
move = randint(0,1)
while candy > 0:
    if move % 2 == 0:
        print("ходит игрок")
        hands = int(input())# дописать что можно брать не более 28
        while hands > 28:
            hands = int(input()) #дописать что можно брать не более 28
            print('ты нарушаешь правила игры, напиши число конфет ещё раз')
        candy = candy - hands
        firstBank+= hands
        print(f' у игрока  конфет {firstBank}, осталось конфет {candy}')
        hands = 0
    else:
        print("ходит ИИ")
        hands = randint(1,28)
    # while hands > 28:
    #             hands = int(input()) #дописать что можно брать не более 28
    #             print('ты нарушаешь правила игры, напиши число конфет ещё раз')
        candy = candy - hands
        secondBank+= hands
        print(f' у Искуственного Инетекта  конфет {firstBank}, осталось конфет {candy}')
        hands = 0
    move+=1
if move % 2 == 0:
    print("И востали машины из пепла ядерной войны")
else:
    print('И снова человек победил машину')
