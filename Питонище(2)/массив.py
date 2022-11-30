n = int(input())
y =1
for x in range(n):
    result = (1+(1/y))**y
    y+=1
    print (result, end= ' ')
