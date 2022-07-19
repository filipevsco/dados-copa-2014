import os


def extract_name(name):
    return name.split(".")[0]


def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read().split("\n")
    _file.close()
    return data


def read_metadata(filename):
    metadata = []
    for column in read_lines(filename):
        if column:
            metadata.append(tuple(column.split("\t")[:3]))
    return metadata
    
    
def prompt():
    print("\nO que deseja ver?")
    print("(l) Listar entidadades")

def main():
    # dicionáriocde nome entidade -> atributos
    meta = {}
    
    # dicionario identificador -> nome entidade
    keys = {}
    
    # dicionario de relacionamentos
    relationships = {}
    
    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_name(meta_data_file)
        attributes = read_metadata(meta_data_file)
        identifier = atributes[0]
        
        meta[table_name] = atributes
        keys[identifier] = table_name
        
    for keys, val in meta.items():
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    relationships[key] = keys[col[0]]
                    
    opcao = prompt()
    while opcao != "s":
        if opcao == "l":
            pass

if __name__ == "__main__":
    main()