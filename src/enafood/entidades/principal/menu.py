from dataclasses import dataclass
from src.enafood.entidades.principal.fornecedor import Fornecedor


@dataclass
class Menu:
    categoria: str
    fornecedor: Fornecedor
