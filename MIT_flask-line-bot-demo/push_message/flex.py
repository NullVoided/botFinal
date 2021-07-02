import os

from linebot.models.events import VideoPlayCompleteEvent

if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, LocationSendMessage,
    VideoSendMessage, ImageSendMessage, StickerSendMessage,
)

app = Flask(__name__)


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
output= FlexSendMessage(
            alt_text='hello',
                contents={
    "type": "bubble",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "MedBot",
            "weight": "bold",
            "color": "#000000",
            "style": "normal",
            "decoration": "none",
            "position": "relative",
            "align": "center",
            "gravity": "top",
            "size": "xl",
            "margin": "none"
        }
        ]
    },
    "hero": {
        "type": "image",
        "url": "https://thumbs-prod.si-cdn.com/aadh5TGxODWzB1Gn3GSgbYNSLao=/800x600/filters:no_upscale()/https://public-media.si-cdn.com/filer/54/78/5478d7cf-4dc1-45ee-998b-ca095579ec00/telemedicine.jpg",
        "size": "5xl"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "text",
            "text": "Hello, how can I help you?",
            "size": "lg",
            "margin": "none",
            "position": "relative",
            "align": "center",
            "gravity": "top",
            "decoration": "none",
            "style": "normal",
            "weight": "regular"
        }
        ]
    },
    "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "CHECK IN",
            "text": "hello"
            },
            "style": "link",
            "color": "#000000",
            "position": "relative",
            "margin": "xs",
            "adjustMode": "shrink-to-fit",
            "height": "md",
            "offsetTop": "none",
            "offsetBottom": "xxl",
            "offsetStart": "xs",
            "offsetEnd": "xs"
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "PRESCRIPTIONS",
            "text": "hello"
            },
            "color": "#000000",
            "style": "link"
        },
        {
            "type": "button",
            "action": {
            "type": "message",
            "label": "EMERGENCY",
            "text": "hello"
            },
            "style": "secondary",
            "color": "#44F7CA"
        }
        ]
    },
    "styles": {
        "header": {
        "backgroundColor": "#44F7CA"
        },
    }
    })
line_bot_api = LineBotApi(channel_access_token)
e1 = 'U82f489e2fc2bfc92f9545281e7beda30'
line_bot_api.push_message(
        e1,
        output
    )
    