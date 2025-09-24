from mercado import Mercado
produto1 = Mercado()
produto1.cadastrar_produto('Macarrao',5)
funcionario1 = Mercado()
funcionario1.cadastrar_funcionario('Luan Cunha', 24)
produto1.listar_produto()
funcionario1.listar_funcionario()