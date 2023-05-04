class Pessoa:
    def __init__(self, nome: str, cpf: str, telefone: str, cep: str):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.cep = cep
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf
    
    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_telefone(self):
        return self.telefone
    
    def set_telefone(self, telefone):
        self.telefone = telefone
    
    def get_cep(self):
        return self.cep
    
    def set_cep(self, cep):
        self.cep = cep
        
