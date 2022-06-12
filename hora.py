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
