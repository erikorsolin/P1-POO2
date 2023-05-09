class Locadora:
    def __init__(self):
        self.automoveis = []
        self.clientes = []
        self.reservas = []
        self.locacoes = []
        self.funcionarios = []

    def get_automoveis(self):
        return self.automoveis

    def get_automovel(self, placa):
        for automovel in self.automoveis:
            if automovel.get_placa() == placa:
                return automovel
        return None
    
    def get_clientes(self):
        return self.clientes

    def get_reservas(self):
        return self.reservas
    
    def get_locacoes(self):
        return self.locacoes
    
    def get_funcionarios(self):
        return self.funcionarios
    
    def add_automovel(self, automovel):
        self.automoveis.append(automovel)
    
    def remover_automovel(self, automovel):
        self.automoveis.remove(automovel)
    
    def add_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)
    
    def add_reserva(self, reserva):
        self.reservas.append(reserva)
    
    def remover_reserva(self, reserva):
        self.reservas.remove(reserva)
    
    def add_locacao(self, locacao):
        self.locacoes.append(locacao)
    
    def remover_locacao(self, locacao):
        self.locacoes.remove(locacao)

    def add_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def remover_funcionario(self, funcionario):
        self.funcionarios.remove(funcionario)

    def autenticar_funcionario(self, matricula, senha):
        for funcionario in self.funcionarios:
            if funcionario.get_matricula() == matricula and funcionario.get_senha() == senha:
                return funcionario
        return None   
    
    def autenticar_cliente(self, email, senha):
        for cliente in self.clientes:
            if cliente.get_email() == email and cliente.get_senha() == senha:
                return cliente
        return None
    