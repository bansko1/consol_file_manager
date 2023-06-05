'''

В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.

'''
import os
from shutil_func import copy_folder_file
import sys
from os_func import create_folder, delete_folder_file, view_work_dir
from famous_persons import get_random_person, get_question, get_file_info
from my_bank import my_bank

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. сохранить содержимое рабочей директории в файл')
    print('8. просмотр информации об операционной системе')
    print('9. создатель программы')
    print('10. играть в викторину')
    print('11. мой банковский счет')
    print('12. смена рабочей директории (*необязательный пункт)')
    print('13. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        create_folder()
    elif choice == '2':
        delete_folder_file()
    elif choice == '3':
        copy_folder_file()
    elif choice == '4':
        view_work_dir(choice)
    elif choice == '5':
        # Список только папок
        view_work_dir(choice)
    elif choice == '6':
        # Список только файлов
        view_work_dir(choice)
    elif choice == '7':
        # Сохранение в файл файлов и папок рабочей дирктории
        dirs = []
        files = []
        content = os.listdir()
        for object in content:
            if os.path.isfile(object):
                files.append(object)
            else:
                dirs.append(object)
        with open('listdir.txt', 'w') as f:
            f.write(f'files: {files}\ndirs: {dirs}')
    elif choice == '8':
        # Пути, где питон ищет файлы
        print(sys.path)
    elif choice == '9':
        print('Создатель программы:', get_file_info())
    elif choice == '10':
        rounds = int(input('Сколько раз будем играть?'))
        for i in range(rounds):
            name, data = get_random_person()
            answer = input(f'Когда родился {name}? ')
            get_question(answer, data)
        print('Викторина завершена.')
    elif choice == '11':
        my_bank()
    elif choice == '12':
        print('Текущая дериктория', os.getcwd())
        key = input('Введите 1, чтобы сменить текущую дерикторию')
        if key == '1':
            path = input('Введите путь к новой дериктории: ')
            os.chdir(path)
    elif choice == '13':
        print('*** Конец работы ***')

        break
    else:
        print('Неверный пункт меню')
