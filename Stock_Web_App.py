# libraries

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# containers
sidebar = st.container()
header = st.container()
data = st.container()
open_close = st.container()
high_low = st.container()
references = st.container()


# 'UTX': 'United Technologies',
# variables
nasdaq = sorted(['AAPL', 'TWTR', 'MSFT', 'TSLA', 'AMZN', 'GOOG', 'FB', 'NFLX', 'INTC', 'CSCO', 'CMCSA'])


nyse = sorted(['HD', 'WMT', 'JPM', 'BAC', 'C', 'WFC', 'PFE', 'T', 'MA', 'UNH', 'KO', 'VZ', 'DIS', 'PG', 'MCD', 'MRK', 'PEP', 'MGM', 'BA', 'CAT', 'DD', 'JNJ', 'MMM', 'AXP', 'XOM', 'PNC', 'XOM', 'CME' , 'TMO', 'COP', 'CVS'])


dictonary = {'AAPL': 'Apple', 'MSFT': 'Microsoft', 'TSLA': 'Tesla', 'AMZN': 'Amazon', 'GOOG': 'Google', 'FB': 'Meta', 'HD': 'Home Depot', 'NFLX': 'Netflix', 'TWTR': 'Twitter', 'WMT': 'Walmart', 'JPM': 'JP Morgan', 'BAC': 'Bank of America', 'C': 'Citigroup', 'WFC': 'Wells Fargo', 'PFE': 'Pfizer', 'T': 'AT&T', 'INTC': 'Intel', 'CSCO': 'Cisco', 'V': 'Visa', 'MA': 'Mastercard', 'UNH': 'UnitedHealth', 'KO': 'Coca-Cola', 'VZ': 'Verizon', 'DIS': 'Disney', 'PG': 'Procter & Gamble', 'MCD': 'McDonalds', 'MRK': 'Merck', 'PEP': 'PepsiCo, Inc.', 'MGM': 'MGM', 'BA': 'Boeing', 'CAT': 'Caterpillar', 'DD': 'DuPont', 'JNJ': 'Johnson & Johnson', 'MMM': '3M', 'AXP': 'American Express', 'PNC': 'PNC', 'UNP': 'Union Pacific', 'CVS': 'CVS Health Corp', 'CMCSA': 'Comcast', 'COP': 'ConocoPhillips', 'TMO': 'T-Mobile', 'CME': 'Chicago Mercantile Exchange', 'XOM':'Exxon Mobil Corp'}



# sidebar
with sidebar:
    stock = st.sidebar.selectbox('Select Stock', ['NYSE', 'NASDAQ'])
    if stock == 'NYSE':
        ticker = st.sidebar.selectbox('Select Stock', nyse)
    elif stock == 'NASDAQ':
        ticker = st.sidebar.selectbox('Select Stock', nasdaq)
begin = st.sidebar.date_input('Starting Date', value=None)
end = st.sidebar.date_input('Ending Date', value=None)
if begin > end:
        st.error('Begin Date must be before End Date')
        
        
with header:
    for key, value in dictonary.items():
        if key == ticker:
            st.header(value)
            break

# data
with data:
    df = yf.download(ticker, start=begin, end=end)
    df.to_csv('data.csv')
    df.reset_index(inplace=True)
    data = pd.read_csv('data.csv')
    col1, col2 = st.columns(2)
    st.subheader('Starting Data')
    st.dataframe(data.head(9))
    st.subheader('Ending Data')
    st.dataframe(data.tail(9))



# open
with open_close:
    st.subheader(value + ' Stock Price')
    open_close = go.Figure()
    open_close.add_trace(go.Line(x=data.Date, y=data.Close, mode='lines', name='Close', marker_color='darkslateblue'))
    open_close.add_trace(go.Line(x=data.Date, y=data.Open, mode='lines', name='Open', marker_color='firebrick'))
    st.plotly_chart(open_close)

with high_low:
    high_low = go.Figure()
    high_low.add_trace(go.Line(x=data.Date, y=data.High, mode='lines', name='High', marker_color='green'))
    high_low.add_trace(go.Line(x=data.Date, y=data.Low, mode='lines', name='Low', marker_color='#d62728'))
    st.plotly_chart(high_low)

with references:
    st.subheader('Reference')
    st.write('The following is a list of the most common stocks in the US and Canada [www.nasdaq.com]')
