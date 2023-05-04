class Pessoa:
    def __init__(self, nome: str, cpf: str, telefone: str, cep: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__cep = cep

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def cep(self):
        return self.__cep
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep