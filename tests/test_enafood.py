from enafood import __version__
from faker import Faker

def test_exemplo():
    fake = Faker()
    assert isinstance(fake.name(), str)

def test_version():
    assert __version__ == '0.1.0'
