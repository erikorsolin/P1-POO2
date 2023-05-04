from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, matricula, senha, nome, cpf, telefone, cep):
        super().__init__(nome, cpf, telefone, cep)
        self.matricula = matricula
        self.senha = senha
       
    
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, matricula):
        self.matricula = matricula
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, salario):
        self.salario = salario
    
    def calcular_salario(self):
        return self.salario
    
    def get_senha(self):
        return self.senha
    
    def set_senha(self, senha):
        self.senha = senha