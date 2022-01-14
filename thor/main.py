import os
from slack_sdk import WebClient

client = WebClient(token=os.environ["TOKEN"])

response = client.chat_postMessage(channel='#bot-test', text="MORE!")
