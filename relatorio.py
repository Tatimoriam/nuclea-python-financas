import yfinance as yf


def obter_dados_acao(ticket, nome_arquivo):
    try:
        # Obter os dados da ação usando o Yahoo Finance (B3)
        acao = yf.download(ticket + '.SA', progress=False)

        # Exibir os dados
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatorio da acao: " + ticket + "\n")
            arquivo.write(str(acao.tail()))

        return print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

    except Exception as e:
        return print(f"Erro ao obter dados da ação. Verifique o código da ação e tente novamente. "
                     f"\nDetalhes do erro: {e}")


def obter_dados_acao2(tickets, nome_arquivo):
    try:
        for ticket in tickets:
            acao = yf.download(ticket, progress=False)

            with open(nome_arquivo, 'a') as arquivo:
                arquivo.write("Relatorio da acao: " + ticket + "\n")
                arquivo.write(str(acao.tail()))
                arquivo.write("\n-----------------\n")

        return print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

    except Exception as e:
        return print(f"Erro ao obter dados da ação. Verifique o código da ação e tente novamente. "
                     f"\nDetalhes do erro: {e}")
