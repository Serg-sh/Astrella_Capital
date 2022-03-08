# import local_utils
import sp_utils
from src import config

tenant_O365 = config.tenant_O365
username_O365 = config.username_O365
password_O365 = config.password_O365
site_O365_path = config.site_O365_path
shared_dir_path = config.shared_dir_path
local_dir_path = config.local_dir_path


# remote_dir_path = ''

# local_utils.net_copy()

list_files = ["/Users/admin/Downloads/2022-02-08 01.29.50.mp4", "/Users/admin/Downloads/2022-03-05 21.13.18.jpg",
              "/Users/admin/Downloads/20220207_202600.mp4", "/Users/admin/Downloads/ClearVPN.dmg"]

sp_utils.copy_file_to_sp(tenant=tenant_O365,
                                  username=username_O365,
                                  password=password_O365,
                                  site_o365=site_O365_path,
                                  shared_folder=shared_dir_path,
                                  list_files=list_files)
