import io
from pprint import pprint

# Занятие №1
# name = "sample1.txt"
# file = open(name, "r") # r, w, a; r - read, w - write, a - append.
# print(file) # <_io.TextIOWrapper name='sample1.txt' mode='r' encoding='cp1251'>
# pprint(file.read())
# file.close() # чтобы оперативная память не перезаполнилась, нужно закрывать файлы.
# многие действия с файлом не сохранятся, если его не закрыть.

# метод "w" - "write" перезаписывает файл. стирает то, что в нем было до этого.
# name = "sample2.txt"
# # file = open(name, "w")
# # pprint(file.write("Hello!"))
# # file.close()

# Метод append - "a" добавляет к существующему тексту изменения.
# name = "sample2.txt"
# file = open(name, "a")
# pprint(file.write("\nHello world 3"))
# file.close()
#
# name = "sample2.txt"
# file = open(name, "r")
# print(file.tell()) # выводит положение курсора (каретки)
# # 0 - начальное положение каретки
# pprint(file.read())
# print(file.tell()) # 90 -конечное положение каретки
# print(file.seek(22)) # сдвигает каретку на число символов
# pprint(file.read()) # результат чтения ''
# file.close()

# Занятие №2
name = "sample2.txt"
file = open(name, "r", encoding="utf-8")
print(file.writable())
print(file.readable())
print(file.seekable())
print(file.tell())
pprint(file.read())
print(file.tell())
file.close()