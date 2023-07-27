import re


def valida_rg(rg):
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9X-x]$'

    while True:
        if re.match(padrao_rg, rg):
            rg.upper()
            return rg
        else:
            rg = input("RG inválido, digite novamente: ")
