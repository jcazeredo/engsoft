import mysql.connector

class Core(object):
    def __init__(self, controlador):
        self.controlador = controlador
        self.logado = False

    def conectar_mysql(self, dict = True):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="engsoft"
        )

        if dict:
            return self.mydb.cursor(dictionary = True)
        else:
            return self.mydb.cursor()

    def desconectar_mysql(self):
        self.mydb.close()



    def autenticar_login(self, usuario, senha):
        cursor = self.conectar_mysql(dict=True)

        sql = ("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s")
        valores = (usuario, senha)
        cursor.execute(sql, valores)

        resultado = cursor.fetchall()

        # Login Válido
        if cursor.rowcount != 0:
            self.logado = True
            self.usuario_logado = resultado[0]

            self.desconectar_mysql()
            return True

        # Login Inválido
        else:
            self.desconectar_mysql()
            return False

    @property
    def obter_dados_usuario(self):
        return self.usuario_logado

    @property
    def obter_cursos(self):
        cursor = self.conectar_mysql(dict=True)

        sql = ("SELECT * FROM cursos")
        cursor.execute(sql)

        resultado = cursor.fetchall()

        if cursor.rowcount != 0:
            dict_cursos = {}
            for row in resultado:
                dict_cursos[row["nome"]] = row["id"]

            self.desconectar_mysql()
            return dict_cursos

        self.desconectar_mysql()

    def atualizar_perfil(self, nome, curso, senha):
        cursor = self.conectar_mysql()

        sql = ("SELECT id FROM cursos WHERE nome = %s")
        valores = (curso,)
        cursor.execute(sql, valores)
        resultado = cursor.fetchall()

        curso_id = resultado[0]["id"]

        sql = ("UPDATE usuarios SET nome = %s, curso_id = %s, senha = %s WHERE id = %s")
        valores = (nome, curso_id, senha, self.usuario_logado["id"])
        cursor.execute(sql, valores)

        self.mydb.commit()

        self.desconectar_mysql()