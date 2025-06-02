class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} unidades")

    def preco_final(self):
        return self.preco


class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)

    def preco_final(self):
        return super().preco_final()  # Mesmo comportamento do Produto


class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao

    def preco_final(self):
        return self.preco * (1 + self.taxa_importacao)

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço c/ Importação: R${self.preco_final():.2f} | Estoque: {self.estoque} unidades")
