import streamlit as st

st.title('Machine Learning App')

st.info('This App builds machine learning model')

df=pd.read_csv('https://raw.githubusercontent.com/IKESUYI/ike-machinelearning/refs/heads/master/penguin%20dataset.csv')
df

