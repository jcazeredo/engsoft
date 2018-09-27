from DAO.datasource import DataSource
from model.curso import Curso

class CursoDAO(object):
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