from json import dumps, loads
from typing import Dict

from kafka import KafkaProducer, KafkaConsumer


class KafkaConnection:
    _instance = None
    _consumer: KafkaConsumer = None
    _producer: KafkaProducer = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance


    def __init__(self):
        pass

    def get_producer(self, message: Dict) -> KafkaProducer:
        if self._producer is None:
            self._producer = KafkaProducer(
                bootstrap_servers=['localhost:9092'],
                value_serializer=lambda v: dumps(v).encode('utf-8'))

        return self._producer


    def get_consumer(self, message: Dict) -> KafkaConsumer :
        if self._consumer is None:
            self._consumer = KafkaConsumer(
                bootstrap_servers='localhost:9092',
                auto_offset_reset='earliest',
                # consumer_timeout_ms=1000,
                value_deserializer = loads)
        
        return self._consumer
