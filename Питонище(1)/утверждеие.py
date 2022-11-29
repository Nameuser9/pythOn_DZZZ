X = True
Y = True
Z = True
A = not (X or Y or Z)
B = (not X) and (not Y) and (not Z)
if (A == B):
    print(True) 
else:
    print(False)
