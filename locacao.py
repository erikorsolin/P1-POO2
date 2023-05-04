class locacao:
    def __init__(self):
        self.n_dias = 0
        self.custo_locacao = 0
        self.id_cliente = 0
        self.automovel = None

    def locar(self, id_cliente, automovel, n_dias):
        self.id_cliente = id_cliente
        self.automovel = automovel
        self.n_dias = n_dias
        self.custo_locacao = n_dias * automovel.get_valor_diaria()
    
    def get_n_dias(self):
        return self.n_dias
    
    def set_n_dias(self, n_dias):
        self.n_dias = n_dias
    
    def get_custo_locacao(self):
        return self.custo_locacao
    
    def set_custo_locacao(self, custo_locacao):
        self.custo_locacao = custo_locacao

    def get_id_cliente(self):
        return self.id_cliente
    
    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def get_automovel(self):
        return self.automovel



    
    