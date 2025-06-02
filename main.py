from produto import FuncionarioCLT, FuncionarioPJ, Produto, ProdutoImportado, ProdutoNacional


# Exemplo de uso:
print("\n   Cadastro de Produtos    ")
produtos = [
    ProdutoNacional("Mouse", 50.0, 30),
    ProdutoImportado("Notebook", 5000.0, 10, 0.2),
    ProdutoNacional("Webcam", 200.0, 15)
]

print("\n    Detalhes e Notas Fiscais    ")
for produto in produtos:
    produto.exibir_detalhes()
    produto.emitir_nota()
    print(f"Preço Final: R${produto.preco_final():.2f}\n")

print("\n    Cadastro de Funcionários    ")
funcionarios = [
    FuncionarioCLT("Lucas", 3000.00),
    FuncionarioPJ("Ana", 160, 40)
]

print("\n    Pagamentos    ")
for funcionario in funcionarios:
    print(f"{funcionario.nome} receberá R${funcionario.calcular_pagamento():.2f}")

print("\n    Venda e Reposição    ")
produto_escolhido = produtos[0]  # Mouse
produto_escolhido.vender(5)
produto_escolhido.repor(10)

print("\n    Estoque Final    ")
for produto in produtos:
    produto.exibir_detalhes()
