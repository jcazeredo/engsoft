class Usuario(object):
    def __init__(self, id, nome, usuario, senha, cartao_aluno, curso, disciplinas_cursadas, privilegio):
        self.id = id
        self.usuario = usuario
        self.nome = nome
        self.senha = senha
        self.cartao_aluno = cartao_aluno
        self.curso = curso
        self.disciplinas_cursadas = disciplinas_cursadas
        self.privilegio = privilegio

    @property
    def id(self):
        return self.__id

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
    def curso(self):
        return self.__curso

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

    @disciplinas_cursadas.setter
    def disciplinas_cursadas(self, valor):
        self.__disciplinas_cursadas = valor

    @cartao_aluno.setter
    def cartao_aluno(self, valor):
        self.__cartao_aluno = valor

    @curso.setter
    def curso(self, valor):
        self.__curso = valor

    @privilegio.setter
    def privilegio(self, valor):
        self.__privilegio = valor