import datetime
class Reserva:
    def __init__(self):
        self.cpf_cliente = None
        self.data = None
        self.hora = None
        self.automovel = None

    def reservar(self, cpf_cliente, automovel):
        self.cpf_cliente = cpf_cliente
        self.automovel = automovel
        self.automovel.set_reservado(True)
        self.data = datetime.date.today()
        self.hora = datetime.datetime.now().time()
    
    def get_cpf_cliente(self):
        return self.cpf_cliente
    
    def set_cpf_cliente(self, cpf_cliente):
        self.cpf_cliente = cpf_cliente
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

    def get_hora(self):
        return self.hora
    
    def set_hora(self, hora):
        self.hora = hora
    
    def get_automovel(self):
        return self.automovel
    
    def set_automovel(self, automovel):
        self.automovel = automovel
    
    def cancelar_reserva(self):
        self.automovel.set_reservado(False)
        self.id_cliente = 0
        self.data = None
        self.hora = None
        self.automovel = None