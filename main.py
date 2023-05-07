import streamlit as st
import yfinance as finance

st.title("Build and Deploy stock market app")
st.header("A Basic data sciene web app")

def get_ticker(name):
    company = finance.Ticker(name)  # google
    return company

company1 = get_ticker("GOOGL")
company2 = get_ticker("TSLA")

google = finance.download("GOOGL", start="2023-04-01", end="2023-04-01") 
microsoft = finance.download("TSLA", start="2023-04-01", end="2023-04-01")

data1 = company1.history(period='3mo')
data2 = company2.history(period='3mo')

st.write("""
### Google
""")

st.write(company1.info['longBusinessSummary'])
st.write(google)

st.line_chart(data1.values)

st.write("""
### Microsoft
""")
st.write(company2.info['longBusinessSummary'], "\n", microsoft)
st.line_chart(data2.values)
