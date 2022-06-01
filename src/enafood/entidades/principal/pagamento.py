from dataclasses import dataclass
from src.enafood.entidades.principal.pedido import Pedido

@dataclass
class Pagamento:
    pedido: Pedido