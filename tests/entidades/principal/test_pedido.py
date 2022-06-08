from faker import Faker

from enafood.entidades.principal.produto import Produto
from enafood.entidades.principal.produto_no_pedido import ProdutoNoPedido
from enafood.entidades.principal.pedido import Pedido

def test_calcular_valor_total_sucesso():
    """
Teste de unidade para o método calcular_valor_total.
    Aqui eu espero que o valor total seja igual ao preço unitário de cada pedido multiplicado pela quantidade.
    Aqui estou testando o caminho feliz, ou seja, o cálculo é feito conforme esperado.

    :return: None
    """

    # setup
    fake = Faker()
    produto = Produto(nome=fake.name(),
                      descricao=fake.text(),
                      preco_unitario=10.0)
    produto_no_pedido01 = ProdutoNoPedido(quantidade=2,
                                        produto=produto)

    pedido = Pedido(data="01/01/2020",
                    valor_entrega=10.0,
                    produtos=[produto_no_pedido01])
    # execução
    valor_total = pedido.calcular_valor_total()

    # asserts
    assert valor_total == 30.0
