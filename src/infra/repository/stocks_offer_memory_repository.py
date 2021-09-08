from typing import List
from uuid import uuid4

from src.core.entity import StocksOffer
from src.contracts.database import StocksOfferDatabaseContract
from src.handlers.not_found_exception import NotFoundException


class StocksOfferMemoryRepository(StocksOfferDatabaseContract):

    offers: List[StocksOffer] = []

    def get_all_offers(self) -> List[StocksOffer]:
        return self.offers


    def get_stock_by_ticket(self, ticket: str) -> StocksOffer:
        stock = list(filter(lambda x: x.ticket == ticket, self.offers))

        if len(stock) > 0:
            return stock[0]
        else:
            raise NotFoundException('The offer not founded in DB')


    def generate_offer(self, stock_offer: StocksOffer) -> StocksOffer:
        stock_offer._id = str(uuid4())
        self.offers.append(stock_offer)
        
        return stock_offer
