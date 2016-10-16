# -*- coding: utf-8 -*-
from os import walk, stat
from os.path import join, exists


def get_file_size(filepath):
    return stat(filepath).st_size


def get_equal_files(directory_path):
    equal_files = []
    files_dictionary = {}
    for dir_address, dirs, files in walk(directory_path):
        for filename in files:
            filepath = join(dir_address, filename)
            filesize = get_file_size(filepath)
            if files_dictionary.get(filename) is not None:
                if files_dictionary[filename][0] == filesize:
                    equal_files.append([filepath, files_dictionary[filename][1]])
            else:
                files_dictionary[filename] = [filesize, filepath]
    return equal_files


if __name__ == '__main__':
    dirpath = input(u'Введите путь к директории для проверки на дублирующиеся файлы:')
    if not exists(dirpath):
        dirpath = None

    if dirpath:
        equal_files = get_equal_files(dirpath)
        print(u'Следующие файлы являются дубликатами:')
        for file in equal_files:
            print('File1: {0[0]};\nFile2: {0[1]}\n'.format(file))
    else:
        print(u'Путь к директории указан неверно')
