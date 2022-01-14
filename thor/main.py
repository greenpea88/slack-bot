import os
from slack_sdk import WebClient

client = WebClient(token=os.environ["TOKEN"])

blocks = [{
  "type": "section",
  "text": {
    "text": "*Sally* has requested you set the deadline for the Nano launch project",
    "type": "mrkdwn"
  },
  "accessory": {
    "type": "datepicker",
    "action_id": "datepicker123",
    "initial_date": "1990-04-28",
    "placeholder": {
      "type": "plain_text",
      "text": "Select a date"
    }
  }
}]

response = client.chat_postMessage(channel='#bot-test', blocks=blocks)
