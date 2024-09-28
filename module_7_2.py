from pprint import pprint

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]


def read_str():
    """Функция открывает файл "module_7_2.txt", считывает содержимое и закрывает файл.
    """
    file_read_str = open("module_7_2.txt", "r", encoding="utf-8")
    try:
        return file_read_str.read()
    finally:
        file_read_str.close()


def personal_request(file_name, *args, strings=None):
    """Функция принимает аргументы file_name - название файла для записи, strings - список строк для записи.
       Функция должна:
       - записывать в файл file_name все строки из списка strings, каждая на новой строке;
       - возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
         а значением - записываемая строка.
       - Для получения номера байта начала строки используйте метод tell() перед записью;
    """
    strings_index = {}
    if strings is None:
        strings = [*args]
    for sub_string in strings:
        if sub_string in read_str():
            print(f"субстрока {sub_string} уже есть в файле, запишите иначе")
        else:
            file = open(file_name, "a", encoding="utf-8")
            num_byte = file.tell()
            file.write(sub_string + "\n")
            file.close()
            file = open(file_name, "r", encoding="utf-8")
            for item, line in enumerate(file):
                a = (item + 1)
            count_str = a
            strings_index.update({(count_str, num_byte): sub_string})
            file.close()

    print(strings_index)


personal_request('module_7_2.txt', 'board', '12 packs', 'Привет со строки три!', 'а это уже четвёртая строка')

