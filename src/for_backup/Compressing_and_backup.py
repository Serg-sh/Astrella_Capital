import os
import zipfile
from datetime import datetime

pachTo1cBases = '\\\\10.123.11.10\\e$\\Vasilieva\\Bases 1C\\'
pathTo1cBackups = '\\\\10.123.11.10\\f$\\BackUp\\Vasilieva_1C\\'


def timeNow():
    return datetime.now().strftime('D%Y%m%dT%H%M%S')


def listBasesForBackup(*args):
    for name in args:
        name_arc = pathTo1cBackups + name + '_backup_' + timeNow() + '.zip'
        dir_pach = pachTo1cBases + name

        with zipfile.ZipFile(name_arc, 'w') as zip_arc:
            for folder, subfolders, files in os.walk(dir_pach):
                for file in files:
                    zip_arc.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), dir_pach),
                                  compress_type=zipfile.ZIP_DEFLATED)


if __name__ == '__main__':
    listBasesForBackup('ADI', 'IKA', 'PF', 'Vikanto', 'БК 1С', 'УкрВап')
