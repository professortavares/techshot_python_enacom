from dataclasses import dataclass
from enafood.entidades.localizacao.uf import Uf

@dataclass
class Cidade:
    """
    Classe que representa uma cidade.
    """
    nome:str
    uf:Uf
