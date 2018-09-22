from model.core import Core

class Controlador(object):
    def __init__(self, interface):
        self.interface = interface
        self.core = Core(self)

    def login(self, usuario, senha):
        if self.core.autenticar_login(usuario, senha):
            self.interface.criar_sidemenu(self.core.obter_dados_usuario)
            self.interface.pos_login()
        else:
            self.interface.login_error()

    def ver_perfil(self):
        self.core.obter_cursos
        self.interface.criar_perfil(self.core.obter_dados_usuario, self.core.obter_cursos)

    def atualizar_perfil(self, nome, curso, senha):
        self.core.atualizar_perfil(nome, curso, senha)
        self.interface.setar_mensagem_status("Perfil Atualizado com Sucesso!")
