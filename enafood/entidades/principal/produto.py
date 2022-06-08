from dataclasses import dataclass

@dataclass
class Produto:
    nome:str
    descricao:str
    foto:any
    preco_unitario:float
    versao:int
    data_ultima_alteracao:str
    pedidos:list[any]