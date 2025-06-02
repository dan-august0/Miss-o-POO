from produto import FuncionarioCLT, FuncionarioPJ, Produto, ProdutoImportado, ProdutoNacional


# Exemplo de uso:

# Testando Produto e subclasses
print("\n--- Produtos ---")
p1 = Produto("Teclado", 100.0, 10)
p2 = ProdutoNacional("Monitor", 800.0, 5)
p3 = ProdutoImportado("Celular", 2000.0, 2, 0.2)

p1.exibir_detalhes()
p2.exibir_detalhes()
p3.exibir_detalhes()

print(f"Preço final do {p3.nome}: R${p3.preco_final():.2f}")
p3.emitir_nota()

# Testando Funcionários
print("\n--- Funcionários ---")
f1 = FuncionarioCLT("João", 3500.00)
f2 = FuncionarioPJ("Mariana", 160, 50)

print(f"{f1.nome} vai receber R${f1.calcular_pagamento():.2f}")
print(f"{f2.nome} vai receber R${f2.calcular_pagamento():.2f}")
