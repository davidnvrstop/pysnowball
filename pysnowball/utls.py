import requests
import json
import pathlib

import pysnowball.cons as cons
import pysnowball.token as token
from datetime import date

def fetch(url, method):
    HEADERS = {'Host': 'stock.xueqiu.com',
               'Accept': 'application/json',
               'Cookie': token.get_token(),
               'User-Agent': 'Xueqiu iPhone 11.8',
               'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
               'Accept-Encoding': 'br, gzip, deflate',
               'Connection': 'keep-alive'}

    response = requests.get(url,headers=HEADERS)

    # print(url)
    # print(HEADERS)
    # print(response)
    # print(response.content)

    if response.status_code != 200:
        raise Exception(response.content)

    if method == cons.JSON_LOADS_MODE:
      return json.loads(response.content)
    elif method == cons.JSON_DUMP_MODE:
      today = date.today()
      root = pathlib.Path(__file__).parent
      #jsonfile = root+today.strftime("%y%m%d_%H%M%S") + ".json"
      jsonfile = "/Users/davidzhao125/Desktop/a.txt"
      with open(jsonfile,'w') as outfile:
        json.dump(response.content, outfile)

    return json.loads(response.content)


def fetch_without_token(url):
    HEADERS = {'Host': 'stock.xueqiu.com',
               'Accept': 'application/json',
               'User-Agent': 'Xueqiu iPhone 11.8',
               'Accept-Language': 'zh-Hans-CN;q=1, ja-JP;q=0.9',
               'Accept-Encoding': 'br, gzip, deflate',
               'Connection': 'keep-alive'}

    response = requests.get(url, headers=HEADERS)

    # print(url)
    # print(HEADERS)
    # print(response)
    # print(response.content)

    if response.status_code != 200:
        raise Exception(response.content)

    return json.loads(response.content)
