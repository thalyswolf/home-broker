from src.infra.providers.memory_stocks.stocks import MemoryStocksProvider
from src.core.usecase import GetStocksByTicket

memory_stocks_provider = MemoryStocksProvider()

stocks = GetStocksByTicket(memory_stocks_provider).execute('ABEV3')

print(stocks.__dict__)