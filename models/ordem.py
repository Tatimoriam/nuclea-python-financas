class Ordem:

    def __init__(self):
        self._nome = None
        self._ticket = None
        self._valor_compra = None
        self._quantidade_compra = None
        self._data_compra = None
        self._id_cliente = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def ticket(self):
        return self._ticket

    @ticket.setter
    def ticket(self, value):
        self._ticket = value

    @property
    def valor_compra(self):
        return self._valor_compra

    @valor_compra.setter
    def valor_compra(self, value):
        self._valor_compra = value

    @property
    def quantidade_compra(self):
        return self._quantidade_compra

    @quantidade_compra.setter
    def quantidade_compra(self, value):
        self._quantidade_compra = value

    @property
    def data_compra(self):
        return self._data_compra

    @data_compra.setter
    def data_compra(self, value):
        self._data_compra = value

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, value):
        self._id_cliente = value
