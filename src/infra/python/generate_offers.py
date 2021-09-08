from src.infra.providers.memory_stocks.stocks import MemoryStocksProvider
from src.infra.repository import StocksOfferMemoryRepository
from src.core.usecase import GenerateOffers

memory_stocks_provider = MemoryStocksProvider()
stocks_offer_memory_repository = StocksOfferMemoryRepository()

stocks = GenerateOffers(memory_stocks_provider, stocks_offer_memory_repository).execute()

for item in stocks:
    print(item.__dict__)
