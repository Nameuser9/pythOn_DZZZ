print ('введите координаты искомых точкек(Х,Y)')
a , b ,c ,d =list(map(int, input().split(" ")))
r = lambda a, b , c ,d:((((c - a)**2) + ((d - c)**2))**0.5)
r(a , b ,c ,d)
if r < 0:
    r = -r
print (f"расстояние между двумя точками - {r} ")
