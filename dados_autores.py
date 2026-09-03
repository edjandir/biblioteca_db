import sqlite3

#conectando o banco de dados. Caso não exista, o banco é criado.
conn = sqlite3.connect("biblioteca.db")

#apaga a tabela editoras
conn.execute("DROP TABLE IF EXISTS autores")

#cria a tabela autores
conn.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT \
             , nome TEXT NOT NULL)")

#inserindo os registros na tabela autores
conn.executemany("INSERT INTO autores(nome) VALUES(?)",
                 [("Horstman",), ("Deitel",)])

#confirmando a criação e os inserts da tabela autores.
conn.commit()