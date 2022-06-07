from dataclasses import dataclass

from enafood.entidades.principal.avaliacao import Avaliacao
from enafood.entidades.principal.menu import Menu

@dataclass
class Fornecedor:
    nome: str
    avaliacoes:list[Avaliacao]
    menus:list[Menu]
    # todo: implementar método para calcular a média de avaliações