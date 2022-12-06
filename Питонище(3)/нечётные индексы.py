#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах
arr = list(map(int, input().split(" ")))
A = 0
sum = 0
while A < len(arr):
    if not A % 2 == 0:
        sum += arr[A]
    A += 1
print (sum)