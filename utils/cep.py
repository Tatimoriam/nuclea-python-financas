import requests

def busca_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json"
    response = requests.get(url)

    print(response)


if __name__ == "__main__":
    busca_cep("01310930")
