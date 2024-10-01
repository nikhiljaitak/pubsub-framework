from google.cloud import pubsub_v1
from google.oauth2 import service_account

class PubSubBroker:
    def __init__(self, project_id):
        self.project_id = project_id