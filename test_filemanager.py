'''
модуль для тестирования функций консольного файлового менеджера
'''

from famous_persons import get_random_person, get_file_info


def test_get_random_person():
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
    assert get_random_person() in list(FAMOUS_PEOPLE.items())


def test_get_file_info():
    assert get_file_info() == 'Стив Джобс'

# def test_copy():
#     os.mkdir('folder_mk')
#     shutil.copy('folder_mk', 'folder_mk_new')
#     assert 'folder_mk_new' in os.listdir()