from dataclasses import dataclass

@dataclass
class Cliente:
    nome:str
    enderecos:any=None
    endereco_padrao:any=None
    pedidos:list[any]=None
