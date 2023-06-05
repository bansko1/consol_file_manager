import random

'''
Функции для блока main.py
'''


def get_random_person():  # Не чистая функция (случайная величина)
    '''
    Получить случайного человека (Имя, дата рождения)
    '''
    FAMOUS_PEOPLE = {
        'А.С.Пушкин': '06.06.1799',
        'Н.В.Гоголь': '01.04.1809',
        'М.Ю.Лермонтов': '15.10.1814',
        'Ф.М.Достоевский': '11.11.1821',
        'С.А.Некрасов': '10.12.1821',
        'Л.Н.Толстой': '09.09.1828',
        'А.П.Чехов': '29.01.1860',
        'М.А.Булгаков': '15.05.1891',
        'С.А.Есенин': '03.10.1895',
        'М.А.Шолохов': '24.05.1905'
    }
    # Выбираем случайного человека
    name, data = random.choice(list(FAMOUS_PEOPLE.items()))
    return name, data


def get_question(answer, data):  # Не чистая функция (вывод данных)
    if answer == data:
        print('Верно')
    else:
        print('Неверно')


def get_file_info():  # Чистая функция
    return 'А.Попов'


if __name__ == '__main__':
    print('Проверка функции: get_random_person()', get_random_person())
    print('Проверка функции: get_file_info()', get_file_info())
