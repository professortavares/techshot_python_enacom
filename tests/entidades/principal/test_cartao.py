from tests.fabricas.entidades.fabrica_cartao import FabricaCartao


def test_testar_criacao_objeto():
    cartao = FabricaCartao().fabricar_objeto_basico()
    assert cartao is not None