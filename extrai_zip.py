import os 
import sys
import zipfile


def main(path):
    if not os.path.exists(path):
        print(f"Arquivo {path} não existe.")
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("Arquivos extraídos")
        

if __name__ == "__main__":
    main(sys.argv[1])

