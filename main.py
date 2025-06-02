from produto import Produto
from produto import ProdutoImportado
from produto import ProdutoNacional

# Exemplo de uso:

# Criando instâncias
produto = Produto("Caderno", 25.00, 50)
nacional = ProdutoNacional("Caneta", 3.50, 100)
importado = ProdutoImportado("Notebook", 3000.00, 10, 0.2)

# Exibindo preços finais
print(f"Preço final (Produto): R${produto.preco_final():.2f}")
print(f"Preço final (ProdutoNacional): R${nacional.preco_final():.2f}")
print(f"Preço final (ProdutoImportado): R${importado.preco_final():.2f}")