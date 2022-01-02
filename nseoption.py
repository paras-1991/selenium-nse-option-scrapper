import requests
import json
import pandas as pd
import datetime
import time
#import matplotlib.pyplot as plt
#import seaborn as sns # Optional, will only affect the color of bars and the grid
#from ipywidgets import widgets, interactive

new_url = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
page = requests.get(new_url,headers=headers)
data = json.loads(page.text)
data1 = data["filtered"]["data"]

