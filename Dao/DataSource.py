import mysql.connector

class DataSource(object):
    def __init__(self):
        if not(self.conectar_mysql()):
            print("Erro de conexão do Banco de Dados")
            self.conectado = False
        self.conectado = True

    def conectar_mysql(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="engsoft"
            )
            return True

        except:
            return False

    @property
    def obter_cursor(self):
        if self.conectado:
            return self.mydb.cursor(dictionary=True)
        else:
            return False

    @property
    def esta_logado(self):
        return self.conectado

    def fechar_conexao(self):
        self.conectado = True
        self.mydb.close()

    def commit(self):
        self.mydb.commit()