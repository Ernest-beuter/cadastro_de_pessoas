class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = int(idade)
        self.email = email
    def printar(self):
        print("Nome: " + self.nome)
        print("idade: " + str(self.idade))
        print("email: " + self.email)
        if self.idade>=18:
            print("situação: maior")
        else:
            print("situação: menor")
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
def cadastrar(lista):
    nome = input("nome: ")
    idade = int(input("idade: "))
    email = input("email: ")
    lista.append(Pessoa(nome, idade, email))
def consultar(lista):
    tipo = input("consultar por |nome|idade|email: ")
    valor = input("a encontrar: ")
    pes = busca(tipo, valor, lista)
    pes.printar()
def alterar(lista):
    valor = input("alterar: |nome|: ")
    pes = busca("nome", valor, lista)
    print("valores atuais: ")
    pes.printar()
    nid = int(input("nova idade: "))
    nnom = input("novo nome: ")
    nemail = input("novo email: ")
    pes.nome   = nnom
    pes.idade  = nid
    pes.email  = nemail
    print("novos valores: ")
    pes.printar
def listar(lista):
    print("\npessoas:\n")
    for x in lista:
        x.printar()
    print("\n")
def busca(caracteristica, valor, lista):
    match(caracteristica):
        case "nome":
            it = iter(lista)
            for x in lista :
                if x.nome == valor:
                    return x
        case "idade":
            it = iter(lista)
            for x in lista :
                if x.idade == valor:
                    return x
        case "email":
            it = iter(lista)
            for x in lista :
                if x.email == valor:
                    return x
op =0
pessoas = list()
while op!=5:
    op = exibir_menu()
    match(op):
        case 1:
            cadastrar(pessoas)
        case 2:
            consultar(pessoas)
        case 3:
            alterar(pessoas)
        case 4:
            listar(pessoas)
        case 6:
            print("lol")
        case _:
            print("comando desconhecido")