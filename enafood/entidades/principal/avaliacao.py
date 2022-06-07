from dataclasses import dataclass

from enafood.entidades.principal.entrega import Entrega
from enafood.entidades.principal.fornecedor import Fornecedor

@dataclass
class Avaliacao:
    nota:int
    descricao:str
    entrega:Entrega
    fornecedor:Fornecedor