from dataclasses import dataclass

@dataclass
class Produto:
    nome:str
    descricao:str
    preco_unitario:float
    foto:any=None
    versao:int=0
    data_ultima_alteracao:str=None
    pedidos:list[any]=None
