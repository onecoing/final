import http.client
import requests
import json
from flask import Flask, render_template
from datetime import datetime
from lxml import html
#import threading



app = Flask(__name__)



one=0
btc=0
eth=0
ltc=0
eurokur = 0



    
@app.route('/') 
def index():
    def cek():  
        global one,btc,eth,ltc  
        try:
            res = requests.get('https://www.paribu.com/ticker')
            data = res.json()
            btc = data['BTC_TL']['highestBid']
            eth = data['ETH_TL']['highestBid']
            ltc = data['LTC_TL']['highestBid'] 
        except:
            btc = 0
            eth = 0
            ltc = 0 
        try:
            res = requests.get('https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCEUR')
            data = res.json()
            btcEURO4 = data[0][3]
            eurokur = btc / btcEURO4
        except:
            eurokur = 0    
        one = eurokur * 42.43
        one ='{:.2f}'.format(one)
        btc ='{:.2f}'.format(btc)
        eth ='{:.2f}'.format(eth)
        ltc ='{:.2f}'.format(ltc)
    cek()
    return render_template('index.html',one=one, btc=btc, eth=eth, ltc=ltc)


if __name__ == "__main__":

    app.run()  
    
