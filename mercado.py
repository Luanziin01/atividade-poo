class mercadinho:
    def produtos(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def listar(self):
        print(f'Produto {self.nome} custa R${self.preco}')

    def funcionarios(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def listar_funcionarios(self):
        print(f'Funcionario {self.nome} tem {self.idade} anos')