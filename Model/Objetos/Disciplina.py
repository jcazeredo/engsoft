class Disciplina(object):

    __disciplinas = {}

    def __init__(self, id, nome, semestre, aprovacao):
        self.__id = id
        self.__nome = nome
        self.__semestre = semestre
        self.__aprovacao = aprovacao
        self.__cursos = {}
        self.__usuarios = {}

        Disciplina.__disciplinas[id] = self

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def semestre(self):
        return self.__semestre

    @property
    def aprovacao(self):
        return self.__aprovacao

    @id.setter
    def id(self, valor):
        self.__id = valor

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @semestre.setter
    def semestre(self, valor):
        self.__semestre = valor

    @semestre.setter
    def aprovacao(self, valor):
        self.__aprovacao = valor

    # @staticmethod
    # def obter_disciplinas():
    #     return Disciplina.__disciplinas

    @staticmethod
    def obter_disciplina(disciplina_id):
        if disciplina_id in Disciplina.__disciplinas:
            print(Disciplina.__disciplinas[disciplina_id])
            return Disciplina.__disciplinas[disciplina_id]
        else:
            return False

    @staticmethod
    def remover_disciplina(id):
        try:
            del Disciplina.__disciplinas[id]
            return True
        except:
            return False

    def adicionar_curso(self, curso_id, associacao):
        self.__cursos[curso_id] = associacao

    def adicionar_usuario(self, usuario_id, associacao):
        self.__usuarios[usuario_id] = associacao

