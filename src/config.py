from environs import Env

env = Env()
env.read_env()

tenant_O365 = env.str("TENANT_O365")
username_O365 = env.str("USERNAME_O365")
password_O365 = env.str("PASSWORD_O365")
site_O365_path = env.str("SITE_O365_PATH")
shared_dir_path = env.str("SHARED_DIR_PATH")
local_dir_path = env.str("LOCAL_DIR_PATH")
list_names_folder_for_backup = env.list("LIST_NAMES_BACKUP_FOLDER")
