from typing import Dict
from src.core.entity import Stocks


class MemoryStocksAdapter:

    def create(result: Dict) -> Stocks:
        stocks = Stocks()
        stocks.company_name = result['name']
        stocks.ticket = result['ticket']
        stocks.line_of_business = result['lineOfBusiness']
        stocks.price_sell = result['priceSell']
        stocks.price_buy = result['priceBuy']
        
        return stocks
