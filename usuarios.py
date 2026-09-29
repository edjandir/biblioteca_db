#arquivo com o código para incluir, buscar e listar usuários

def inclui_usuario(con, nome):
    con.execute("INSERT INTO usuarios(nome) VALUES(?)",
                 (nome,))
    con.commit()

def lista_usuarios(con):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    #executa o sql
    cursor.execute("SELECT * FROM usuarios")

    #pega os registros e guarda na variável resultados
    resultados = cursor.fetchall()

    #percorre os registros que retornaram
    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome']}")
        #print(f"id: {linha[0]} | nome: {linha[1]}")