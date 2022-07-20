class DataTable:
    """
    Representa uma Tabela de dados.

    Essa classe representa uma tabela de dados do portal da transparência. Deve
    ser capaz de validar linhas inseridas de acordo com as colunas que possui. As
    linhas inseridas ficam registradas dentro dela.

    Attibutes:
        name: Nome da tabela
        columns: [Lista de colunas]
        data: [Lista de dados]
    """
    def __init__(self, name):
        """
        Construtor

            Args:
                name: Nome da Tabela
        """
        self.__name = name
        self.__columns = []
        self.__data = []

    def add_column(self, name, kind, description):
        column = Column(name, kind, description)
        self.__columns.append(column)
        return column


class Column:
    """Representa uma coluna em um DataTable

        Essa classe contém as informações de uma coluna e deve validar um dado
        de acordo com o tipo de dado configurado no construtor

        Attributes:
            name: Nome da Coluna
            kind: Tipo de Dado (varchar, bigint, numeric)
            description: Descrição da coluna
        """
    def __init__(self):
        """Construtor

            Args:
                name: Nome da Coluna
                kind: Tipo de dado (varchar. bigint, numeric)
                description: Descrição da coluna
        """
        self.__name = name
        self.__kind = kind
        self.__description = description


class Relationship:
    """Classe que representa uma relação entre DataTables
    
       Essa classe tem todas as informações que identificam um relacionamento entre tabelas. Em qual coluna ele existe, de onde vem e pra onde vai.
    """
    def __init__(self, name, __from, to, on):
        """Construtor
        
            Args:
                name: None
                from: Tabela de onde sai
                to: Tabela pra onde vai
                on: instância de coluna onde existe
        """
        self.__name = name
        self. __from = __from
        self.__to = to
        self.__on = on
        