def inclui_livro(con, titulo, autor_id, editora_id, ano, edicao):
    ##montando o sql do insert
    sql_insert = """INSERT INTO livros(titulo, autor_id, editora_id, ano_publicacao, edicao,
    disponivel) VALUES(?, ?, ?, ?, ?, ?)"""
    con.execute(sql_insert, (titulo, autor_id, editora_id, ano, edicao, 1))
    con.commit()

def listar_livros(con):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    #executa o sql
    sql = """SELECT l.id, l.titulo, l.ano_publicacao, 
    l.edicao, l.disponivel, a.nome as autor, e.nome as editora FROM livros l, 
    autores a, editoras e WHERE (l.autor_id = a.id) AND
    (l.editora_id = e.id)"""
    cursor.execute(sql)
    
    #pega os registros e guarda na variável resultados
    resultados = cursor.fetchall()

    #percorre os registros que retornaram
    for linha in resultados:
        print(f"id: {linha['id']} | título: {linha['titulo']}" +
              f" | autor: {linha['autor']} | editora: {linha['editora']}")
        #print(f"id: {linha[0]} | nome: {linha[1]}")

def get_id_livro(con, nome_livro):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    #executa o sql
    cursor.execute(f"SELECT id FROM livros WHERE nome = '{nome_livro}'")
    resultado = cursor.fetchone()
    return resultado[0]