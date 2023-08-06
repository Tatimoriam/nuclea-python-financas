import unittest
from datetime import datetime
from unittest.mock import patch
from faker import Faker

from main import main
from models.cliente import Cliente
from models.ordem import Ordem
from repository.cliente_server import ClienteServer
from repository.ordem_server import OrdemServer
from utils.valida_cpf import gera_cpf


class TestStringMethodsOrdem(unittest.TestCase):
    def test_inserir_ordem(self):
        cpf = '203.035.130-04'

        inputs = ["2", "1", cpf, "Embraer", "EMBR3", "17.50", "7", "5", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cli = Cliente()
        cli.cpf = cpf
        cli_server = ClienteServer(cli)
        id_cli = cli_server.buscar_id_cliente()

        ord_esperado = Ordem()
        ord_esperado.nome = "Embraer"
        ord_esperado.ticket = "EMBR3"
        ord_esperado.valor_compra = "17.50"
        ord_esperado.quantidade_compra = "7"
        ord_esperado.data_compra = datetime.now().date()
        ord_esperado.id_cliente = id_cli

        ord_cli = OrdemServer(ord_esperado)
        ord_inserida = ord_cli.busca_ordem()

        self.assertEqual(ord_inserida, ord_esperado)

    def test_alterar_ordem(self):
        cpf = '203.035.130-04'

        inputs = ["2", "2", cpf, "EMBR3", "Embraer", "EMBR3", "17.50", "10", "5", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cli = Cliente()
        cli.cpf = cpf
        cli_server = ClienteServer(cli)
        id_cli = cli_server.buscar_id_cliente()

        ord_alterado = Ordem()
        ord_alterado.nome = "Embraer"
        ord_alterado.ticket = "EMBR3"
        ord_alterado.valor_compra = "17.50"
        ord_alterado.quantidade_compra = "10"
        ord_alterado.data_compra = datetime.now().date()
        ord_alterado.id_cliente = id_cli

        ord_cli = OrdemServer(ord_alterado)
        ord_inserida = ord_cli.busca_ordem()

        self.assertEqual(ord_inserida, ord_alterado)

    def test_buscar_ordem(self):
        cpf = '203.035.130-04'

        inputs = ["2", "3", cpf, "Voltar", "5", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cli = Cliente()
        cli.cpf = cpf
        cli_server = ClienteServer(cli)
        id_cli = cli_server.buscar_id_cliente()

        ord_alterado = Ordem()
        ord_alterado.nome = "Embraer"
        ord_alterado.ticket = "EMBR3"
        ord_alterado.valor_compra = "17.50"
        ord_alterado.quantidade_compra = "10"
        ord_alterado.data_compra = datetime.now().date()
        ord_alterado.id_cliente = id_cli

        ord_cli = OrdemServer(ord_alterado)
        ord_inserida = ord_cli.busca_ordem()

        self.assertEqual(ord_inserida, ord_alterado)

    def test_deletar_cliente(self):
        cpf = "20303513004"
        inputs = ["2", "4", cpf, "EMBR3", "5", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente = Cliente()
        cliente.cpf = cpf
        cli_server = ClienteServer(cliente)
        resultado = cli_server.buscar_cliente()

        self.assertEqual([], resultado)
