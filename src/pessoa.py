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
    def niver(self, anos):
        self.idade = self.idade+anos
    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade
    def getEmail(self):
        return self.email
    def setNome(self, nome):
        self.nome = nome
    def setIdade(self, idade):
        self.idade = idade
    def setEmail(self, email):
        self.email = email
