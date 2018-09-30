from model.core import Core

class Controlador(object):
    def __init__(self, interface):
        self.interface = interface
        self.core = Core()

    def login(self, usuario, senha):
        if self.core.autenticar_login(usuario, senha):
            privilegio = self.core.usuario.privilegio
            nome = self.core.usuario.nome
            self.interface.criar_sidemenu(nome, privilegio)
            self.interface.pos_login()
        else:
            self.interface.login_error()

    def ver_perfil(self):
        nome = self.core.usuario.nome
        senha = self.core.usuario.senha
        self.interface.criar_perfil(nome, senha)

    def atualizar_perfil(self, nome, senha):
        if self.core.atualizar_perfil(nome, senha):
            self.interface.setar_mensagem_status("Perfil Atualizado com Sucesso!")
            self.interface.label_boas_vindas.setText("Bem vindo, " + nome)
        else:
            self.interface.setar_mensagem_status("Erro ao atualizar!")
