class DisciplinaCurso(object):

    def __init__(self, curso_id, disciplina_id):
        self.__curso_id = curso_id
        self.__disciplina_id = disciplina_id

    @property		
    def curso_id(self):
        return self.__curso_id
        
    @property
    def disciplina_id(self):
        return self.__disciplina_id

