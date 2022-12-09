from math import pi  
d =float(input('Введите точность определения числа'))
a = 1 /d 
b = (a **(1/10))+1
bb = round (b)
print (bb)
print(round( pi , bb))