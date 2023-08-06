import re
from datetime import datetime

from models.cliente import Cliente
from repository.banco_de_dados import BancoDeDados


class ClienteServer:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente

    def inserir_cliente(self):
        bd = BancoDeDados()

        insert_query = """
            INSERT INTO public.cliente(nome, cpf, rg, data_nascimento, cep, logradouro, complemento, 
            bairro, cidade, estado, numero_residencia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
        values = (
            self.cliente.nome,
            self.cliente.cpf,
            self.cliente.rg,
            self.cliente.data_nascimento,
            self.cliente.cep,
            self.cliente.logradouro,
            self.cliente.complemento,
            self.cliente.bairro,
            self.cliente.cidade,
            self.cliente.estado,
            self.cliente.numero_residencia
        )

        try:
            bd.cursor.execute(insert_query, values)
            bd.connection.commit()
        except Exception as e:
            return print("Falha ao Inserir:", e)

    def buscar_cliente(self):
        bd = BancoDeDados()

        select_query = "SELECT * FROM public.cliente WHERE cpf = %s"
        values = (
            self.cliente.cpf
        )

        try:
            bd.cursor.execute(select_query, (values,))

            clientes = bd.cursor.fetchall()

            if clientes:
                self.cliente.nome = clientes[0][1]
                self.cliente.cpf = re.sub("[-.]", "", clientes[0][2])
                self.cliente.rg = clientes[0][3]
                self.cliente.data_nascimento = datetime.strptime(str(clientes[0][4]), '%Y-%m-%d').strftime('%d/%m/%Y')
                self.cliente.cep = clientes[0][5]
                self.cliente.logradouro = clientes[0][6]
                self.cliente.complemento = clientes[0][7]
                self.cliente.bairro = clientes[0][8]
                self.cliente.cidade = clientes[0][9]
                self.cliente.estado = clientes[0][10]
                self.cliente.numero_residencia = clientes[0][11]

                return self.cliente
            else:
                return clientes

        except Exception as e:
            return print("Falha ao Buscar:", e)

    def alterar_cliente(self, cpf):
        bd = BancoDeDados()

        update_query = ("UPDATE public.cliente"
                        " SET nome=%s, cpf=%s, rg=%s, data_nascimento=%s, cep=%s, logradouro=%s, complemento=%s, "
                        "bairro=%s, cidade=%s, estado=%s, numero_residencia=%s "
                        "WHERE cpf = %s")
        values = (
            self.cliente.nome,
            self.cliente.cpf,
            self.cliente.rg,
            self.cliente.data_nascimento,
            self.cliente.cep,
            self.cliente.logradouro,
            self.cliente.complemento,
            self.cliente.bairro,
            self.cliente.cidade,
            self.cliente.estado,
            self.cliente.numero_residencia,
            cpf
        )

        try:
            bd.cursor.execute(update_query, values)
            bd.connection.commit()

        except Exception as e:
            return print("Falha ao Alterar:", e)

    def deletar_cliente(self):
        bd = BancoDeDados()

        delete_query = "DELETE FROM public.cliente WHERE cpf = %s;"
        values = (
            self.cliente.cpf
        )

        try:
            bd.cursor.execute(delete_query, (values,))
            bd.connection.commit()

        except Exception as e:
            return print("Falha ao Deletar:", e)

    def listar_clientes(self):
        bd = BancoDeDados()

        listar_query = "SELECT * FROM public.cliente"

        try:
            bd.cursor.execute(listar_query)
            clientes = bd.cursor.fetchall()

            return clientes
        except Exception as e:
            return print("Falha ao Listar:", e)

    def buscar_id_cliente(self):
        bd = BancoDeDados()

        buscar_query = "SELECT id FROM public.cliente WHERE cpf = %s;"
        values = (
            self.cliente.cpf
        )

        try:
            bd.cursor.execute(buscar_query, (values,))

            id_cliente = bd.cursor.fetchone()
            return id_cliente

        except Exception as e:
            return print("Falha ao Buscar id:", e)
