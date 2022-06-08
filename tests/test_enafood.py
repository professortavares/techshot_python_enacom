from enafood import __version__
from faker import Faker

from enafood.entidades.principal.cliente import Cliente

def test_exemplo():
    fake = Faker()
    assert isinstance(fake.name(), str)

def test_criar_entidade():
    # setup (criação do objeto)
    fake = Faker()
    cliente = Cliente(nome=fake.name())

    assert cliente.nome is not None

def test_version():
    assert __version__ == '0.1.2'
