import json
from threading import Timer

import Ice
from confluent_kafka import Consumer, Message

from .publisher import Publisher
from .worker import Worker


class Receiver:
    def __init__(self, broker: str, group: str, topic: str, producer: Publisher):
        config = {
            "bootstrap.servers": broker,
            "group.id": group,
        }
        
        self.kconsumer = Consumer(**config)
        self.kconsumer.subscribe([topic])
        self.producer = producer
        self.comm = Ice.initialize()
    
    def run(self):
        while True:
            for msg in self.kconsumer.consume():
                print("Msg received...")
                self.process_single_event(msg.value())
    
    def process_single_event(self, value: bytes) -> None:
        # Check JSON schema
        try:
            event = json.loads(value)

            if not isinstance(event, dict):
                print("Message discarded")
                return

            proxy = self.comm.stringToProxy(event.get("proxy"))
            delay = event.get("delay", None)
            worker = Worker(proxy, self.producer, delay)
            worker.start()

        except json.JSONDecodeError as ex:
            print("Message discarded")            
            return
    
    def __del__(self):
        self.comm.destroy()
