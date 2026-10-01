import sqlite3 as sqlite
from util import limpa_tela

from usuarios import inclui_usuario, lista_usuarios
from autores import inclui_autor, lista_autores, get_id_autor
from editoras import inclui_editora, lista_editoras, get_id_editora
from emprestimos import inclui_emprestimo, lista_emprestimos

#abre a conexão com o banco
conn = sqlite.connect("biblioteca.db")
conn.row_factory = sqlite.Row

def menu_usuarios():
    while (True):
        limpa_tela()
        print("===== Menu de usuários ======")
        print("(1)-Incluir\n(2)-Listar\n(3)-Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome = input("Nome do usuário: ")
            inclui_usuario(conn, nome)
        elif (opcao == '2'):
            lista_usuarios(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Digite uma tecla para continuar...")

def menu_autores():
    while (True):
        limpa_tela()
        print("===== Menu de autores ======")
        print("(1)-Incluir\n(2)-Listar\n(3)-Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome = input("Nome do autor: ")
            inclui_autor(conn, nome)
        elif (opcao == '2'):
            lista_autores(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Digite uma tecla para continuar...")

def menu_editoras():
    while (True):
        limpa_tela()
        print("===== Menu de editoras ======")
        print("(1)-Incluir\n(2)-Listar\n(3)-Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome = input("Nome do editora: ")
            inclui_editora(conn, nome)
        elif (opcao == '2'):
            lista_editoras(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Digite uma tecla para continuar...")

def menu_livros():
    while (True):
        limpa_tela()
        print("===== Menu de livros ======")
        print("(1)-Incluir\n(2)-Listar\n(3)-Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor: ")
            id_autor = get_id_autor(conn, nome_autor)
            nome_editora = input("Nome do editora: ")
            id_editora = get_id_editora(conn, nome_editora)
            ano_publicacao = int(input("Ano de publicação: "))
            edicao = int(input("Ano da edição: "))
            inclui_editora(conn, titulo)
        elif (opcao == '2'):
            lista_editoras(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Digite uma tecla para continuar...")

def menu_emprestimos():
    while (True):
        limpa_tela()
        print("===== Menu de Empréstimos ======")
        print("(1)-Incluir\n(2)-Listar\n(3)-Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            usuario = 1
            livros = []
            while (True):
                titulo_livro = input("Digite o título do livro: ")
                livros.append(titulo_livro)
                opcao = input("Digite S para incluir novo livro ou qualquer tecla para fechar a lista.")
                if (opcao.upper() != 'S'):
                    break
            inclui_emprestimo(conn, usuario, livros)
        elif (opcao == '2'):
            lista_emprestimos(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == '3'):
            limpa_tela()
            break
        else:
            input("Opção inválida! Digite uma tecla para continuar...")


while (True):
    limpa_tela()
    print("===== Sistema da biblioteca ======")
    print("(1)-Usuários\n(2)-Autores\n(3)-Editoras\n(4)-Livros")
    opcao = input("Digite a opção: ")

    if (opcao == '1'):
        menu_usuarios()
    elif (opcao == '2'):
        menu_autores()
    elif (opcao == '3'):
        menu_editoras()
    elif (opcao == '4'):
        menu_livros()
    elif (opcao == '5'):
        menu_emprestimos()
    else:
        break

#fecha a conexão
conn.close()