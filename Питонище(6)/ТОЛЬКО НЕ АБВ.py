# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'
# my_text2 = list(my_text.split())
# [my_text2.append(i) for i in my_text if i not ']
# for i in my_text2:
#     if i in my_text =='абв':
#         my_text.remove('абв')
# print (my_text)
my_text = list(map(str, input().split(" ")))

def del_ABC_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_ABC_words(my_text)
print(my_text)