import threading
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.cloud import pubsub_v1
from loguru import logger

class Subscriber:
    def __init__(self, broker, email_settings):
        self.broker = broker
        self.callbacks = {}
        self.email_settings = email_settings
        self.subscriber_threads = {}

    def register_callback(self, subscription_name, callback):
        self.callbacks[subscription_name] = callback

    def _send_email_notification(self, error_message):
        try:
            sender_email = self.email_settings["sender_email"]
            recipient_email = self.email_settings["recipient_email"]
            smtp_server = self.email_settings["smtp_server"]
            smtp_port = self.email_settings["smtp_port"]
            smtp_username = self.email_settings["smtp_username"]
            smtp_password = self.email_settings["smtp_password"]

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = recipient_email
            message["Subject"] = "Subscriber Thread Error Notification"

            body = f"An error occurred in the subscriber thread:\n\n{error_message}"
            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(sender_email, recipient_email, message.as_string())
            logger.info(f"Notification email sent to {recipient_email}")
        except Exception as e:
            logger.error(f"Failed to send email notification: {str(e)}")

    def _listen_to_subscription(self, subscription_name):
        try:
            subscriber = pubsub_v1.SubscriberClient(credentials=self.broker.credentials)
            subscription_path = subscriber.subscription_path(self.broker.project_id, subscription_name)

            def callback_wrapper(message):
                try:
                    logger.info(f"Received message on {subscription_name}: {message.data.decode('utf-8')}")
                    if subscription_name in self.callbacks:
                        self.callbacks[subscription_name](message)
                    message.ack()
                except Exception as e:
                    logger.error(f"Error in callback for subscription {subscription_name}: {str(e)}")
                    self._send_email_notification(f"Callback error in subscription {subscription_name}: {str(e)}")

            future = subscriber.subscribe(subscription_path, callback_wrapper)
            self.subscriber_threads[subscription_name] = future
            logger.info(f"Listening on subscription {subscription_name}")
            future.result()
        except Exception as e:
            error_message = f"Error in subscription {subscription_name}: {str(e)}"
            logger.error(error_message)
            self._send_email_notification(error_message)

    def listen(self):
        for subscription_name in self.callbacks.keys():
            thread = threading.Thread(target=self._listen_to_subscription, args=(subscription_name,))
            thread.daemon = True
            thread.start()
            logger.info(f"Started thread for subscription {subscription_name}")

    def monitor_threads(self):
        while True:
            for subscription_name, future in self.subscriber_threads.items():
                if future.done() or future.cancelled():
                    error_message = f"Thread for subscription {subscription_name} stopped running."
                    logger.error(error_message)
                    self._send_email_notification(error_message)
            time.sleep(60)