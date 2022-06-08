from dataclasses import dataclass


@dataclass
class Avaliacao:
    nota:int
    descricao:str
    entrega:any
    fornecedor:any