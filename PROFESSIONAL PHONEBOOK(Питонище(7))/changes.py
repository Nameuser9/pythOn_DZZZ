import csv
import controller
import contacts as con


def change_name(name):
    con.search_contact(name)#проблема2 не совсем понимаю как он должна выглядеть замена данных, по идее переменная Name должна быть в методе поиска контакта
    #new_name = input(str) проблема 2 решена(возможно)
    with open("spravochnik.csv", 'w') as file:
         file[name]=input("введите новое имя")

def change_surname(surname):
   con.search_contact(surname)
   with open("spravochnik.csv", 'w') as file:
         file[surname]=input("введите новое фамилию")



def change_phone(surname):#
    con.search_contact(surname)
    with open("spravochnik.csv", 'w') as file:#проблема 3не понимаю как сделать поиск по фамилии и изменить в результате номер
         file[con.phone]=input("введите новое номер")