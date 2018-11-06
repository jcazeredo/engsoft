class DisciplinaCurso(object):

    __associacoes = {}

    def __init__(self, curso_id, disciplina_id):
        self.__curso_id = curso_id
        self.__disciplina_id = disciplina_id

        DisciplinaCurso.__associacoes = self

    @property		
    def curso_id(self):
        return self.__curso_id
        
    @property
    def disciplina_id(self):
        return self.__disciplina_id