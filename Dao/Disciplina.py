from Dao.DataSource import DataSource
from Model.Objetos.Disciplina import Disciplina


class DisciplinaDao(object):
    """
    Obtém todas disciplinas relacionadas ao curso_id.
    Retorno: False || Lista[Ids Disciplinas]
    """

    def obter_disciplinas_curso(self, curso_id):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM disciplinas_curso WHERE curso_id = %s"
        valores = (curso_id,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()
        # Verfica se retornou algum resultado
        disciplinas = []
        if cursor.rowcount != 0:

            for row in resultado_sql:
                id = row["disciplina_id"]

                # Cria a disciplina informada pelo id
                if not self.obter_disciplina_id(id):
                    return False

                disciplinas.append(id)

        return disciplinas

    def obter_nome_disciplinas(self):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM disciplinas"
        cursor.execute(sql)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Disciplinas Existem
        if cursor.rowcount != 0:
            nomes_disciplinas = []
            for disciplina_row in resultado_sql:
                nome = disciplina_row["nome"]
                nomes_disciplinas.append(nome)

        return nomes_disciplinas

    """
    Obtém todas disciplinas relacionadas ao usuario.
    Retorno: False || Lista[Ids Disciplinas]
    """
    def obter_disciplinas_usuario(self, usuario_id):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM historico WHERE usuario_id = %s"
        valores = (usuario_id,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        disciplinas = []
        # Verfica se retornou algum resultado
        if cursor.rowcount != 0:

            for row in resultado_sql:
                id = row["disciplina_id"]
                disciplinas.append(id)

            # Retorna lista com todas ids de disciplina do usuario

        return disciplinas

    """
    Obtém uma disciplina pelo seu id. Retorno: False || Obj Disciplina
    """

    def obter_disciplina_id(self, id):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM disciplinas WHERE id = %s"
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
            taxa_aprovacao = disciplina_row["taxa_aprovacao"]
            segunda = disciplina_row["segunda"]
            terca = disciplina_row["terca"]
            quarta = disciplina_row["quarta"]
            quinta = disciplina_row["quinta"]
            sexta = disciplina_row["sexta"]
            Disciplina(id, nome, semestre, taxa_aprovacao, segunda, terca, quarta, quinta, sexta)

            return True

        else:
            return False

    def atualizar(self, nome,nome_novo, semestre, aprovacao, segunda, terca, quarta, quinta, sexta):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "UPDATE disciplinas SET nome = %s , semestre = %s, taxa_aprovacao = %s , segunda = %s, terca = %s, quarta = %s, quinta = %s, sexta = %s WHERE nome = %s"
        valores = (nome_novo, semestre, aprovacao, segunda, terca, quarta, quinta, sexta, nome)
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        if cursor.rowcount > 0:
            return self.obter_id_criado(nome_novo)
        else:
            return False

    def criar(self, nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "INSERT INTO disciplinas (nome, semestre, taxa_aprovacao, segunda, terca, quarta, quinta, sexta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (nome, semestre, aprovacao, segunda, terca, quarta, quinta, sexta)
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

        sql = "SELECT * FROM disciplinas WHERE nome = %s"
        valores = (nome,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Disciplina Existe
        if cursor.rowcount != 0:
            disciplina_row = resultado_sql[0]

            id = disciplina_row["id"]

            return id

        else:
            return False



    def excluir(self, id):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "DELETE FROM disciplinas WHERE id = %s"
        valores = (id,)
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        if cursor.rowcount > 0:
            return True
        else:
            return False
