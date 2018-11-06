from Model.Core import Core

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

    def gerenciar_disciplinas(self):
        disciplinas = self.core.carregar_nomes_disciplinas()

        if disciplinas == False:
            print("Erro ao obter disciplinas")
        else:
            self.interface.criar_gerenciar_disciplinas(disciplinas)

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
        self.core.criar_curso(nome)

    def atualizar_curso(self, nome):
        self.core.atualizar_curso(nome)

    def excluir_curso(self, nome):
        if self.core.excluir_curso(nome):
            self.interface.setar_mensagem_status("Curso excluído com sucesso!")

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
        self.core.gerar_horario_csv(r'C:\Users\Ian\UFRGS\EngSoft\teste.csv')
        
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


