import os
import requests
from flask import Flask, request, Response
import json

address_api_itilium = os.environ['AddressApiItilium']
login_itilium = os.environ['LoginItilium']
password_itilium = os.environ['PasswordItilium']
auth_key = os.environ['AuthKey']

app = Flask(__name__)

viber = Api(BotConfiguration(
    name='SimpleViberBot-bot',
    avatar='http://site.com/avatar.jpg',
    auth_token=auth_key
))

@app.route('/SetWebHook', methods=['GET'])
def setWebHook():
 #   viber = Api(BotConfiguration(
 #               name='SimpleViberBot-bot',
 #               avatar='http://site.com/avatar.jpg',
 #               auth_token=auth_key
 #               ))
 #           viber.unset_webhook()
 #           viber.set_webhook(request.url)
    return "Success" + str(request.url)