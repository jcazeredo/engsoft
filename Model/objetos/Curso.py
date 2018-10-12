class Curso(object):
    def __init__(self, id, nome, disciplinas):
        self.id = id
        self.nome = nome
        self.disciplinas = disciplinas

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def disciplinas(self):
        return self.__disciplinas

    @id.setter
    def id(self, valor):
        self.__id = valor

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @disciplinas.setter
    def disciplinas(self, valor):
        self.__disciplinas = valor