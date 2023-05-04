class Pessoa:
    def __init__(self, nome, cpf, telefone, cep):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cep = cep

    @property
    def nome(self):
        return self.nome
    
    @property
    def cpf(self):
        return self.cpf
    
    @property
    def telefone(self):
        return self.telefone
    
    @property
    def cep(self):
        return self.cep
    
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    @cpf.setter
    def cpf(self, cpf):
        self.cpf = cpf
    
    @telefone.setter
    def telefone(self, telefone):
        self.telefone = telefone
    
    @cep.setter
    def cep(self, cep):
        self.cep = cep