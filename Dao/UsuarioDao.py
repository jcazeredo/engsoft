from Dao.DataSource import DataSource
from Model.objetos.Usuario import Usuario

class UsuarioDao(object):
    """
    Autentica o login. Retorno: False, None || True, curso_id
    """
    def autenticar_login(self, usuario, senha):
        conexao = DataSource()

        if not(conexao.esta_logado):
            return False, None

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s")
        valores = (usuario, senha)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        # Login Válido
        if cursor.rowcount != 0:
            usuario = resultado_sql[0]
            return True, usuario["curso_id"]

        # Login Inválido
        else:
            return False, None

    """
    Obtém todas disciplinas que o usuario_id já cursou.
    Retorno: False || list[Obj Disciplina]
    """
    def obter_historico(self, usuario_id, disciplinas):
        conexao = DataSource()

        if not(conexao.esta_logado):
            return False

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM historico WHERE usuario_id = %s")
        valores = (usuario_id,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        if cursor.rowcount != 0:
            disciplinas_row = []
            disciplinas_historico = []

            # Pega todos os ID das disciplinas do resultado sql
            for disciplina in resultado_sql:
                id_row = disciplina["disciplina_id"]
                disciplinas_row.append(id_row)

            # Verifica quais estão na lista de disciplinas do curso
            for disciplina_curso in disciplinas:
                disciplina_curso.id in disciplinas_row
                disciplinas_historico.append(disciplina_curso)

            return disciplinas_historico

        else:
            return False


    """
    Obtém usuário que possui o user informado
    Retorno: False || Obj Usuario
    """
    def obter_usuario_user(self, usuario, disciplinas, curso):
        conexao = DataSource()

        if not (conexao.esta_logado):
            return False

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM usuarios WHERE usuario = %s")
        valores = (usuario,)
        cursor.execute(sql, valores)

        resultado_sql = cursor.fetchall()
        conexao.fechar_conexao()

        if cursor.rowcount != 0:
            usuario_row = resultado_sql[0]

            id = usuario_row["id"]
            nome = usuario_row["nome"]
            usuario = usuario_row["usuario"]
            senha = usuario_row["senha"]
            cartao_aluno = usuario_row["cartao_aluno"]
            disciplinas_cursadas = self.obter_historico(id, disciplinas)
            privilegio = usuario_row["privilegio"]

            usuario = Usuario(id, nome, usuario, senha, cartao_aluno, curso, disciplinas_cursadas, privilegio)

            return usuario

        else:
            return False


    def existe_usuario(self, usuario):
        conexao = DataSource()

        if not (conexao.esta_logado):
            return -1

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM usuarios WHERE usuario = %s")
        valores = (usuario,)
        cursor.execute(sql, valores)

        cursor.fetchall()
        conexao.fechar_conexao()

        if cursor.rowcount != 0:
            return True
        else:
            return False

    def existe_cartao(self, cartao_aluno):
        conexao = DataSource()

        if not (conexao.esta_logado):
            return -1

        cursor = conexao.obter_cursor

        sql = ("SELECT * FROM usuarios WHERE cartao_aluno = %s")
        valores = (cartao_aluno,)
        cursor.execute(sql, valores)

        res = cursor.fetchall()
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

        sql = ("UPDATE usuarios SET nome = %s, senha = %s WHERE id = %s")
        valores = (nome, senha, id)
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def criar(self, senha, usuario, nome, cartao_aluno, curso_id, privilegio):
        conexao = DataSource()
        cursor = conexao.obter_cursor

        sql = "INSERT INTO usuarios (nome, senha, usuario, cartao_aluno, curso_id, privilegio) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nome, senha, usuario, cartao_aluno, curso_id, privilegio )
        cursor.execute(sql, valores)

        conexao.commit()
        conexao.fechar_conexao()

        if cursor.rowcount > 0:
            return True
        else:
            return False

    def excluir(self):
        pass
        # conexao = DataSource
        # cursor = conexao.obter_cursor
        #
        # conexao.fechar_conexao()
