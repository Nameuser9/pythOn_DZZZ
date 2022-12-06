#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
nums = list(map(float, input("Введите числа через пробел:\n").split()))
new_nums = [round(i%1,2) for i in nums if i%1 != 0]
print(max(new_nums) - min(new_nums))