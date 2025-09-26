# Блок функций для работы с файлами и папками
import os
import shutil


from decorators import *


@save_call_to_file  # 🟡
def change_dir(path):  # смена рабочего каталога на любой другой (относительный путь применим)
    if path[0] != '/':
        path = os.getcwd() + '/' + path
    try:
        os.chdir(path)
        # print("Текущий рабочий каталог: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Каталог [{0}] не существует".format(path))
    except NotADirectoryError:
        print("{0} - не является каталогом".format(path))
    except PermissionError:
        print("Не хватает прав!")
    finally:  # 🟡
        print("Текущий рабочий каталог: {0}".format(os.getcwd()))
    return


@save_call_to_file  # 🟡
def mk_dir(path):  # создание папки в теущем каталоге # 🟡
    # if path[0] == '/':
    #    path = os.getcwd() + path
    # else:
    #    path = os.getcwd() + '/' + path
    path = (os.getcwd() + path) if path[0] == '/' else (os.getcwd() + '/' + path)  # 🟡

    if not os.path.exists(path):
        os.mkdir(path)
        print("Папка создана:", path)
    else:
        print("Создать {0} невозможно - уже существует!".format(path))
    return


@save_call_to_file  # 🟡
def rm_dir(path):  # удаление файла или папки в текущем каталоге
    if path[0] == '/':
        path = path[1:]
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
        print("{0}: удаление успешное!".format(path))
    else:
        print("Папку или файл {0} не удалось найти в каталоге {1}!".format(path, os.getcwd()))
    return


"""
def file_copy(path1, path2):  # копировать файл или папку (задать два пути)
    if path2[0] == '/':
        if not os.path.exists(path2):
            path2 = os.getcwd() + path2
    else:
        path2 = os.getcwd() + '/' + path2

    if os.path.exists(path1):
        try:
            if os.path.isdir(path1):
                shutil.copytree(path1, path2)
                print('', 'Результат:', path2, *os.listdir(path2), sep='\n')
            elif os.path.exists(path2) and os.path.isfile(path1):
                res = shutil.copy(path1, path2)
                print('\nРезультат:', res, Path(res).stat().st_size, 'bytes')
            elif not os.path.exists(path2):
                os.mkdir(path2)
                res = shutil.copy(path1, path2)
                print('\nРезультат:', res)
        except FileExistsError:
            print('\nПапка/файл уже существует!')
    else:
        print('\nОшибка ввода! Копировать нечего!')
    return
"""


@save_call_to_file  # 🟡
@check_time  # 🟡
def file_copy(source, destination):
    if os.path.exists(source):
        try:
            if os.path.isdir(source):
                shutil.copytree(source, destination)
                print('Директория {} скопирована в {}'.format(source, destination))
            elif os.path.isfile(source):
                shutil.copy2(source, destination)
                print('Файл {} скопирован в {}'.format(source, destination))
        except Exception as e:
            print('Ошибка копирования файлов: {}'.format(e))
    else:
        print('\nОшибка ввода! Копировать нечего: {}'.format(source))
    return


@save_call_to_file  # 🟡
@check_time  # 🟡
def list_all():  # вывод всех объектов в рабочей папке
    path = os.getcwd()
    print(path, ' ==>', *os.listdir(path), sep='\n')
    return


@save_call_to_file  # 🟡
def list_dir():  # вывод только папок, которые находятся в рабочей папке
    path = os.getcwd()
    folders = sorted([dirs for dirs in os.listdir(path) if os.path.isdir(dirs)])
    print(path, ' ==>', *folders, sep='\n')
    return folders


@save_call_to_file  # 🟡
def list_to_sep_str(my_list):
    delim = ", "
    temp = list(map(str, my_list))
    my_txt = delim.join(temp)
    return my_txt


@save_call_to_file  # 🟡
@check_time  # 🟡
def save_dir():
    all_files = list_to_sep_str(list_files())
    all_dirs = list_to_sep_str(list_dir())
    files_dirs = f'files: {all_files}\ndirs: {all_dirs}\n'
    f_name = 'listdir.txt'
    with open(f_name, 'w') as f:
        f.write(files_dirs)
    return files_dirs


@save_call_to_file  # 🟡
def list_files():  # вывод только файлов, которые находятся в рабочей папке
    path = os.getcwd()
    only_files = sorted([files for files in os.listdir(path) if os.path.isfile(files)])
    print(path, ' ==>', *only_files, sep='\n')
    return only_files
