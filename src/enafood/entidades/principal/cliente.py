from dataclasses import dataclass
from src.enafood.entidades.localizacao.endereco import Endereco
from src.enafood.entidades.principal.pedido import Pedido

@dataclass
class Cliente:
    nome:str
    enderecos:list[Endereco]
    endereco_padrao:Endereco
    pedidos:list[Pedido]
