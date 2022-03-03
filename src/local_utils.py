import os
import zipfile
from datetime import datetime
from typing import Union

pachTo1cBases = ""
pathTo1cBackups = ""

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
                    zip_arc.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), dir_patch),
                                  compress_type=zipfile.ZIP_DEFLATED)
        list_arc_name.append(name_arc)
    return list_arc_name
