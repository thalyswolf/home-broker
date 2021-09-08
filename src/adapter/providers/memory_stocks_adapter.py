from typing import Dict
from src.core.entity import Stocks


class MemoryStocksAdapter:

    def create(result: Dict) -> Stocks:
        return Stocks(
            company_name=result['name'],
            ticket=result['ticket'],
            line_of_business=result['lineOfBusiness'],
            price_sell=result['priceSell'],
            price_buy=result['priceBuy']
        )
