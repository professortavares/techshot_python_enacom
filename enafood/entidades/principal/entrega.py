from dataclasses import dataclass

from enafood.entidades.principal.entregador import Entregador
from enafood.entidades.principal.pedido import Pedido
from enafood.entidades.principal.avaliacao import Avaliacao

@dataclass
class Entrega:
    entregador:Entregador
    pedido:Pedido
    avaliacao:Avaliacao