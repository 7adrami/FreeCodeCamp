import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 500)
y = np.cumsum(np.random.randn(500, 6), 0)
plt.figure(figsize=(12, 7))
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')


def get_historic_price(symbol, after='2018-09-01'):
    url = 'curl "https://api.kraken.com/0/public/OHLC?pair=BTCUSD&interval=15"'
    pair = f"{symbol.upper()}USD"  # XBTUSD when symbol='xbt' for example

    resp = requests.get(url, params={
        "pair": pair,
        'interval': 60,
        'since': str(int(pd.Timestamp(after).timestamp()))
    })
    resp.raise_for_status()

    data = resp.json()

    results_key = [k for k in data['result'].keys() if k != 'last'][0]
    results = [
        (close_time, float(open), float(high), float(low), float(close), float(volume))
        for (close_time, open, high, low, close, vwap, volume, count)
        in data['result'][results_key]
    ]
    df = pd.DataFrame(results, columns=[
        'CloseTime', 'OpenPrice', 'HighPrice', 'LowPrice', 'ClosePrice', 'Volume'
    ])
    df['CloseTime'] = pd.to_datetime(df['CloseTime'], unit='s')
    df.set_index('CloseTime', inplace=True)
    return df


last_week = (pd.Timestamp.now() - pd.offsets.Day(7))
last_week

btc = get_historic_price('btc', after=last_week)
eth = get_historic_price('eth', after=last_week)
#
# btc.head()
# btc.info()
#
# btc['ClosePrice'].plot(figsize=(15, 7))
#
# eth.head()
# eth['ClosePrice'].plot(figsize=(15, 7))
# eth.head()
# from bokeh.plotting import figure, output_file, show
# from bokeh.io import output_notebook
#
#
# p1 = figure(x_axis_type="datetime", title="Crypto Prices", width=800)
# p1.grid.grid_line_alpha=0.3
# p1.xaxis.axis_label = 'Date'
# p1.yaxis.axis_label = 'Price'
#
# p1.line(btc.index, btc['ClosePrice'], color='#f2a900', legend ='Bitcoin')
# #p1.line(eth.index, eth['ClosePrice'], color='#A6CEE3', legend='Ether')
#
# p1.legend.location = "top_left"
#
# show(p1)
#
#

writer = pd.ExcelWriter('C:/Users/dell/Desktop/FreeCodeCamp/cryptos.xlsx')
btc.to_excel(writer, sheet_name='Bitcoin')
eth.to_excel(writer, sheet_name='Ether')
writer.save()
