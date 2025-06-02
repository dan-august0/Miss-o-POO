class Produto:
   def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

   def exibir_detalhes(self):
            print(f"Produto: {self.nome} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} unidades")

   def preco_final(self):
            return self.preco

   def emitir_nota(self):
            print(f"Nota gerada para {self.nome}.")

   def repor(self, quantidade):
            if quantidade > 0:
                self.estoque += quantidade
                print(f"{quantidade} unidades de {self.nome} adicionadas ao estoque. Estoque atual: {self.estoque}")
            else:
                print("A quantidade para reposição deve ser positiva.")

   def vender(self, quantidade):
            if quantidade <= 0:
                print("A quantidade para venda deve ser positiva.")
            elif quantidade > self.estoque:
                print(f"Estoque insuficiente para vender {quantidade} unidades de {self.nome}. Estoque atual: {self.estoque}")
            else:
                self.estoque -= quantidade
                print(f"{quantidade} unidades de {self.nome} vendidas. Estoque restante: {self.estoque}")


class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)

    def preco_final(self):
        return super().preco_final()

    def emitir_nota(self):
        print(f"Nota fiscal nacional para {self.nome}.")


class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao

    def preco_final(self):
        return self.preco * (1 + self.taxa_importacao)

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço c/ Importação: R${self.preco_final():.2f} | Estoque: {self.estoque} unidades")

    def emitir_nota(self):
        print(f"Nota de importação para {self.nome} com taxa aplicada.")
