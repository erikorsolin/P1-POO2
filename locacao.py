class Locacao:
    def __init__(self):
        self.n_dias = 0
        self.custo_locacao = 0
        self.cpf_cliente = None
        self.automovel = None
        self.data_locacao = None
        self.data_devolucao = None

    def locar(self, cpf_cliente, automovel, n_dias):
        self.cpf_cliente = cpf_cliente
        self.automovel = automovel
        self.n_dias = n_dias
        self.custo_locacao = n_dias * automovel.get_valor_diaria()
        automovel.set_locado(True)
    
    def get_n_dias(self):
        return self.n_dias
    
    def set_n_dias(self, n_dias):
        self.n_dias = n_dias
    
    def get_custo_locacao(self):
        return self.custo_locacao
    
    def set_custo_locacao(self, custo_locacao):
        self.custo_locacao = custo_locacao

    def get_cpf_cliente(self):
        return self.cpf_cliente
    
    def set_cpf_cliente(self, cpf_cliente):
        self.cpf_cliente = cpf_cliente

    def get_automovel(self):
        return self.automovel

    def set_automovel(self, automovel):
        self.automovel = automovel

    def get_data_locacao(self):
        return self.data_locacao
    
    def set_data_locacao(self, data_locacao):
        self.data_locacao = data_locacao

    def get_data_devolucao(self):
        return self.data_devolucao
    
    def set_data_devolucao(self, data_devolucao):
        self.data_devolucao = data_devolucao
    
    