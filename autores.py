#arquivo com o código para incluir, buscar e listar autores

def inclui_autor(con, nome):
    con.execute("INSERT INTO autores(nome) VALUES(?)",
                 (nome,))
    con.commit()

def get_id_autor(con, nome_autor):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    #executa o sql
    cursor.execute(f"SELECT id FROM autores WHERE nome = '{nome_autor}'")
    resultado = cursor.fetchone()
    return resultado[0]


def lista_autores(con):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

    #executa o sql
    cursor.execute("SELECT * FROM autores")

    #pega os registros e guarda na variável resultados
    resultados = cursor.fetchall()

    #percorre os registros que retornaram
    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome']}")
        #print(f"id: {linha[0]} | nome: {linha[1]}")