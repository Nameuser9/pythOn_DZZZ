arr = list(map(int, input().split(" ")))
numb = []
[numb.append(i) for i in arr if i not in numb]
print (numb)
