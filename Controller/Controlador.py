from Model.Core import Core
import pandas as pd

class Controlador(object):
    def __init__(self, interface):
        self.interface = interface
        self.core = Core()

    def login(self, usuario, senha):
        if self.core.autenticar_login(usuario, senha):
            dados = self.core.carregar_dados_sidemenu()
            nome = dados[0]
            privilegio = dados[1]

            self.interface.criar_sidemenu(nome, privilegio)
            self.interface.pos_login()
        else:
            self.interface.setar_mensagem_login("Dados Inválidos.")

    def gerenciar_admins(self):
        cursos = self.core.carregar_nomes_cursos()
        admins = self.core.carregar_cartoes_admins()

        if cursos == False:
            print("Erro ao obter cursos")
        elif admins == False:
            print("Erro ao obter admins")
        else:
            self.interface.criar_gerenciar_admins(admins, cursos)

    def obter_disciplinas_curso(self, curso):
        return self.core.obter_disciplinas_curso(curso)

    def gerenciar_disciplinas(self):
        disciplinas = self.core.carregar_nomes_disciplinas()

        if disciplinas == False:
            print("Erro ao obter disciplinas")
        else:
            self.interface.criar_gerenciar_disciplinas(disciplinas)

    def gerenciar_cursos(self):
        cursos = self.core.carregar_nomes_cursos()

        if cursos == False:
            print("Erro ao obter cursos")
        else:
            self.interface.criar_gerenciar_cursos(cursos)

    def criar_cadastro(self):
        cursos = self.core.carregar_nomes_cursos()
        if not cursos:
            print("Erro ao obter cursos")
        else:
            self.interface.criar_cadastro(cursos)

    def criar_disciplinas(self, nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta):
        resultado = self.core.criar_disciplina(nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta)
        if resultado:
            self.gerenciar_disciplinas()
            self.interface.setar_mensagem_status("Disciplina adicionada com sucesso!")

    def atualizar_disciplina(self, nome, nome_novo, semestre, aprovacao, segunda, terca, quarta, quinta, sexta):
        if self.core.atualizar_disciplina(nome, nome_novo, semestre, aprovacao, segunda, terca, quarta, quinta, sexta):
            self.interface.setar_mensagem_status("Disciplina Atualizada com Sucesso!")
            self.editar_disciplina(nome_novo)
        else:
            self.interface.setar_mensagem_status("Erro ao atualizar!")

    def excluir_disciplina(self, disciplina):
        if self.core.excluir_disciplina(disciplina):
            self.interface.setar_mensagem_status("Disciplina excluída com sucesso!")
            self.gerenciar_disciplinas()
        else:
            self.interface.setar_mensagem_status("Erro ao excluir disciplina!")

    def criar_curso(self, nome):
        if self.core.criar_curso(nome):
            self.gerenciar_cursos()
            self.interface.setar_mensagem_status("Curso adicionado com sucesso!")

    def atualizar_curso(self, nome, nome_novo):
        if self.core.atualizar_curso(nome, nome_novo):
            self.interface.setar_mensagem_status("Curso Atualizado com Sucesso!")
            self.editar_curso(nome_novo)
        else:
            self.interface.setar_mensagem_status("Erro ao atualizar!")

    def excluir_curso(self, nome):
        if self.core.excluir_curso(nome):
            self.interface.setar_mensagem_status("Curso excluído com sucesso!")
            self.gerenciar_cursos()
        else:
            self.interface.setar_mensagem_status("Erro ao excluir curso!")

    def ver_perfil(self):
        dados = self.core.carregar_dados_perfil()
        cursos = self.core.carregar_nomes_cursos()
        self.interface.criar_perfil(dados, cursos)

    def atualizar_perfil(self, nome, senha, curso):
        if self.core.atualizar_perfil(nome, senha, curso):
            self.interface.setar_mensagem_status("Perfil Atualizado com Sucesso!")
            self.interface.setar_boas_vindas("Bem vindo, " + nome)
            self.ver_perfil()
        else:
            self.interface.setar_mensagem_status("Erro ao atualizar!")

    def gerenciar_horarios(self):
        # TO DO
        # exibir na interface a tabela de horario e permitir exportar como csv
        # self.core.gerar_horarios_csv(id_disciplinas, path_or_buf)
        id_disciplinas = [1,2,3,4,5]
        #horarios = self.core.gerar_horarios(id_disciplinas) # devolve um dataframe
        #self.interface.criar_gerenciar_horarios(horarios)
        path_or_buf = r"C:\Users\Ian\UFRGS\EngSoft\teste.csv"
        self.core.gerar_horarios_csv(id_disciplinas, path_or_buf)		
		
    def atualizar_admin(self, cartao_aluno, nome, senha, curso):
        if self.core.atualizar_admin(cartao_aluno, nome, senha, curso):
            self.interface.setar_mensagem_status("Perfil Atualizado com Sucesso!")
            self.editar_admin(cartao_aluno)
        else:
            self.interface.setar_mensagem_status("Erro ao atualizar!")

    def nova_conta(self, senha, nome, cartao_aluno, curso):
        # Verifica se já existe cartão. Se existir, dá mensagem de erro
        existe_cartao = self.core.verificar_dados_unicos(cartao_aluno)

        if existe_cartao:
            self.interface.setar_mensagem_cadastro("Cartão do Aluno já cadastrado!")

        else:
            # Se não existir, cria nova conta e exibe mensagem de sucesso
            resultado = self.core.criar_conta(senha, nome, cartao_aluno, curso, 1)
            if resultado:
                self.interface.criar_login()
                self.interface.setar_mensagem_login("Cadastro efetuado com sucesso!")

    def novo_admin(self, senha, nome, cartao_aluno, curso):
        # Verifica se já existe cartão. Se existir, dá mensagem de erro
        existe_cartao = self.core.verificar_dados_unicos(cartao_aluno)

        if existe_cartao:
            self.interface.setar_mensagem_status("Cartão do Aluno já cadastrado!")

        else:
            # Se não existir, cria nova conta e exibe mensagem de sucesso
            resultado = self.core.criar_conta(senha, nome, cartao_aluno, curso, 0)
            if resultado:
                self.gerenciar_admins()
                self.interface.setar_mensagem_status("Admin adicionado com sucesso!")

    def excluir_admin(self, admin):
        if self.core.excluir_admin(admin):
            self.interface.setar_mensagem_status("Admin excluído com sucesso!")
            self.gerenciar_admins()
        else:
            self.interface.setar_mensagem_status("Erro ao excluir admin!")

    def editar_admin(self, admin_selecionado):
        dados = self.core.carregar_dados_usuario(admin_selecionado)
        cursos = self.core.carregar_nomes_cursos()
        admins = self.core.carregar_cartoes_admins()

        if cursos == False:
            print("Erro ao obter cursos")
        elif admins == False:
            print("Erro ao obter admins")
        else:
            self.interface.criar_editar_admin(admins, cursos, dados)

    def editar_disciplina(self, disciplina_selecionada):
        dados = self.core.carregar_disciplina(disciplina_selecionada)
        disciplinas = self.core.carregar_nomes_disciplinas()

        if dados == False:
            print("Erro ao obter disciplina")
        elif disciplinas == False:
            print("Erro ao obter disciplinas")
        else:
            self.interface.criar_editar_disciplina(disciplinas, dados)

    def adicionar_disciplinas(self, nome_curso, lista_disciplinas):
        self.core.adicionar_disciplinas(nome_curso, lista_disciplinas)
        self.relacionar_disciplinas(nome_curso)

    def atualizar_historico(self, lista_disciplinas):
        self.core.atualizar_historico(lista_disciplinas)
        self.editar_historico()

    def editar_curso(self, curso_selecionado):
        dados = self.core.carregar_curso_por_nome(curso_selecionado)
        cursos = self.core.carregar_nomes_cursos()

        if dados == False:
            print("Erro ao obter curso")
        elif cursos == False:
            print("Erro ao obter cursos")
        else:
            self.interface.criar_editar_curso(cursos, dados.nome)

    def relacionar_disciplinas(self, curso):
        disciplinas = self.core.carregar_nomes_disciplinas()
        disciplinas_curso = self.core.obter_disciplinas_curso(curso)

        if disciplinas == False:
            print("Erro ao obter disciplinas")
        else:
            self.interface.criar_relacionar_disciplinas(disciplinas, disciplinas_curso)

    def editar_historico(self):
        disciplinas_usuario = self.core.obter_historico_nomes()
        disciplinas_curso = self.core.obter_disciplinas_curso_usuario()

        if disciplinas_curso == False or disciplinas_usuario == False:
            print("Erro ao obter disciplinas")
        else:
            self.interface.criar_historico_disciplinas(disciplinas_usuario, disciplinas_curso)