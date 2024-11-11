"""Consumer example."""

import sys

from confluent_kafka import Consumer


def create_consumer(bootstrap_server: str, consumer_group: str) -> Consumer:
    """Create a new Consumer for the given consumer group."""

    config = {
        "bootstrap.servers": bootstrap_server,
        "group.id": consumer_group,
    }
    return Consumer(**config)


def consume_messages_loop(consumer: Consumer, topic: str) -> None:
    """Consume messages from the given topic."""
    consumer.subscribe([topic])

    while True:
        for msg in consumer.consume():
            print(f"Event received: {msg.value()}")

            if msg.key() == b"STOP":
                print("Stop sign received")
                return


if __name__ == "__main__":
    server = sys.argv[1]
    topic = sys.argv[2]
    consumer_group = sys.argv[3]

    consumer = create_consumer(server, consumer_group)
    consume_messages_loop(consumer, topic)
    print("Program end")
