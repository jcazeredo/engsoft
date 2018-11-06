class Disciplina(object):

    __disciplinas = {}

    def __init__(self, id, nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta):
        self.__id = id
        self.__nome = nome
        self.__semestre = semestre
        self.__aprovacao = aprovacao
        self.__segunda = segunda
        self.__terca = terca
        self.__quarta = quarta
        self.__quinta = quinta
        self.__sexta = sexta
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

    @property
    def segunda(self):
        return self.__segunda

    @property
    def terca(self):
        return self.__terca

    @property
    def quarta(self):
        return self.__quarta

    @property
    def quinta(self):
        return self.__quinta

    @property
    def sexta(self):
        return self.__sexta

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

    @semestre.setter
    def segunda(self, valor):
        self.__segunda = valor

    @semestre.setter
    def terca(self, valor):
        self.__terca = valor

    @semestre.setter
    def quarta(self, valor):
        self.__quarta = valor

    @semestre.setter
    def quinta(self, valor):
        self.__quinta = valor

    @semestre.setter
    def sexta(self, valor):
        self.__sexta = valor

    # @staticmethod
    # def obter_disciplinas():
    #     return Disciplina.__disciplinas

    @staticmethod
    def obter_disciplina(disciplina_id):
        if disciplina_id in Disciplina.__disciplinas:
            #print(Disciplina.__disciplinas[disciplina_id])
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

    @staticmethod
    def exibir_tudo():
        print(Disciplina.__disciplinas)
