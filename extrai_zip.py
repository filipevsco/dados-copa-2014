import os 
import sys
import zipfile


def main(path):
    if not os.path.exists(path):
        print(f."Arquivo {path} não existe.")
    else:
        zfile = zipfile.Zipfile(path)
        zfile.extractall()
        print("Arquivos extraídos")