import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackAPI:
    def __init__(self):
        self.client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

    def get_channel_id(self, channel_name):
        # conversations_list() 메서드 호출
        result = self.client.conversations_list()
        # 채널 정보 딕셔너리 리스트
        channels = result.data['channels']
        # 채널 명이 'test'인 채널 딕셔너리 쿼리
        channel = list(filter(lambda c: c["name"] == channel_name, channels))[0]
        # 채널ID 파싱
        channel_id = channel["id"]
        return channel_id

    def post_message(self, channel_id, text):
        res = self.client.chat_postMessage(
            channel=channel_id,
            text=text
        )

        return res

    def post_message_to_thread(self, channel_id, message_ts, text):
        # 채널 내 메세지의 thread에 글 작성하기
        res = self.client.chat_postMessage(
            channel=channel_id,
            thread_ts=message_ts,
            text=text
        )
