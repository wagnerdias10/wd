#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from warnings import warn
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_httpauth import HTTPTokenAuth

API_TOKEN = os.getenv("API_TOKEN")

app = Flask(__name__)
auth = HTTPTokenAuth("Token")

@auth.verify_token
def verify_token(token):
    if not API_TOKEN:
        warn("API_TOKEN environment variable is required to enable Token authentication.")
        return False
    return token == API_TOKEN

@app.route("/")
@auth.login_required
def main_route():
   return "DevOps test server flying!!"

if __name__ == '__main__':
    app.run("0.0.0.0", port=80)
