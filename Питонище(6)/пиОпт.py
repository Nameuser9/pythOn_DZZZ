from math import pi  
d =float(input('Введите точность определения числа'))
a = 1 /d 
b = lambda a:(a **(1/10))+1
b(1/d)
bb = round (b)
print (bb)
print(round( pi , bb))