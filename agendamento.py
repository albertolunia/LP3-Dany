class Agendamento:
    def __init__(self, nome, data, hora_inicio, duracao, participantes):
        self.__nome = nome
        self.__data = data
        self.__hora_inicio = hora_inicio
        self.__duracao = duracao
        self.__participantes = participantes

    def mostra_agendamento(self):
        print(f'Agendamento\nNome: {self.__nome}\nData: {self.__data}\nHora Inicial: {self.__hora_inicio}\nDuração: {self.__duracao}\nParticipantes: {self.__participantes}')

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def hora_inicio(self):
        return self.__hora_inicio

    @nome.setter
    def hora_inicio(self, value):
        self.__hora_inicio = value

    @property
    def duracao(self):
        return self.__duracao

    @nome.setter
    def duracao(self, value):
        self.__duracao = value

    @property
    def participantes(self):
        return self.__participantes

    @nome.setter
    def participantes(self, value):
        self.__participantes = value

agendamento1 = Agendamento('Alberto', '14/02/1999', '14:00', '02:00', 4)
agendamento1.mostra_agendamento()
