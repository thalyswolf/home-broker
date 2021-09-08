from typing import List
from abc import ABC, abstractmethod

from src.core.entity import Stocks


class StocksProvidersContract(ABC):

    @abstractmethod
    def list_all_stocks(self) -> List[Stocks]:
        pass

    @abstractmethod
    def get_stock_by_ticket(self, ticket: str) -> Stocks:
        pass
