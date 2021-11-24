import os
import requests
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/setWebHook', methods=['GET'])
def setWebHook():
   # adress = request.url
   # print(adress)
    return "Success"


