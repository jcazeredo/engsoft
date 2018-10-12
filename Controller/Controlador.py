from Model.Core import Core

class Controlador(object):
    def __init__(self, interface):
        self.interface = interface
        self.core = Core()

    def login(self, usuario, senha):
        if self.core.autenticar_login(usuario, senha):
            privilegio = self.core.usuario_logado.privilegio
            nome = self.core.usuario_logado.nome
            self.interface.criar_sidemenu(nome, privilegio)
            self.interface.pos_login()
        else:
            self.interface.setar_mensagem_login("Dados Inválidos.")

    def ver_perfil(self):
        nome = self.core.usuario.nome
        senha = self.core.usuario.senha
        self.interface.criar_perfil(nome, senha)

    def atualizar_perfil(self, nome, senha):
        if self.core.atualizar_perfil(nome, senha):
            self.interface.setar_mensagem_status("Perfil Atualizado com Sucesso!")
            self.interface.setar_boas_vindas("Bem vindo, " + nome)
        else:
            self.interface.setar_mensagem_status("Erro ao atualizar!")

    def obter_cursos(self):
        cursos = self.core.carregar_nomes_cursos()
        if cursos == False:
            print("Erro")
        else:
            return cursos

    def nova_conta(self, senha, usuario, nome, cartao_aluno, curso):
        # Verifica se já existe usuário e cartão. Se existir, dá mensagem de erro
        tuple_resultado = self.core.verificar_dados_unicos(usuario, cartao_aluno)

        existe_usuario = tuple_resultado[0]
        existe_cartao = tuple_resultado[1]

        if existe_usuario:
            self.interface.setar_mensagem_cadastro("Nome de usuário já cadastrado!")
        elif existe_cartao:
            self.interface.setar_mensagem_cadastro("Cartão do Aluno já cadastrado!")

        else:
            # Se não existir, cria nova conta e exibe mensagem de sucesso
            resultado = self.core.criar_conta(senha, usuario, nome, cartao_aluno, curso, 1)
            if resultado:
                self.interface.criar_login()
                self.interface.setar_mensagem_login("Cadastro efetuado com sucesso!")

