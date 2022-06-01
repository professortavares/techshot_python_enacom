from dataclasses import dataclass
from src.enafood.entidades.util.foto import Foto
from src.enafood.entidades.principal.produto_no_pedido import ProdutoNoPedido


@dataclass
class Produto:
    nome:str
    descricao:str
    foto:Foto
    preco_unitario:float
    versao:int
    data_ultima_alteracao:str
    pedidos:list[ProdutoNoPedido]