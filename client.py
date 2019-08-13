#!/usr/bin/env python3

from pprint import pprint
from slack import RTMClient


@RTMClient.run_on(event = 'message')
def test(**payload):

	pprint(payload)

	data = payload['data']
	web_client = payload['web_client']

	if 'bot_id' not in data:
		channel_id = data['channel']
		web_client.chat_postMessage(
			channel = channel_id,
			text = 'The Pangram Bot is out of order, please insert another quarter.'
		)

slack_token = 'xoxb-230601492624-726247533222-Fghzq2AfhcdffcmIwmIPqsYg'
rtm_client = RTMClient(token = slack_token)
rtm_client.start()
