#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from flask import Flask, request

# flaskインスタンスを生成
app = Flask(__name__)


# /の時の動作
@app.route('/',methods=['GET'])
def print_totp():
  # アクセス元IP
  client_ip = request.remote_addr
  
  # 現在時刻
  dt = datetime.datetime.now()
  dt_str = dt.strftime("%Y/%m/%d %H:%M:%S")

  # 結果表示用HTML
  result_html = "<html><body>" + dt_str + " Access from " + str(client_ip) + "<br><br></body><html>"
  
  return result_html


if __name__ == "__main__":
  app.run()


