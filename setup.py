from setuptools import setup, find_packages

setup(
    name="pubsub_framework",
    version="0.1.0",
    description="A Pub/Sub framework with Google Pub/Sub support and error handling",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "google-cloud-pubsub",
        "loguru"
    ],
)
