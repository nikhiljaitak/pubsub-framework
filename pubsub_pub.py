from pubsub_framework.broker import PubSubBroker
from pubsub_framework.publisher import Publisher
from pubsub_framework.subscriber import Subscriber

# Initialize the broker with project ID and credential file path
broker = PubSubBroker("adroit-particle-362414", "/Users/Downloads/adroit-particle-362414-913321d43362.json")

# Create Publisher
publisher = Publisher(broker)

# Publish a message
publisher.publish("test-1", "Hello, Guru")