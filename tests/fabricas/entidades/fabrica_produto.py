from tests.fabricas.fabrica_abstrata import FabricaAbstrata
from enafood.entidades.principal.produto import Produto
from faker import Faker

class FabricaProduto(FabricaAbstrata):

    def fabricar_objeto_basico(self):
        """
        Cria uma instância básica de produto.
        Cada produto custa originalmente R$ 10,00.
        :return: Produto
        """
        fake = Faker()
        produto = Produto(nome=fake.name(),
                          descricao=fake.text(),
                          preco_unitario=10.0)
        return produto
