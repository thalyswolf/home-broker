from typing import List
from src.contracts.providers import StocksProvidersContract
from src.core.entity import Stocks


class ListStocks:

    def __init__(self, stocks_provider: StocksProvidersContract):
        self.stocks_provider = stocks_provider

    def execute(self) -> List[Stocks]:
        return self.stocks_provider.list_all_stocks()
