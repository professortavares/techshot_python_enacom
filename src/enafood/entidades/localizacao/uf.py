from dataclasses import dataclass

from src.enafood.entidades.localizacao.cidade import Cidade

@dataclass
class Uf:
    sigla: str
    nome: str
    cidades: list[Cidade] = None