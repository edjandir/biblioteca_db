#arquivo com o código para incluir, buscar e listar usuários

def inclui_editora(con, nome):
    con.execute("INSERT INTO editoras(nome) VALUES(?)",
                 (nome,))
    con.commit()

def get_id_editora(con, nome_editora):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    #executa o sql
    cursor.execute(f"SELECT id FROM editoras WHERE nome = '{nome_editora}'")
    resultado = cursor.fetchone()
    return resultado[0]


def lista_editoras(con):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    #executa o sql
    cursor.execute("SELECT * FROM editoras")

    #pega os registros e guarda na variável resultados
    resultados = cursor.fetchall()

    #percorre os registros que retornaram
    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome']}")
        #print(f"id: {linha[0]} | nome: {linha[1]}")