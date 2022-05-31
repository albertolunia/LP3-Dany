class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def verificar_data(self):
        if 1 <= self.__dia <= 31 and 1 <= self.__mes <= 12:
            print('Data valida!')
        else:
            print('Data invalida')

    def mostra_data(self):
        print(f'Data\nDia: {self.__dia}\nMes: {self.__mes}\nAno: {self.__ano}')

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        self.__dia = value

    @property
    def mes(self):
        return self.__mes

    @dia.setter
    def mes(self, value):
        self.__mes = value

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, value):
        self.__ano = value


class Hora:
    def __init__(self, horas, minutos, segundos):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def verificar_hora(self):
        if 0 <= self.horas <= 24 and 0 <= self.minutos <= 60 and 0 <= self.__segundos <= 60:
            print("Hora Valida!")
        else:
            print("Hora Invalida")

    def mostra_hora(self):
        print(f'Hora: {self.__horas}\nMinutos: {self.__minutos}\nSegundos: {self.__segundos}')

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, value):
        self.__horas = value

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, value):
        self.__minutos = value

    @property
    def segundos(self):
        return self.__segundos

    @segundos.setter
    def segundos(self, value):
        self.__segundos = value


class Contato:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def mostra_contato(self):
        print(f'Contato\nNome: {self.__nome}\nEmail: {self.__email}\nTelefone: {self.__telefone}')

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def nome(self, value):
        self.__email = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def nome(self, value):
        self.__telefone = value

class Agendamento:
    def __init__(self, nome, data, hora_inicio, duracao, participantes):
        self.__nome = nome
        self.__data = data
        self.__hora_inicio = hora_inicio
        self.__duracao = duracao
        self.__participantes = participantes

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