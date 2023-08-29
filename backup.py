# This module makes backup of actual data files in this sequence of steps:
# 1. Makes zip copy of previous backup to save space and adds datetimestamp to the name of the backup file
# 2. Removes zip copy to Recycle Bin, leaving opportunity to retrieve backup later if next steps go wrong
# 3. Permanently removes old backup
# 4. Saves copy of data files to the backup directory


from datetime import datetime
from pathlib import Path
import os
import zipfile
import send2trash
import shutil

def backup_data_files(terminal_instance_ref):

    # Set and change as needed backup paths
    path_to_backup = Path('data')
    path_where_backup = Path(r'backup\data')
    path_to_zip = Path(r'backup\data')
    path_to_remove = Path('backup')

    # Make zip file from old backup folder to save Recycle Bin space and add datetimestamp
    datetimestamp = datetime.now()
    datetime_str = datetimestamp.strftime("%Y_%m_%d_%H_%M_%S")
    zip_file_name = Path("backup", f"{datetime_str}" + "_backup.zip")
    terminal_instance_ref.fill_terminal(log_text_message="The backup folder is being compressed.. Please wait..\n")
    def zipdir(path, ziph):
        for root, dirs, files in os.walk(path):
        	terminal_instance_ref.fill_terminal(log_text_message=f"Compressing folder: {root}\n")
        	for file in files:
        		ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

    with zipfile.ZipFile(f"{zip_file_name}", 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(path_to_zip, zipf)
    terminal_instance_ref.fill_terminal(log_text_message=f"The backup folder compressed to file: {zip_file_name}\n")

    # Remove zip file backup to the trash - the last option to restore files later
    send2trash.send2trash(f"{zip_file_name}")
    terminal_instance_ref.fill_terminal(log_text_message=f"File {zip_file_name} was sent to Recycle Bin\n")

    # Delete permanently old backup folder
    shutil.rmtree(path_to_remove)
    terminal_instance_ref.fill_terminal(log_text_message="Old backup folder permanently deleted\n")

    # Copy data folder to backup folder
    shutil.copytree(path_to_backup, path_where_backup)
    terminal_instance_ref.fill_terminal(log_text_message="Data folder with files was successfully copied to backup folder\n")

