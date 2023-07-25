def retorna_menu_principal():
    retorno = input("Deseja retornar ao menu principal? (sim/não) ")
    global validador
    if retorno == "sim":
        validador = True
    else:
        validador = False


def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado