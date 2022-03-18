import local_utils
import sp_utils
from src import config

tenant_O365 = config.tenant_O365
username_O365 = config.username_O365
password_O365 = config.password_O365
site_O365_path = config.site_O365_path
shared_dir_path = config.shared_dir_path
local_dir_path = config.local_dir_path
list_folder_name = config.list_names_folder_for_backup
path_to_1c_db = config.path_to_1c_db
path_to_1c_backups = config.path_to_1c_backups

# remote_dir_path = ''

# local_utils.net_copy()

if __name__ == '__main__':
    list_files = local_utils.zip_and_copy(list_name_folder=list_folder_name,
                                          path_to_1c_bases=path_to_1c_db,
                                          path_to_1c_backups=path_to_1c_backups)

    sp_utils.copy_file_to_sp(tenant=tenant_O365,
                             username=username_O365,
                             password=password_O365,
                             site_o365=site_O365_path,
                             shared_folder=shared_dir_path,
                             list_files=list_files)
