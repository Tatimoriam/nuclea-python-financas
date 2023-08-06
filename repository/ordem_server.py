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


if __name__ == "__main__":
    cli = Cliente()
    cli.cpf = '757.025.340-00'

    cliServer = ClienteServer(cli)
    idCli = cliServer.buscar_id_cliente()

    ord = Ordem()
    ord.id_cliente = idCli
    ord.ticket = 'DXCO3'
    ordServer = OrdemServer(ord)

    ord = ordServer.busca_ordem()

    ticket = 'ITSA4'

    ord.nome = 'Itaúsa'
    ord.ticket = 'DXCO3'
    ord.valor_compra = '9.35'
    ord.quantidade_compra = 8
    ord.data_compra = datetime.now().date()
    ord.id_cliente = idCli



    # ordServer.alterar_ordem(ticket)
