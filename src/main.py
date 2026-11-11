from cadastro import CadastroPessoas
from repositorio_pessoas_mysql import RepositorioPessoasMySQL
from repositorio_pessoas_memoria import RepositorioPessoasMemoria

USAR_MYSQL = True

def criar_repositorio():
    if USAR_MYSQL:
        return RepositorioPessoasMySQL.aPartirDoAmbiente()
    return RepositorioPessoasMemoria()

def exibir_menu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
    ops = int(input("Escolha uma opcao: "))
    return ops

cadastro = CadastroPessoas(criar_repositorio())

op =0
while op!=5:
    op = exibir_menu()
    match(op):
        case 1:
            nome = input("nome: ")
            idade = int(input("idade: "))
            email = input("email: ")
            cadastro.cadastrar(nome, idade, email)
        case 2:

            tipo = input("consultar por |nome|idade|email: ")
            valor = input("a encontrar: ")
            cadastro.buscarPorNome(valor)
        case 3:

            valor = input("alterar: |nome|: ")

            nnom = input("novo nome: ")
            nid = int(input("nova idade: "))
            nemail = input("novo email: ")
            cadastro.alterar(valor, nnom, nid, nemail)
        case 4:
            for x in cadastro.listar():
                x.printar()
        case 6:
            print("lol")
        case _:
            print("comando desconhecido")
