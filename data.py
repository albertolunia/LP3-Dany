from math import floor


class Data:
    def __init__(self, *args):
        if len(args) == 3:
            self.__dia = args[0]
            self.__mes = args[1]
            self.__ano = args[2]
        elif len(args) == 2:
            self.__dia = args[0].dia + args[1]
            self.__mes = args[0].mes
            self.__ano = args[0].ano
        elif len(args) == 1:
            self.__dia = args[0].dia
            self.__mes = args[0].mes
            self.__ano = args[0].ano
        else:
            self.__dia = 0
            self.__mes = 0
            self.__ano = 0

    def verificar_data(self):
        if 1 <= self.__dia <= 31 and 1 <= self.__mes <= 12:
            print('Data valida!')
        else:
            print('Data invalida')

    def mostra_data(self):
        print(f'Data\nDia: {self.__dia}\nMes: {self.__mes}\nAno: {self.__ano}')

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

    def muda_data_para(self, *args):
        if len(args) == 3:
            self.__dia = args[0]
            self.__mes = args[1]
            self.__ano = args[2]
        elif len(args) == 2:
            self.__dia = args[0].dia + args[1]
            self.__mes = args[0].mes
            self.__ano = args[0].ano
        elif len(args) == 1:
            self.__dia = args[0].dia
            self.__mes = args[0].mes
            self.__ano = args[0].ano

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


data1 = Data(3, 4, 2022)
data2 = Data(data1)
data3 = Data(data2, 10)

data1.mostra_data()
data2.mostra_data()
data3.mostra_data()

data1.muda_data_para(14, 2, 1999)

data1.mostra_data()
