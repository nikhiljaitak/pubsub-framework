from google.cloud import pubsub_v1
from loguru import logger

class Publisher:
    def __init__(self, broker):
        self.broker = broker

    def publish(self, topic_name, message):
        try:
            publisher = pubsub_v1.PublisherClient(credentials=self.broker.credentials)
            topic_path = publisher.topic_path(self.broker.project_id, topic_name)
            future = publisher.publish(topic_path, message.encode('utf-8'))
            future.result()
            logger.info(f"Published message to {topic_name}: {message}")
        except Exception as e:
            logger.error(f"Error publishing message: {str(e)}")
