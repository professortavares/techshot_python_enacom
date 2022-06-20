import pytest
from faker import Faker

from enafood.entidades.principal.produto import Produto
from enafood.entidades.principal.produto_no_pedido import ProdutoNoPedido
from enafood.entidades.principal.pedido import Pedido
from enafood.entidades.principal.status_pedido import StatusPedido
from enafood.excecoes.excecao_alteracao_status_invalida import ExcecaoAlteracaoDeStatusInvalida
from enafood.excecoes.excecao_pedido_vazio import ExcecaoPedidoVazio

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


def test_status_inicial_pedido():
    """
    Teste de unidade para o método status_inicial_pedido.
    Aqui eu espero que o status inicial do pedido seja EM_COMPRA.
    Aqui estou testando o caminho feliz, ou seja, o status inicial é o esperado.

    :return: None
    """

    # setup
    pedido = Pedido(data="01/01/2020",
                    valor_entrega=10.0,
                    produtos=[])
    # execução
    status_inicial = pedido.status

    # asserts
    assert status_inicial == StatusPedido.EM_COMPRA

def test_alterar_status_pedido_em_compra_para_em_conferencia():
    """
    Teste de unidade para o método alterar_status_pedido.
    Aqui eu espero que o status do pedido seja alterado para EM_CONFERENCIA.
    Aqui estou testando o caminho feliz, ou seja, o status é alterado com sucesso.

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

    # pre assert
    assert pedido.historico is None, "É esperado que o pedido não tenha histórico"

    # execução
    pedido.conferir_pedido()

    # asserts
    assert pedido.status == StatusPedido.EM_CONFERENCIA

    assert pedido.historico is not None, "É esperado que o pedido tenha o histórico inicializado"
    assert len(pedido.historico) == 1, "É esperado que o pedido tenha 1 evento no seu histórico"
    ultimo_evento = pedido.historico[-1]
    assert ultimo_evento.status == StatusPedido.EM_CONFERENCIA, "É esperado que o último evento seja a conferência do pedido"



def test_alterar_status_pedido_em_conferencia_para_em_compra():
    """
    Teste de unidade para o método alterar_status_pedido.
    Aqui eu espero que o status do pedido seja alterado para EM_COMPRA.
    Aqui estou testando o caminho feliz, ou seja, o status é alterado com sucesso.

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

    pedido.conferir_pedido()

    # execução
    pedido.voltar_pedido_em_compra()

    # asserts
    assert pedido.status == StatusPedido.EM_COMPRA

    assert pedido.historico is not None, "É esperado que o pedido tenha o histórico inicializado"
    assert len(pedido.historico) == 2, "É esperado que o pedido tenha 1 evento no seu histórico"
    ultimo_evento = pedido.historico[-1]
    assert ultimo_evento.status == StatusPedido.EM_COMPRA, "É esperado que o último evento seja a conferência do pedido"


def test_alterar_status_pedido_em_compra_para_em_pagamento():
    """
    Teste de unidade para o método alterar_status_pedido.
    Aqui eu espero que o status do pedido seja alterado para EM_PAGAMENTO.
    Aqui estou testando o caminho alternativo, ou seja, o status não é alterado
    e a exceção é levantada.

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


    with pytest.raises(ExcecaoAlteracaoDeStatusInvalida):
        # execução
        pedido.alterar_status_pedido(StatusPedido.EM_PAGAMENTO)

def test_alterar_status_pedido_em_conferencia_para_cartao_valido():
    """
    Teste de unidade para o método alterar_status_pedido.
    Aqui eu espero que o status do pedido seja alterado para CARTÃO_VALIDO.
    Aqui estou testando o caminho alternativo, ou seja, o status não é alterado
    e a exceção é levantada.

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

    pedido.alterar_status_pedido(StatusPedido.EM_CONFERENCIA)

    # execução
    with pytest.raises(ExcecaoAlteracaoDeStatusInvalida):
        pedido.alterar_status_pedido(StatusPedido.CARTAO_VALIDO)


def test_conferir_pedido_sucesso():
    """
    Teste de unidade para o método conferir_pedido.
    Aqui eu espero que o status do pedido seja alterado para EM CONFERÊNCIA.
    Aqui estou testando o caminho feliz, ou seja, o status é alterado com sucesso.

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
    pedido.conferir_pedido()

    # asserts
    assert pedido.status == StatusPedido.EM_CONFERENCIA


def test_conferir_pedido_vazio():
    """
    Teste de unidade para o método conferir_pedido.
    Aqui eu espero que seja levanta uma exceção me informando
    que o pedido está vazio.

    :return: None
    """

    # setup
    pedido = Pedido(data="01/01/2020",
                    valor_entrega=10.0,
                    produtos=[])

    with pytest.raises(ExcecaoPedidoVazio):
        # execução
        pedido.conferir_pedido()

    assert pedido.status == StatusPedido.EM_COMPRA