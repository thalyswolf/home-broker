from src.infra.providers.memory_stocks.stocks import MemoryStocksProvider
from src.core.usecase import ListStocks

memory_stocks_provider = MemoryStocksProvider()

list_stocks = ListStocks(memory_stocks_provider).execute()

for item in list_stocks:
    print(item.__dict__)