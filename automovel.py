class Automovel: 
    def __init__(self, cor, modelo, tipo, placa, ano, valor_diaria):
        self.cor = cor
        self.modelo = modelo
        self.tipo = tipo
        self.placa = placa
        self.ano = ano
        self.valor_diaria = valor_diaria
    
    def get_cor(self):
        return self.cor
    
    def set_cor(self, cor):
        self.cor = cor
    
    def get_modelo(self):
        return self.modelo
    
    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo = tipo
    
    def get_placa(self):
        return self.placa
    
    def set_placa(self, placa):
        self.placa = placa

    def get_ano(self):
        return self.ano
    
    def set_ano(self, ano):
        self.ano = ano

    def get_valor_diaria(self):
        return self.valor_diaria
    
    def set_valor_diaria(self, valor_diaria):
        self.valor_diaria = valor_diaria
    
    def __str__(self):
        return f"Cor: {self.cor}\nModelo: {self.modelo}\nTipo: {self.tipo}\nPlaca: {self.placa}\nAno: {self.ano}\nValor da diária: {self.valor_diaria}"