from kafka import KafkaProducer

from src.core.entity import StocksOffer
from src.contracts.message import StocksOfferMessageContract
from src.infra.kafka.connection import KafkaConnection


class StocksOfferKafkaMessage(StocksOfferMessageContract):

    _producer: KafkaProducer

    def __init__(self):
        self._producer = KafkaConnection().get_producer()


    def send_offers_notifications(self, stock_offer: StocksOffer) -> None:
        self._producer.send('offers', stock_offer.__dict__)
        self._producer.flush()
        print("Notified by Kafka")
