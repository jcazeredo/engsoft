class UsuarioDisciplina(object):
    def __init__(self, disciplina_id, usuario_id):
        self.__disciplina_id = disciplina_id
        self.__usuario_id = usuario_id

    @property		
    def disciplina_id(self):
        return self.__disciplina_id
        
    @property
    def usuario_id(self):
        return self.__usuario_id