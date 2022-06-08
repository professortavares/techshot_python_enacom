from dataclasses import dataclass

@dataclass
class Fornecedor:
    nome: str
    avaliacoes:list[any]
    menus:list[any]
    # todo: implementar método para calcular a média de avaliações