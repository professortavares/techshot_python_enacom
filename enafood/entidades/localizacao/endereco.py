from dataclasses import dataclass

@dataclass
class Endereco:
    """
    Classe que representa um endereço.
    """
    rua: str
    numero: int
    bairro:any
    cidade:any
    estado:any
    cep: str
    # este complemento nem sempre é necessário no endereço
    complemento: str = None