import pytest
from enafood.entidades.principal.status_pedido import StatusPedido
from enafood.excecoes.excecao_alteracao_status_invalida import ExcecaoAlteracaoDeStatusInvalida
from enafood.excecoes.excecao_pedido_vazio import ExcecaoPedidoVazio

from tests.fabricas.entidades.fabrica_cartao import FabricaCartao
from tests.fabricas.entidades.fabrica_pedido import FabricaPedido

def test_calcular_valor_total_sucesso():
    """
    Teste de unidade para o método calcular_valor_total.
    Aqui eu espero que o valor total seja igual ao preço unitário de cada pedido multiplicado pela quantidade.
    Aqui estou testando o caminho feliz, ou seja, o cálculo é feito conforme esperado.

    :return: None
    """

    # setup
    pedido = FabricaPedido().fabricar_pedido_com_1_produto()

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
    pedido = FabricaPedido().fabricar_pedido_com_1_produto()

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
    pedido = FabricaPedido().fabricar_pedido_com_1_produto()

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
    pedido = FabricaPedido().fabricar_pedido_status_em_conferencia()

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
    pedido = FabricaPedido().fabricar_pedido_com_1_produto()

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
    pedido = FabricaPedido().fabricar_pedido_status_em_conferencia()

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
    pedido = FabricaPedido().fabricar_pedido_com_1_produto()

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
    pedido = FabricaPedido().fabricar_objeto_basico()

    with pytest.raises(ExcecaoPedidoVazio):
        # execução
        pedido.conferir_pedido()

    assert pedido.status == StatusPedido.EM_COMPRA


def test_alterar_status_emconferencia_empagamento_sucesso():
    """
    Teste de unidade para o método alterar_status_pedido.
    Aqui eu espero que o status do pedido seja alterado para PAGAMENTO_APROVADO.
    Aqui estou testando o caminho feliz, ou seja, o status é alterado com sucesso.
    :return: None
    """

    # setup
    pedido = FabricaPedido().fabricar_pedido_status_em_conferencia()
    cartao = FabricaCartao().fabricar_objeto_basico()
    pedido.pagamento = cartao
    cartao.pedido = pedido

    # execução
    pedido.realizar_pagamento()

    # asserts
    assert pedido.status == StatusPedido.PAGAMENTO_APROVADO

    assert pedido.historico is not None, "É esperado que o pedido tenha o histórico inicializado"
    assert len(pedido.historico) == 5, "É esperado que o pedido tenha 5 eventos registrados no seu histórico"
    ultimo_evento = pedido.historico[-1]
    assert ultimo_evento.status == StatusPedido.PAGAMENTO_APROVADO, "É esperado que o último evento seja a aprovação do pedido"

def test_alterar_status_emconferencia_empagamento_cartao_invalido():
    """
    Teste de unidade para o método alterar_status_pedido.
    Aqui eu espero que o status do pedido seja alterado para EM_PAGAMENTO.
    Aqui estou testando o caminho alternativo, ou seja, o cartão
    está inválido
    :return: None
    """

    # setup
    pedido = FabricaPedido().fabricar_pedido_status_em_conferencia()
    cartao = FabricaCartao().fabricar_objeto_basico()
    pedido.pagamento = cartao
    cartao.pedido = pedido

    # execução
    cartao.invalidar_cartao()
    pedido.realizar_pagamento()

    # asserts
    assert pedido.status == StatusPedido.EM_PAGAMENTO

    assert pedido.historico is not None, "É esperado que o pedido tenha o histórico inicializado"
    assert len(pedido.historico) == 4, "É esperado que o pedido tenha 3 eventos registrados no seu histórico"
    ultimo_evento = pedido.historico[-1]
    assert ultimo_evento.status == StatusPedido.EM_PAGAMENTO, "É esperado que o último evento seja a volta do status para em pagamento"
