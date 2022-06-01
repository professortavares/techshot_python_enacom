from dataclasses import dataclass

from src.enafood.entidades.principal.avaliacao import Avaliacao
from src.enafood.entidades.principal.menu import Menu

@dataclass
class Fornecedor:
    nome: str
    avaliacoes:list[Avaliacao]
    menus:list[Menu]
    # todo: implementar método para calcular a média de avaliações