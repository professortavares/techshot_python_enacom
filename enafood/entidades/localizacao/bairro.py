from dataclasses import dataclass

from enafood.entidades.localizacao.cidade import Cidade

@dataclass
class Bairro:
    nome: str
    cidade:Cidade