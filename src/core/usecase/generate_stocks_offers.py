from typing import List
from time import time

from src.contracts.providers import StocksProvidersContract
from src.contracts.database import StocksOfferDatabaseContract
from src.core.entity import StocksOffer

""" 
    1 - Consult values in provider
    2 - Insert Offers in database 
    3 - Notify the microservices notifications
"""

class GenerateOffers:


    def __init__(self, stocks_provider: StocksProvidersContract, stocks_offer_repository: StocksOfferDatabaseContract):
        self.stocks_provider = stocks_provider
        self.stocks_offer_repository = stocks_offer_repository

    def execute(self) -> List[StocksOffer]:
        stocks_providers = self.stocks_provider.list_all_stocks()

        for item in stocks_providers:
            offer = StocksOffer()
            offer.price_buy = item.price_buy
            offer.price_sell = item.price_sell
            offer.ticket = item.ticket
            offer.expire_timestamp = int(time()) + 900

            self.stocks_offer_repository.generate_offer(offer)

        stocks_generated = self.stocks_offer_repository.get_all_offers()

        return stocks_generated
