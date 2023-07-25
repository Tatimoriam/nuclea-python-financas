from validate_docbr import CPF
import re


def valida_cpf(cpf):
    cpf_validador = CPF()

    while True:
        if cpf_validador.validate(cpf):
            cpf = re.sub("\D", "", cpf)
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            return cpf_formatado
        else:
            cpf = input("CPF inválido, digite novamente: ")
