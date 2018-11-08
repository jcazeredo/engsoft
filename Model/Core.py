from Dao.Curso import CursoDao
from Dao.Disciplina import DisciplinaDao
from Dao.Usuario import UsuarioDao
from Model.Associacoes.DisciplinaCurso import DisciplinaCurso
from Model.Associacoes.UsuarioDisciplina import UsuarioDisciplina
from Model.Objetos.Curso import Curso
from Model.Objetos.Usuario import Usuario
from Model.Objetos.Disciplina import Disciplina
from Model.Objetos.Horario import Horario
import os

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

    def obter_disciplinas_usuario(self):
        disciplina_dao = DisciplinaDao()
        disciplinas_usuario = disciplina_dao.obter_disciplinas_usuario(self.__usuario_logado.id)
        return disciplinas_usuario

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

        try:
            # Criar Associações Disciplinas-Usuarios
            for disciplina in disciplinas_usuario:
                associacao = UsuarioDisciplina(disciplina, usuario.id)
                usuario.adicionar_disciplina(disciplina, associacao)
                disciplina_obj = Disciplina.obter_disciplina(disciplina)
                disciplina_obj.adicionar_usuario(usuario.id, associacao)
        except:
            pass

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

    def carregar_disciplina(self, nome):
        disciplina_dao = DisciplinaDao()
        id = disciplina_dao.obter_id_criado(nome)

        # Testa para ver se a disciplina já existe
        disciplina = Disciplina.obter_disciplina(id)

        if disciplina == False:
            disciplina_dao.obter_disciplina_id(id)
            disciplina = Disciplina.obter_disciplina(id)

            if disciplina == False:
                return False

        if disciplina.segunda == 0:
            segunda = "-"
        else:
            segunda = str(disciplina.segunda) + "h"

        if disciplina.terca == 0:
            terca = "-"
        else:
            terca = str(disciplina.terca) + "h"

        if disciplina.quarta == 0:
            quarta = "-"
        else:
            quarta = str(disciplina.quarta) + "h"

        if disciplina.quinta == 0:
            quinta = "-"
        else:
            quinta = str(disciplina.quinta) + "h"

        if disciplina.sexta == 0:
            sexta = "-"
        else:
            sexta = str(disciplina.sexta) + "h"

        dados = {
            "nome": str(nome),
            "semestre": str(disciplina.semestre),
            "aprovacao": disciplina.aprovacao,
            "segunda": segunda,
            "terca": terca,
            "quarta": quarta,
            "quinta": quinta,
            "sexta": sexta
        }

        return dados

    def carregar_curso(self, curso_id):
        # Testa para ver se o curso já existe
        curso = Curso.obter_curso(curso_id)

        if curso != False:
            return curso

        curso_dao = CursoDao()
        curso = curso_dao.obter_curso_id(curso_id)

        if curso == False:
            return False

        # Carrega Disciplinas
        disciplina_dao = DisciplinaDao()

        # Recebe lista com as ids de disciplinas cursadas pelo curso
        disciplinas_curso = disciplina_dao.obter_disciplinas_curso(curso_id)

        if disciplinas_curso == False:
            return curso

        # Criar Associações Disciplinas-Cursos
        for disciplina in disciplinas_curso:
            associacao = DisciplinaCurso(curso_id, disciplina)
            curso.adicionar_disciplina(disciplina, associacao)
            disciplina_obj = Disciplina.obter_disciplina(disciplina)
            disciplina_obj.adicionar_curso(curso_id, associacao)
        return curso

    def carregar_curso_por_nome(self, nome):
        curso_dao = CursoDao()
        curso_id = curso_dao.obter_id_curso(nome)
        # Testa para ver se o curso já existe
        curso = Curso.obter_curso(curso_id)

        if curso != False:
            return curso

        curso = curso_dao.obter_curso_id(curso_id)

        if curso == False:
            return False

        # Carrega Disciplinas
        disciplina_dao = DisciplinaDao()

        # Recebe lista com as ids de disciplinas cursadas pelo curso
        disciplinas_curso = disciplina_dao.obter_disciplinas_curso(curso_id)

        if disciplinas_curso == False:
            return curso

        # Criar Associações Disciplinas-Cursos
        for disciplina in disciplinas_curso:
            associacao = DisciplinaCurso(curso_id, disciplina)
            curso.adicionar_disciplina(disciplina, associacao)
            disciplina_obj = Disciplina.obter_disciplina(disciplina)
            disciplina_obj.adicionar_curso(curso_id, associacao)
        return curso

    def carregar_dados_usuario(self, cartao_aluno):
        usuario_obj = Usuario.obter_usuario(cartao_aluno)
        if usuario_obj == False:
            usuario_dao = UsuarioDao()
            usuario_obj = usuario_dao.obter_usuario(cartao_aluno)

        nome = usuario_obj.nome
        senha = usuario_obj.senha
        curso_id = usuario_obj.curso_id
        if curso_id == 0:
            curso = "Nenhum"
        else:
            curso = Curso.obter_curso(curso_id)
            if curso == False:
                self.carregar_curso(curso_id)
                curso = Curso.obter_curso(curso_id)
                if curso == False:
                    return False

            curso = curso.nome


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
            if Usuario.obter_usuario(cartao_aluno) != False:
                Usuario.remover_usuario(id)
            return usuario_dao.excluir(id)

        return False

    def atualizar_perfil(self, nome, senha, curso):
        # Caso Usuário não possua curso ainda, permite que ele escolha um.
        if self.__usuario_logado.curso_id == 0:
            curso_dao = CursoDao()
            curso_id = curso_dao.obter_id_curso(curso)
            curso_dao.obter_curso_id(curso_id)
            self.__usuario_logado.curso_id = curso_id

        self.__usuario_logado.nome = nome
        self.__usuario_logado.senha = senha

        usuario_dao = UsuarioDao()

        return usuario_dao.atualizar(self.__usuario_logado)

    def atualizar_admin(self, cartao_aluno, nome, senha, curso):
        curso_dao = CursoDao()
        curso_id = curso_dao.obter_id_curso(curso)
        self.carregar_curso(curso_id)
        usuario_obj = Usuario.obter_usuario(cartao_aluno)
        usuario_obj.curso_id = curso_id

        usuario_obj.nome = nome
        usuario_obj.senha = senha

        usuario_dao = UsuarioDao()
        return usuario_dao.atualizar(usuario_obj)

    def carregar_nomes_cursos(self):
        curso_dao = CursoDao()
        return curso_dao.obter_nome_cursos()

    def carregar_nomes_disciplinas(self):
        disciplina_dao = DisciplinaDao()
        return disciplina_dao.obter_nome_disciplinas()

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

    def criar_disciplina(self, nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta):
        disciplina_dao = DisciplinaDao()
        id = disciplina_dao.criar(nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta)
        if id == False:
            return False
        Disciplina(id, nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta)
        return True

    def atualizar_disciplina(self, nome, nome_novo, semestre, aprovacao, segunda, terca, quarta, quinta, sexta):
        disciplina_dao = DisciplinaDao()
        id = disciplina_dao.atualizar(nome, nome_novo, semestre, aprovacao, segunda, terca, quarta, quinta, sexta)

        objeto_disciplina = Disciplina.obter_disciplina(id)
        objeto_disciplina.nome = nome_novo
        objeto_disciplina.semestre = semestre
        objeto_disciplina.aprovacao = aprovacao
        objeto_disciplina.segunda = segunda
        objeto_disciplina.terca = terca
        objeto_disciplina.quarta = quarta
        objeto_disciplina.quinta = quinta
        objeto_disciplina.sexta = sexta
        return True

    def criar_curso(self, nome):
        curso_dao = CursoDao()
        id = curso_dao.criar(nome)
        Curso(id, nome)
        return True

    def atualizar_curso(self, nome, nome_novo):
        curso_dao = CursoDao()
        id = curso_dao.atualizar(nome, nome_novo)
        objeto_curso = Curso.obter_curso(id)
        objeto_curso.nome = nome_novo

        return True

    def adicionar_disciplinas(self, nome_curso, lista_disciplinas):
        curso_dao = CursoDao()
        disciplina_dao = DisciplinaDao()

        lista_id_disciplina = []

        for disciplina in lista_disciplinas:
            id = disciplina_dao.obter_id_criado(disciplina)
            lista_id_disciplina.append(id)

        curso_id = curso_dao.obter_id_curso(nome_curso)
        lista_disciplinas_antiga = disciplina_dao.obter_disciplinas_curso(curso_id)

        adicionar = [e for e in lista_id_disciplina if e not in lista_disciplinas_antiga]
        excluir = [e for e in lista_disciplinas_antiga if e not in lista_id_disciplina]

        curso_dao.atualiza_disciplinas(curso_id, adicionar)
        curso_dao.remover_disciplinas(curso_id, excluir)

    def atualizar_historico(self, lista_disciplinas):
        usuario_dao = UsuarioDao()
        disciplina_dao = DisciplinaDao()

        lista_id_disciplina = []

        for disciplina in lista_disciplinas:
            id = disciplina_dao.obter_id_criado(disciplina)
            lista_id_disciplina.append(id)

        lista_disciplinas_antiga = self.obter_historico()

        adicionar = [e for e in lista_id_disciplina if e not in lista_disciplinas_antiga]
        excluir = [e for e in lista_disciplinas_antiga if e not in lista_id_disciplina]

        usuario_dao.atualiza_disciplinas(self.__usuario_logado.id, adicionar)
        usuario_dao.remover_disciplinas(self.__usuario_logado.id, excluir)

    def obter_disciplinas_restantes(self):
        historico = self.obter_historico_nomes()
        disciplinas_curso = self.obter_disciplinas_curso_usuario()
        restantes = [e for e in disciplinas_curso if e not in historico]

        return restantes

    def obter_historico(self):
        disciplina_dao = DisciplinaDao()
        lista_disciplinas = disciplina_dao.obter_disciplinas_usuario(self.__usuario_logado.id)

        return lista_disciplinas

    def obter_historico_nomes(self):
        disciplina_dao = DisciplinaDao()
        lista_disciplinas = disciplina_dao.obter_disciplinas_usuario(self.__usuario_logado.id)
        lista_nomes = []
        for disciplina in lista_disciplinas:
            nome = disciplina_dao.obter_nome_disciplina(disciplina)
            lista_nomes.append(nome)

        return lista_nomes

    def obter_disciplinas_curso(self, nome):
        curso_dao = CursoDao()
        id = curso_dao.obter_id_curso(nome)
        disciplina_dao = DisciplinaDao()
        lista_disciplinas = disciplina_dao.obter_disciplinas_curso(id)
        lista_nomes = []
        for disciplina in lista_disciplinas:
            nome = disciplina_dao.obter_nome_disciplina(disciplina)
            lista_nomes.append(nome)

        return lista_nomes

    def obter_disciplinas_curso_usuario(self):
        disciplina_dao = DisciplinaDao()
        lista_disciplinas = disciplina_dao.obter_disciplinas_curso(self.__usuario_logado.curso_id)
        lista_nomes = []
        for disciplina in lista_disciplinas:
            nome = disciplina_dao.obter_nome_disciplina(disciplina)
            lista_nomes.append(nome)

        return lista_nomes

    def obter_id_disciplinas_curso_usuario(self):
        disciplina_dao = DisciplinaDao()
        lista_disciplinas = disciplina_dao.obter_disciplinas_curso(self.__usuario_logado.curso_id)

        return lista_disciplinas

    def excluir_curso(self, nome):
        curso_dao = CursoDao()
        id = curso_dao.obter_id_curso(nome)

        if id != False:
            if Curso.obter_curso(id) != False:
                Curso.remover_curso(id)
            curso_dao.excluir(id)
            curso_dao.excluir_dos_usuarios(id)
            return True

        return False

    def excluir_disciplina(self, disciplina):
        disciplina_dao = DisciplinaDao()
        id = disciplina_dao.obter_id_criado(disciplina)
        if id == False:
            return False
        disciplina = Disciplina.obter_disciplina(id)

        if disciplina != False:
            disciplina.remover_disciplina(id)
        disciplina_dao.excluir(id)
        disciplina_dao.excluir_do_historico(id)
        disciplina_dao.excluir_dos_cursos(id)

        return True

    def obter_id_logado(self):
        return self.__usuario_logado.__id

    def gerar_horarios(self, disciplinas):
        disciplina_dao = DisciplinaDao()

        disciplinas_usuario = []
        for disciplina in disciplinas:
            id = disciplina_dao.obter_id_criado(disciplina)
            disciplinas_usuario.append(id)

        # disciplinas_usuario = self.seleciona_horarios(disciplinas_usuario)
        horario = Horario()
        try:
            count_aprovacao_baixa = 0
            aprovacao_media = 0
            aviso_reprovacao = False
            for id in disciplinas_usuario:
                disciplina_aux = Disciplina.obter_disciplina(id)

                aprovacao_media += disciplina_aux.aprovacao
                if disciplina_aux.aprovacao < 40:
                    count_aprovacao_baixa += 1
                if (disciplina_aux.segunda > 0):
                    horario.add_elemento(disciplina_aux.segunda, "segunda", disciplina_aux.nome)
                if (disciplina_aux.terca > 0):
                    horario.add_elemento(disciplina_aux.terca, "terca", disciplina_aux.nome)
                if (disciplina_aux.quarta > 0):
                    horario.add_elemento(disciplina_aux.quarta, "quarta", disciplina_aux.nome)
                if (disciplina_aux.quinta > 0):
                    horario.add_elemento(disciplina_aux.quinta, "quinta", disciplina_aux.nome)
                if (disciplina_aux.sexta > 0):
                    horario.add_elemento(disciplina_aux.sexta, "sexta", disciplina_aux.nome)
        except:
            pass

        aprovacao_media = aprovacao_media / len(disciplinas_usuario)
        self.ultimo_horario = horario
        if count_aprovacao_baixa >= 2:
            aviso_reprovacao = True

        return (horario.dataframe, aviso_reprovacao, aprovacao_media)
				
    def gerar_horarios_csv(self, disciplinas_usuario, path_or_buf):
		# True - certo, False - erro
        # disciplinas_usuario é uma lista com os ids das disciplinas que o usuario vai cursar
        horario = Horario()
        for id in disciplinas_usuario:
            disciplina_aux = Disciplina.obter_disciplina(id)
            if (disciplina_aux.segunda > 0):
                horario.add_elemento(disciplina_aux.segunda, "segunda", disciplina_aux.nome)
            if (disciplina_aux.terca > 0):
                horario.add_elemento(disciplina_aux.terca, "terca", disciplina_aux.nome)
            if (disciplina_aux.quarta > 0):
                horario.add_elemento(disciplina_aux.quarta, "quarta", disciplina_aux.nome)
            if (disciplina_aux.quinta > 0):
                horario.add_elemento(disciplina_aux.quinta, "quinta", disciplina_aux.nome)
            if (disciplina_aux.sexta > 0):
                horario.add_elemento(disciplina_aux.sexta, "sexta", disciplina_aux.nome)
        horario.to_csv(path_or_buf)

    def salvar_csv(self):
        diretorio_atual = os.getcwd() + "/"
        caminho_arquivo = diretorio_atual + "horario_gerado.csv"
        self.ultimo_horario.to_csv(caminho_arquivo)

    # # Remove horários conflitantes
	# def seleciona_horarios(self, disciplinas_id):
    #     pass
    #     # TO-DO
    #     # horarios_ocupados = pd.DataFrame(index=["13h", "15h"], columns=["segunda-feira", "terca-feira"])
    #     # if horarios_ocupados.loc["13h"]["segunda-feira"] is np.nan:
    #     #     xd = 1
    #     # for id in disciplinas_id:
    #     #     disciplina_aux = Disciplina.obter_disciplina(id)