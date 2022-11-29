print ('введите координаты искомой точки(Х,Y)')
a = float(input())
b = float(input())
print ('введите координаты второй вискомой точки(Х,Y)')
c = float(input())
d = float(input())
r = ((((c - a)**2) + ((d - c)**2))**0.5)
if r < 0:
    r = -r
print (f"расстояние между двумя точками - {r} ")

