from random import randint
MaxVal=100
k = int(input('Введите натуральную степень k:'))
koff=[randint(0,MaxVal) for i in range(k)]+[randint(1,MaxVal)]
mnogo='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koff) if j][::-1])
mnogo=mnogo.replace('x^1+', 'x+')
mnogo=mnogo.replace('x^0', '')
mnogo+=('','1')[mnogo[-1]=='+']
mnogo=(mnogo, mnogo[:-2])[mnogo[-2:]=='^1']
print(mnogo)