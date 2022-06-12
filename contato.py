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


class Nome:
    def __init__(self, nome):
        self.__nome = nome

    def mostra_nome(self):
        print(f'Nome: {self.__nome}')


class Email:
    def __init__(self, email):
        self.__email = email

    def mostra_email(self):
        print(f'Email: {self.__email}')


class Telefone:
    def __init__(self, telefone):
        self.__telefone = telefone

    def mostra_telefone(self):
        print(f'Nome: {self.__telefone}')
