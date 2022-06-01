from dataclasses import dataclass

from src.enafood.entidades.localizacao.cidade import Cidade

@dataclass
class Bairro:
    nome: str
    cidade:Cidade