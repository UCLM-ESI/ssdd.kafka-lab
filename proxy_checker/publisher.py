import json
from typing import Optional

from confluent_kafka import Producer


class Publisher:
    def __init__(self, server, topic):
        self.producer = Producer(**{"bootstrap.servers": server})
        self.topic = topic
    
    def notify_result(self, proxy: str, result: bool, ordinal: Optional[int] = 0):
        result_message = {
            "proxy": proxy,
            "result": result,
        }

        if ordinal > 0:
            result_message["iteration"] = ordinal
        
        self.producer.produce(self.topic, json.dumps(result_message).encode())
        self.producer.flush()
