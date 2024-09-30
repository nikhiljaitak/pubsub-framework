# setup.py

from setuptools import setup, find_packages

setup(
    name="pubsub-framework",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "google-cloud-pubsub>=2.0.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Pub/Sub framework for Google Cloud.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pubsub-framework",  # Update with your repo URL
)
