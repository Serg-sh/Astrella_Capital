import os
import traceback
import zipfile
from datetime import datetime
from typing import Union

SIZE = 245


# bases_1C = ('ADI',
#             'IKA',
#             'PF',
#             'Vikanto',
#             'БК 1С',
#             'УкрВап',
#             'УкрДиабаз_БАС',
#             'ФайфСтарТрейдинг'
#             )


def time_now():
    return datetime.now().strftime('D%Y%m%d_T%H%M%S')


def logging(text):
    with open('log.txt', "a") as log:
        data = f"--------\n{text}--------\n"
        log.write(data)


def check_size_file(file) -> bool:
    """
    Возвращает True если файл меньше 245 Мб и False если больше.
    :param file:
    :return: bool
    """
    return True if os.path.getsize(file) // 1024 // 1024 <= SIZE else False


def split_file(file):
    parts_of_file = []
    num_parts = 1
    with open(file, 'rb') as f:
        data = f.read(SIZE * 1024 * 1024)
        while data:
            with open(f"{file}_part{num_parts}", 'wb') as out_file:
                out_file.write(data)
            parts_of_file.append(f"{file}_part{num_parts}")
            num_parts += 1
            data = f.read(SIZE * 1024 * 1024)
    return parts_of_file


def zip_and_copy(list_name_folder: Union[list, tuple],
                 path_to_1c_bases: str,
                 path_to_1c_backups: str) -> list:
    list_arc_name = []
    for name in list_name_folder:
        name_arc = f'{path_to_1c_backups}{name}_backup_{time_now()}.zip'
        dir_patch = f'{path_to_1c_bases}{name}'

        with zipfile.ZipFile(name_arc, 'w') as zip_arc:
            for folder, subfolders, files in os.walk(dir_patch):
                for file in files:
                    try:
                        zip_arc.write(os.path.join(folder, file),
                                      os.path.relpath(os.path.join(folder, file), dir_patch),
                                      compress_type=zipfile.ZIP_DEFLATED)
                        logging(f"{time_now()}\nDONE! {file} zipped successfully!")
                    except Exception as e:
                        logging(f"{time_now()}\nERROR!!! File {file} don't copyed!\n"
                                f"{e}"
                                f"{traceback.format_exc()}")
        if check_size_file(name_arc):
            list_arc_name.append(name_arc)
        else:
            list_arc_name.extend(split_file(name_arc))

    return list_arc_name


def merge_files(files_l: list[str]):
    """
    Сливает бинарные файлы _part в исходный
    :param files_l:
    :return:
    """
    for f in files_l:
        with open(f, 'rb') as p, open(f"{files_l[0].split('_')[0]}_", 'ab') as out:
            out.write(p.read())


# files = ["./data/big.zip_part1", "./data/big.zip_part2"]
# merge_files(files)
