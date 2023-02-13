import os
import boto3
from pyunpack import Archive
import gzip
import shutil
from ftplib import FTP
import os
from py7zr import unpack_7zarchive

user: str   = os.getlogin()

path_master = "/Volumes/Expansion/MBA/Desafio1" 

path_7zip   = "/DATA_7ZIP/"  
path_txt    = "/DATA_TXT/"
path_gzip   = "/DATA_GZIP/"

extension_7z  = ".7z"
extension_txt = ".txt"
extension_gz  = ".gz"

dir_source_7z = f"{path_master}{path_7zip}"
dir_targe_txt = f"{path_master}{path_txt}"

for namefilegz in os.listdir(path=dir_source_gzip):
    if namefilegz.endswith(extension_gz):
        print(namefilegz)
        client.upload_file(f"{dir_source_gzip}{namefilegz}", 
                   "datalake-desafio-mod1-tf", 
                   f"raw-data/{namefilegz}")