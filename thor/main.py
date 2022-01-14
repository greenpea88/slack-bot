import os
from slack_sdk import WebClient

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])


def post_message():
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
  response = client.chat_postMessage(channel='bot-test', blocks=blocks)


def post_message_to_thread():
    res = client.conversations_list()
    channels = res.data["channels"]
    channel = list(filter(lambda c: c["name"] == "bot-test", channels))[0]
    channel_id = channel["id"]

    # conversations_history() 메서드 호출
    result = client.conversations_history(channel=channel_id)
    # 채널 내 메세지 정보 딕셔너리 리스트
    messages = result.data['messages']
    # 채널 내 메세지가 query와 일치하는 메세지 딕셔너리 쿼리
    message = list(filter(lambda m: m["text"] == "MORE!", messages))[0]
    # 해당 메세지ts 파싱
    message_ts = message["ts"]

    res = client.chat_postMessage(
      channel=channel_id,
      thread_ts=message_ts,
      text="hello"
    )

    return res


if __name__ == "__main__":
  res = post_message_to_thread()
  print(res)
