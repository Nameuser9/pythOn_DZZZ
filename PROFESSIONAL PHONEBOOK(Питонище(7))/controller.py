import csv
import changes as ch
import contacts as con
import uservision as uv
import logger as lg


def choice():
    global num_choice
    num_choice = int(input)
    if num_choice == 0:
        con.csv_init()
    elif num_choice == 1:
        con.add_contact()
    elif num_choice == 2:
        num_choice2 = input('что нужно изменить в контакте\n 1- имя 2-фамилия 3-номер')
        if num_choice2 == 1:
            ch.change_name()
        elif num_choice2 == 2:
            ch.change_surname()
        elif num_choice2 == 3:
            ch.change_phone()
    elif num_choice == 3:
        con.del_contact()
    elif num_choice == 4 :
        con.show_contacts()
    elif num_choice == 5:
        lg.make_logs()
    elif num_choice == 6:
        print('спасибо за обращение')
