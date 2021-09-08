from unittest import TestCase, main

from src.infra.providers.memory_stocks.stocks import MemoryStocksProvider
from src.core.usecase import GetStocksByTicket

class GetStocksByTicketTest(TestCase):

    def test_shoud_return_correct_stocks_entity(self):
        ticket = 'ABEV3'
        memory_stocks_provider = MemoryStocksProvider()
        stocks = GetStocksByTicket(memory_stocks_provider).execute(ticket)

        TestCase().assertEqual(stocks.ticket, ticket)
        TestCase().assertEqual(stocks.company_name, 'AMBEV S/A')
        TestCase().assertEqual(stocks.line_of_business, 'Consumo não Cíclico / Bebidas / Cervejas e Refrigerantes')
        TestCase().assertTrue(isinstance(stocks.price_buy, float))
        TestCase().assertTrue(isinstance(stocks.price_sell, float))


if __name__ == '__main__':
    main()
