# 两个经典的网络爬虫的例子
import requests
import re
import pandas as pd
 
def retrieve_dji_list():
    try:
        r = requests.get('https://money.cnn.com/data/dow30/')
    except ConnectionError as err:
        print(err)  
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*<span.*">(.*?)<\/span>.*\n.*class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    dji_list = []
    for item in dji_list_in_text:
        dji_list.append({'code': item[0], 'name': item[1], 'price': float(item[2])})
    return dji_list
 
dji_list = retrieve_dji_list()
djidf = pd.DataFrame(dji_list)
print(djidf)

import requests
import re
import json
import pandas as pd
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)  
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])     # m = ['[{...},{...},...]']
        quotes = quotes[::-1]
    return  [item for item in quotes if 'type' not in item]
 
quotes = retrieve_quotes_historical('AXP')
quotesdf_ori = pd.DataFrame(quotes)
quotesdf = quotesdf_ori.drop(['adjclose'], axis = 1)
print(quotesdf)



df = pd.read_csv('地址')
type(df)
index_col指定某一列为索引列
df.to_csv('文件名')
pd.read_excel(sheet_name = )

# API获取数据
