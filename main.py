from produto import Produto


# Exemplo de uso:

p = Produto("Monitor", 800.00, 10)

p.exibir_detalhes()
p.vender(3)
p.repor(5)
p.vender(20)   # Estoque insuficiente
p.vender(-1)   # Valor inválido
p.repor(0)     # Valor inválido