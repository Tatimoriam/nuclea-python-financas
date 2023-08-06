import unittest
from unittest.mock import patch
from faker import Faker

from main import main
from models.cliente import Cliente
from repository.cliente_server import ClienteServer
from utils.valida_cpf import gera_cpf


class TestStringMethodsCliente(unittest.TestCase):
    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()

    def test_inserir_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        inputs = ["1", "1", nome, cpf, "12.345.678-x", "12/02/2001", "05003060", "45", "6", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = Cliente()
        cliente_esperado.nome = nome
        cliente_esperado.cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        cliente_esperado.rg = "12.345.678-x"
        cliente_esperado.data_nascimento = "12/02/2001"
        cliente_esperado.cep = '05003-060'
        cliente_esperado.logradouro = 'Rua Higino Pellegrini'
        cliente_esperado.complemento = ''
        cliente_esperado.bairro = 'Água Branca'
        cliente_esperado.cidade = 'São Paulo'
        cliente_esperado.estado = 'SP'
        cliente_esperado.numero_residencia = "45"

        cli_server = ClienteServer(cliente_esperado)
        cliente_inserido = cli_server.buscar_cliente()

        self.assertEqual(cliente_inserido, cliente_esperado)

    def test_alterar_cliente(self):
        cpf = "98181820657"
        inputs = ["1", "2", cpf, 'Peter Callahan', cpf, "12.345.678-1", "12/02/2001", "68902016", "45", "6", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = Cliente()
        cliente_esperado.nome = 'Peter Callahan'
        cliente_esperado.cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        cliente_esperado.rg = "12.345.678-1"
        cliente_esperado.data_nascimento = "12/02/2001"
        cliente_esperado.cep = '68902016'
        cliente_esperado.logradouro = 'Avenida Seis de Setembro'
        cliente_esperado.complemento = 'até 240/241"'
        cliente_esperado.bairro = 'Beirol'
        cliente_esperado.cidade = 'Macapá'
        cliente_esperado.estado = 'AP'
        cliente_esperado.numero_residencia = "3"

        cli_server = ClienteServer(cliente_esperado)
        cliente_alterado = cli_server.buscar_cliente()

        self.assertEqual(cliente_alterado, cliente_esperado)

    def test_buscar_cliente(self):
        cpf = "68331293800"
        inputs = ["1", "3", cpf, "voltar", "6", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = Cliente()
        cliente_esperado.nome = 'Rhonda Carpenter'
        cliente_esperado.cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        cliente_esperado.rg = "12.345.678-x"
        cliente_esperado.data_nascimento = "12/02/2001"
        cliente_esperado.cep = '05003-060'
        cliente_esperado.logradouro = 'Rua Higino Pellegrini'
        cliente_esperado.complemento = ''
        cliente_esperado.bairro = 'Água Branca'
        cliente_esperado.cidade = 'São Paulo'
        cliente_esperado.estado = 'SP'
        cliente_esperado.numero_residencia = "42"

        cli_server = ClienteServer(cliente_esperado)
        cliente_existente = cli_server.buscar_cliente()

        self.assertEqual(cliente_existente, cliente_esperado)

    def test_deletar_cliente(self):
        cpf = "981.818.206-57"
        inputs = ["1", "4", cpf, "6", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente = Cliente()
        cliente.cpf = cpf
        cli_server = ClienteServer(cliente)
        resultado = cli_server.buscar_cliente()

        self.assertEqual([], resultado)
