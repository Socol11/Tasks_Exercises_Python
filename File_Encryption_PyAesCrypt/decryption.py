"""
Дешифрование файлов и директорий
"""


import pyAesCrypt
import os
import sys

# Функция дешифровки файла
def decryption(file, password):

    # Задаём размер буфера
    buffer_size = 512 * 1024

    # Вызываем метод дешифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # Чтобы видеть результат, выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' расшифрован]")

    # Удаляем исходный файл
    os.remove(file)


# Функция сканирования директорий
def walking_by_dirs(dir, password):

    # Перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если находим файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # Если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для дешифрования: ")
walking_by_dirs("files_for_decryption", password)    # первый аргумент - директория с зашифрованными файлами
