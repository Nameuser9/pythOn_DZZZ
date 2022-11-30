N = 4
a = N
N =((N*2)+1)
num =[0]*N
sum =[]
i = 0
print (a)
while i < N:
    num[i] =-a
    a =a- 1
    i +=1
print(num)
b = 3
print('vvedy')
sum = list(map(int, input().split(" ")))
print (sum)
summa = 0
counter = 0
while counter < len(sum):
    if counter < 1:
        summa = (num[sum[counter]])
    print(num[sum[counter]])
    summa *=(num[sum[counter]])
    counter+=1
print (summa)