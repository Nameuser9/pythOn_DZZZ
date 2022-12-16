list = [ [0, 0, 0] ,
         [0, 0, 0] ,
         [0, 0, 0] ]
#print(list)    
def printtt(list) :
    for num in list:
        print (num)
printtt(list)
i = 0
while ( i < 9):
    if (i % 2 == 0):
        #firsthod:
        print("Ходит первый игрок")
        print("укажите координату хода")
        a , b = (map(int, input().split(" ")))
        while ((list[a-1][b-1] == "V" or list[a-1][b-1] == "Z")):
            print("клетка уже занята, выбери ещё раз")
            #goto firsthod;
            a , b = (map(int, input().split(" ")))
        list[a-1][b-1] = "Z"
        printtt(list)
    else:
    #   secondhod: 
        print("Ходит второй игрок")
        print("укажите координату хода")
        x , y = (map(int, input().split(" ")))
        if ((list[x-1][y-1] == "Z" or list[x-1][y-1] == "V")):
            print("клетка уже занята, выбери ещё раз")
            # goto secondhod;}
            x , y = (map(int, input().split(" ")))
        list[x-1][y-1] = "V"
        printtt(list)
    i+=1
    if (i > 4):
        if  (list[0][0] == list[1][1] or list[1][1] == list[2][2]):
            if (list[1][1]=="Z"):
                    print("победил первый игрок")
                    break
            else:
                    print("победил второй игрок")
                    break
        if (list[0][0]==list[1][0] or list[1][0] ==list[2][0]):
            if (list[1][0]=="Z"):
                print("победил первый игрок")
                break
            else:
                print("победил второй игрок")
                break 
        if (list[0][0]==list[0][1] or list[0][2] ==list[0][2]):
            if (list[0][1]=="Z"):
                print("победил первый игрок")
                break
            else:
                print("победил второй игрок")
                break
        if (list[0][1]==list[1][1] or list[1][1]==list[2][1]):
            if (list[1][1]=="Z"):
                print("победил первый игрок")
                break
            else:
                print("победил второй игрок")
                break
        if (list[2][0]==list[2][1] or list[2][1]==list[2][2]):
            if (list[2][1]=="Z"):
                print("победил первый игрок")
                break
            else:
                print("победил второй игрок")
                break
        if (list[0][2]==list[1][2] or list[1][2]==list[2][2]):
            if (list[1][2]=="Z"):
                print("победил первый игрок")
                break
            else:
                print("победил второй игрок")
                break
        if (list[0][0]==list[1][1] or list[1][1]==list[1][2]):
            if (list[1][1]=="Z"):
                print("победил первый игрок")
                break
            else:
                print("победил второй игрок")
                break
        if (list[0][2]==list[1][1] or list[1][1]==list[2][0]):
            if (list[1][1]=="Z"):
                print("победил первый игрок")
                break
            else:
                print("победил второй игрок")
                break