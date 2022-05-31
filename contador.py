class Contador:
    def __init__(self, *args):
        self.__valor = args[0]

    def incrementa(self, *args):
        if len(args) == 1:
            self.__valor += args[0]

    def decrementa(self, *args):
        if len(args) == 1:
            self.__valor -= args[0]

    def menor_que(self, value):
        if self.__valor < value:
            return 1

    def menor_ou_igual_que(self, value):
        if self.__valor <= value:
            return 1

    def igual_a(self, value):
        if self.__valor == value:
            return 1

    def maior_ou_igual_que(self, value):
        if self.__valor >= value:
            return 1

    def maior_que(self, value):
        if self.__valor > value:
            return 1

    def diferente_de(self, value):
        if self.__valor != value:
            return 1
