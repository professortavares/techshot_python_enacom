from dataclasses import dataclass
from enafood.entidades.util.foto import Foto
from enafood.entidades.principal.produto_no_pedido import ProdutoNoPedido


@dataclass
class Produto:
    nome:str
    descricao:str
    foto:Foto
    preco_unitario:float
    versao:int
    data_ultima_alteracao:str
    pedidos:list[ProdutoNoPedido]