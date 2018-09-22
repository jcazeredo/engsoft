from controller.controlador import Controlador
from PyQt5 import QtCore, QtGui, QtWidgets
import sip
import sys

class Interface(object):
    def __init__(self, MainWindow):

        self.controlador = Controlador(self)

        # Padrão
        MainWindow.setObjectName("engsoft")
        MainWindow.resize(761, 433)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        # self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        # self.mainToolBar.setObjectName("mainToolBar")
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        # Define Side Menu Frame
        self.sidemenu = QtWidgets.QFrame(self.centralWidget)
        self.sidemenu.setGeometry(QtCore.QRect(0, 0, 161, 411))
        self.sidemenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidemenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidemenu.setObjectName("sidemenu")

        self.mainframe = QtWidgets.QFrame(self.centralWidget)
        self.mainframe.setEnabled(True)
        self.mainframe.setGeometry(QtCore.QRect(160, 0, 601, 411))
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "engsoft"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.atualFrame = ""
        self.criar_login()

    def esconde_frame_atual(self):
        if self.atualFrame == "":
            pass

        elif self.atualFrame == "login":
            self.remover_login()

        elif self.atualFrame == "login2":
            self.login2.setVisible(False)

        self.mainframe.setVisible(False)

    def novo_frame(self, frame_atual):
        self.esconde_frame_atual()
        self.atualFrame = frame_atual



    def criar_login(self):
        self.novo_frame("login")

        self.label_login = QtWidgets.QLabel(self.mainframe)
        self.label_login.setGeometry(QtCore.QRect(70, 150, 41, 21))
        self.label_login.setObjectName("label_login")
        self.label_login.setText("Login:")

        self.label_senha = QtWidgets.QLabel(self.mainframe)
        self.label_senha.setGeometry(QtCore.QRect(70, 180, 41, 21))
        self.label_senha.setObjectName("label_senha")
        self.label_senha.setText("Senha:")

        self.input_login = QtWidgets.QLineEdit(self.mainframe)
        self.input_login.setGeometry(QtCore.QRect(120, 150, 113, 22))
        self.input_login.setObjectName("input_login")

        self.input_senha = QtWidgets.QLineEdit(self.mainframe)
        self.input_senha.setGeometry(QtCore.QRect(120, 180, 113, 22))
        self.input_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_senha.setObjectName("input_senha")

        self.botao_login = QtWidgets.QPushButton(self.mainframe)
        self.botao_login.setGeometry(QtCore.QRect(160, 210, 80, 22))
        self.botao_login.setObjectName("botao_login")
        self.botao_login.setText("Login")

        self.label_mensagem_login = QtWidgets.QLabel(self.mainframe)
        self.label_mensagem_login.setGeometry(QtCore.QRect(70, 240, 231, 21))
        self.label_mensagem_login.setObjectName("label_mensagem_login")
        self.label_mensagem_login.setText("Faça o login ou crie uma nova conta.")

        self.botao_criarConta = QtWidgets.QPushButton(self.mainframe)
        self.botao_criarConta.setGeometry(QtCore.QRect(70, 210, 80, 22))
        self.botao_criarConta.setObjectName("botao_criarConta")
        self.botao_criarConta.setText("Criar Conta")

        self.botao_login.clicked.connect(self.botao_login_pressionado)

        self.mainframe.setVisible(True)

    def remover_login(self):
        sip.delete(self.botao_criarConta)
        self.botao_criarConta = None

        sip.delete(self.label_login)
        self.label_login = None

        sip.delete(self.label_senha)
        self.label_senha = None

        sip.delete(self.input_login)
        self.input_login = None

        sip.delete(self.input_senha)
        self.input_senha = None

        sip.delete(self.label_mensagem_login)
        self.label_mensagem_login = None

        sip.delete(self.botao_login)
        self.botao_login = None

    def pos_login(self):
        self.mainframe.setVisible(True)
        self.setar_mensagem_status("Login efetuado com sucesso!")

    def criar_sidemenu(self, dados):
        self.novo_frame("")
        self.sidemenu.setVisible(False)

        self.logo = QtWidgets.QLabel(self.sidemenu)
        self.logo.setGeometry(QtCore.QRect(50, 20, 59, 14))
        self.logo.setObjectName("logo")
        self.logo.setText("ENGSOFT")

        self.botao_gerenciar_horarios = QtWidgets.QPushButton(self.sidemenu)
        self.botao_gerenciar_horarios.setGeometry(QtCore.QRect(10, 100, 131, 22))
        self.botao_gerenciar_horarios.setObjectName("botao_gerenciar_horarios")
        self.botao_gerenciar_horarios.setText("Gerenciar Horários")

        self.label_boas_vindas = QtWidgets.QLabel(self.sidemenu)
        self.label_boas_vindas.setGeometry(QtCore.QRect(10, 50, 141, 41))
        self.label_boas_vindas.setText("")
        self.label_boas_vindas.setWordWrap(True)
        self.label_boas_vindas.setObjectName("label_boas_vindas")
        self.label_boas_vindas.setText("Bem vindo, " + dados['nome'])

        self.botao_perfil = QtWidgets.QPushButton(self.sidemenu)
        self.botao_perfil.setGeometry(QtCore.QRect(10, 130, 51, 22))
        self.botao_perfil.setObjectName("botao_perfil")
        self.botao_perfil.setText("Perfil")

        if dados['privilegio'] == 0:
            self.label_admin = QtWidgets.QLabel(self.sidemenu)
            self.label_admin.setGeometry(QtCore.QRect(10, 180, 131, 16))
            self.label_admin.setObjectName("label_admin")
            self.label_admin.setText("vc eh admin caraio")

            self.botao_gerenciar_cursos = QtWidgets.QPushButton(self.sidemenu)
            self.botao_gerenciar_cursos.setGeometry(QtCore.QRect(10, 200, 121, 22))
            self.botao_gerenciar_cursos.setObjectName("botao_gerenciar_cursos")
            self.botao_gerenciar_cursos.setText("Gerenciar Cursos")

            self.botao_gerenciar_disciplinas = QtWidgets.QPushButton(self.sidemenu)
            self.botao_gerenciar_disciplinas.setGeometry(QtCore.QRect(10, 230, 141, 22))
            self.botao_gerenciar_disciplinas.setObjectName("botao_gerenciar_disciplinas")
            self.botao_gerenciar_disciplinas.setText("Gerenciar Disciplinas")

            self.botao_gerenciar_admins = QtWidgets.QPushButton(self.sidemenu)
            self.botao_gerenciar_admins.setGeometry(QtCore.QRect(10, 260, 121, 22))
            self.botao_gerenciar_admins.setObjectName("botao_gerenciar_admins")
            self.botao_gerenciar_admins.setText("Gerenciar Admins")

        self.botao_perfil.clicked.connect(self.botao_perfil_pressionado)

        self.sidemenu.setVisible(True)

    def criar_perfil(self, dados, cursos):
        self.novo_frame("perfil")

        self.label_curso = QtWidgets.QLabel(self.mainframe)
        self.label_curso.setGeometry(QtCore.QRect(70, 100, 41, 21))
        self.label_curso.setObjectName("label_curso")
        self.label_curso.setText("Curso:")

        self.botao_atualizar = QtWidgets.QPushButton(self.mainframe)
        self.botao_atualizar.setGeometry(QtCore.QRect(70, 300, 80, 22))
        self.botao_atualizar.setObjectName("botao_atualizar")
        self.botao_atualizar.setText("Atualizar")

        self.label_senha = QtWidgets.QLabel(self.mainframe)
        self.label_senha.setGeometry(QtCore.QRect(70, 150, 41, 21))
        self.label_senha.setObjectName("label_senha")
        self.label_senha.setText("Senha:")

        self.label_nome = QtWidgets.QLabel(self.mainframe)
        self.label_nome.setGeometry(QtCore.QRect(70, 70, 41, 21))
        self.label_nome.setObjectName("label_nome")
        self.label_nome.setText("Nome:")

        self.input_curso = QtWidgets.QListWidget(self.mainframe)
        self.input_curso.setGeometry(QtCore.QRect(120, 100, 256, 41))
        self.input_curso.setObjectName("input_curso")
        self.input_curso.addItems(cursos.keys())
        # to-do: deixar selecionado o curso q ja ta

        self.input_senha = QtWidgets.QLineEdit(self.mainframe)
        self.input_senha.setGeometry(QtCore.QRect(120, 150, 113, 22))
        self.input_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_senha.setObjectName("input_senha")
        self.input_senha.setText(dados["senha"])

        self.input_nome = QtWidgets.QLineEdit(self.mainframe)
        self.input_nome.setGeometry(QtCore.QRect(120, 70, 311, 22))
        self.input_nome.setObjectName("input_nome")
        self.input_nome.setText(dados["nome"])

        self.botao_atualizar.clicked.connect(self.botao_atualizar_pressionado)

        self.mainframe.setVisible(True)

    def botao_atualizar_pressionado(self):
        if len(self.input_curso.selectedItems()) != 0:
            self.controlador.core.atualizar_perfil(self.input_nome.text(), self.input_curso.selectedItems()[0].text(), self.input_senha.text())
        else:
            pass
            self.setar_mensagem_status("Erro! Selecione um curso.")

    def botao_perfil_pressionado(self):
        self.controlador.ver_perfil()

    def botao_login_pressionado(self):
        self.controlador.login(self.input_login.text(), self.input_senha.text())

    def login_error(self):
        self.label_mensagem_login.setText("Dados Inválidos.")
        self.setar_mensagem_status("Dados Inválidos.")

    def setar_mensagem_status(self, mensagem):
        self.statusBar.showMessage(mensagem)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    engsoft = QtWidgets.QMainWindow()
    user_interface = Interface(engsoft)
    engsoft.show()
    sys.exit(app.exec_())
