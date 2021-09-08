from unittest import TestCase, main

from src.infra.providers.memory_stocks.stocks import MemoryStocksProvider
from src.infra.repository import StocksOfferMemoryRepository
from src.infra.message.stocks_offer_memory_message import StocksOfferMemoryMessage
from src.core.usecase import GenerateOffers

class GenerateOfferTest(TestCase):

    def test_insert_offer_in_db(self):
        ticket = 'ABEV3'
        memory_stocks_provider = MemoryStocksProvider()
        stocks_offer_memory_repository = StocksOfferMemoryRepository()
        stocks_offer_memory_message = StocksOfferMemoryMessage()

        stocks = GenerateOffers(memory_stocks_provider, stocks_offer_memory_repository, stocks_offer_memory_message).execute()
        TestCase().assertTrue(isinstance(stocks, list))


        stock = stocks_offer_memory_repository.get_stock_by_ticket(ticket)

        TestCase().assertEqual(stock.ticket, ticket)
        TestCase().assertTrue(isinstance(stock.price_buy, float))
        TestCase().assertTrue(isinstance(stock.price_sell, float))
        TestCase().assertTrue(isinstance(stock._id, str))
        TestCase().assertTrue(isinstance(stock.expire_timestamp, int))

if __name__ == '__main__':
    main()
