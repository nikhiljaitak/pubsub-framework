# pubsub/subscriber.py

from .broker import PubSubBroker

class Subscriber:
    def __init__(self, broker: PubSubBroker, subscription_name: str):
        self.broker = broker
        self.subscription_name = subscription_name

    def callback(self, message):
        """Callback function to process received messages."""
        print(f"Received message: {message.data.decode('utf-8')}")
        message.ack()  # Acknowledge the message

    def listen(self):
        """Start listening for messages on the subscription."""
        self.broker.subscribe_messages(self.subscription_name, self.callback)
