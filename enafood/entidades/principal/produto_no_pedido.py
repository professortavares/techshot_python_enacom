from dataclasses import dataclass

@dataclass
class ProdutoNoPedido:
    quantidade: int
    produto: any
    pedido: any = None

    def calcular_valor_total(self) -> float:
        """
        Calcula o valor total do produto no pedido
        :return: float - preco unitário * quantidade
        """
        return self.produto.preco_unitario * self.quantidade
