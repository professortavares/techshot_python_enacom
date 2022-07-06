from enum import Enum

class StatusCartao(Enum):
    CARTAO_VALIDO = 0
    CARTAO_ATIVO = 1
    PAGAMENTO_APROVADO = 2
    CARTAO_INVALIDO = 3
    CARTAO_INATIVO = 4