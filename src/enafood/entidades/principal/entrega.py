from dataclasses import dataclass

from src.enafood.entidades.principal.entregador import Entregador
from src.enafood.entidades.principal.pedido import Pedido
from src.enafood.entidades.principal.avaliacao import Avaliacao

@dataclass
class Entrega:
    entregador:Entregador
    pedido:Pedido
    avaliacao:Avaliacao