from dataclasses import dataclass
from enafood.entidades.principal.pagamento import Pagamento
from enafood.entidades.principal.status_cartao import StatusCartao

@dataclass
class Cartao(Pagamento):

    numero: str
    nome_titular: str
    data_validade: str
    cvv: str
    eh_valido: bool
    eh_ativo: bool
    # Existe simplesmente para facilitar o teste
    pagamento_aprovado = True

    def invalidar_cartao(self):
        self.eh_valido = False

    def realizar_pagamento(self):
        # Primeira verificação: cartão válido
        if self.eh_valido:
            self.pedido.notificar_pagamento(StatusCartao.CARTAO_VALIDO)

            # Segunda verificação: cartão ativo
            if self.eh_ativo:
                self.pedido.notificar_pagamento(StatusCartao.CARTAO_ATIVO)

                if self.aprovar_pagamento():
                    self.pedido.notificar_pagamento(StatusCartao.PAGAMENTO_APROVADO)

            else: self.pedido.notificar_pagamento(StatusCartao.CARTAO_INATIVO)
        else: self.pedido.notificar_pagamento(StatusCartao.CARTAO_INVALIDO)

    def aprovar_pagamento(self):
        return self.pagamento_aprovado
