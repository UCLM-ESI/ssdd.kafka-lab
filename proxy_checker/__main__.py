import sys

from .consumer import Receiver
from .publisher import Publisher


broker, group, consumer_topic, publisher_topic = sys.argv[1:5]

publisher = Publisher(broker, publisher_topic)
consumer = Receiver(broker, group, consumer_topic, publisher)

consumer.run()
