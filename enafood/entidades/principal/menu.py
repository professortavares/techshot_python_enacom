from dataclasses import dataclass
from enafood.entidades.principal.fornecedor import Fornecedor


@dataclass
class Menu:
    categoria: str
    fornecedor: Fornecedor
