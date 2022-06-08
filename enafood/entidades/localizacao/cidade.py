from dataclasses import dataclass
import enafood.entidades.localizacao as loc

@dataclass
class Cidade:
    """
    Classe que representa uma cidade.
    """
    nome:str
    uf:any
