from __future__ import annotations
from abc import ABC, abstractmethod


class FabricaAbstrata(ABC):

    @abstractmethod
    def fabricar_objeto_basico(self):
        """
        Cria um objeto básico de uma determinada entidade.
        :return: Objeto básico de uma determinada entidade.
        """
        pass