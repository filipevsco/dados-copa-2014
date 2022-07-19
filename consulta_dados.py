import os


def main():
    # dicionáriocde nome entidade -> atributos
    meta = {}
    
    # dicionario identificador -> nome entidade
    keys = {}
    
    # dicionario de relacionamentos
    relationchips = {}
    
    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = atributes[0]
        
        meta[table_name] = 

if __name__ == "__main__":
    main()