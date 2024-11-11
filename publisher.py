"""Publisher example."""

import sys

from confluent_kafka import Producer


def create_publisher(bootstrap_server: str) -> Producer:
    """Generate a Publisher for the given server."""
    return Producer(**{"bootstrap.servers": bootstrap_server})


def send_message(producer: Producer, topic: str, payload: str, key: str) -> None:
    """Send a single message to the given topic."""
    producer.produce(topic, payload, key)



if __name__ == "__main__":
    server = sys.argv[1]
    topic = sys.argv[2]
    message = sys.argv[3]

    key = sys.argv[4] if len(sys.argv) >= 5 else None
    
    publisher = create_publisher(server)
    send_message(publisher, topic, message, key)
    publisher.flush()
