import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela livros
conn.execute("DROP TABLE IF EXISTS livros")

#montando sql de criação de livros
sql_create = """CREATE TABLE livros (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            titulo TEXT NOT NULL, autor_id INTEGER REFERENCES autores(id), 
            editora_id INTEGER REFERENCES editoras(id),
            ano_publicacao INTEGER,
            edicao INTEGER,
            disponivel BOOLEAN NOT NULL DEFAULT 1 CHECK (disponivel IN(0,1))
            )"""

#cria a tabela editoras
conn.execute(sql_create)

##montando o sql do insert
sql_insert = """INSERT INTO livros(titulo, autor_id, editora_id, ano_publicacao, edicao,
    disponivel) VALUES(?, ?, ?, ?, ?, ?)"""
 

#inserindo os registros na tabela editoras
conn.executemany(sql_insert, 
    [("Java como programar", 1, 2, 2000, 2, 1), 
     ("Python para iniciantes", 2, 1, 2020, 1, 0)])

#confirmando a criação e os inserts da tabela editoras.
conn.commit()