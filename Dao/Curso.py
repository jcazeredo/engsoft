from Dao.DataSource import DataSource
from Model.Objetos.Curso import Curso


class CursoDao(object):
    """
    Obtém curso que possui a id. Retorno: False || Obj Curso
    """

    def obter_curso_id(self, id):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM cursos WHERE id = %s"
        valores = (id,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Curso Existe
        if cursor.rowcount != 0:
            curso_row = resultado_sql[0]

            id = curso_row["id"]
            nome = curso_row["nome"]

            curso_obj = Curso(id, nome)

            return curso_obj
        else:
            return False

    def obter_id_curso(self, nome_curso):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM cursos WHERE nome = %s"
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

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM cursos"
        cursor.execute(sql)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Cursos Existem
        if cursor.rowcount != 0:
            nomes_cursos = []
            for curso_row in resultado_sql:
                nome = curso_row["nome"]
                if nome != "Nenhum":
                    nomes_cursos.append(nome)

        return nomes_cursos

    def criar(self, nome):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "INSERT INTO cursos (nome) VALUES (%s)"
        valores = (nome,)
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        if cursor.rowcount > 0:
            return self.obter_id_criado(nome)
        else:
            return False

    def obter_id_criado(self, nome):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM cursos WHERE nome = %s"
        valores = (nome,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Curso Existe
        if cursor.rowcount != 0:
            curso_row = resultado_sql[0]

            id = curso_row["id"]

            return id

        else:
            return False

    def atualiza_disciplinas(self, curso_id, lista_id):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        for disciplina_id in lista_id:
            sql = "INSERT INTO disciplinas_curso (curso_id, disciplina_id) VALUES (%s, %s)"
            valores = (curso_id, disciplina_id)
            cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

    def remover_disciplinas(self, curso_id, lista_id):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        for disciplina_id in lista_id:
            sql = "DELETE FROM disciplinas_curso WHERE disciplina_id = %s AND curso_id = %s"
            valores = (disciplina_id, curso_id)
            cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()


    def atualizar(self, nome, nome_novo):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "UPDATE cursos SET nome = %s WHERE nome = %s"
        valores = (nome_novo, nome)
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        return self.obter_id_criado(nome_novo)

    def excluir(self, id):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "DELETE FROM cursos WHERE id = %s"
        valores = (id, )
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        return True

    def excluir_dos_usuarios(self, curso_id):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM usuarios WHERE curso_id = %s"
        valores = (curso_id,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        lista_usuarios = []

        if cursor.rowcount != 0:
            row = resultado_sql[0]

            id = curso_row["id"]

            return id

        else:
            return False
