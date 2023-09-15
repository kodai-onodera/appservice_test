#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from flask import Flask, request
import socket

app = Flask(__name__)


@app.route('/',methods=['GET'])
def print_ip():
  client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
  dt = datetime.datetime.now()
  dt_str = dt.strftime("%Y/%m/%d %H:%M:%S")
  form = '<form action="/" method="POST"><input name="imput_data"></input><button type="submit">送信</button></form>'
  result = dt_str + " \nAccess from " + str(client_ip) + "\n" + form + "\n"
  return result

@app.route('/', methods=['POST'])
def sample_form_temp():
    result = "Imput value: " + str(request.form['imput_data']) 
    return result

if __name__ == "__main__":
  app.run()


