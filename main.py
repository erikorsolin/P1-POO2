from cliente import Cliente
from funcionario import Funcionario
from automovel import Automovel
from reserva import Reserva
from locacao import Locacao
from locadora import Locadora

locadora = Locadora()

# cor, modelo, tipo, placa, ano, valor_diaria
automoveis = [Automovel("Azul", "Fiat Uno", "Hatch", "ABC-1234", 2010, 100),
              Automovel("Preto", "Fiat Palio", "Hatch", "DEF-5678", 2015, 150),
              Automovel("Branco", "Fiat Siena", "Sedan", "GHI-9012", 2018, 200),
              Automovel("Vermelho", "Fiat Toro", "Pickup", "JKL-3456", 2019, 250),
              Automovel("Prata", "Fiat Strada", "Pickup", "MNO-7890", 2020, 300),
              Automovel("Verde", "Fiat Mobi", "Hatch", "PQR-1234", 2021, 350),
              Automovel("Amarelo", "Fiat Argo", "Hatch", "STU-5678", 2021, 400),
              Automovel("Rosa", "Fiat Cronos", "Sedan", "VWX-9012", 2021, 450),
              Automovel("Roxo", "Fiat Fiorino", "Pickup", "YZA-3456", 2021, 500),
              Automovel("Laranja", "Fiat Ducato", "Pickup", "BCD-7890", 2021, 550),
              Automovel("Marrom", "Fiat Ducato", "Pickup", "EFG-1234", 2021, 600)]

for automovel in automoveis:
    locadora.add_automovel(automovel)

logado = False
rodando = True

while rodando:
    
    while not logado:
        decisao = input("Você deseja:\n1 - Logar\n2 - Cadastrar\n")
        if decisao == "1":
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            cliente = locadora.autenticar_cliente(email, senha)
            if cliente is not None:
                logado = True
                print("Bom te ver novamente {}! Logado com sucesso.".format(cliente.get_nome()))
            else:
                print("Email ou senha incorretos.")
                
        elif decisao == "2":
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            telefone = input("Digite seu telefone: ")
            cep = input("Digite seu CEP: ")
            cliente = Cliente(email, senha, nome, cpf, telefone, cep)
            locadora.add_cliente(cliente)
            logado = True
            print("Cliente cadastrado com sucesso!")
        



















        
    


              

              