from controller.controlador import Controlador
from PyQt5 import QtCore, QtWidgets
import sip

# View
class Interface(object):
    def __init__(self, MainWindow):
        """
        A interface é composta de dois frames: sidemenu e mainframe. Dentro de cada frame estão os
        elementos (botão, label, input e etc).
        """
        self.controlador = Controlador(self)

        """
        Todos os elementos criados no mainframe são adicionados nessa lista.
        Quando é necessário trocar de layout, é chamada uma função que exclui todos elementos dessa lista
        """
        self.elementos = []

        # Código configuração da janela
        MainWindow.setObjectName("engsoft")
        MainWindow.resize(761, 433)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "engsoft"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        """
        Side Menu é o frame da esquerda, que contêm o menu do usuário (só é ativado quando logado)
        """
        # Define Side Menu Frame
        self.sidemenu = QtWidgets.QFrame(self.centralWidget)
        self.sidemenu.setGeometry(QtCore.QRect(0, 0, 161, 411))
        self.sidemenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidemenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidemenu.setObjectName("sidemenu")

        """
        Main Frame é o frame do meio-direita, é onde ficarão todos os elementos principais do programa.
        Note que esse frame vai alterar seu layout conforme a função que o usuário estiver executando.
        A estratégia para trocar de layout é a seguinte: Criar o layout colocando todos os elementos na lista
        self.elementos, para quando for criar o próximo layout, poder excluir todos os elementos ativos.
        
        Exemplo: criar_login() é a função que cria todos os elementos necessários para fazer o login. Antes
        de começar a adicionar os elementos, é chamada a função novo_frame(), que deleta todos os elementos
        atuais do main frame.
        
        É necessário sempre chamar novo_frame() antes de criar os elementos, e ao terminar, chamar
        self.mainframe.setVisible(True)
        """
        # Define Main Frame
        self.mainframe = QtWidgets.QFrame(self.centralWidget)
        self.mainframe.setEnabled(True)
        self.mainframe.setGeometry(QtCore.QRect(160, 0, 601, 411))
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")

        # Cria o layout login no mainframe
        self.criar_login()

    # Deleta todos os elementos adicionados no main frame
    def novo_frame(self):
        for elemento in self.elementos:
            sip.delete(elemento)
        self.elementos.clear()

        self.mainframe.setVisible(False)

    # Cria elementos do layout login
    def criar_login(self):
        self.novo_frame()

        #1 - Label Login
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 150, 41, 21))
        dummy.setObjectName("label_login")
        dummy.setText("Login:")
        self.elementos.append(dummy)

        #2 - Label Senha
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 180, 41, 21))
        dummy.setObjectName("label_senha")
        dummy.setText("Senha:")
        self.elementos.append(dummy)

        #3 - Input Login
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 150, 113, 22))
        dummy.setObjectName("input_login")
        self.elementos.append(dummy)

        #4 - Input Senha
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 180, 113, 22))
        dummy.setEchoMode(QtWidgets.QLineEdit.Password)
        dummy.setObjectName("input_senha")
        self.elementos.append(dummy)

        #5 - Botao login
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(160, 210, 80, 22))
        dummy.setObjectName("botao_login")
        dummy.setText("Login")
        dummy.clicked.connect(self.botao_login_pressionado)
        self.elementos.append(dummy)

        #6 - Label Mensagem Login
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 240, 231, 21))
        dummy.setObjectName("label_mensagem_login")
        dummy.setText("Faça o login ou crie uma nova conta.")
        self.elementos.append(dummy)

        #7 - Botao Criar Conta
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 210, 80, 22))
        dummy.setObjectName("botao_criarConta")
        dummy.setText("Criar Conta")
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Função chamada após fazer login com sucesso
    def pos_login(self):
        self.mainframe.setVisible(True)
        self.setar_mensagem_status("Login efetuado com sucesso!")

    # Cria elementos do menu lateral esquerdo, baseado no privilegio do usuário logado
    def criar_sidemenu(self, nome, privilegio):
        self.novo_frame()
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
        self.label_boas_vindas.setText("Bem vindo, " + nome)

        self.botao_perfil = QtWidgets.QPushButton(self.sidemenu)
        self.botao_perfil.setGeometry(QtCore.QRect(10, 130, 51, 22))
        self.botao_perfil.setObjectName("botao_perfil")
        self.botao_perfil.setText("Perfil")

        if privilegio == 0:
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

    # Cria elementos necessários para fazer login
    def criar_perfil(self, nome, senha):
        self.novo_frame()

        #1
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 140, 80, 22))
        dummy.setObjectName("botao_atualizar")
        dummy.setText("Atualizar")
        dummy.clicked.connect(self.botao_atualizar_pressionado)
        self.elementos.append(dummy)

        #2
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 100, 41, 21))
        dummy.setObjectName("label_senha")
        dummy.setText("Senha:")
        self.elementos.append(dummy)

        #3
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 70, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        #4
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 100, 113, 22))
        dummy.setEchoMode(QtWidgets.QLineEdit.Password)
        dummy.setObjectName("input_senha")
        dummy.setText(senha)
        self.elementos.append(dummy)

        #5
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 70, 311, 22))
        dummy.setObjectName("input_nome")
        dummy.setText(nome)
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Função chamada quando o botão atualizar (Layout Perfil) for pressionado
    def botao_atualizar_pressionado(self):
        input_nome = self.elementos[4].text()
        input_senha = self.elementos[3].text()
        self.controlador.atualizar_perfil(input_nome, input_senha)

    # Função chamada quando o botão Ver Perfil (Menu Lateral) for pressionado
    def botao_perfil_pressionado(self):
        self.controlador.ver_perfil()

    # Função chamada quando o botão Login (Layout Login) for pressionado
    def botao_login_pressionado(self):
        self.controlador.login(self.elementos[2].text(), self.elementos[3].text())

    # Exibe erro de login mal sucedido
    def login_error(self):
        self.elementos[5].setText("Dados Inválidos.")
        self.setar_mensagem_status("Dados Inválidos.")

    # Função para setar mensagem na barra de status da janela
    def setar_mensagem_status(self, mensagem):
        self.statusBar.showMessage(mensagem)