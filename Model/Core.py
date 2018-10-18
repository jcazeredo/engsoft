from Dao.Curso import CursoDao
from Dao.Disciplina import DisciplinaDao
from Dao.Usuario import UsuarioDao
from Model.Associacoes.DisciplinaCurso import DisciplinaCurso
from Model.Associacoes.UsuarioDisciplina import UsuarioDisciplina
from Model.Objetos.Curso import Curso
from Model.Objetos.Usuario import Usuario
from Model.Objetos.Disciplina import Disciplina


class Core(object):
    def __init__(self):
        self.__logado = False
        self.__usuario_logado = None

    def autenticar_login(self, cartao_aluno, senha):
        """ Verifica se o login é válido """
        user_dao = UsuarioDao()
        usuario = user_dao.autenticar_login(cartao_aluno, senha)

        if not usuario:
            return False
        self.__usuario_logado = usuario
        self.__logado = True

        return self.carregar_dados_login(usuario)

    def carregar_dados_login(self, usuario):
        # Carrega Curso
        curso_dao = CursoDao()
        curso_id = usuario.curso_id
        curso = curso_dao.obter_curso_id(curso_id)

        if not curso:
            return False

        # Carrega Disciplinas
        disciplina_dao = DisciplinaDao()

        # Recebe lista com as ids de disciplinas cursadas pelo curso
        disciplinas_curso = disciplina_dao.obter_disciplinas_curso(curso_id)

        # Recebe lista com as ids de disciplinas cursadas pelo usuário
        disciplinas_usuario = disciplina_dao.obter_disciplinas_usuario(usuario.id)

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

    def carregar_dados_sidemenu(self):
        nome = self.__usuario_logado.nome
        privilegio = self.__usuario_logado.privilegio

        return nome, privilegio

    def carregar_dados_perfil(self):
        nome = self.__usuario_logado.nome
        senha = self.__usuario_logado.senha
        cartao_aluno = self.__usuario_logado.cartao_aluno
        curso_id = self.__usuario_logado.curso_id
        curso = Curso.obter_curso(curso_id)

        if curso == False:
            curso = self.carregar_curso(curso_id)

        curso = curso.nome

        dados = {
            "nome": nome,
            "senha": senha,
            "cartao_aluno": cartao_aluno,
            "curso": curso
        }

        return dados

    def carregar_curso(self, curso_id):
        curso_dao = CursoDao()
        curso = curso_dao.obter_curso_id(curso_id)

        if not curso:
            return False

        # Carrega Disciplinas
        disciplina_dao = DisciplinaDao()

        # Recebe lista com as ids de disciplinas cursadas pelo curso
        disciplinas_curso = disciplina_dao.obter_disciplinas_curso(curso_id)

        # Criar Associações Disciplinas-Cursos
        for disciplina in disciplinas_curso:
            associacao = DisciplinaCurso(curso_id, disciplina)
            curso.adicionar_disciplina(disciplina, associacao)
            disciplina_obj = Disciplina.obter_disciplina(disciplina)
            disciplina_obj.adicionar_curso(curso_id, associacao)
        return curso

    def carregar_dados_usuario(self, cartao_aluno):
        usuario_dao = UsuarioDao()
        usuario_obj = usuario_dao.obter_usuario(cartao_aluno)

        nome = usuario_obj.nome
        senha = usuario_obj.senha
        cartao_aluno = usuario_obj.cartao_aluno
        curso_id = usuario_obj.curso_id
        if curso_id == 0:
            curso = "Nenhum"
        else:
            curso = Curso.obter_curso(curso_id).nome

        dados = {
            "nome": nome,
            "senha": senha,
            "cartao_aluno": cartao_aluno,
            "curso": curso
        }

        return dados

    def excluir_admin(self, cartao_aluno):
        usuario_dao = UsuarioDao()
        id = usuario_dao.obter_id_cartao(cartao_aluno)

        if id != False:
            if Usuario.obter_usuario(id) != False:
                Usuario.remover_usuario(id)
            return usuario_dao.excluir(id)

        return False

    def atualizar_perfil(self, nome, senha, curso):
        curso_dao = CursoDao()
        curso_id = curso_dao.obter_id_curso(curso)
        self.__usuario_logado.nome = nome
        self.__usuario_logado.senha = senha
        self.__usuario_logado.curso_id = curso_id
        usuario_dao = UsuarioDao()

        return usuario_dao.atualizar(self.__usuario_logado)

    def carregar_nomes_cursos(self):
        curso_dao = CursoDao()
        return curso_dao.obter_nome_cursos()

    def carregar_cartoes_admins(self):
        usuario_dao = UsuarioDao()
        return usuario_dao.obter_cartao_admins(self.__usuario_logado.id)

    def verificar_dados_unicos(self, cartao_aluno):
        usuario_dao = UsuarioDao()
        return usuario_dao.existe_cartao(cartao_aluno)

    def criar_conta(self, senha, nome, cartao_aluno, curso, privilegio):
        curso_dao = CursoDao()
        curso_id = curso_dao.obter_id_curso(curso)
        usuario_dao = UsuarioDao()
        return usuario_dao.criar(senha, nome, cartao_aluno, curso_id, privilegio)

    def criar_disciplina(self, nome, semestre):
        disciplina_dao = DisciplinaDao()
        id = disciplina_dao.criar(nome, semestre)
        Disciplina(id, nome, semestre)
        return True

    def obter_id_logado(self):
        return self.__usuario_logado.__id