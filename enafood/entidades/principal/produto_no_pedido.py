from dataclasses import dataclass
from enafood.entidades.principal.pedido import Pedido
from enafood.entidades.principal.produto import Produto

@dataclass
class ProdutoNoPedido:
    pedido: Pedido
    produto: Produto