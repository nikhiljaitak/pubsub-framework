# pubsub/publisher.py

from .broker import PubSubBroker

class Publisher:
    def __init__(self, broker: PubSubBroker):
        self.broker = broker

    def publish(self, topic_name: str, message: str):
        """Publish a message to the specified topic."""
        self.broker.publish_message(topic_name, message)
