from kafka import KafkaProducer, KafkaConsumer

from src.core.entity import StocksOffer
from src.contracts.message import StocksOfferMessageContract
from src.infra.kafka.connection import KafkaConnection


class StocksOfferKafkaMessage(StocksOfferMessageContract):

    _producer: KafkaProducer
    _consumer: KafkaConsumer

    def __init__(self):
        connection = KafkaConnection()
        self._producer = connection.get_producer()
        self._consumer = connection.get_consumer()



    def send_offers_notifications(self, stock_offer: StocksOffer) -> None:
        self._producer.send('offers', stock_offer.__dict__)
        self._producer.flush()
        print("Notified by Kafka")

    def listening_offers(self):
        self._consumer.subscribe(['offers'])

        for msg in self._consumer:
            print('Consuming in Kafka')
            print(msg.value)
