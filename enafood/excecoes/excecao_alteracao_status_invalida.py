
class ExcecaoAlteracaoDeStatusInvalida(Exception):
    def __init__(self,
                 status_pedido_atual=None,
                 status_pedido_novo=None):
        message = f"Esta alteração não está prevista em nosso workflow de status do pedido {status_pedido_atual} -> {status_pedido_novo}.",
        self.message = message