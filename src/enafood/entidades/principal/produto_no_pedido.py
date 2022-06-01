from dataclasses import dataclass
from src.enafood.entidades.principal.pedido import Pedido
from src.enafood.entidades.principal.produto import Produto


class ProdutoNoPedido:
    pedido: Pedido
    produto: Produto