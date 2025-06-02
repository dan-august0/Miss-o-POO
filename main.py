from produto import Produto
from produto import ProdutoImportado
from produto import ProdutoNacional

# Exemplo de uso:
p = Produto("Teclado", 100.0, 20)
p.exibir_detalhes()

nacional = ProdutoNacional("Livro", 50.0, 10)
nacional.exibir_detalhes()

importado = ProdutoImportado("Celular", 2000.0, 5, 0.15)
importado.exibir_detalhes()