class DisciplinaCurso(object):

    __associacoes = []

    def __init__(self, curso_id, disciplina_id):
        self.__curso_id = curso_id
        self.__disciplina_id = disciplina_id

        DisciplinaCurso.__associacoes.append(self)
