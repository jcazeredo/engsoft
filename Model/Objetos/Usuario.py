class Usuario(object):

    def __init__(self, id, nome, usuario, senha, cartao_aluno, curso_id, privilegio):
        self.__id = id
        self.__usuario = usuario
        self.__nome = nome
        self.__senha = senha
        self.__cartao_aluno = cartao_aluno
        self.__curso_id = curso_id
        self.__privilegio = privilegio
        self.__disciplinas = {}

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def usuario(self):
        return self.__usuario

    @property
    def senha(self):
        return self.__senha

    @property
    def cartao_aluno(self):
        return self.__cartao_aluno

    @property
    def curso_id(self):
        return self.__curso_id

    @property
    def privilegio(self):
        return self.__privilegio

    @property
    def disciplinas_cursadas(self):
        return self.__disciplinas_cursadas

    @property
    def disciplinas_cursadas(self):
        return self.__disciplinas_cursadas

    @id.setter
    def id(self, valor):
        self.__id = valor

    @usuario.setter
    def usuario(self, valor):
        self.__usuario = valor

    @senha.setter
    def senha(self, valor):
        self.__senha = valor

    @senha.setter
    def nome(self, valor):
        self.__nome = valor

    @disciplinas_cursadas.setter
    def disciplinas_cursadas(self, valor):
        self.__disciplinas_cursadas = valor

    @cartao_aluno.setter
    def cartao_aluno(self, valor):
        self.__cartao_aluno = valor

    @curso_id.setter
    def curso(self, valor):
        self.__curso_id = valor

    @privilegio.setter
    def privilegio(self, valor):
        self.__privilegio = valor

    def adicionar_disciplina(self, disciplina_id, associacao):
        self.__disciplinas[disciplina_id] = associacao

    # @staticmethod
    # def adiciona(id, usuario):
    #     Usuario.__usuarios[id] = usuario