import csv
import controller
def csv_init():
    with open("spravochnik.csv", 'w') as file:
        writer=csv.writer(file)
        writer.writerow(
            "имя"
            "фамилия"
            "номер телефона"
        )

def add_contact():
    global name , surname , phone
    name , surname , phone = list(map(int, input("Введите имя,фамилию и телефон(через пробел)").split(" ")))
    with open("spravochnik.csv", 'a') as file:#проблема№1 не знаю как делать чтобы он мог понимать два формата без костылей(сделать развилку как именно вводить данные)
        writer=csv.writer(file)
        writer.writerow(
            (
            [name , surname , phone]
            )
        )
    print("контакт добавлен")
    controller.choice()

def del_contact():
    name = input('Введите имя или фамилию контакта, которого надо удалить:  ')
    with open("spravochnik.csv", 'r') as file:
        data = csv.DictReader(file, delimiter=' ')
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
        with open("spravochnik.csv", 'w') as file:
            writer=csv.writer(file)
            writer.writerow(
            (
            [name , surname , phone]
            )
        )
    print("контакт удалён")




def search_contact():
    name = input('Введите имя или фамилию контакта, которого надо найти:  ')
    with open("spravochnik.csv", 'r') as file:
        data = csv.DictReader(file, delimiter=' ')
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname'] or name == data[i]['phone']:
                print(f"Имя {name} Фамилия {surname} телефон {phone}")


def show_contacts():
    with open("spravochnik.csv", 'r') as file:
        for names in name:
            print(f"Имя {name} Фамилия {surname} телефон {phone}") 