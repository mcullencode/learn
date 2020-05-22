import bitmex_v1
import arrow
import functions
from functions import *
import arguments
from arguments import TimeRange
import sys
import time
import base64
import requests
import json
import hmac
import hashlib

"""Insert download path here, i.e. /Users/xyz/Trading/Stats"""
dl_path = '/Users/mc/Documents/Trading/Statistics'

arguments = arguments.Arguments(sys.argv[1:], 'download utility')
arguments.testdata_dl_options()
args = arguments.parse_args()


"""variables, enter how many days you want to run over. for timeframes, i think the bitmex only gives out bucketed trades of
5m and 1d. but resampling using pandas is pretty easy. timeframes below uses 5m and 1d so will download both with same run if you like"""
#count = 1000
#keep as True otherwise the data is backwards
reverse = True

#how many days of data you want
days = 30
#havent used alt pairs with this before but i think the format XRPZ19 etc would work.
PAIRS = ["ETHUSD", "XBTUSD"]

timeframes = ['1d']



timerange = TimeRange()
time_since = arrow.utcnow().shift(days=-days)
time_since = time_since.strftime("%Y%m%d")
timerange = arguments.parse_timerange(f'{time_since}-')
print(f'timerange is {timerange}' + '-' * 20)



for pair in PAIRS:

    for tick_interval in timeframes:
        pair_print = pair.replace('/', '_')
        filename = f'{pair_print}-{tick_interval}.json'
        dl_file = dl_path + '/' + filename
        print(f'downloading pair {pair}, interval {tick_interval}')
        print(type(dl_file))
        download_backtesting_testdata(str(dl_path),
                                      pair=pair,
                                      tick_interval=tick_interval,
                                      timerange=timerange)



#####data = requests.get(f'https://www.bitmex.com/api/v1/trade/bucketed?binSize={binsize}&symbol={symbol}&count={count}&reverse={reverse}').json()

