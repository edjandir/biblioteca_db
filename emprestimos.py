from livros import get_id_livro

def inclui_emprestimo(con, usuario, livros):

    sql_insert = f"INSERT INTO emprestimos (usuario_id) VALUES ({usuario})"
    cursor = con.cursor()
    cursor.execute(sql_insert)
    con.commit()

    id_gerado = cursor.lastrowid()

    for livro in livros:
        id_livro = get_id_livro(livro)
        sql = "INSERT INTO emprestimos_livros(emprestimo_id, livro_id) VALUES(?,?)"
        con.execute(sql, (id_gerado, id_livro,))

    con.commit()



    
