from dao.datasource import DataSource
from model.objetos.disciplina import Disciplina

class Disciplina_DAO(object):
    """
    Obtém todas disciplinas relacionadas ao curso_id. Retorno: False || Lista[Obj Disciplina]
    """
    def obter_disciplinas_curso(self, curso_id):
        conexao = DataSource()

        if not(conexao.esta_logado):
            return False

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM disciplinas_curso WHERE curso_id = %s")
        valores = (curso_id,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()
        # Verfica se retornou algum resultado
        if cursor.rowcount != 0:
            disciplinas = []
            for disciplina_curso in resultado_sql:
                id = disciplina_curso["disciplina_id"]
                disciplina = self.obter_disciplina_id(id)
                disciplinas.append(disciplina)

            # Retorna lista com todos objetos de disciplina
            return disciplinas

        else:
            return False

    """
    Obtém uma disciplina pelo seu id. Retorno: False || Obj Disciplina
    """
    def obter_disciplina_id(self, id):
        conexao = DataSource()

        if not(conexao.esta_logado):
            return False

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM disciplinas WHERE id = %s")
        valores = (id,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Disciplina Existe
        if cursor.rowcount != 0:
            disciplina_row = resultado_sql[0]

            id = disciplina_row["id"]
            nome = disciplina_row["nome"]
            semestre = disciplina_row["semestre"]

            disciplina = Disciplina(id, nome, semestre)

            return disciplina

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





# Core vai ter o usuario, logo vai usar usuarioDAO.
# Core manda salvar no banco