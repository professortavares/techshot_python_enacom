from dataclasses import dataclass

@dataclass
class Cidade:
    """
    Classe que representa uma cidade.
    """
    nome:str
    uf:Uf
