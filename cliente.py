from pessoa import Pessoa

# Cliente herda de Pessoa e adiciona os atributos email, senha, reservas e locacoes
class Cliente(Pessoa):
    def __init__(self, email, senha, nome, cpf, telefone, cep):
        super().__init__(nome, cpf, telefone, cep)
        self.email = email
        self.senha = senha
        self.reservas = []
        self.locacoes = [] 
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email
    
    def get_senha(self):
        return self.senha
    
    def set_senha(self, senha):
        self.senha = senha
    
    def get_reservas(self):
        return self.reservas
    
    def get_locacoes(self):
        return self.locacoes
    
    def add_reserva(self, reserva):
        self.reservas.append(reserva)
    
    def add_locacao(self, locacao):
        self.locacoes.append(locacao)
    
    def remover_reserva(self, reserva):
        self.reservas.remove(reserva)
    
    def remover_locacao(self, locacao):
        self.locacoes.remove(locacao)