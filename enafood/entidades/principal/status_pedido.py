from enum import Enum

class StatusPedido(Enum):
    EM_COMPRA = 0
    EM_CONFERENCIA = 1
    EM_PAGAMENTO = 2
    CARTAO_INVALIDO = 3
    CARTAO_VALIDO = 4
    CARTAO_ATIVO = 5
    PAGAMENTO_APROVADO = 6
    AGUARDANDO_ENTREGA = 7
    NO_CAMINHO_PARA_ENTREGA = 8
    ENTREGA_REALIZADA = 9
