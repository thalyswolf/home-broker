from src.core.entity import StocksOffer
from src.contracts.message import StocksOfferMessageContract

"""
    The objective this class is simulate a message sent by Apache Kafka or other service of message
"""
class StocksOfferMemoryMessage(StocksOfferMessageContract):


    def send_offers_notifications(self, stock_offer: StocksOffer) -> None:
        """ Just mock!!! is not need returning values """
        print('Notifing {} ...'.format(stock_offer.ticket))
        print('Notified {}'.format(stock_offer.ticket))
