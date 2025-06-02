from produto import Produto
from produto import ProdutoImportado
from produto import ProdutoNacional

# Exemplo de uso:

# Criando produtos
p1 = Produto("Fone", 150.00, 30)
p2 = ProdutoNacional("Mouse", 80.00, 60)
p3 = ProdutoImportado("Tablet", 1200.00, 10, 0.25)

# Emitindo notas
p1.emitir_nota()
p2.emitir_nota()
p3.emitir_nota()
