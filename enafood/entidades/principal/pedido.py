from dataclasses import dataclass
import enafood.entidades.principal as prinp

@dataclass
class Pedido:
    data: str
    valor_entrega:float
    produtos: list[any]
    pagamento: any=None
    historico: list[any]=None
    cliente: any=None
    status: any=None

    # Débito técnico
    # TODO: rever a obrigatoriedade dos campos

    def calcular_valor_total(self):
        """
        Calcula o valor total do pedido
        :return: float - preco unitário * quantidade
        """
        valor_total = 0.0
        for produto_no_pedido in self.produtos:
            valor_total += produto_no_pedido.calcular_valor_total()

        return valor_total + self.valor_entrega
