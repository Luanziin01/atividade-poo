class Mercado:
    def cadastrar_produto(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def listar_produto(self):
        print(f'Produto {self.nome} custa R${self.preco} ')

    def cadastrar_funcionario(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def listar_funcionario(self):
        print(f'Funcionario {self.nome} tem {self.idade} anos')