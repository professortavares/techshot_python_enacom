class ExcecaoPedidoVazio(Exception):
    def __init__(self):
        self.message = f"O pedido está vazio."
