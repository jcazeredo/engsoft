class Curso(object):

    __cursos = {}

    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        self.__disciplinas = {}

        Curso.__cursos[id] = self

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @id.setter
    def id(self, valor):
        self.__id = valor

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    def adicionar_disciplina(self, disciplina_id, associacao):
        self.__disciplinas[disciplina_id] = associacao

    @staticmethod
    def obter_curso(curso_id):
        if curso_id in Curso.__cursos:
            return Curso.__cursos[curso_id]
        else:
            return False





