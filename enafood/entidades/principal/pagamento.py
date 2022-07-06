from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Pagamento(ABC):
    pedido: any

    @abstractmethod
    def realizar_pagamento(self):
        """
        Realiza o pagamento do pedido
        :return:
        """
        pass