import os
import zipfile
from datetime import datetime

pachTo1cBases = 'E:\\Vasilieva\\Bases 1C\\'
pathTo1cBackups = 'G:\\DB_backups\\Vasilieva_1C\\'

bases_1C = ('ADI',
            'IKA',
            'PF',
            'Vikanto',
            'БК 1С',
            'УкрВап',
            'УкрДиабаз_БАС',
            'ФайфСтарТрейдинг'
            )


def time_now():
    return datetime.now().strftime('D%Y%m%d_T%H%M%S')


def zip_and_copy(*args):
    for name in args:
        name_arc = f'{pathTo1cBackups}{name}_backup_{time_now()}.zip'
        dir_pach = f'{pachTo1cBases}{name}'

        with zipfile.ZipFile(name_arc, 'w') as zip_arc:
            for folder, subfolders, files in os.walk(dir_pach):
                for file in files:
                    zip_arc.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), dir_pach),
                                  compress_type=zipfile.ZIP_DEFLATED)


if __name__ == '__main__':
    zip_and_copy(*bases_1C)
