from dataclasses import dataclass

from enafood.entidades.localizacao.bairro import Bairro
from enafood.entidades.localizacao.cidade import Cidade
from enafood.entidades.localizacao.uf import Uf

@dataclass
class Endereco:
    """
    Classe que representa um endereço.
    """
    rua: str
    numero: int
    bairro: Bairro
    cidade: Cidade
    estado: Uf
    cep: str
    # este complemento nem sempre é necessário no endereço
    complemento: str = None