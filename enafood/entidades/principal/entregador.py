from dataclasses import dataclass
from enafood.entidades.util.foto import Foto

@dataclass
class Entregador:
    nome: str
    foto:Foto
