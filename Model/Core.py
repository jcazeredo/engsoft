from Dao.Usuario import UsuarioDao
from Dao.Disciplina import DisciplinaDao
from Dao.Curso import CursoDao
from Model.Objetos.Usuario import Usuario
from Model.Objetos.Disciplina import Disciplina
from Model.Objetos.Curso import Curso
from Model.Associacoes.DisciplinaCurso import DisciplinaCurso
from Model.Associacoes.UsuarioDisciplina import UsuarioDisciplina

class Core(object):
    def __init__(self):
        self.__logado = False
        self.usuario_logado = None
        self.curso = None

    def autenticar_login(self, usuario, senha):
        """ Verifica se o login é válido """
        user_dao = UsuarioDao()
        usuario = user_dao.autenticar_login(usuario, senha)

        if usuario == False:
            return False

        self.usuario_logado = usuario
        self.__logado = True

        return self.carrega_dados_login(usuario)

    def carrega_dados_login(self, usuario):
        # Carrega Curso
        curso_dao = CursoDao()
        curso_id = usuario.curso_id
        curso = curso_dao.obter_curso_id(curso_id)

        if curso == False:
            return False

        # Carrega Disciplinas
        disciplina_dao = DisciplinaDao()

        # Recebe lista com as ids de disciplinas cursadas pelo curso
        disciplinas_curso = disciplina_dao.obter_disciplinas_curso(curso_id)

        # Recebe lista com as ids de disciplinas cursadas pelo usuário
        disciplinas_usuario = disciplina_dao.obter_disciplinas_usuario(usuario.id)

        # Se alguma for False
        if not(disciplinas_curso and disciplinas_usuario):
            print("Erro")
            return

        # Criar Associações Disciplinas-Cursos
        for disciplina in disciplinas_curso:
            associacao = DisciplinaCurso(curso_id, disciplina)
            curso.adicionar_disciplina(disciplina, associacao)
            disciplina_obj = Disciplina.obter_disciplina(disciplina)
            disciplina_obj.adicionar_curso(curso_id, associacao)

        # Criar Associações Disciplinas-Usuarios
        for disciplina in disciplinas_usuario:
            associacao = UsuarioDisciplina(disciplina, usuario.id)
            usuario.adicionar_disciplina(disciplina, associacao)
            disciplina_obj = Disciplina.obter_disciplina(disciplina)
            disciplina_obj.adicionar_usuario(usuario.id, associacao)

        return True

    # @property
    # def obter_cursos(self):
    #     pass
    #
    # def atualizar_perfil(self, nome, senha):
    #     self.usuario.nome = nome
    #     self.usuario.senha = senha
    #     dao = DAO()
    #
    #     return dao.atualizar_usuario(self.usuario)
    #
    # def carregar_nomes_cursos(self):
    #     dao = DAO()
    #     return dao.carregar_nomes_cursos()
    #
    # def verificar_dados_unicos(self, usuario, cartao_aluno):
    #     dao = DAO()
    #     return (dao.verificar_usuario_unico(usuario), dao.verificar_cartao_unico(cartao_aluno))
    #
    # def criar_conta(self, senha, usuario, nome, cartao_aluno, curso, privilegio):
    #     dao = DAO()
    #     return dao.criar_conta(senha, usuario, nome, cartao_aluno, curso, privilegio)
    #

