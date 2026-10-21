from pessoa import Pessoa

pessoas = []
def cadastrar(nome, idade, email):
    pessoas.append(Pessoa(nome, idade, email))
def consultar(tipo, valor):
    pes = busca(tipo, valor)
    pes.printar()
def alterar(nomeantigo, nomenovo, idadenova, emailnovo):
    pes = busca("nome", nomeantigo)
    print("valores atuais: ")
    pes.printar()
    pes.nome   = nomenovo
    pes.idade  = idadenova
    pes.email  = emailnovo
    print("novos valores: ")
    pes.printar()
def listar():
    return pessoas
def busca(caracteristica, valor):
    match(caracteristica):
        case "nome":
            for x in pessoas :
                if x.nome == valor:
                    return x
        case "idade":
            for x in pessoas :
                if x.idade == valor:
                    return x
        case "email":
            for x in pessoas :
                if x.email == valor:
                    return x
    return "unknown"