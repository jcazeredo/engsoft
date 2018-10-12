class UsuarioDisciplina(object):
    __associacoes = []

    def __init__(self, disciplina_id, usuario_id):
        self.__disciplina_id = disciplina_id
        self.__usuario_id = usuario_id

        UsuarioDisciplina.__associacoes.append(self)
