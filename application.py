#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from flask import Flask, request

app = Flask(__name__)


@app.route('/',methods=['GET'])
def print_totp():
  client_ip = request.remote_addr
  
  dt = datetime.datetime.now()
  dt_str = dt.strftime("%Y/%m/%d %H:%M:%S")
  result = dt_str + " Access from " + str(client_ip)
  
  return result


if __name__ == "__main__":
  app.run()


