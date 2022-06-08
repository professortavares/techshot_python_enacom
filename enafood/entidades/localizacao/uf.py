from dataclasses import dataclass

@dataclass
class Uf:
    sigla: str
    nome: str
    cidades: list[any] = None