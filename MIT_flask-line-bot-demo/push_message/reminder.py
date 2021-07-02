import os
import time
from linebot.models import TextSendMessage

if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys
from linebot import LineBotApi

channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'QeNDzovLdlZSMyJR/lj0bqT/ON2ZXFzeWZCfaA9syt2SoLEjxoXnNOd02BOKdWF/RyBdNzB7WQltroEgCRRNCH3d19+u05m+0mAtC28MI41D3gIMoHKF7Tbz5g28rOuoBQzTU2npHfZDVNxCrV51oAdB04t89/1O/w1cDnyilFU='
print(channel_access_token)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

# Example: https://github.com/line/line-bot-sdk-python#push_messageself-to-messages-notification_disabledfalse-timeoutnone
# Document: https://developers.line.biz/en/reference/messaging-api/#send-push-message

e1 = ['U82f489e2fc2bfc92f9545281e7beda30']
for i in e1:
    line_bot_api.push_message(i, TextSendMessage(text=("Good day Lucia,\nIt's time for your daily checkup! Please measure and send your Blood Sugar as a message and remember to take your prescription.")))
