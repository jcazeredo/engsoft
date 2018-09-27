class Disciplina(object):
    def __init__(self, id, nome, semestre):
        self.id = id
        self.nome = nome
        self.semestre = semestre

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def semestre(self):
        return self.__semestre

    @id.setter
    def id(self, valor):
        self.__id = valor

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @semestre.setter
    def semestre(self, valor):
        self.__semestre = valor