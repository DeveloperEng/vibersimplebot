import os
import requests
from flask import Flask, request, Response
import json
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.picture_message import PictureMessage
from viberbot.api.messages.text_message import TextMessage
from viberbot.api.messages.keyboard_message import KeyboardMessage
from viberbot.api.messages.rich_media_message import RichMediaMessage
from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest
from viberbot.api.viber_requests import ViberDeliveredRequest

address_api_itilium = os.environ['AddressApiItilium']
#login_itilium = os.environ['LoginItilium']
#password_itilium = os.environ['PasswordItilium']
auth_key = os.environ['AuthToken']

app = Flask(__name__)

viber = Api(BotConfiguration(
    name='SimpleViberBot-bot',
    avatar='http://site.com/avatar.jpg',
    auth_token=auth_key
))

@app.route('/SetWebHook', methods=['GET'])
def setWebHook():
    viber = Api(BotConfiguration(
                name='SimpleViberBot-bot',
                avatar='http://site.com/avatar.jpg',
                auth_token=auth_key
               ))
 #           viber.unset_webhook()
 #           viber.set_webhook(request.url)
    return "Success" + str(request.url)