# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:41:16 2022

@author: nikhil
"""

import pandas as pd
import requests
import streamlit as st

st.title('Bitcoin prices')

days = st.slider('Number of days',min_value=1, max_value=365)
currency=st.radio("Select currency",('cad', 'usd', 'inr'))

API_URL = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'

payload = {'vs_currency':currency,'days':days,'interval':'daily'}
req = requests.get(API_URL, params=payload)


if req.status_code == 200:
    raw_data = req.json()
else:
    print("Something's wrong!!! Status code - ", req.status_code)
    
df = pd.DataFrame(raw_data['prices'])
df.columns=['date','price']

df['date']=pd.to_datetime(df['date'], unit='ms')

df = df.rename(columns={'date':'index'}).set_index('index')

#print(df)

st.line_chart(df)

st.write("Average price during this time period was ",df['price'].mean()," cad")

