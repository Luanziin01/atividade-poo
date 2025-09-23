from mercado import mercadinho

produto1 = mercadinho()
produto1.produtos('arroz',5)
funcionario1 = mercadinho()
funcionario1.funcionarios('Luan', 24)

mercadinho.listar(produto1)

mercadinho.listar_funcionarios(funcionario1)