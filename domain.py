from decimal import Decimal


class Relationship:
    """Classe que representa uma relação entre DataTables
    
       Essa classe tem todas as informações que identificam um relacionamento entre tabelas.
       Em qual coluna ele existe, de onde vem e pra onde vai.
    """

    def __init__(self, name, __from, to, on):
        """Construtor
        
            Args:
                name: None
                __from: Tabela de onde sai
                to: Tabela pra onde vai
                on: instância de coluna onde existe
        """
        self.__name = name
        self.__from = __from
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
        """Cria uma referência desss tabela para outra tabela.
        
            Args:
                name: nome da relacao
                to: instância da tabela apontada
                on: instância em que existe a relação
        """
        relationship = Relationship(name, self, to, on)
        self.__references.append(relationship)

    def add_referenced(self, name, by, on):
        """Cria uma referência para outra tabela que aponta para essa tabela.
        
            Args:
                name: nome da relação
                by: instancia da tabela que aponta para essa.
                on: instância coluna que existe a relacao 
        """
        relationship = Relationship(name, by, self, on)
        self.__referenced.append(relationship)

    def __validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception('Tipo invalido')

    def __get__name(self):
        print("Getter executado")
        return self.__name

    def __set__name(self, __name):
        print("Setter executado")
        self.__name = __name

    def __del__name(self):
        print("Deletter executado")
        raise AttributeError("Não pode deletar esse atributo")

    name = property(__get__name, __set__name, __del__name)


class Column:
    """Representa uma coluna em um DataTable

        Essa classe contém as informações de uma coluna e deve validar um dado
        de acordo com o tipo de dado configurado no construtor

        Attributes:
            name: Nome da Coluna
            kind: Tipo de Dado (varchar, bigint, numeric)
            description: Descrição da coluna
        """

    def __init__(self, name, kind, description=""):
        """Construtor

            Args:
                name: Nome da Coluna
                kind: Tipo de dado (varchar. bigint, numeric)
                description: Descrição da coluna
        """
        self.__name = name
        self.__kind = kind
        self.__description = description
        self.__is_pk = False

    def __str__(self):
        return "Col {} : {} {}".format(self.__name,
                                       self.__kind,
                                       self.__description)

    def __validate(kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True

    validate = staticmethod(__validate)

class PrimaryKey(Column):
    def __int__(self, table, name, kind, description=""):
        super().__init__(name, kind, description=description)
        self.__is_pk = True

    def __str__(self):
        _str = "Col: {} : {} {}".format(self.__name,
                                        self.__kind,
                                        self.__description)
        return "{} - {}".format('PK', _str)
