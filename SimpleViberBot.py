import os
import requests
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def setWebHook():

    return "Success" + str(request.url)