from dao.usuario_dao import Usuario_DAO
from dao.disciplina_dao import Disciplina_DAO
from dao.curso_dao import Curso_DAO

class DAO(object):
    def autenticar_login(self, usuario, senha):
        # Autentica Login
        usuario_dao = Usuario_DAO()

        sucesso, curso_id = usuario_dao.autenticar_login(usuario, senha)

        if not(sucesso):
            return False, None

        # Carrega todos as disciplinas do curso
        disciplina_dao = Disciplina_DAO()
        disciplinas = disciplina_dao.obter_disciplinas_curso(curso_id)

        # Carrega curso do usuário
        curso_dao = Curso_DAO()
        curso = curso_dao.obter_curso_id(curso_id, disciplinas)

        # Cria objeto usuário
        usuario = usuario_dao.obter_usuario_user(usuario, disciplinas, curso)

        return True, (disciplinas, usuario)

    def atualizar_usuario(self, usuario):
        dao_usuario = Usuario_DAO()

        return dao_usuario.atualizar(usuario)

    def carregar_nomes_cursos(self):
        dao_curso = Curso_DAO()
        return dao_curso.obter_nome_cursos()

    def verificar_usuario_unico(self, usuario):
        usuario_dao = Usuario_DAO()
        return usuario_dao.existe_usuario(usuario)

    def verificar_cartao_unico(self, cartao_aluno):
        usuario_dao = Usuario_DAO()
        return usuario_dao.existe_cartao(cartao_aluno)

    def criar_conta(self, senha, usuario, nome, cartao_aluno, curso, privilegio):
        usuario_dao = Usuario_DAO()
        curso_dao = Curso_DAO()
        curso_id = curso_dao.obter_id_curso(curso)

        if curso_id == False:
            return False
        else:
            return usuario_dao.criar(senha, usuario, nome, cartao_aluno, curso_id, privilegio)