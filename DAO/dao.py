from DAO.usuarioDAO import UsuarioDAO
from DAO.disciplinaDAO import DisciplinaDAO
from DAO.cursoDAO import CursoDAO

class DAO(object):
    def autenticar_login(self, usuario, senha):
        # Autentica Login
        usuario_dao = UsuarioDAO()

        sucesso, curso_id = usuario_dao.autenticar_login(usuario, senha)

        if not(sucesso):
            return False, None

        # Carrega todos as disciplinas do curso
        disciplina_dao = DisciplinaDAO()
        disciplinas = disciplina_dao.obter_disciplinas_curso(curso_id)

        # Carrega curso do usuário
        curso_dao = CursoDAO()
        curso = curso_dao.obter_curso_id(curso_id, disciplinas)

        # Cria objeto usuário
        usuario = usuario_dao.obter_usuario_user(usuario, disciplinas, curso)

        return True, (disciplinas, usuario)

    def atualizar_usuario(self, usuario):
        dao_usuario = UsuarioDAO()

        return dao_usuario.atualizar(usuario)