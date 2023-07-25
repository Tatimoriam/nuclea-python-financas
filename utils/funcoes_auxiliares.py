def retorna_menu_principal():
    retorno = input("Deseja retornar ao menu principal? (sim/não) ").lower()
    if retorno == "sim" or retorno == "s":
        retorna_menu = True
    else:
        retorna_menu = False
    return retorna_menu


def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado