num = int(input("Введите число: "))
i = 2 
arr = []
arr2 = []
old = num
while i <= num:
    if num % i == 0:
        arr.append(i)
        num //= i
        i = 2
    else:
        i += 1
[arr2.append(a) for a in arr if i not in arr2]
print(f"Простые множители числа {old} приведены в списке: {arr2}")