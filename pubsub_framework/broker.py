# pubsub/broker.py

import os
from google.cloud import pubsub_v1

class PubSubBroker:
    def __init__(self, project_id: str, credentials_path: str):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
        self.project_id = project_id
        self.publisher = pubsub_v1.PublisherClient()
        self.subscriber = pubsub_v1.SubscriberClient()

    def publish_message(self, topic_name: str, message: str):
        topic_path = self.publisher.topic_path(self.project_id, topic_name)
        future = self.publisher.publish(topic_path, message.encode("utf-8"))
        print(f"Published {message} to {topic_path} with message ID: {future.result()}")

    def subscribe_messages(self, subscription_name: str, callback):
        subscription_path = self.subscriber.subscription_path(self.project_id, subscription_name)

        streaming_pull_future = self.subscriber.subscribe(subscription_path, callback=callback)
        print(f"Listening for messages on {subscription_path}...")

        try:
            streaming_pull_future.result()
        except KeyboardInterrupt:
            streaming_pull_future.cancel()
