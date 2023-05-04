from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, email, senha, nome, cpf, telefone, cep):
        super().__init__(nome, cpf, telefone, cep)
        self.email = email
        self.senha = senha
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
    
    def get_senha(self):
        return self.senha
    
    def set_senha(self, senha):
        self.senha = senha