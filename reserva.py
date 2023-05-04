class Reserva:
    def __init__(self):
        self.id_cliente = 0
        self.data = None
        self.hora = None
        self.automovel = None

    def reservar(self, id_cliente, automovel, data, hora):
        self.id_cliente = id_cliente
        self.automovel = automovel
        self.automovel.set_reservado(True)
        self.data = data
        self.hora = hora
    
    def get_id_cliente(self):
        return self.id_cliente
    
    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente
    
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