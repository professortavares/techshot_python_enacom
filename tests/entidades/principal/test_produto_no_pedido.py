from faker import Faker

from enafood.entidades.principal.produto import Produto
from enafood.entidades.principal.produto_no_pedido import ProdutoNoPedido

def test_calcular_valor_total_sucesso():
    """
    Teste de unidade para o método calcular_valor_total.
    Aqui eu espero que o valor total seja igual ao preço unitário multiplicado pela quantidade.
    Aqui estou testando o caminho feliz, ou seja, o cálculo é feito conforme esperado.

    :return: None
    """

    # setup
    fake = Faker()
    produto = Produto(nome=fake.name(),
                      descricao=fake.text(),
                      preco_unitario=10.0)
    produto_no_pedido = ProdutoNoPedido(quantidade=2,
                                        produto=produto)

    # execução
    valor_total = produto_no_pedido.calcular_valor_total()

    # asserts
    assert valor_total == 20.0

def test_calcular_valor_total_quantidade_zero():
    """
    Teste de unidade para o método calcular_valor_total.
    Aqui eu espero que o valor total seja igual ao preço unitário multiplicado pela quantidade.
    Aqui estou testando um caminho alternativo, ou seja, a quantidade 0 deveria retornar 0.0.

    :return: None
    """

    # setup
    fake = Faker()
    produto = Produto(nome=fake.name(),
                      descricao=fake.text(),
                      preco_unitario=10.0)
    produto_no_pedido = ProdutoNoPedido(quantidade=0,
                                        produto=produto)

    # execução
    valor_total = produto_no_pedido.calcular_valor_total()

    # asserts
    assert valor_total == 0.0