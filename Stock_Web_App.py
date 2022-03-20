# libraries

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# containers
intro = st.container()
sidebar = st.container()
datetime = st.container()
header = st.container()
data = st.container()
open_close = st.container()
high_low = st.container()
references = st.container()
source = st.container()


# variables
nasdaq = sorted(
['AAPL',
'TWTR',
'MSFT',
'TSLA',
'AMZN',
'GOOG',
'FB',
'NFLX',
'INTC',
'CSCO',
'CMCSA',
'NVDA',
'AMD',
'ADBE',
'ADP',
'ADSK',
'AKAM',
'ADI',
'QCOM',
'AMGN',
]
)


nyse = sorted(
['HD',
'WMT',
'JPM',
'BAC',
'C',
'WFC',
'PFE',
'T',
'MA',
'UNH',
'KO',
'VZ',
'DIS',
'PG',
'MCD',
'MRK',
'PEP',
'MGM',
'BA',
'CAT',
'DD',
'JNJ',
'MMM',
'AXP',
'XOM',
'PNC',
'XOM',
'CME',
'TMO',
'COP',
'CVS',
'ORCL',
'PLTR',
'NKE',
'NOC'])


dictonary = {
'AAPL': 'Apple',
'MSFT': 'Microsoft', 
'TSLA': 'Tesla',
'AMZN': 'Amazon',
'GOOG': 'Google',
'FB': 'Meta', 
'HD': 'Home Depot',
'NFLX': 'Netflix',
'TWTR': 'Twitter',
'WMT': 'Walmart',
'JPM': 'JP Morgan',
'BAC': 'Bank of America',
'C': 'Citigroup',
'WFC': 'Wells Fargo',
'PFE': 'Pfizer',
'T': 'AT&T',
'INTC': 'Intel Corp',
'CSCO': 'Cisco',
'V': 'Visa',
'MA': 'Mastercard',
'UNH': 'UnitedHealth',
'KO': 'Coca-Cola',
'VZ': 'Verizon',
'DIS': 'Disney',
'PG': 'Procter & Gamble',
'MCD': 'McDonalds',
'MRK': 'Merck',
'PEP': 'PepsiCo, Inc.',
'MGM': 'MGM Resorts International',
'BA': 'Boeing',
'CAT': 'Caterpillar',
'DD': 'DuPont',
'JNJ': 'Johnson & Johnson',
'MMM': '3M',
'AXP': 'American Express',
'PNC': 'PNC',
'UNP': 'Union Pacific',
'CVS': 'CVS Health Corp',
'CMCSA': 'Comcast',
'COP': 'ConocoPhillips',
'TMO': 'T-Mobile',
'CME': 'Chicago Mercantile Exchange',
'XOM':'Exxon Mobil Corp',
'ORCL': 'Oracle Corp',
'NVDA': 'Nvidia',
'AMD': 'Advanced Micro Devices',
'ADBE': 'Adobe Systems Inc',
'ADP': 'Automatic Data Processing',
'PLTR': 'Paylocity',
'AMAT': 'Applied Materials',
'ADSK': 'Autodesk',
'AKAM': 'Akamai Technologies',
'QCOM': 'Qualcomm',
'NKE': 'Nike',
'AMGN': 'Amgen',
'ADI': 'Analog Devices',
'NOC': 'Northrop Grumman'
}

with intro:
    st.title('Stock Price App')

# sidebar
with sidebar:
    stock = st.sidebar.selectbox('Select Stock', ['NYSE', 'NASDAQ'])
    if stock == 'NYSE':
        ticker = st.sidebar.selectbox('Select Stock', nyse)
    elif stock == 'NASDAQ':
        ticker = st.sidebar.selectbox('Select Stock', nasdaq)

with datetime:
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
    # st.subheader('Opening and Closing Price Graph')
    open_close = go.Figure()
    open_close.add_trace(go.Line(x=data.Date, y=data.Close, mode='lines', 
    name='Close', marker_color='darkslateblue'))
    open_close.add_trace(go.Line(x=data.Date, y=data.Open, mode='lines', 
    name='Open', marker_color='firebrick'))
    open_close.update_layout(title_text='Opening and closing price over time ', 
    title_x=0.5, xaxis_title='Date', yaxis_title='Price', xaxis_rangeslider_visible=True, font=dict(family='Roboto Mono, monospace', size=14, color='#7f7f7f'))
    st.plotly_chart(open_close)

with high_low:
    high_low = go.Figure()
    high_low.add_trace(go.Line(x=data.Date, y=data.High, mode='lines', name='High', marker_color='green'))
    high_low.add_trace(go.Line(x=data.Date, y=data.Low, mode='lines', name='Low', marker_color='#d62728'))
    high_low.update_layout(title_text='Highest and lowest price over time', title_x=0.5, xaxis_title='Date', yaxis_title='Price', xaxis_rangeslider_visible=True, font=dict(family='Roboto Mono, monospace', size=14, color='#7f7f7f'))
    st.plotly_chart(high_low)

with references:
    st.header('Source Code')
    code = '''
# libraries
# libraries

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# containers
intro = st.container()
sidebar = st.container()
header = st.container()
data = st.container()
open_close = st.container()
high_low = st.container()
references = st.container()
source = st.container()


# variables
nasdaq = sorted(
['AAPL',
'TWTR',
'MSFT',
'TSLA',
'AMZN',
'GOOG',
'FB',
'NFLX',
'INTC',
'CSCO',
'CMCSA',
'NVDA',
'AMD',
'ADBE',
'ADP',
'ADSK',
'AKAM',
'ADI',
'QCOM',
'AMGN',
]
)


nyse = sorted(
['HD',
'WMT',
'JPM',
'BAC',
'C',
'WFC',
'PFE',
'T',
'MA',
'UNH',
'KO',
'VZ',
'DIS',
'PG',
'MCD',
'MRK',
'PEP',
'MGM',
'BA',
'CAT',
'DD',
'JNJ',
'MMM',
'AXP',
'XOM',
'PNC',
'XOM',
'CME',
'TMO',
'COP',
'CVS',
'ORCL',
'PLTR',
'NKE',
'NOC'])


dictonary = {
'AAPL': 'Apple',
'MSFT': 'Microsoft', 
'TSLA': 'Tesla',
'AMZN': 'Amazon',
'GOOG': 'Google',
'FB': 'Meta', 
'HD': 'Home Depot',
'NFLX': 'Netflix',
'TWTR': 'Twitter',
'WMT': 'Walmart',
'JPM': 'JP Morgan',
'BAC': 'Bank of America',
'C': 'Citigroup',
'WFC': 'Wells Fargo',
'PFE': 'Pfizer',
'T': 'AT&T',
'INTC': 'Intel Corp',
'CSCO': 'Cisco',
'V': 'Visa',
'MA': 'Mastercard',
'UNH': 'UnitedHealth',
'KO': 'Coca-Cola',
'VZ': 'Verizon',
'DIS': 'Disney',
'PG': 'Procter & Gamble',
'MCD': 'McDonalds',
'MRK': 'Merck',
'PEP': 'PepsiCo, Inc.',
'MGM': 'MGM Resorts International',
'BA': 'Boeing',
'CAT': 'Caterpillar',
'DD': 'DuPont',
'JNJ': 'Johnson & Johnson',
'MMM': '3M',
'AXP': 'American Express',
'PNC': 'PNC',
'UNP': 'Union Pacific',
'CVS': 'CVS Health Corp',
'CMCSA': 'Comcast',
'COP': 'ConocoPhillips',
'TMO': 'T-Mobile',
'CME': 'Chicago Mercantile Exchange',
'XOM':'Exxon Mobil Corp',
'ORCL': 'Oracle Corp',
'NVDA': 'Nvidia',
'AMD': 'Advanced Micro Devices',
'ADBE': 'Adobe Systems Inc',
'ADP': 'Automatic Data Processing',
'PLTR': 'Paylocity',
'AMAT': 'Applied Materials',
'ADSK': 'Autodesk',
'AKAM': 'Akamai Technologies',
'QCOM': 'Qualcomm',
'NKE': 'Nike',
'AMGN': 'Amgen',
'ADI': 'Analog Devices',
'NOC': 'Northrop Grumman'
}

with intro:
    st.title('Stock Price App')

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
    open_close.add_trace(go.Line(x=data.Date, y=data.Close, mode='lines', 
    name='Close', marker_color='darkslateblue'))
    open_close.add_trace(go.Line(x=data.Date, y=data.Open, mode='lines', 
    name='Open', marker_color='firebrick'))
    open_close.update_layout(title_text='Opening and closing price over time ', 
    title_x=0.5, xaxis_title='Date', yaxis_title='Price',
    xaxis_rangeslider_visible=True, 
    font=dict(family='Roboto Mono, monospace', size=14, color='#7f7f7f'))
    st.plotly_chart(open_close)

with high_low:
    high_low = go.Figure()
    high_low.add_trace(go.Line(x=data.Date, y=data.High, mode='lines', 
    name='High', marker_color='green'))
    high_low.add_trace(go.Line(x=data.Date, y=data.Low, mode='lines', 
    name='Low', marker_color='#d62728'))
    high_low.update_layout(title_text='Highest and lowest price over time', 
    title_x=0.5, xaxis_title='Date', yaxis_title='Price', 
    xaxis_rangeslider_visible=True, 
    font=dict(family='Roboto Mono, monospace', size=14, color='#7f7f7f'))
    st.plotly_chart(high_low)

    '''
    st.code(code)
