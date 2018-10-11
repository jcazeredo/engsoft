from dao.datasource import DataSource
from model.objetos.curso import Curso

class Curso_DAO(object):
    """
    Obtém curso que possui a id. Retorno: False || Obj Curso
    """
    def obter_curso_id(self, id, disciplinas):
        conexao = DataSource()

        if not(conexao.esta_logado):
            return False

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM cursos WHERE id = %s")
        valores = (id,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Curso Existe
        if cursor.rowcount != 0:
            curso_row = resultado_sql[0]

            id = curso_row["id"]
            nome = curso_row["nome"]

            curso = Curso(id, nome, disciplinas)

            return curso
        else:
            return False

    def obter_id_curso(self, nome_curso):
        conexao = DataSource()

        if not (conexao.esta_logado):
            return False

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM cursos WHERE nome = %s")
        valores = (nome_curso,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Cursos com esse nome existem
        if cursor.rowcount != 0:
            return resultado_sql[0]["id"]
        else:
            return False

    def obter_nome_cursos(self):
        conexao = DataSource()

        if not (conexao.esta_logado):
            return False

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM cursos")
        cursor.execute(sql)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Cursos Existem
        if cursor.rowcount != 0:
            nomes_cursos = []
            for curso_row in resultado_sql:

                nome = curso_row["nome"]
                nomes_cursos.append(nome)

            return nomes_cursos
        else:
            return False

    def atualizar(self):
        pass
        # conexao = DataSource()
        # cursor = conexao.obter_cursor
        #
        # conexao.fechar_conexao()

    def excluir(self):
        pass
        # conexao = DataSource()
        # cursor = conexao.obter_cursor
        #
        # conexao.fechar_conexao()