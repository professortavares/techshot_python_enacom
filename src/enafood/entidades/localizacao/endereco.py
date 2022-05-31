from dataclasses import dataclass

@dataclass
class Endereco:
    """
    Classe que representa um endereço.
    """
    rua: str
    numero: int
    bairro: Bairro
    cidade: Cidade
    estado: UF
    cep: str
    # este complemento nem sempre é necessário no endereço
    complemento: str = None