from typing import List
from abc import ABC, abstractmethod

from src.core.entity import StocksOffer


class StocksOfferDatabaseContract(ABC):

    @abstractmethod
    def get_all_offers(self) -> List[StocksOffer]:
        pass

    @abstractmethod
    def get_stock_by_ticket(self, ticket: str) -> StocksOffer:
        pass

    @abstractmethod
    def generate_offer(self, stock_offer: StocksOffer) -> StocksOffer:
        pass
