from cliente import Cliente
from funcionario import Funcionario
from automovel import Automovel
from reserva import Reserva
from locacao import Locacao
from locadora import Locadora
from datetime import *
from random import randint

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
    
    # Essa parte do código é referente ao login do Usuário
    while not logado:
        decisao = input("Você deseja:\n1 - Logar como cliente\n2 - Cadastrar como cliente\n3 - Logar como Funcionario\n4 - Cadastrar como Funcionario\n")
       
        # Logar como cliente
        if decisao == "1":
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")
            cliente = locadora.autenticar_cliente(email, senha)
            if cliente is not None:
                logado = True
                print("\nBom te ver novamente {}! Logado com sucesso.\n".format(cliente.get_nome()))
            else:
                print("\nEmail ou senha incorretos.\n")

        # Cadastrar como cliente       
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
            print("\nCliente cadastrado com sucesso!\n")
        
        # Logar como funcionario       
        elif decisao == "3":
            matricula = input("Digite sua matrícula: ")
            senha = input("Digite sua senha: ")
            funcionario = locadora.autenticar_funcionario(matricula, senha)
            if funcionario is not None:
                logado = True
                print("Bom te ver novamente {}! Logado com sucesso.".format(funcionario.get_nome()))
            else:
                print("Matricula ou senha incorretos.")

        # Cadastrar como funcionario
        elif decisao == "4":
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")
            telefone = input("Digite seu telefone: ")
            cep = input("Digite seu CEP: ")

            # Gerando matricula aleatória
            matricula = 'F'+str(randint(10000, 99999))

            funcionario = Funcionario(matricula, senha, nome, cpf, telefone, cep)
            locadora.add_funcionario(funcionario)
            logado = True
            print("\nFuncionario cadastrado com sucesso!")
            print(f"Matricula: {matricula}")



    # Menu de opções para o usuário
    print()  
    print('-'*35)      
    print('Opções do cliente')
    print('1 - Ver automóveis')
    print('2 - Locar um automóvel')
    print('3 - Reservar um automóvel')
    print('4 - Ver automóveis locados')
    print('5 - Ver automóveis reservados')
    print('6 - Pesquisar preço de locação um automóvel')
    print('7 - Cancelar reserva')
    print('8 - Cancelar locação')
    print("-"*35)
    print('Opções do Funcionário')
    print("-"*35)
    print('9 - Adicionar automóvel ao sistema')
    print('10 - Remover automóvel do sistema')
    print("-"*35)
    print('Opções gerais')
    print('11 - Deslogar')
    print('12 - Encerrar programa')
    print('-'*35)
    acao = int(input('\nDigite a ação a ser tomada: '))
    print()

    # Ver automóveis disponíveis
    if acao == 1:
        for automovel in locadora.get_automoveis():
            print(120*'-')
            if automovel.get_locado() == False and automovel.get_reservado() == False:
                print(f' Placa: {automovel.get_placa()} | Modelo: {automovel.get_modelo()} | Tipo: {automovel.get_tipo()} | Cor: {automovel.get_cor()} | Ano: {automovel.get_ano()} | Valor da diária: {automovel.get_valor_diaria()} -> Disponível')
            else:
                print(f' Placa: {automovel.get_placa()} | Modelo: {automovel.get_modelo()} | Tipo: {automovel.get_tipo()} | Cor: {automovel.get_cor()} | Ano: {automovel.get_ano()} | Valor da diária: {automovel.get_valor_diaria()} -> Não Disponível')


    # Locar um automóvel          
    if acao == 2:
        placa = input("Digite a placa do automóvel que deseja locar: ")
        automovel = locadora.get_automovel(placa)
        if automovel is None:
            print("\nAutomóvel não encontrado.")
            continue
        if automovel.get_locado() == True:
            print("\nAutomóvel já locado.")
            continue

        if automovel.get_reservado() == True:
            print("\nAutomóvel reservado.")
            continue
        else:
            dias = int(input("Digite a quantidade de dias que deseja locar o automóvel: "))
            loc = Locacao()
            loc.set_automovel(automovel)
            loc.set_cpf_cliente(cliente.get_cpf())
            loc.set_data_locacao(datetime.now())
            loc.set_data_devolucao(datetime.now() + timedelta(days=dias))
            loc.locar(cliente.get_cpf(), automovel, dias)
            cliente.add_locacao(loc)
            locadora.add_locacao(loc)
            print("\nAutomóvel {} locado com sucesso na data {} com entrega prevista para {}\nValor {} R$!".format(automovel.get_modelo(), loc.get_data_locacao().strftime("%Y-%m-%d às %H:%M"), loc.get_data_devolucao().strftime("%Y-%m-%d às %H:%M"), loc.get_custo_locacao()))
            automovel.set_locado(True)
    

    # Reservar um automóvel   
    if acao == 3:
        placa = input("Digite a placa do automóvel que deseja reservar: ")
        automovel = locadora.get_automovel(placa)
        if automovel is None:
            print("\nAutomóvel não encontrado.")
            continue
        if automovel.get_reservado() == True:
            print("\nAutomóvel já reservado.")
            continue
        else:
            data = input("Digite a data que deseja reservar o automóvel (dd/mm/aaaa): ")
            res = Reserva()
            res.set_automovel(automovel)
            res.set_cpf_cliente(cliente.get_cpf())
            res.reservar(cliente.get_cpf(), automovel, data)
            cliente.add_reserva(res)
            locadora.add_reserva(res)
            print("\nAutomóvel {} reservado com sucesso para a data {} ".format(automovel.get_modelo(), res.get_data()))
            automovel.set_reservado(True)


    # Ver automóveis locados
    if acao == 4:
        if len(cliente.get_locacoes()) == 0:
            print("\nNenhum automóvel locado.")
        else:
            for locacao in cliente.get_locacoes():
                print(35*'-')
                print(f'Placa: {locacao.get_automovel().get_placa()}\nModelo: {locacao.get_automovel().get_modelo()}\nTipo: {locacao.get_automovel().get_tipo()}\nCor: {locacao.get_automovel().get_cor()}\nAno: {locacao.get_automovel().get_ano()}\nValor da diária: {locacao.get_automovel().get_valor_diaria()} R$\nData de locação: {locacao.get_data_locacao().strftime("%Y-%m-%d às %H:%M")}\nData de devolução: {locacao.get_data_devolucao().strftime("%Y-%m-%d às %H:%M")}\nCusto da locação: {locacao.get_custo_locacao()} R$')
     

    # Ver automóveis reservados      
    if acao == 5:
        if len(cliente.get_reservas()) == 0:
            print("Você não possui reservas.")
        else:
            for reserva in cliente.get_reservas():
                print(35*'-')
                print(f'Placa: {reserva.get_automovel().get_placa()}\nModelo: {reserva.get_automovel().get_modelo()}\nTipo: {reserva.get_automovel().get_tipo()}\nCor: {reserva.get_automovel().get_cor()}\nAno: {reserva.get_automovel().get_ano()}\nValor da diária: {reserva.get_automovel().get_valor_diaria()} R$\nData da reserva: {reserva.get_data()}')
    

    # Pesquisar preço de locação um automóvel
    if acao == 6:
        placa = input("Digite a placa do automóvel que deseja pesquisar: ")
        automovel = locadora.get_automovel(placa)
        if automovel is None:
            print("Automóvel não encontrado.")
            continue
        print("\nValor da diária: {} R$".format(automovel.get_valor_diaria()))
    

    # Cancelar reserva
    if acao == 7:
        placa = input("Digite a placa do automóvel que deseja cancelar a reserva: ")
        automovel = locadora.get_automovel(placa)
        if automovel is None:
            print("\nAutomóvel não encontrado.")
            continue
        if automovel.get_reservado() == False:
            print("\nAutomóvel não reservado.")
            continue
        else:
            for reserva in cliente.get_reservas():
                if reserva.get_automovel().get_placa() == automovel.get_placa():
                    cliente.get_reservas().remove(reserva)
                    locadora.get_reservas().remove(reserva)
                    automovel.set_reservado(False)
                    print("\nReserva cancelada com sucesso!")
                    break


    # Cancelar locação            
    if acao == 8:
        placa = input("Digite a placa do automóvel que deseja cancelar a locação: ")
        automovel = locadora.get_automovel(placa)
        if automovel is None:
            print("\nAutomóvel não encontrado.")
            continue
        if automovel.get_locado() == False:
            print("\nAutomóvel não locado.")
            continue
        else:
            for locacao in cliente.get_locacoes():
                if locacao.get_automovel().get_placa() == automovel.get_placa():
                    cliente.get_locacoes().remove(locacao)
                    locadora.get_locacoes().remove(locacao)
                    automovel.set_locado(False)
                    print("\nLocação cancelada com sucesso!")
                    break
    

    # ações do Funcionário
    if acao in [9, 10]:
        senha = input("Digite a senha: ")
        if senha != "123456":
            print("\nVocê não possui permissão para realizar esta ação.")
            continue
        else:
            # Adicionar automóvel
            if acao == 9:
                placa = input("Digite a placa do automóvel que deseja cadastrar: ")
                modelo = input("Digite o modelo do automóvel: ")
                tipo = input("Digite o tipo do automóvel: ")
                cor = input("Digite a cor do automóvel: ")
                ano = input("Digite o ano do automóvel: ")
                valor_diaria = input("Digite o valor da diária do automóvel: ")
                automovel = Automovel(placa, modelo, tipo, cor, ano, valor_diaria)
                locadora.add_automovel(automovel)
                print("\nAutomóvel cadastrado com sucesso!")
            
            # Remover automóvel
            if acao == 10:
                placa = input("Digite a placa do automóvel que deseja remover: ")
                automovel = locadora.get_automovel(placa)
                if automovel is None:
                    print("\nAutomóvel não encontrado.")
                    continue
                else:
                    locadora.get_automoveis().remove(automovel)
                    print("\nAutomóvel removido com sucesso!")
    
    if acao == 11:
        logado = False
        print("\nVocê saiu da sua conta.")
        continue

    if acao == 12:
        print("\nObrigado por utilizar nossos serviços!")
        rodando = False