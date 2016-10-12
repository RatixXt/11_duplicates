# -*- coding: utf-8 -*-
from os import walk, stat
from os.path import join, exists
from pprint import pprint


def get_file_size(filepath):
    return stat(filepath).st_size


def get_filepath(dir_address, filename):
    return join(dir_address, filename)


def get_files_information(directory_path):
    files_information = []
    for dir_address, dirs, files in walk(directory_path):
        for file in files:
            filepath = get_filepath(dir_address, file)
            files_information.append([file, get_file_size(filepath), filepath])
    return files_information


def get_equal_files(files_information):
    equal_files = []
    files_dictionary = {}
    for filename, filesize, filepath in files_information:
        if files_dictionary.get(filename) is not None:
            if files_dictionary[filename][0] == filesize:
                equal_files.append([filepath, files_dictionary[filename][1]])
        else:
            files_dictionary[filename] = [filesize, filepath]
    return equal_files


def choose_directory_for_check():
    dirpath = input(u'Введите путь к директории для проверки на дублирующиеся файлы:')
    if exists(dirpath):
        return dirpath


if __name__ == '__main__':
    dirpath = choose_directory_for_check()
    if dirpath:
        files_information = get_files_information(dirpath)
        equal_files = get_equal_files(files_information)
        print(u'Следующие файлы являются дубликатами:')
        pprint(equal_files)
    else:
        print(u'Путь к директории указан неверно')
