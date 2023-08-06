import re
from datetime import datetime

from models.cliente import Cliente
from models.ordem import Ordem
from repository.banco_de_dados import BancoDeDados
from repository.cliente_server import ClienteServer


class OrdemServer:
    def __init__(self, ordem: Ordem):
        self.ordem = ordem

    def inserir_ordem(self):
        bd = BancoDeDados()

        insert_query = ("INSERT INTO public.ordem(nome, ticket, valor_compra, quantidade_compra, data_compra, "
                        "cliente_id) VALUES (%s, %s, %s, %s, %s, %s)")

        values = (
            self.ordem.nome,
            self.ordem.ticket,
            self.ordem.valor_compra,
            self.ordem.quantidade_compra,
            self.ordem.data_compra,
            self.ordem.id_cliente
        )

        try:
            bd.cursor.execute(insert_query, values)
            bd.connection.commit()
        except Exception as e:
            return print("Falha ao Inserir:", e)

    def listar_ordem(self):
        bd = BancoDeDados()

        select_query = "SELECT * FROM public.ordem WHERE cliente_id = %s"
        values = (
            self.ordem.id_cliente
        )

        try:
            bd.cursor.execute(select_query, (values,))

            ordem = bd.cursor.fetchall()

            return ordem
        except Exception as e:
            return print("Falha ao Buscar:", e)

    def alterar_ordem(self, ticket):
        bd = BancoDeDados()

        update_query = ("UPDATE public.ordem"
                        " SET nome=%s, ticket=%s, valor_compra=%s, quantidade_compra=%s, data_compra=%s "
                        "WHERE ticket = %s AND cliente_id = %s")
        values = (
            self.ordem.nome,
            self.ordem.ticket,
            self.ordem.valor_compra,
            self.ordem.quantidade_compra,
            self.ordem.data_compra,
            ticket,
            self.ordem.id_cliente
        )

        try:
            bd.cursor.execute(update_query, values)
            bd.connection.commit()

        except Exception as e:
            return print("Falha ao Alterar:", e)

    def deletar_ordem(self):
        bd = BancoDeDados()

        delete_query = "DELETE FROM public.ordem WHERE ticket = %s AND cliente_id = %s"
        values = (
            self.ordem.ticket,
            self.ordem.id_cliente
        )

        try:
            bd.cursor.execute(delete_query, values)
            bd.connection.commit()

        except Exception as e:
            return print("Falha ao Deletar:", e)

    def busca_ordem(self):
        bd = BancoDeDados()

        buscar_query = "SELECT * FROM public.ordem WHERE ticket = %s AND cliente_id = %s"
        values = (
            self.ordem.ticket,
            self.ordem.id_cliente
        )

        try:
            bd.cursor.execute(buscar_query, values)

            ordem = bd.cursor.fetchall()

            if ordem:
                self.ordem.nome = ordem[0][1]
                self.ordem.ticket = ordem[0][2]
                self.ordem.valor_compra = ordem[0][3]
                self.ordem.quantidade_compra = ordem[0][4]
                self.ordem.data_compra = datetime.strptime(str(ordem[0][5]), '%Y-%m-%d').strftime('%d/%m/%Y')
                self.ordem.id_cliente = ordem[0][6]

                return self.ordem
            else:
                return ordem

        except Exception as e:
            return print("Falha ao Buscar id:", e)

    def lista_ordem_cliente(self, cpf):
        bd = BancoDeDados()

        buscar_query = ("SELECT ordem.* FROM cliente INNER JOIN ordem ON cliente.id = ordem.cliente_id "
                        "WHERE cliente.CPF = %s")
        values = (
            cpf
        )

        try:
            bd.cursor.execute(buscar_query, (values,))

            ordem = bd.cursor.fetchall()

            return ordem

        except Exception as e:
            return print("Falha ao Buscar id:", e)

