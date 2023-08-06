from datetime import datetime

from carteira import analisar_carteira
from models.cliente import Cliente
from models.ordem import Ordem
from relatorio import obter_dados_acao, obter_dados_acao2
from repository.cliente_server import ClienteServer
from repository.ordem_server import OrdemServer
from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg

while True:
    print(
        "Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
    print("1 - Cliente")
    print("2 - Ordem")
    print("3 - Realizar análise da carteira")
    print("4 - Imprimir relatório da carteira")
    print("5 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        while True:
            print("Menu Cliente ")
            print("1 - Cadastrar Cliente")
            print("2 - Alterar Cliente")
            print("3 - Buscar Cliente")
            print("4 - Deletar Cliente")
            print("5 - Listar Clientes")
            print("6 - Voltar ao menu anterior")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                cli = Cliente()

                cli.nome = formata_texto(input("Nome: "))
                cli.cpf = valida_cpf()
                cli.rg = valida_rg()
                cli.data_nascimento = valida_data_nascimento()
                endereco = valida_cep()
                cli.cep = endereco['CEP']
                cli.logradouro = endereco['Logradouro']
                cli.complemento = endereco['Complemento']
                cli.bairro = endereco['Bairro']
                cli.cidade = endereco['Cidade']
                cli.estado = endereco['Estado']
                cli.numero_residencia = input("Número casa: ")

                cliServer = ClienteServer(cli)
                cliServer.inserir_cliente()
                print("Cliente Inserido com sucesso.")
            elif opcao == "2":
                cli = Cliente()
                cli.cpf = valida_cpf()
                cpf = cli.cpf

                cliServer = ClienteServer(cli)
                cli = cliServer.buscar_cliente()

                if cli:
                    print("Nome:", cli.nome)
                    print("CPF:", cli.cpf)
                    print("RG:", cli.rg)
                    print("Data Nascimento:", cli.data_nascimento)
                    print("CEP:", cli.cep)
                    print("Numero casa:", cli.numero_residencia)

                    print("Insira os novos dados: ")

                    cli.nome = formata_texto(input("Nome: "))
                    cli.cpf = valida_cpf()
                    cli.rg = valida_rg()
                    cli.data_nascimento = valida_data_nascimento()
                    endereco = valida_cep()
                    cli.cep = endereco['CEP']
                    cli.logradouro = endereco['Logradouro']
                    cli.complemento = endereco['Complemento']
                    cli.bairro = endereco['Bairro']
                    cli.cidade = endereco['Cidade']
                    cli.estado = endereco['Estado']
                    cli.numero_residencia = input("Número casa: ")

                    cliServer = ClienteServer(cli)
                    cliServer.alterar_cliente(cpf)

                    print("Cliente Alterado com sucesso.")
                else:
                    print("Não há nenhum cliente com este CPF cadastrado.")

            elif opcao == "3":
                cli = Cliente()
                cli.cpf = valida_cpf()

                cliServer = ClienteServer(cli)
                cli = cliServer.buscar_cliente()

                if cli:
                    print("Nome:", cli.nome)
                    print("CPF:", cli.cpf)
                    print("RG:", cli.rg)
                    print("Data Nascimento:", cli.data_nascimento)
                    print("CEP:", cli.cep)
                    print("Numero casa:", cli.numero_residencia)
                else:
                    print("Não há nenhum cliente com este CPF cadastrado.")

                while True:
                    voltar = input("\nDigite 'voltar' para sair ").lower()
                    if voltar == "voltar":
                        break

            elif opcao == "4":
                cli = Cliente()
                cli.cpf = valida_cpf()

                cliServer = ClienteServer(cli)
                cli = cliServer.buscar_cliente()

                if cli:
                    print("Cliente Deletado com sucesso.")
                else:
                    print("Não há nenhum cliente com este CPF cadastrado.")

            elif opcao == "5":
                cli = Cliente()
                cliServer = ClienteServer(cli)

                cli = cliServer.listar_clientes()
                print("Lista de Clientes")
                for cliente in cli:
                    print(cliente)
                print('\n')

                while True:
                    voltar = input("\nDigite 'voltar' para sair ").lower()
                    if voltar == "voltar":
                        break

            elif opcao == "6":
                break
    elif opcao == "2":
        while True:
            print("Menu Ordem ")
            print("1 - Cadastrar Ordem de Compra")
            print("2 - Alterar Ordem Adquirida")
            print("3 - Buscar Ordem Adquirida")
            print("4 - Deletar Ordem Adquirida")
            print("5 - Voltar ao menu anterior")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                cli = Cliente()
                print("Para qual cliente será registrada a ordem?\n")
                cli.cpf = valida_cpf()

                cliServer = ClienteServer(cli)
                idCli = cliServer.buscar_id_cliente()

                if idCli:
                    ord = Ordem()

                    print("Informações da Ação")
                    ord.nome = input("Nome: ")
                    ord.ticket = input("Ticket: ")
                    ord.valor_compra = input("Valor da Compra: ")
                    ord.quantidade_compra = input("Quantidade da Compra: ")
                    ord.data_compra = datetime.now().date()
                    ord.id_cliente = idCli

                    ordServer = OrdemServer(ord)
                    ordServer.inserir_ordem()

                    print("Ordem cadastrada com sucesso.\n")
                else:
                    print("Não há nenhum cliente com este CPF cadastrado.\n")

            elif opcao == "2":
                cli = Cliente()
                print("De quem é a ordem que gostaria de alterar?\n")
                cli.cpf = valida_cpf()

                cliServer = ClienteServer(cli)
                idCli = cliServer.buscar_id_cliente()

                if idCli:
                    ord = Ordem()

                    ord.id_cliente = idCli
                    ord.ticket = input("Informe o nome do Ticket que gostaria de alterar: ")
                    ticket = ord.ticket

                    ordServer = OrdemServer(ord)
                    ord = ordServer.busca_ordem()

                    if ord:
                        print("Nome:", ord.nome)
                        print("Ticket:", ord.ticket)
                        print("Valor da Compra:", ord.valor_compra)
                        print("Quantidade da Compra", ord.quantidade_compra)
                        print("Data da Compra:", ord.valor_compra)

                        print("Insira os novos dados: ")
                        ord.nome = input("Nome: ")
                        ord.ticket = input("Ticket: ")
                        ord.valor_compra = input("Valor da Compra: ")
                        ord.quantidade_compra = input("Quantidade da Compra: ")
                        ord.data_compra = datetime.now().date()

                        ordServer.alterar_ordem(ticket)

                        print("Ordem cadastrada com sucesso.\n")
                    else:
                        print(f"Não há nenhuma ordem da {ticket} cadastrada.\n")
                else:
                    print("Não há nenhum cliente com este CPF cadastrado.\n")

            elif opcao == "3":
                cli = Cliente()
                print("Qual cliente gostaria de verificar as ordens?\n")
                cli.cpf = valida_cpf()

                cliServer = ClienteServer(cli)
                idCli = cliServer.buscar_id_cliente()

                if idCli:
                    ord = Ordem()
                    ord.id_cliente = idCli

                    ordServer = OrdemServer(ord)
                    ordens = ordServer.listar_ordem()

                    if ordens:
                        print("Ordens do Cliente de CPF", cli.cpf)
                        for ordem in ordens:
                            print(ordem)
                    else:
                        print("Nenhuma Ordem encontrada.")
                else:
                    print("Não há nenhum cliente com este CPF cadastrado.\n")

                while True:
                    voltar = input("\nDigite 'voltar' para sair ").lower()
                    if voltar == "voltar":
                        break
            elif opcao == "4":
                cli = Cliente()
                print("De quem é a ordem que gostaria de deletar?\n")
                cli.cpf = valida_cpf()

                cliServer = ClienteServer(cli)
                idCli = cliServer.buscar_id_cliente()

                if idCli:
                    ord = Ordem()

                    ord.id_cliente = idCli
                    ord.ticket = input("Informe o nome do Ticket que gostaria de deletar: ")

                    ordServer = OrdemServer(ord)
                    ord = ordServer.deletar_ordem()

                    print("Ordem deletada com sucesso.\n")

                else:
                    print("Não há nenhum cliente com este CPF cadastrado.\n")

            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == "3":
        cli = Cliente()
        print("De quem é a carteira que gostaria de analisar?")
        cli.cpf = valida_cpf()

        cliServer = ClienteServer(cli)
        idCli = cliServer.buscar_id_cliente()

        if idCli:
            ord = Ordem()
            ord.id_cliente = idCli

            ordServer = OrdemServer(ord)
            ordens = ordServer.listar_ordem()

            if ordens:
                lista_ordem = []

                for ordem in ordens:
                    lista_ordem.append(ordem[2]+".SA")

                analisar_carteira(lista_ordem)
            else:
                print("Nenhuma Ordem encontrada.")
        else:
            print("Não há nenhum cliente com este CPF cadastrado.\n")
    elif opcao == "4":
        while True:
            print("\n1 - Gerar relatório de uma ação específica.")
            print("2 - Gerar relatório de das ações do cliente.")
            print("3 - Voltar ao menu anterior")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                ticket = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
                nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()

                obter_dados_acao(ticket, nome_arquivo)
            if opcao == "2":
                cli = Cliente()
                print("De quem é a carteira que gostaria de gerar o relátorio?")
                cli.cpf = valida_cpf()

                nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()

                cliServer = ClienteServer(cli)
                idCli = cliServer.buscar_id_cliente()

                if idCli:
                    ord = Ordem()
                    ord.id_cliente = idCli

                    ordServer = OrdemServer(ord)
                    ordens = ordServer.listar_ordem()

                    if ordens:
                        lista_ordem = []

                        for ordem in ordens:
                            lista_ordem.append(ordem[2] + ".SA")

                        obter_dados_acao2(lista_ordem, nome_arquivo)
                    else:
                        print("Nenhuma Ordem encontrada.")
                else:
                    print("Não há nenhum cliente com este CPF cadastrado.\n")
            if opcao == "3":
                break
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")

    retornar = input("Deseja retornar ao menu principal? (sim/não) ").lower()
    if retornar == "nao" or retornar == "não":
        break

print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
