from slack_sdk import WebClient

TOKEN = "xoxb-2975781091040-2949213389317-8P4daKKMSlL6km3zMFgw2GfC"

client = WebClient(token=TOKEN)

response = client.chat_postMessage(channel='#bot-test', text="Hello world!")
