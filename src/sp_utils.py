import os
import sys
import time
import traceback

from datetime import datetime
from shareplum import Office365
from shareplum import Site
from shareplum.site import Version


# \venv\lib\site-packages\shareplum\folder.py" Need change field timeout in __init__ to None

# tenant: Tenant O365 -
# username: Login/email O365
# password: Password O365
# site_O365: Site O365 -
# shared_folder: Shared folder an site - 'Shared Documents/ИТ Служба/BackUps/Astrella/1C_UTP/'
# local_folder: Local folder an server - '//10.123.11.10/DB_backups/astrella/'


def time_now():
    return datetime.now().strftime('D%Y%m%d_T%H%M%S')


def o365_login(tenant, username, password, site_o365, shared_folder):
    """
    подключается к шар поинт
    :param tenant:
    :param username:
    :param password:
    :param site_o365:
    :param shared_folder:
    :return: возвращяет авторизированую папку на шар поинт
    """
    authcookie = Office365(tenant, username=username, password=password).GetCookies()
    site = Site(site_o365, version=Version.v365, authcookie=authcookie)
    folder_shared_o365 = site.Folder(shared_folder)
    logging(f"{time_now()}\nLogin to O365 to {site_o365} is successful!")
    # print(time_now(), f'    Login to O365 to {site_o365} is successful!')
    return folder_shared_o365


def copy_to_sp_two_last_file(tenant: str, username: str, password: str,
                             site_o365: str, shared_folder: str, local_folder: str):
    """
    Копирует 2 последних файла в ШП из указанной директории,
     предварительно сортирует файлы по временисоздания

    :param tenant:
    :param username:
    :param password:
    :param site_o365:
    :param shared_folder:
    :param local_folder:
    :return:
    """
    try:
        folder_shared_o365 = o365_login(tenant, username, password, site_o365, shared_folder)

        files_local = [f for f in os.listdir(local_folder)]  # список файлов в указанной директории

        for file in sorted(files_local, key=lambda f: os.path.getatime(os.path.join(local_folder, f)),
                           reverse=True)[:2]:
            file_abs_path = os.path.join(local_folder, file)
            print(time_now(), f'    File: {file_abs_path}')
            print(time_now(), f'    Created: {time.ctime(os.path.getatime(file_abs_path))}')
            print(time_now(), f'    File size: {os.path.getsize(file_abs_path) // 1024 // 1024} Mb')

            with open(file_abs_path, 'rb', buffering=1024) as f:
                data = f.read()
                folder_shared_o365.upload_file(data, file)
                print(time_now(), f'    File: {file} copied successfully.')
    except Exception as e:
        print(time_now(), f'    Script is end with error!!!.'.upper())
        print(time_now(), f'    {e}')
        print(time_now(), f'    {traceback.format_exc()}')
        sys.exit()
    else:
        print((time_now()), f'    Copy to folder {site_o365 + shared_folder} completed successfully.')


def copy_file_to_sp(tenant: str, username: str, password: str,
                    site_o365: str, shared_folder: str, list_files: list[str]):
    try:
        folder_shared_o365 = o365_login(tenant, username, password, site_o365, shared_folder)
        for file in list_files:
            text = f'{time_now()}\n' \
                   f'File: {file}\n' \
                   f'Created: {time.ctime(os.path.getatime(file))}\n' \
                   f'File size: {os.path.getsize(file) // 1024 // 1024} Mb\n'

            logging(text)

            with open(file, 'rb', buffering=1024) as f:
                data = f.read()
                folder_shared_o365.upload_file(data, file_name=file.split('/')[-1])
                # print(time_now(), f'    File: {file} copied successfully.')
                text = f'{time_now()}\n' \
                       f'File: {file}\n' \
                       f'Created: {time.ctime(os.path.getatime(file))}\n' \
                       f'File size: {os.path.getsize(file) // 1024 // 1024} Mb\n' \
                       f'{time_now()}  File: {file} copied to SP folder:\n' \
                       f'{site_o365 + shared_folder}\ncompleted successfully.\n'
                logging(text)

    except Exception as e:
        text = f"{time_now()}\n" \
               f"{'Script is end with error!!!'.upper()}\n" \
               f"{e}\n" \
               f"{traceback.format_exc()}\n"
        logging(text)
        sys.exit()
    else:
        logging(f'{time_now()}\nCopy to folder:\n{site_o365 + shared_folder}\ncompleted successfully.\n')


def logging(text):
    with open('log.txt', 'a') as log:
        data = f"--------\n{text}--------\n"
        log.write(data)
