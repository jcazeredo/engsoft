from Controller.Controlador import Controlador
from PyQt5 import QtCore, QtWidgets
from Model.Objetos.Disciplina import Disciplina
from Dao.Disciplina import DisciplinaDao
import sip
import pandas as pd


# View
class Interface(object):
    def __init__(self, main_window):

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
        self.temp = None

        # Código configuração da janela
        main_window.setObjectName("engsoft")
        main_window.resize(761, 433)
        self.centralWidget = QtWidgets.QWidget(main_window)
        self.centralWidget.setObjectName("centralWidget")
        main_window.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(main_window)
        self.statusBar.setObjectName("statusBar")
        main_window.setStatusBar(self.statusBar)

        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "engsoft"))
        QtCore.QMetaObject.connectSlotsByName(main_window)

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

        # 1 - Label Cartão do Aluno
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(10, 150, 101, 21))
        dummy.setObjectName("label_cartao_do_aluno")
        dummy.setText("Cartão do Aluno:")
        self.elementos.append(dummy)

        # 2 - Label Senha
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 180, 41, 21))
        dummy.setObjectName("label_senha")
        dummy.setText("Senha:")
        self.elementos.append(dummy)

        # 3 - Input Cartão do Aluno
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 150, 113, 22))
        dummy.setObjectName("input_cartao_do_aluno")
        self.elementos.append(dummy)

        # 4 - Input Senha
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 180, 113, 22))
        dummy.setEchoMode(QtWidgets.QLineEdit.Password)
        dummy.setObjectName("input_senha")
        self.elementos.append(dummy)

        # 5 - Botao login
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(160, 210, 80, 22))
        dummy.setObjectName("login")
        dummy.setText("Login")
        dummy.clicked.connect(self.login_pressionado)
        self.elementos.append(dummy)

        # 6 - Label Mensagem Login
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 240, 231, 21))
        dummy.setObjectName("label_mensagem_login")
        dummy.setText("Faça o login ou crie uma nova conta.")
        self.elementos.append(dummy)

        # 7 - Botao Criar Conta
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 210, 80, 22))
        dummy.setObjectName("criar_conta")
        dummy.setText("Criar Conta")
        dummy.clicked.connect(self.criar_conta_pressionado)
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Função chamada após fazer login com sucesso
    def pos_login(self):
        self.mainframe.setVisible(True)
        self.setar_mensagem_status("Login efetuado com sucesso!")

    def criar_relacionar_disciplinas(self, disciplinas, disciplinas_curso):
        self.novo_frame()

        # 1 - Botão Adicionar Disciplinas
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 340, 141, 22))
        dummy.setObjectName("botao_adicionar_disciplinas")
        dummy.setText("Adicionar Disciplinas")
        dummy.clicked.connect(self.adicionar_disciplinas_pressionado)
        self.elementos.append(dummy)

        # 2 - Botão Voltar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(220, 340, 61, 22))
        dummy.setObjectName("botao_voltar")
        dummy.setText("Voltar")
        dummy.clicked.connect(self.voltar_editar_curso_pressionado)
        self.elementos.append(dummy)

        # 3 - Tabela
        dummy = QtWidgets.QTableWidget(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 40, 231, 281))
        dummy.setObjectName("tableWidget")
        dummy.setColumnCount(1)
        dummy.setRowCount(len(disciplinas))

        item = QtWidgets.QTableWidgetItem()
        item.setText("Disciplinas")
        dummy.setHorizontalHeaderItem(0, item)

        for i in range(len(disciplinas)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(disciplinas[i])
            dummy.setItem(i, 0, item)
            if disciplinas[i] in disciplinas_curso:
                item.setSelected(True)

        dummy.horizontalHeader().setDefaultSectionSize(200)
        self.elementos.append(dummy)

        # 4 - Label Disciplinas
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 20, 81, 16))
        dummy.setObjectName("label_disciplinas")
        dummy.setText("Disciplinas:")
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    def criar_historico_disciplinas(self, disciplinas_curso, disciplinas):
        self.novo_frame()

        # 1 - Botão Adicionar Disciplinas
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 340, 141, 22))
        dummy.setObjectName("botao_adicionar_disciplinas")
        dummy.setText("Adicionar Disciplinas")
        dummy.clicked.connect(self.atualizar_historico_pressionado)
        self.elementos.append(dummy)

        # 2 - Botão Voltar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(220, 340, 61, 22))
        dummy.setObjectName("botao_voltar")
        dummy.setText("Voltar")
        dummy.clicked.connect(self.ver_perfil_pressionado)
        self.elementos.append(dummy)

        # 3 - Tabela
        dummy = QtWidgets.QTableWidget(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 40, 231, 281))
        dummy.setObjectName("tableWidget")
        dummy.setColumnCount(1)
        dummy.setRowCount(len(disciplinas))

        item = QtWidgets.QTableWidgetItem()
        item.setText("Disciplinas")
        dummy.setHorizontalHeaderItem(0, item)

        for i in range(len(disciplinas)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(disciplinas[i])
            dummy.setItem(i, 0, item)
            if disciplinas[i] in disciplinas_curso:
                item.setSelected(True)

        dummy.horizontalHeader().setDefaultSectionSize(200)
        self.elementos.append(dummy)

        # 4 - Label Disciplinas
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 20, 81, 16))
        dummy.setObjectName("label_disciplinas")
        dummy.setText("Disciplinas:")
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Cria elementos do menu lateral esquerdo, baseado no privilegio do usuário logado
    def criar_sidemenu(self, nome, privilegio):
        self.novo_frame()
        self.sidemenu.setVisible(False)

        self.logo = QtWidgets.QLabel(self.sidemenu)
        self.logo.setGeometry(QtCore.QRect(50, 20, 59, 14))
        self.logo.setObjectName("logo")
        self.logo.setText("ENGSOFT")

        self.gerenciar_horarios = QtWidgets.QPushButton(self.sidemenu)
        self.gerenciar_horarios.setGeometry(QtCore.QRect(10, 100, 131, 22))
        self.gerenciar_horarios.setObjectName("gerenciar_horarios")
        self.gerenciar_horarios.clicked.connect(self.gerenciar_horarios_pressionado)
        self.gerenciar_horarios.setText("Gerenciar Horários")

        self.label_boas_vindas = QtWidgets.QLabel(self.sidemenu)
        self.label_boas_vindas.setGeometry(QtCore.QRect(10, 50, 141, 41))
        self.label_boas_vindas.setText("")
        self.label_boas_vindas.setWordWrap(True)
        self.label_boas_vindas.setObjectName("label_boas_vindas")
        self.label_boas_vindas.setText("Bem vindo, " + nome)

        self.perfil = QtWidgets.QPushButton(self.sidemenu)
        self.perfil.setGeometry(QtCore.QRect(10, 130, 51, 22))
        self.perfil.setObjectName("perfil")
        self.perfil.setText("Perfil")

        if privilegio == 0:
            self.label_admin = QtWidgets.QLabel(self.sidemenu)
            self.label_admin.setGeometry(QtCore.QRect(10, 180, 131, 16))
            self.label_admin.setObjectName("label_admin")
            self.label_admin.setText("Administrador")

            self.gerenciar_cursos = QtWidgets.QPushButton(self.sidemenu)
            self.gerenciar_cursos.setGeometry(QtCore.QRect(10, 200, 121, 22))
            self.gerenciar_cursos.setObjectName("gerenciar_cursos")
            self.gerenciar_cursos.clicked.connect(self.gerenciar_cursos_pressionado)
            self.gerenciar_cursos.setText("Gerenciar Cursos")

            self.gerenciar_disciplinas = QtWidgets.QPushButton(self.sidemenu)
            self.gerenciar_disciplinas.setGeometry(QtCore.QRect(10, 230, 141, 22))
            self.gerenciar_disciplinas.setObjectName("gerenciar_disciplinas")
            self.gerenciar_disciplinas.clicked.connect(self.gerenciar_disciplinas_pressionado)
            self.gerenciar_disciplinas.setText("Gerenciar Disciplinas")

            self.gerenciar_admins = QtWidgets.QPushButton(self.sidemenu)
            self.gerenciar_admins.setGeometry(QtCore.QRect(10, 260, 121, 22))
            self.gerenciar_admins.setObjectName("gerenciar_admins")
            self.gerenciar_admins.clicked.connect(self.gerenciar_admins_pressionado)
            self.gerenciar_admins.setText("Gerenciar Admins")


        self.perfil.clicked.connect(self.ver_perfil_pressionado)

        self.sidemenu.setVisible(True)

    # Cria elementos necessários para fazer login
    def criar_perfil(self, dados, cursos):
        self.novo_frame()

        # 1 - Botão Atualizar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 220, 80, 22))
        dummy.setObjectName("atualizar")
        dummy.setText("Atualizar")
        dummy.clicked.connect(self.atualizar_pressionado)
        self.elementos.append(dummy)

        # 2 - Label Senha
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 130, 41, 21))
        dummy.setObjectName("label_senha")
        dummy.setText("Senha:")
        self.elementos.append(dummy)

        # 3 -Label Nome
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 100, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        # 4 - Input Nome
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 100, 311, 22))
        dummy.setObjectName("input_nome")
        dummy.setText(str(dados["nome"]))
        self.elementos.append(dummy)

        # 5 - Input Senha
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 130, 113, 22))
        dummy.setEchoMode(QtWidgets.QLineEdit.Password)
        dummy.setObjectName("input_senha")
        dummy.setText(str(dados["senha"]))
        self.elementos.append(dummy)

        # 6 - Input Cartão Aluno
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(False)
        dummy.setGeometry(QtCore.QRect(120, 160, 113, 22))
        dummy.setObjectName("input_cartao_aluno")
        dummy.setText(str(dados["cartao_aluno"]))
        self.elementos.append(dummy)

        # 7 - Label Cartão do Aluno
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(10, 160, 111, 21))
        dummy.setObjectName("label_cartao_aluno")
        dummy.setText("Cartão do Aluno:")
        self.elementos.append(dummy)

        # 8 - Input Curso
        dummy = QtWidgets.QComboBox(self.mainframe)
        if dados["curso"] == "Nenhum":
            dummy.setEnabled(True)
        else:
            dummy.setEnabled(False)
        dummy.setGeometry(QtCore.QRect(120, 190, 211, 22))
        dummy.setObjectName("input_curso")
        dummy.addItem("Nenhum")
        for curso in cursos:
            dummy.addItem(curso)
        dummy.setCurrentText(dados["curso"])
        self.elementos.append(dummy)

        # 9 - Label Curso
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 190, 41, 21))
        dummy.setObjectName("label_curso")
        dummy.setText("Curso:")
        self.elementos.append(dummy)

        # 10 - Botão Editar Histórico
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(170, 220, 101, 22))
        dummy.setObjectName("editar_historico")
        dummy.setText("Editar Historico")
        dummy.clicked.connect(self.editar_historico_pressionado)
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Cria elementos necessários para criar uma conta
    def criar_cadastro(self, cursos):
        self.novo_frame()

        # 1 - Input Nome
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 150, 231, 22))
        dummy.setObjectName("input_nome")
        self.elementos.append(dummy)

        # 2 - Input Senha
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 180, 113, 22))
        dummy.setEchoMode(QtWidgets.QLineEdit.Password)
        dummy.setObjectName("input_senha")
        self.elementos.append(dummy)

        # 3 - Input Cartão do Aluno
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 210, 113, 22))
        dummy.setObjectName("input_cartao_aluno")
        self.elementos.append(dummy)

        # 4 - Input Curso
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 240, 231, 22))
        dummy.setObjectName("input_curso")
        for curso in cursos:
            dummy.addItem(curso)
        self.elementos.append(dummy)

        # 5 - Label Senha
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 180, 41, 21))
        dummy.setObjectName("label_senha")
        dummy.setText("Senha:")
        self.elementos.append(dummy)

        # 6 - Label Mensagem
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(40, 310, 311, 21))
        dummy.setText("")
        dummy.setObjectName("label_mensagem")
        self.elementos.append(dummy)

        # 7 - Botão Criar Conta
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(270, 280, 80, 22))
        dummy.setObjectName("criar_conta")
        dummy.setText("Criar Conta")
        dummy.clicked.connect(self.nova_conta_pressionado)
        self.elementos.append(dummy)

        # 8 - Label Nome
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 150, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        # 9 - Label Cartão do Aluno
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(30, 210, 81, 21))
        dummy.setObjectName("label_cartao_aluno")
        dummy.setText("Cartão Aluno:")
        self.elementos.append(dummy)

        # 10 - Label Curso
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 240, 41, 21))
        dummy.setObjectName("label_curso")
        dummy.setText("Curso:")
        self.elementos.append(dummy)

        # 11 - Botão Voltar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(210, 280, 51, 22))
        dummy.setObjectName("voltar")
        dummy.setText("Voltar")
        dummy.clicked.connect(self.voltar_cadastro_pressionado)
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Cria layout Gerenciar Admins
    def criar_gerenciar_admins(self, admins, cursos):
        self.novo_frame()

        # 1 - Label Curso
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 220, 41, 21))
        dummy.setObjectName("label_curso")
        dummy.setText("Curso:")
        self.elementos.append(dummy)

        # 2 - Botão Criar Admin
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 260, 91, 22))
        dummy.setObjectName("botao_criarAdmin")
        dummy.setText("Criar Admin")
        dummy.clicked.connect(self.criar_admin_pressionado)
        self.elementos.append(dummy)

        # 3 - Label Admnistradores
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(60, 70, 101, 21))
        dummy.setObjectName("label_administradores")
        dummy.setText("Admnistradores:")
        self.elementos.append(dummy)

        # 4 - Botão Editar Admin
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(220, 90, 61, 22))
        dummy.setObjectName("botao_editarAdmin")
        dummy.setText("Editar")
        dummy.clicked.connect(self.editar_admin_pressionado)
        if len(admins) == 0:
            dummy.setEnabled(False)
        self.elementos.append(dummy)

        # 5 - Botão Excluir Admin
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(290, 90, 61, 22))
        dummy.setObjectName("botao_excluirAdmin")
        dummy.setText("Excluir")
        dummy.clicked.connect(self.excluir_admin_pressionado)
        if len(admins) == 0:
            dummy.setEnabled(False)
        self.elementos.append(dummy)

        # 6 - Label Cartão Aluno
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(20, 130, 111, 21))
        dummy.setObjectName("label_cartao_aluno")
        dummy.setText("Cartão do Aluno:")
        self.elementos.append(dummy)

        # 7 - Label Senha
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 190, 41, 21))
        dummy.setObjectName("label_senha")
        dummy.setText("Senha:")
        self.elementos.append(dummy)

        # 8 - Label Nome
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 160, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        # 9 - Input Cartão Aluno
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(True)
        dummy.setGeometry(QtCore.QRect(130, 130, 113, 22))
        dummy.setObjectName("input_cartao_aluno")
        self.elementos.append(dummy)

        # 10 - Input Nome
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(130, 160, 311, 22))
        dummy.setObjectName("input_nome")
        self.elementos.append(dummy)

        # 11 - Input Senha
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(130, 190, 113, 22))
        dummy.setObjectName("input_senha")
        self.elementos.append(dummy)

        # 12 - Input Curso
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(130, 220, 211, 22))
        dummy.setObjectName("input_curso")
        dummy.addItem("Nenhum")
        for curso in cursos:
            dummy.addItem(curso)
        self.elementos.append(dummy)

        # 13 - Input Admin
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(60, 90, 151, 22))
        dummy.setObjectName("input_admin")
        for admin in admins:
            dummy.addItem(admin)
        # dummy.setCurrentText()
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)


    # Cria layout Gerenciar Disciplinas
    def criar_gerenciar_disciplinas(self, disciplinas):
        self.novo_frame()

        horarios = ["8h", "10h", "13h", "15h", "17h", "19h", "21h"]

        # 1 - Label Nome
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(140, 100, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        # 2 - Label Semestre
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 130, 61, 21))
        dummy.setObjectName("label_semestre")
        dummy.setText("Semestre:")
        self.elementos.append(dummy)

        # 3 - Input Taxa Aprovação
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(True)
        dummy.setGeometry(QtCore.QRect(190, 160, 31, 22))
        dummy.setObjectName("input_taxa_aprovacao")
        self.elementos.append(dummy)

        # 4 - Label Taxa Aprovação
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(40, 160, 151, 21))
        dummy.setObjectName("label_taxa_aprovacao")
        dummy.setText("Taxa de Aprovação (%):")
        self.elementos.append(dummy)

        # 5 - Botão Criar Disciplina
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(50, 330, 101, 22))
        dummy.setObjectName("botao_criarDisciplina")
        dummy.setText("Criar Disciplina")
        dummy.clicked.connect(self.criar_disciplina_pressionado)
        self.elementos.append(dummy)

        # 6 - Label Disciplina
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 40, 71, 21))
        dummy.setObjectName("label_disciplina")
        dummy.setText("Disciplina:")
        self.elementos.append(dummy)

        # 7 - Botão Editar Disciplina
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(240, 60, 61, 22))
        dummy.setObjectName("botao_editarDisciplina")
        dummy.setText("Editar")
        if len(disciplinas) == 0:
            dummy.setEnabled(False)
        dummy.clicked.connect(self.editar_disciplina_pressionado)
        self.elementos.append(dummy)

        # 8 - Botão Excluir Disciplina
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(310, 60, 61, 22))
        dummy.setObjectName("botao_excluirDisciplina")
        dummy.setText("Excluir")
        if len(disciplinas) == 0:
            dummy.setEnabled(False)
        dummy.clicked.connect(self.excluir_disciplina_pressionado)
        self.elementos.append(dummy)

        # 9 - Input Semestre
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 130, 41, 22))
        dummy.setObjectName("input_semestre")
        dummy.addItem("1")
        dummy.addItem("2")
        dummy.addItem("3")
        dummy.addItem("4")
        dummy.addItem("5")
        dummy.addItem("6")
        dummy.addItem("7")
        dummy.addItem("8")
        dummy.addItem("9")
        dummy.addItem("10")
        dummy.addItem("11")
        dummy.addItem("12")
        self.elementos.append(dummy)

        # 10 - Label Horários
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(40, 200, 61, 21))
        dummy.setObjectName("label_horarios")
        dummy.setText("Horários:")
        self.elementos.append(dummy)

        # 11 - Input Segunda
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 230, 51, 22))
        dummy.setObjectName("input_segunda")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        self.elementos.append(dummy)

        # 12 - Label Terça
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(110, 260, 71, 21))
        dummy.setObjectName("label_terca")
        dummy.setText("Terça-feira:")
        self.elementos.append(dummy)

        # 13 - Label Quarta
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(100, 290, 81, 21))
        dummy.setObjectName("label_quarta")
        dummy.setText("Quarta-feira:")
        self.elementos.append(dummy)

        # 14 - Input Terça
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 260, 51, 22))
        dummy.setObjectName("input_terca")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        self.elementos.append(dummy)

        # 15 - Input Quarta
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 290, 51, 22))
        dummy.setObjectName("input_quarta")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        self.elementos.append(dummy)

        # 16 - Input Quinta
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(345, 230, 51, 22))
        dummy.setObjectName("input_quinta")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        self.elementos.append(dummy)

        # 17 - Input Sexta
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(345, 260, 51, 22))
        dummy.setObjectName("input_sexta")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        self.elementos.append(dummy)

        # 18 - Label Quinta
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(260, 230, 81, 21))
        dummy.setObjectName("label_quinta")
        dummy.setText("Quinta-feira:")
        self.elementos.append(dummy)

        # 19 - Label Sexta
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(265, 260, 71, 21))
        dummy.setObjectName("label_sexta")
        dummy.setText("Sexta-feira:")
        self.elementos.append(dummy)

        # 20 - Input Nome
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(True)
        dummy.setGeometry(QtCore.QRect(190, 100, 113, 22))
        dummy.setObjectName("input_nome")
        self.elementos.append(dummy)

        # 21 - Input Disciplina
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 60, 151, 22))
        dummy.setObjectName("input_disciplina")
        for disciplina in disciplinas:
            dummy.addItem(disciplina)
        self.elementos.append(dummy)

        # 22 - Label Segunda
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(90, 230, 91, 21))
        dummy.setObjectName("label_segunda")
        dummy.setText("Segunda-feira:")
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Cria layout Gerenciar Disciplinas
    def criar_editar_disciplina(self, disciplinas, dados):
        self.novo_frame()

        horarios = ["8h", "10h", "13h", "15h", "17h", "19h", "21h"]
        self.temp = dados["nome"]

        # 1 - Label Nome
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(140, 100, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        # 2 - Label Semestre
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(120, 130, 61, 21))
        dummy.setObjectName("label_semestre")
        dummy.setText("Semestre:")
        self.elementos.append(dummy)

        # 3 - Input Taxa Aprovação
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(True)
        dummy.setGeometry(QtCore.QRect(190, 160, 31, 22))
        dummy.setObjectName("input_taxa_aprovacao")
        dummy.setText(str(dados["aprovacao"]))
        self.elementos.append(dummy)

        # 4 - Label Taxa Aprovação
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(40, 160, 151, 21))
        dummy.setObjectName("label_taxa_aprovacao")
        dummy.setText("Taxa de Aprovação (%):")
        self.elementos.append(dummy)

        # 5 - Botão Criar Disciplina
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(50, 330, 121, 22))
        dummy.setObjectName("botao_atualizarDisciplina")
        dummy.setText("Atualizar Disciplina")
        dummy.clicked.connect(self.atualizar_disciplina_pressionado)
        self.elementos.append(dummy)

        # 6 - Label Disciplina
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 40, 71, 21))
        dummy.setObjectName("label_disciplina")
        dummy.setText("Disciplina:")
        self.elementos.append(dummy)

        # 7 - Botão Editar Disciplina
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(240, 60, 61, 22))
        dummy.setObjectName("botao_editarDisciplina")
        dummy.setText("Editar")
        if len(disciplinas) == 0:
            dummy.setEnabled(False)
        dummy.clicked.connect(self.editar_disciplina_pressionado)
        self.elementos.append(dummy)

        # 8 - Botão Excluir Disciplina
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(180, 330, 61, 22))
        dummy.setObjectName("botao_excluirDisciplina")
        dummy.setText("Excluir")
        dummy.clicked.connect(self.excluir_disciplina_pressionado2)
        self.elementos.append(dummy)

        # 9 - Input Semestre
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 130, 41, 22))
        dummy.setObjectName("input_semestre")
        dummy.addItem("1")
        dummy.addItem("2")
        dummy.addItem("3")
        dummy.addItem("4")
        dummy.addItem("5")
        dummy.addItem("6")
        dummy.addItem("7")
        dummy.addItem("8")
        dummy.addItem("9")
        dummy.addItem("10")
        dummy.addItem("11")
        dummy.addItem("12")
        dummy.setCurrentText(dados["semestre"])
        self.elementos.append(dummy)

        # 10 - Label Horários
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(40, 200, 61, 21))
        dummy.setObjectName("label_horarios")
        dummy.setText("Horários:")
        self.elementos.append(dummy)

        # 11 - Input Segunda
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 230, 51, 22))
        dummy.setObjectName("input_segunda")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        dummy.setCurrentText(dados["segunda"])
        self.elementos.append(dummy)

        # 12 - Label Terça
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(110, 260, 71, 21))
        dummy.setObjectName("label_terca")
        dummy.setText("Terça-feira:")
        self.elementos.append(dummy)

        # 13 - Label Quarta
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(100, 290, 81, 21))
        dummy.setObjectName("label_quarta")
        dummy.setText("Quarta-feira:")
        self.elementos.append(dummy)

        # 14 - Input Terça
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 260, 51, 22))
        dummy.setObjectName("input_terca")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        dummy.setCurrentText(dados["terca"])
        self.elementos.append(dummy)

        # 15 - Input Quarta
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 290, 51, 22))
        dummy.setObjectName("input_quarta")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        dummy.setCurrentText(dados["quarta"])
        self.elementos.append(dummy)

        # 16 - Input Quinta
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(345, 230, 51, 22))
        dummy.setObjectName("input_quinta")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        dummy.setCurrentText(dados["quinta"])
        self.elementos.append(dummy)

        # 17 - Input Sexta
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(345, 260, 51, 22))
        dummy.setObjectName("input_sexta")
        dummy.addItem("-")
        for horario in horarios:
            dummy.addItem(horario)
        dummy.setCurrentText(dados["sexta"])
        self.elementos.append(dummy)

        # 18 - Label Quinta
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(260, 230, 81, 21))
        dummy.setObjectName("label_quinta")
        dummy.setText("Quinta-feira:")
        self.elementos.append(dummy)

        # 19 - Label Sexta
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(265, 260, 71, 21))
        dummy.setObjectName("label_sexta")
        dummy.setText("Sexta-feira:")
        self.elementos.append(dummy)

        # 20 - Input Nome
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(True)
        dummy.setGeometry(QtCore.QRect(190, 100, 113, 22))
        dummy.setObjectName("input_nome")
        dummy.setText(dados["nome"])
        self.elementos.append(dummy)

        # 21 - Input Disciplina
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 60, 151, 22))
        dummy.setObjectName("input_disciplina")
        for disciplina in disciplinas:
            dummy.addItem(disciplina)
        dummy.setCurrentText(dados["nome"])
        self.elementos.append(dummy)

        # 22 - Label Segunda
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(90, 230, 91, 21))
        dummy.setObjectName("label_segunda")
        dummy.setText("Segunda-feira:")
        self.elementos.append(dummy)

        # 23 - Botão Voltar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(250, 330, 61, 22))
        dummy.setObjectName("botao_voltar")
        dummy.setText("Voltar")
        dummy.clicked.connect(self.voltar_editar_disciplina_pressionado)
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Cria layout Editar Admin
    def criar_editar_admin(self, admins, cursos, dados):
        self.novo_frame()

        # 1 - Label Curso
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 220, 41, 21))
        dummy.setObjectName("label_curso")
        dummy.setText("Curso:")
        self.elementos.append(dummy)

        # 2 - Botão Atualizar Admin
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 260, 101, 22))
        dummy.setObjectName("botao_atualizarAdmin")
        dummy.setText("Atualizar Admin")
        dummy.clicked.connect(self.atualizar_admin_pressionado)
        self.elementos.append(dummy)

        # 3 - Label Admnistradores
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(60, 70, 101, 21))
        dummy.setObjectName("label_administradores")
        dummy.setText("Admnistradores:")
        self.elementos.append(dummy)

        # 4 - Botão Editar Admin
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(220, 90, 61, 22))
        dummy.setObjectName("botao_editarAdmin")
        dummy.setText("Editar")
        dummy.clicked.connect(self.editar_admin_pressionado)
        self.elementos.append(dummy)

        # 5 - Botão Excluir Admin
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(180, 260, 61, 22))
        dummy.setObjectName("botao_excluirAdmin")
        dummy.setText("Excluir")
        dummy.clicked.connect(self.excluir_admin_pressionado2)
        if len(admins) == 0:
            dummy.setEnabled(False)
        self.elementos.append(dummy)

        # 6 - Botão Voltar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(250, 260, 61, 22))
        dummy.setObjectName("botao_voltar")
        dummy.setText("Voltar")
        dummy.clicked.connect(self.voltar_editar_admin_pressionado)
        self.elementos.append(dummy)

        # 7 - Label Cartão Aluno
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(20, 130, 111, 21))
        dummy.setObjectName("label_cartao_aluno")
        dummy.setText("Cartão do Aluno:")
        self.elementos.append(dummy)

        # 8 - Label Senha
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 190, 41, 21))
        dummy.setObjectName("label_senha")
        dummy.setText("Senha:")
        self.elementos.append(dummy)

        # 9 - Label Nome
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 160, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        # 10 - Input Cartão Aluno
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(False)
        dummy.setGeometry(QtCore.QRect(130, 130, 113, 22))
        dummy.setObjectName("input_cartao_aluno")
        dummy.setText(dados["cartao_aluno"])
        self.elementos.append(dummy)

        # 11 - Input Nome
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(130, 160, 311, 22))
        dummy.setObjectName("input_nome")
        dummy.setText(dados["nome"])
        self.elementos.append(dummy)

        # 12 - Input Senha
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setGeometry(QtCore.QRect(130, 190, 113, 22))
        dummy.setObjectName("input_senha")
        dummy.setText(dados["senha"])
        self.elementos.append(dummy)

        # 13 - Input Curso
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(130, 220, 211, 22))
        dummy.setObjectName("input_curso")
        dummy.addItem("Nenhum")
        for curso in cursos:
            dummy.addItem(curso)
        dummy.setCurrentText(dados["curso"])
        self.elementos.append(dummy)

        # 14 - Input Admin
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(60, 90, 151, 22))
        dummy.setObjectName("input_admin")
        for admin in admins:
            dummy.addItem(admin)
        dummy.setCurrentText(dados["cartao_aluno"])
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    # Cria layout gerenciar cursos
    def criar_gerenciar_cursos(self, cursos):
        self.novo_frame()

        # 1 - Label Nome
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 100, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        # 2 - Input Nome
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(True)
        dummy.setGeometry(QtCore.QRect(130, 100, 113, 22))
        dummy.setObjectName("input_nome")
        self.elementos.append(dummy)

        # 3 - Botão Criar Curso
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 140, 91, 22))
        dummy.setObjectName("botao_criarCurso")
        dummy.setText("Criar Curso")
        dummy.clicked.connect(self.criar_curso_pressionado)
        self.elementos.append(dummy)

        # 4 - Input Curso
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 60, 151, 22))
        dummy.setObjectName("input_curso")
        for curso in cursos:
            dummy.addItem(curso)
        self.elementos.append(dummy)

        # 5 - Label Curso
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 40, 51, 21))
        dummy.setObjectName("label_curso")
        dummy.setText("Curso:")
        self.elementos.append(dummy)

        # 6 - Botão Editar Curso
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(240, 60, 61, 22))
        dummy.setObjectName("botao_editarCurso")
        dummy.setText("Editar")
        dummy.clicked.connect(self.editar_curso_pressionado)
        if len(cursos) == 0:
            dummy.setEnabled(False)
        self.elementos.append(dummy)

        # 7 - Botão Excluir Curso
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(310, 60, 61, 22))
        dummy.setObjectName("botao_excluirCurso")
        dummy.setText("Excluir")
        dummy.clicked.connect(self.excluir_curso_pressionado)
        if len(cursos) == 0:
            dummy.setEnabled(False)
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    def criar_editar_curso(self, cursos, dados):
        self.novo_frame()

        self.temp = dados

        # 1 - Label Nome
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 100, 41, 21))
        dummy.setObjectName("label_nome")
        dummy.setText("Nome:")
        self.elementos.append(dummy)

        # 2 - Input Nome
        dummy = QtWidgets.QLineEdit(self.mainframe)
        dummy.setEnabled(True)
        dummy.setGeometry(QtCore.QRect(130, 100, 113, 22))
        dummy.setObjectName("input_nome")
        dummy.setText(dados)
        self.elementos.append(dummy)

        # 3 - Botão Atualizar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 140, 91, 22))
        dummy.setObjectName("botao_criarCurso")
        dummy.setText("Atualizar")
        dummy.clicked.connect(self.atualizar_curso_pressionado)
        self.elementos.append(dummy)

        # 4 - Input Curso
        dummy = QtWidgets.QComboBox(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 60, 151, 22))
        dummy.setObjectName("input_curso")
        for curso in cursos:
            dummy.addItem(curso)
        dummy.setCurrentText(dados)
        self.elementos.append(dummy)

        # 5 - Label Curso
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(80, 40, 51, 21))
        dummy.setObjectName("label_curso")
        dummy.setText("Curso:")
        self.elementos.append(dummy)

        # 6 - Botão Editar Curso
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(240, 60, 61, 22))
        dummy.setObjectName("botao_editarCurso")
        dummy.setText("Editar")
        dummy.clicked.connect(self.editar_curso_pressionado)
        if len(cursos) == 0:
            dummy.setEnabled(False)
        self.elementos.append(dummy)

        # 7 - Botão Excluir Curso
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(330, 140, 61, 22))
        dummy.setObjectName("botao_excluirCurso")
        dummy.setText("Excluir")
        dummy.clicked.connect(self.excluir_curso_pressionado)
        self.elementos.append(dummy)

        # 8 - Botão Voltar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(400, 140, 61, 22))
        dummy.setObjectName("botao_excluirCurso")
        dummy.setText("Voltar")
        dummy.clicked.connect(self.voltar_editar_curso_pressionado)
        self.elementos.append(dummy)

        # 8 - Botão Adicionar Horários
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(180, 140, 141, 22))
        dummy.setObjectName("botao_relacionar_horarios")
        dummy.setText("Relacionar Horários")
        dummy.clicked.connect(self.relacionar_disciplinas_pressionado)
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    def criar_horario_gerado(self, dataframe, aviso_reprovacao, aprovacao_media):
        self.novo_frame()

        # 1 - Botão Salvar CSV
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 310, 111, 22))
        dummy.setObjectName("botao_salvar_csv")
        dummy.setText("Salvar em CSV")
        dummy.clicked.connect(self.controlador.salvar_horarios)
        self.elementos.append(dummy)

        # 2 - Botão Voltar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(190, 310, 61, 22))
        dummy.setObjectName("botao_voltar")
        dummy.setText("Voltar")
        dummy.clicked.connect(self.controlador.gerenciar_horarios)
        self.elementos.append(dummy)

        # 3 - Tabela Gerada
        dummy = QtWidgets.QTableWidget(self.mainframe)
        dummy.setGeometry(QtCore.QRect(20, 60, 533, 233))
        dummy.setObjectName("tableWidget")
        dummy.setColumnCount(5)
        dummy.setRowCount(7)
        dummy.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        item = QtWidgets.QTableWidgetItem()
        item.setText("8h")
        dummy.setVerticalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        dummy.setVerticalHeaderItem(1, item)
        item.setText("10h")

        item = QtWidgets.QTableWidgetItem()
        dummy.setVerticalHeaderItem(2, item)
        item.setText("13h")

        item = QtWidgets.QTableWidgetItem()
        dummy.setVerticalHeaderItem(3, item)
        item.setText("15h")

        item = QtWidgets.QTableWidgetItem()
        dummy.setVerticalHeaderItem(4, item)
        item.setText("17h")

        item = QtWidgets.QTableWidgetItem()
        dummy.setVerticalHeaderItem(5, item)
        item.setText("19h")

        item = QtWidgets.QTableWidgetItem()
        dummy.setVerticalHeaderItem(6, item)
        item.setText("21h")

        item = QtWidgets.QTableWidgetItem()
        dummy.setHorizontalHeaderItem(0, item)
        item.setText("Segunda")

        item = QtWidgets.QTableWidgetItem()
        dummy.setHorizontalHeaderItem(1, item)
        item.setText("Terça")

        item = QtWidgets.QTableWidgetItem()
        dummy.setHorizontalHeaderItem(2, item)
        item.setText("Quarta")

        item = QtWidgets.QTableWidgetItem()
        dummy.setHorizontalHeaderItem(3, item)
        item.setText("Quinta")

        item = QtWidgets.QTableWidgetItem()
        dummy.setHorizontalHeaderItem(4, item)
        item.setText("Sexta")

        ### Populate
        for i in range(7):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem()
                horario = dataframe.iloc[i][j]
                if horario == "-":
                    item.setText("")
                else:
                    item.setText(horario)
                dummy.setItem(i, j, item)

        dummy.horizontalHeader().setDefaultSectionSize(100)
        self.elementos.append(dummy)

        # 4 - Label Horário Gerado
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(20, 40, 231, 16))
        dummy.setObjectName("label_horario_gerado")
        dummy.setText("Horário Gerado:")
        self.elementos.append(dummy)

        # 5 - Label Aviso Reprovação
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(180, 40, 371, 16))
        dummy.setObjectName("label_aviso_reprovacao")
        if aviso_reprovacao:
            dummy.setText("Essa tabela contém disciplinas com alta taxa de reprovação!")
        else:
            dummy.setText("")
        self.elementos.append(dummy)

        # 6 - Label Taxa Média Aprovação
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(280, 310, 210, 16))
        dummy.setObjectName("label_media_reprovacao")
        texto = "Taxa Média de Aprovação: " + str(aprovacao_media) + "%"
        dummy.setText(texto)
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)


    def criar_gerenciar_horarios(self, disciplinas):
        self.novo_frame()

        # 1 - Botão Adicionar Disciplinas
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 340, 141, 22))
        dummy.setObjectName("botao_gerar_horario")
        dummy.setText("Gerar Horário")
        dummy.clicked.connect(self.gerar_horario_pressionado)
        self.elementos.append(dummy)

        # 2 - Botão Voltar
        dummy = QtWidgets.QPushButton(self.mainframe)
        dummy.setGeometry(QtCore.QRect(220, 340, 61, 22))
        dummy.setObjectName("botao_voltar")
        dummy.setText("Voltar")
        dummy.clicked.connect(self.ver_perfil_pressionado)
        self.elementos.append(dummy)

        # 3 - Tabela
        dummy = QtWidgets.QTableWidget(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 40, 231, 281))
        dummy.setObjectName("tableWidget")
        dummy.setColumnCount(1)
        dummy.setRowCount(len(disciplinas))

        item = QtWidgets.QTableWidgetItem()
        item.setText("Disciplinas")
        dummy.setHorizontalHeaderItem(0, item)

        for i in range(len(disciplinas)):
            item = QtWidgets.QTableWidgetItem()
            item.setText(disciplinas[i])
            dummy.setItem(i, 0, item)

        dummy.horizontalHeader().setDefaultSectionSize(200)
        self.elementos.append(dummy)

        # 4 - Label Disciplinas
        dummy = QtWidgets.QLabel(self.mainframe)
        dummy.setGeometry(QtCore.QRect(70, 20, 300, 16))
        dummy.setObjectName("label_disciplinas")
        dummy.setText("Selecione as disciplinas para gerar o horário:")
        self.elementos.append(dummy)

        self.mainframe.setVisible(True)

    def gerar_horario_pressionado(self):
        lista_disciplinas = []
        for item_selecionado in self.elementos[2].selectedItems():
            lista_disciplinas.append(item_selecionado.text())

        self.controlador.gerar_horario(lista_disciplinas)

    def relacionar_disciplinas_pressionado(self):
        self.controlador.relacionar_disciplinas(self.temp)

    # Ação para botão de Voltar, no layout Editar Admin
    def voltar_editar_admin_pressionado(self):
        self.controlador.gerenciar_admins()

    def voltar_editar_curso_pressionado(self):
        self.controlador.gerenciar_cursos()

    # Ação para botão de Voltar, no layout Editar Disciplinas
    def voltar_editar_disciplina_pressionado(self):
        self.controlador.gerenciar_disciplinas()

    # Ação para botão de Excluir, no layout Excluir Admin
    def excluir_admin_pressionado(self):
        admin = self.elementos[12].currentText()
        self.controlador.excluir_admin(admin)

    def editar_admin_pressionado(self):
        admin = self.elementos[12].currentText()
        self.controlador.editar_admin(admin)

    def excluir_admin_pressionado2(self):
        admin = self.elementos[9].text()
        self.controlador.excluir_admin(admin)

    def excluir_disciplina_pressionado2(self):
        disciplina = self.elementos[20].currentText()
        self.controlador.excluir_disciplina(disciplina)

    def editar_disciplina_pressionado(self):
        disciplina = self.elementos[20].currentText()
        self.controlador.editar_disciplina(disciplina)

    def editar_curso_pressionado(self):
        curso = self.elementos[3].currentText()
        self.controlador.editar_curso(curso)

    def excluir_curso_pressionado(self):
        curso = self.elementos[3].currentText()
        self.controlador.excluir_curso(curso)

    def excluir_curso_pressionado2(self):
        curso = self.elementos[1].text()
        self.controlador.excluir_curso(curso)

    def excluir_disciplina_pressionado(self):
        disciplina = self.elementos[20].currentText()
        self.controlador.excluir_disciplina(disciplina)

    # Ação para botão de Gerenciar Admins, no sidemenu
    def gerenciar_admins_pressionado(self):
        self.controlador.gerenciar_admins()

    def atualizar_admin_pressionado(self):
        input_nome = self.elementos[10].text()
        input_senha = self.elementos[11].text()
        input_cartao = self.elementos[9].text()
        input_curso = self.elementos[12].currentText()
        self.controlador.atualizar_admin(input_cartao, input_nome, input_senha, input_curso)

    def adicionar_disciplinas_pressionado(self):
        lista_disciplinas = []
        for item_selecionado in self.elementos[2].selectedItems():
            lista_disciplinas.append(item_selecionado.text())

        self.controlador.adicionar_disciplinas(self.temp, lista_disciplinas)

    def atualizar_historico_pressionado(self):
        lista_disciplinas = []
        for item_selecionado in self.elementos[2].selectedItems():
            lista_disciplinas.append(item_selecionado.text())

        self.controlador.atualizar_historico(lista_disciplinas)

    def atualizar_curso_pressionado(self):
        input_nome = self.elementos[1].text()
        self.controlador.atualizar_curso(self.temp, input_nome)

    def atualizar_disciplina_pressionado(self):
        nome = self.elementos[19].text()
        semestre = int(self.elementos[8].currentText())
        aprovacao = self.elementos[2].text()

        segunda = self.elementos[10].currentText()
        if segunda == "-":
            segunda = 0
        else:
            segunda = segunda.replace("h", "")
            segunda = int(segunda)

        terca = self.elementos[13].currentText()
        if terca == "-":
            terca = 0
        else:
            terca = terca.replace("h", "")
            terca = int(terca)

        quarta = self.elementos[14].currentText()
        if quarta == "-":
            quarta = 0
        else:
            quarta = quarta.replace("h", "")
            quarta = int(quarta)

        quinta = self.elementos[15].currentText()
        if quinta == "-":
            quinta = 0
        else:
            quinta = quinta.replace("h", "")
            quinta = int(quinta)

        sexta = self.elementos[16].currentText()
        if sexta == "-":
            sexta = 0
        else:
            sexta = sexta.replace("h", "")
            sexta = int(sexta)

        self.controlador.atualizar_disciplina(self.temp, nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta)

    # Ação para botão de Editar Histórico, no layout Ver Perfil
    def editar_historico_pressionado(self):
        self.controlador.editar_historico()

    # Ação para botão atualizar, no layout Ver Perfil
    def atualizar_pressionado(self):
        input_nome = self.elementos[3].text()
        input_senha = self.elementos[4].text()
        input_curso = self.elementos[7].currentText()
        self.controlador.atualizar_perfil(input_nome, input_senha, input_curso)

    # Ação para botão criar conta, no layout Login
    def criar_conta_pressionado(self):
        self.controlador.criar_cadastro()

    # Ação para voltar atualizar, no layout Cadastro
    def voltar_cadastro_pressionado(self):
        self.criar_login()

    def nova_conta_pressionado(self):
        # Verifica se todos os campos foram preenchidos
        senha = self.elementos[1].text()
        nome = self.elementos[0].text()
        cartao_aluno = self.elementos[2].text()
        curso = self.elementos[3].currentText()

        if senha == "" or nome == "" or cartao_aluno == "":
            self.setar_mensagem_cadastro("Preencha todos os campos.")
        else:
            try:
                cartao_aluno = int(cartao_aluno)
                self.controlador.nova_conta(senha, nome, cartao_aluno, curso)
            except ValueError:
                self.setar_mensagem_cadastro("Cartão do aluno deve ter apenas números")

    def criar_admin_pressionado(self):
        # Verifica se todos os campos foram preenchidos
        senha = self.elementos[10].text()
        nome = self.elementos[9].text()
        cartao_aluno = self.elementos[8].text()
        curso = self.elementos[11].currentText()

        if senha == "" or nome == "" or cartao_aluno == "":
            self.setar_mensagem_status("Preencha todos os campos.")
        else:
            try:
                x = int(cartao_aluno)
                self.controlador.novo_admin(senha, nome, str(cartao_aluno), curso)
            except ValueError:
                self.setar_mensagem_status("Cartão do aluno deve ter apenas números")

    def criar_curso_pressionado(self):
        nome = self.elementos[1].text()
        self.controlador.criar_curso(nome)

    def criar_disciplina_pressionado(self):
        nome = self.elementos[19].text()
        semestre = int(self.elementos[8].currentText())
        aprovacao = self.elementos[2].text()

        segunda = self.elementos[10].currentText()
        if segunda == "-":
            segunda = 0
        else:
            segunda = segunda.replace("h", "")
            segunda = int(segunda)

        terca = self.elementos[13].currentText()
        if terca == "-":
            terca = 0
        else:
            terca = terca.replace("h", "")
            terca = int(terca)

        quarta = self.elementos[14].currentText()
        if quarta == "-":
            quarta = 0
        else:
            quarta = quarta.replace("h", "")
            quarta = int(quarta)

        quinta = self.elementos[15].currentText()
        if quinta == "-":
            quinta = 0
        else:
            quinta = quinta.replace("h", "")
            quinta = int(quinta)

        sexta = self.elementos[16].currentText()
        if sexta == "-":
            sexta = 0
        else:
            sexta = sexta.replace("h", "")
            sexta = int(sexta)

        self.controlador.criar_disciplinas(nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta)

	# Ação para botão Gerenciar Horários, no sidemenu
    def gerenciar_horarios_pressionado(self):
        self.controlador.gerenciar_horarios()
				
    # Ação para botão Ver Perfil, no sidemenu
    def ver_perfil_pressionado(self):
        self.controlador.ver_perfil()

    # Ação para botão Gerenciar Cursos, no sidemenu
    def gerenciar_cursos_pressionado(self):
        self.controlador.gerenciar_cursos()

    # Ação para botão Gerenciar Disciplinas, no sidemenu
    def gerenciar_disciplinas_pressionado(self):
        self.controlador.gerenciar_disciplinas()

    # Ação para botão login, no layout Login
    def login_pressionado(self):
        self.controlador.login(self.elementos[2].text(), self.elementos[3].text())

    # Exibe mensagem no layout de login
    def setar_mensagem_login(self, mensagem):
        self.elementos[5].setText(mensagem)
        self.setar_mensagem_status(mensagem)

    # Exibe mensagem no layout de cadastro
    def setar_mensagem_cadastro(self, mensagem):
        self.elementos[2].setText(mensagem)
        self.setar_mensagem_status(mensagem)

    # Exibe mensagem na barra de status da janela
    def setar_mensagem_status(self, mensagem):
        self.statusBar.showMessage(mensagem)

    # Exibe mensagem no boas vindas do sidemenu
    def setar_boas_vindas(self, mensagem):
        self.label_boas_vindas.setText(mensagem)
