
def inclui_emprestimo(con, usuario, livros):

    sql_insert = f"INSERT INTO emprestimos (usuario_id) VALUES ({usuario})"
    con.execute(sql_insert)
    
