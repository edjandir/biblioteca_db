import sqlite3 as sqlite
from util import limpa_tela

from usuarios import inclui_usuario, lista_usuarios

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

while (True):
    limpa_tela()
    print("===== Sistema da biblioteca ======")
    print("(1)-Usuários\n(2)-Autores\n(3)-Editoras")
    opcao = input("Digite a opção: ")

    if (opcao == '1'):
        menu_usuarios()
    else:
        break

#fecha a conexão
conn.close()