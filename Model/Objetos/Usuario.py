class Usuario(object):

    __usuarios = {}

    def __init__(self, id, nome, senha, cartao_aluno, curso_id, privilegio):
        self.__id = id
        self.__nome = nome
        self.__senha = senha
        self.__cartao_aluno = cartao_aluno
        self.__curso_id = curso_id
        self.__privilegio = privilegio
        self.__disciplinas = {}

        Usuario.__usuarios[cartao_aluno] = self

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

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
    def disciplinas(self):
        return self.__disciplinas

    @id.setter
    def id(self, valor):
        self.__id = valor

    @senha.setter
    def senha(self, valor):
        self.__senha = valor

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @cartao_aluno.setter
    def cartao_aluno(self, valor):
        self.__cartao_aluno = valor

    @curso_id.setter
    def curso_id(self, valor):
        self.__curso_id = valor

    @privilegio.setter
    def privilegio(self, valor):
        self.__privilegio = valor

    def adicionar_disciplina(self, disciplina_id, associacao):
        self.__disciplinas[disciplina_id] = associacao

    @staticmethod
    def obter_usuario(id):
        if id in Usuario.__usuarios:
            return Usuario.__usuarios[id]
        else:
            return False

    @staticmethod
    def remover_usuario(id):
        try:
            del Usuario.__usuarios[id]
            return True
        except:
            return False

    @staticmethod
    def exibir_tudo():
        print(Usuario.__usuarios)
