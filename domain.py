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
        self.__references = []
        self.__referenced = []
        self.__data = []

    def add_column(self, name, kind, description=""):
        column = Column(name, kind, description=description)
        self.__columns.append(column)
        return column
        
    def add_references(self, name, to, on):
        """Cria uma referência dessa tabela para que aponta para essa.
        
            Args:
                name: nome da relacao
                to: instância da tabela apontada
                on: instância em que existe a relação
        """
        relationship = Relationship(name, self, to, on):
            self.__references.append(relationship)
            
    def add_referenced(self, name, by, on):
        relationship = Relationship(name, by, self, on):
        self.__referenced.append(relationship)


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