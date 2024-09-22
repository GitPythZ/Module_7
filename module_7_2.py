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
    file_read_str = open("module_7_2.txt", "r")
    try:
        return file_read_str.read()
    finally:
        file_read_str.close()


def custom_write(file_name, strings):
    """Функция принимает аргументы file_name - название файла для записи, strings - список строк для записи.
       Функция должна:
       - записывать в файл file_name все строки из списка strings, каждая на новой строке;
       - возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
         а значением - записываемая строка.
       - Для получения номера байта начала строки используйте метод tell() перед записью;
    """
    strings_index = {}
    for sub_string in strings:
        if sub_string in read_str():
            print("isinstance")
        else:
            file = open(file_name, "a", encoding="utf-8")
            num_byte = file.tell()
            file.write(sub_string + "\n")
            file.close()
            file = open(file_name, "r", encoding="utf-8")
            for item, line in enumerate(file):
                a = (item + 1)
            num_str = a
            strings_index.update({(num_str, num_byte): sub_string})
            file.close()

    print(strings_index)


custom_write('module_7_2.txt', info)

