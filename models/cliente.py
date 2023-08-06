from datetime import datetime

class Cliente:

    def __init__(self):
        self._nome = None
        self._cpf = None
        self._rg = None
        self._data_nascimento = None
        self._cep = None
        self._logradouro = None
        self._complemento = None
        self._bairro = None
        self._cidade = None
        self._estado = None
        self._numero_residencia = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, value):
        self._rg = value

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self._data_nascimento = datetime.strptime(value, "%d/%m/%Y").date()

    @property
    def cep(self):
        return self._cep

    @cep.setter
    def cep(self, value):
        self._cep = value

    @property
    def logradouro(self):
        return self._logradouro

    @logradouro.setter
    def logradouro(self, value):
        self._logradouro = value

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, value):
        self._complemento = value

    @property
    def bairro(self):
        return self._bairro

    @bairro.setter
    def bairro(self, value):
        self._bairro = value

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, value):
        self._cidade = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value

    @property
    def numero_residencia(self):
        return self._numero_residencia

    @numero_residencia.setter
    def numero_residencia(self, value):
        self._numero_residencia = value
