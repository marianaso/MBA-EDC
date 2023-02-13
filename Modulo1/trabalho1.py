import boto3
import os

s3_client = boto3.client('s3')

#s3_client.upload_file("/Users/marianaoliveira/Downloads/MBA/microdados_enem_2020/DADOS/MICRODADOS_ENEM_2020.csv",
#                     "datalake-mariana-494654695792", "raw-data/MICRODADOS_ENEM_2020.csv")

diretorio_gzip = "/Volumes/Expansion/MBA/Desafio1/DATA_GZIP/"

for namefilegz in os.listdir(path=diretorio_gzip):
    
    print(f"Arquivo: {namefilegz}")
    s3_client.upload_file(f"{diretorio_gzip}{namefilegz}", 
                   "datalake-desafio-mod1", 
                   f"raw-data/{namefilegz}")