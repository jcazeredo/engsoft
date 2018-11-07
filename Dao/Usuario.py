from Dao.DataSource import DataSource
from Model.Objetos.Usuario import Usuario


class UsuarioDao(object):
    """
    Autentica o login.
    Retorno: None caso não autenticar || Objeto Usuário caso autenticar
    """
    def autenticar_login(self, cartao_aluno, senha):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False, None

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM usuarios WHERE cartao_aluno = %s AND senha = %s"
        valores = (cartao_aluno, senha)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Login Válido
        if cursor.rowcount != 0:
            row = resultado_sql[0]
            id = row["id"]
            nome = row["nome"]
            senha = row["senha"]
            cartao_aluno = row["cartao_aluno"]
            curso_id = row["curso_id"]
            privilegio = row["privilegio"]
            usuario_obj = Usuario(id, nome, senha, cartao_aluno, curso_id, privilegio)

            return usuario_obj

        # Login Inválido
        else:
            return False

    def atualiza_disciplinas(self, user_id, lista_id):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        for disciplina_id in lista_id:
            sql = "INSERT INTO historico (usuario_id, disciplina_id) VALUES (%s, %s)"
            valores = (user_id, disciplina_id)
            cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

    def remover_disciplinas(self, user_id, lista_id):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        for disciplina_id in lista_id:
            sql = "DELETE FROM historico WHERE disciplina_id = %s AND usuario_id = %s"
            valores = (disciplina_id, user_id)
            cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

    """
    Obtém um usuário pelo cartão do aluno.
    Retorno: False || Objeto Usuário
    """
    def obter_usuario(self, cartao_aluno):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False, None

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM usuarios WHERE cartao_aluno = %s"
        valores = (cartao_aluno,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Login Válido
        if cursor.rowcount != 0:
            row = resultado_sql[0]
            id = row["id"]
            nome = row["nome"]
            senha = row["senha"]
            cartao_aluno = row["cartao_aluno"]
            curso_id = row["curso_id"]
            privilegio = row["privilegio"]
            usuario_obj = Usuario(id, nome, senha, cartao_aluno, curso_id, privilegio)

            return usuario_obj

        # Login Inválido
        else:
            return False

    def obter_id_cartao(self, cartao_aluno):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False, None

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM usuarios WHERE cartao_aluno = %s"
        valores = (cartao_aluno,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Login Válido
        if cursor.rowcount != 0:
            row = resultado_sql[0]
            id = row["id"]

            return id

        # Login Inválido
        else:
            return False

    def existe_cartao(self, cartao_aluno):
        conexao = DataSource()

        if not conexao.esta_logado:
            return -1

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM usuarios WHERE cartao_aluno = %s"
        valores = (cartao_aluno,)
        cursor.execute(sql, valores)

        cursor.fetchall()
        conexao.fechar_conexao()

        if cursor.rowcount != 0:
            return True
        else:
            return False

    """
    Atualiza alguns dados do usuário no banco de dados.
    Retorno: False || True
    """
    def atualizar(self, usuario):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        id = usuario.id
        nome = usuario.nome
        senha = usuario.senha
        curso_id = usuario.curso_id

        sql = "UPDATE usuarios SET nome = %s, senha = %s, curso_id = %s WHERE id = %s"
        valores = (nome, senha, curso_id, id)
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        return True

    def obter_cartao_admins(self, id):
        conexao = DataSource()

        if not conexao.esta_logado:
            return False

        cursor = conexao.obter_cursor

        sql = "SELECT * FROM usuarios WHERE privilegio = 0"
        cursor.execute(sql)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Admins Existem
        if cursor.rowcount != 0:
            cartoes_admin = []
            for row in resultado_sql:
                if row["id"] != id:
                    cartao_aluno = row["cartao_aluno"]
                    cartoes_admin.append(cartao_aluno)

        return cartoes_admin



    def criar(self, senha, nome, cartao_aluno, curso_id, privilegio):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "INSERT INTO usuarios (nome, senha, cartao_aluno, curso_id, privilegio) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, senha, str(cartao_aluno), curso_id, privilegio)
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def excluir(self, id):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "DELETE FROM usuarios WHERE id = %s"
        valores = (id,)
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        if cursor.rowcount > 0:
            return True
        else:
            return False
