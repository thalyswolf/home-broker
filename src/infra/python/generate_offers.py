from src.infra.message.stocks_offer_memory_message import StocksOfferMemoryMessage
from src.infra.providers.memory_stocks.stocks import MemoryStocksProvider
from src.infra.repository import StocksOfferMemoryRepository
from src.core.usecase import GenerateOffers

memory_stocks_provider = MemoryStocksProvider()
stocks_offer_memory_repository = StocksOfferMemoryRepository()
stocks_offer_memory_message = StocksOfferMemoryMessage()

stocks = GenerateOffers(memory_stocks_provider, stocks_offer_memory_repository, stocks_offer_memory_message).execute()

for item in stocks:
    print(item.__dict__)
