import os
from zipfile import ZipFile
import glob


files_to_unzip = glob.glob("metals/*.zip")

for file_path in files_to_unzip:
    basename = os.path.basename(file_path)
    basename = os.path.splitext(basename)[0]
    create_dir = os.path.join("metals", basename) 
    os.mkdir(create_dir)
    with ZipFile(file_path, 'r') as zipObj:
        zipObj.extractall(create_dir)


