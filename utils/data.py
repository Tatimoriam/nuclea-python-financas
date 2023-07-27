from datetime import datetime


def valida_data_nascimento(data_nascimento):
    while True:
        try:
            data_convertida = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("A data de nascimento não pode ser maior que a data atual.")
        except ValueError:
            data_nascimento = input("Data inválida. Digite novamente: ")
