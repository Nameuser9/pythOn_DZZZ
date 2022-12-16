
A = lambda X,Z,Y :not (X or Y or Z)
B = lambda X,Z,Y :(not X) and (not Y) and (not Z)
A,B(True,True,True)


if (A == B):
    print(True) 
else:
    print(False)
