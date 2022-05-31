class Hora:
    def __init__(self, *args):
        if len(args) == 3:
            self.__horas = args[0]
            self.__minutos = args[1]
            self.__segundos = args[2]
        elif len(args) == 4:
            self.__horas = args[0].horas + args[1]
            self.__minutos = args[0].minutos + args[2]
            self.__segundos = args[0].segundos + args[3]
        elif len(args) == 1:
            self.__horas = args[0].horas
            self.__minutos = args[0].minutos
            self.__segundos = args[0].segundos
        else:
            self.__horas = 0
            self.__minutos = 0
            self.__segundos = 0

    def verificar_hora(self):
        if 0 <= self.horas <= 24 and 0 <= self.minutos <= 60 and 0 <= self.__segundos <= 60:
            print("Hora Valida!")
        else:
            print("Hora Invalida")

    def mostra_hora(self):
        print(f'Hora: {self.horas}\nMinutos: {self.__minutos}\nSegundos: {self.__segundos}')

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

    def muda_hora_para(self, *args):
        if len(args) == 3:
            self.__horas = args[0]
            self.__minutos = args[1]
            self.__segundos = args[2]
        elif len(args) == 4:
            self.__horas = args[0].horas + args[1]
            self.__minutos = args[0].minutos + args[2]
            self.__segundos = args[0].segundos + args[3]
        elif len(args) == 1:
            self.__horas = args[0].horas
            self.__minutos = args[0].minutos
            self.__segundos = args[0].segundos
        else:
            self.__horas = 0
            self.__minutos = 0
            self.__segundos = 0

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


hora1 = Hora(2, 60, 60)

hora1.verificar_hora()
hora1.mostra_hora()

if hora1.eam():
    print('É AM')
else:
    print('NÃO É AM')

hora1.cronometa('3:1:0')
hora1.adianta_em_segundos(1)
hora1.mostra_hora()

hora2 = Hora(4, 3, 2)
hora2.mostra_hora()

hora3 = Hora(hora2)
hora3.mostra_hora()

hora4 = Hora(hora2, 1, 1, 1)
hora4.mostra_hora()

hora4.muda_hora_para(1, 1, 1)
hora4.mostra_hora()

hora4.muda_hora_para(hora2)
hora4.mostra_hora()

hora4.muda_hora_para(hora2, 1, 1, 1)
hora4.mostra_hora()
