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

sp_utils.copy_to_sp_two_last_file(tenant=tenant_O365,
                                  username=username_O365,
                                  password=password_O365,
                                  site_o365=site_O365_path,
                                  shared_folder=shared_dir_path,
                                  local_folder=local_dir_path)
