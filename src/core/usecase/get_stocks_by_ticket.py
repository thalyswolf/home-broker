from src.contracts.providers import StocksProvidersContract
from src.core.entity import Stocks


class GetStocksByTicket:

    def __init__(self, stocks_provider: StocksProvidersContract):
        self.stocks_provider = stocks_provider

    def execute(self, ticket: str) -> Stocks:
        return self.stocks_provider.get_stock_by_ticket(ticket=ticket)
