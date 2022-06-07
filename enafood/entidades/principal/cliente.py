from dataclasses import dataclass
from enafood.entidades.localizacao.endereco import Endereco
from enafood.entidades.principal.pedido import Pedido

@dataclass
class Cliente:
    nome:str
    enderecos:list[Endereco]
    endereco_padrao:Endereco
    pedidos:list[Pedido]
