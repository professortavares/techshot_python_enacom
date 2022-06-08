from dataclasses import dataclass
import enafood.entidades.principal as prinp

@dataclass
class Pedido:
    data: str
    valor_entrega:float
    produtos: list[any]
    pagamento: any
    historico: list[any]
    cliente: any
    status: any

    # todo: colocar um status para o pedido
    # todo: colocar função para calcular valor total