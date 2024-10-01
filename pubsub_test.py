# from pubsub_plain import PubSubBroker, Publisher, Subscriber

# # Initialize the broker with project ID and credential file path
# broker = PubSubBroker("adroit-particle-362414", "/Users//Downloads/adroit-particle-.json")

# # Create a publisher
# publisher = Publisher(broker)
# publisher.publish("test-1", "This is a test message!")

# # Set up email settings for notifications
# email_settings = {
#     "sender_email": "@iitj.ac.in",
#     "recipient_email": "@iitj.ac.in",
#     "smtp_server": "smtp.example.com",
#     "smtp_port": 587,
#     "smtp_username": "@iitj.ac.in",
#     "smtp_password": ""
# }

# # Create a subscriber
# subscriber = Subscriber(broker, email_settings)

# # Register callbacks for subscriptions
# def callback_one(message):
#     print("Received 1: ", message.data.decode("utf-8"))

# subscriber.register_callback("test-sub", callback_one)

# # Register callbacks for subscriptions
# def callback_two(message):
#     print("Received 2: ", message.data.decode("utf-8"))

# subscriber.register_callback("test-sub-2", callback_two)

# # Start listening for messages
# subscriber.listen()
# subscriber.monitor_threads()
