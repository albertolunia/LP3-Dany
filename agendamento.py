from math import floor


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
        return f'Dia: {self.__dia}\nMes: {self.__mes}\nAno: {self.__ano}'

    def e_anterior(self, p_data):
        if self.__ano > p_data.ano:
            return 0
        elif self.__ano < p_data.ano:
            return 1
        elif self.__mes > p_data.mes:
            return 0
        elif self.__mes < p_data.mes:
            return 1
        elif self.__dia > p_data.dia:
            return 0
        else:
            return 1

    def quantos_dias_ate(self, p_data):

        dia1 = self.__ano * 365 + self.__mes * 30 + self.__dia

        dia2 = p_data.ano * 365 + p_data.mes * 30 + p_data.dia

        if dia1 < dia2:
            print(f'{dia2 - dia1} dia(s)')
        else:
            print(f'-{dia1 - dia2} dia(s)')

    def qual_dia_da_semana(self):

        dias = ['Sabado', 'Domingo', 'Segunda-Feira', 'Terca-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira']

        dia = self.__dia
        mes = self.__mes
        ano = self.__ano

        if dia < 3:
            mes += 12
            ano -= 1

        aux = dia + (2 * mes) + ((3 * (mes + 1)) / 5) + ano + (ano / 4) - (ano / 100) + (ano / 400) + 2

        DiaDaSemana = floor(aux % 7)

        print(f'Dia da semana: {dias[DiaDaSemana]}')

    def muda_data_para(self):
        pass

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        self.__dia = value

    @property
    def mes(self):
        return self.__mes

    @mes.setter
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
        return f'Hora: {self.horas}\nMinutos: {self.__minutos}\nSegundos: {self.__segundos}'

    def eam(self):
        if self.__horas < 12:
            return 1
        else:
            return 0

    def cronometa(self, value):
        strhoras = value.split(':')
        horas1 = int(strhoras[0]) * 3600 + int(strhoras[1]) * 60 + int(strhoras[2])
        horas2 = self.__horas * 3600 + self.__minutos * 60 + self.__segundos

        if horas1 > horas2:
            return print(f'Tantos {horas1 - horas2} segundos')
        else:
            return print(f'Tantos {horas1 - horas2 + 86400} segundos')

    def adianta_em_segundos(self, value):
        if value >= 3600:
            self.__horas += int(value / 3600)
            resto = value % 3600
            if resto:
                self.__minutos += resto / 60
                resto = resto % 60
                if resto:
                    self.__segundos += resto
        elif value >= 60:
            self.__minutos += int(value / 60)
            resto = value % 60
            if resto:
                self.__segundos += resto
        else:
            self.__segundos += value

        if self.__segundos > 60:
            self.__segundos -= 60
            self.__minutos += 1

        if self.__minutos > 60:
            self.__minutos -= 60
            self.__horas += 1

        if self.__horas > 24:
            self.__horas -= 24

    def muda_hora_para(self):
        pass

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
        return f'Contato\nNome: {self.__nome}\nEmail: {self.__email}\nTelefone: {self.__telefone}'

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
    def email(self, value):
        self.__email = value

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, value):
        self.__telefone = value


class Agendamento:
    def __init__(self, nome, email, telefone, horas, minutos, segundos, dia, mes, ano):
        self.__contato = Contato(nome, email, telefone)
        self.__hora = Hora(horas, minutos, segundos)
        self.__data = Data(dia, mes, ano)

    def mostra_agendamento(self):
        return f'{self.__contato.mostra_contato()}\n{self.__hora.mostra_hora()}\n{self.__data.mostra_data()}'


test = Agendamento('Alberto', 'Albertolunia@gmail.com', '73981079722', '14', '30', '0', '14', '2', '1999')
print(test.mostra_agendamento())
