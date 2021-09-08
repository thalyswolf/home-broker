from typing import List
from abc import ABC, abstractmethod

from src.core.entity import StocksOffer


class StocksOfferMessageContract(ABC):

    @abstractmethod
    def send_offers_notifications(self, stock_offer: StocksOffer) -> None:
        pass
