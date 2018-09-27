from DAO.dao import DAO
from model.usuario import Usuario

class Core(object):
    def __init__(self):
        self.logado = False

    def autenticar_login(self, usuario, senha):
        """ Verifica se o login é válido """
        dao = DAO()

        sucesso, dados = dao.autenticar_login(usuario, senha)

        if sucesso:
            self.logado = True
            self.disciplinas = dados[0]
            self.usuario = dados[1]

            return True

        else:
            return False

    @property
    def obter_dados_usuario(self):
        return self.usuario_logado

    @property
    def obter_cursos(self):
        pass

    def atualizar_perfil(self, nome, senha):
        self.usuario.nome = nome
        self.usuario.senha = senha
        dao = DAO()

        return dao.atualizar_usuario(self.usuario)


