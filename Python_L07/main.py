# Main Menu
from bank_account import my_bank
from file_tools import *


menu = {'21': 'создать папку',
        '22': 'удалить (файл/папку)',
        '23': 'копировать (файл/папку)',
        '24': 'просмотр содержимого директории',
        '25': 'посмотреть только папки',
        '26': 'посмотреть только файлы',
        '27': 'смена рабочей директории',
        '28': 'сохранить содержимое директории в файл',
        '32': 'мой банковский счет',
        '00': 'выход.'
        }


def stop_menu():
    print('😎 До скорой встречи!')
    return False


def print_menu():
    title = ' МЕНЮ '
    max_str = int((max((len(v)) for v in menu.values()) + 4 - len(title)) / 2)
    print('\n', '=' * max_str, title, '=' * max_str)
    for key, val in menu.items():
        print(f'{key}. {val}')
    print('-' * (max_str * 2 + len(title) + 2))
    return


def start_menu(ask=True):
    while ask:
        print_menu()
        item = input('... Ваш выбор: ')
        if item in menu.keys():
            if item == "00":
                ask = stop_menu()
            elif item == "21":
                mk_dir(input('\nВведите новую папку для создания: '))
            elif item == "22":
                rm_dir(input('\nВведите папку или файл для удаления: '))
            elif item == "23":
                p1 = input('\nВведите файл/папку для копирования: ')
                p2 = input('Введите файл/папку назначения: ')
                file_copy(p1, p2)
            elif item == "24":
                list_all()
            elif item == "25":
                list_dir()
            elif item == "26":
                list_files()
            elif item == "27":
                change_dir(input('\nВведите новую рабочую директорию: '))
            elif item == "28":
                files_dirs = save_dir()
                print('\n\n')
                print(files_dirs)
            elif item == "32":
                my_bank()
            else:
                print('Ok')
        else:
            print(' 🚫 Ошибка выбора пункта меню!')
    return


if __name__ == '__main__':
    start_menu()
