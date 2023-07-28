import requests

def busca_cep(cep):

    while True:

        if cep.isdigit() and len(cep) == 8:

            try:
                url = f"http://viacep.com.br/ws/{cep}/json"
                response = requests.get(url)
                endereco = response.json()

                if "erro" in endereco:
                    cep = input("CEP inválido. Digite novamente: ")

                else:
                    lista_key = ['ibge', 'gia', 'ddd', 'siafi']
                    [endereco.pop(key) for key in lista_key]
                    return endereco

            except Exception as err:
                print("A consulta retornou um erro: ", err)

        else:
            cep = input("CEP inválido. Informe somente números: ")


#if __name__ == "__main__":
    #busca_cep("00000000")
    #busca_cep("01001000")
