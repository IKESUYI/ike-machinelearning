import streamlit as st
import pandas as pd
import numpy as np

st.title('Machine Learning App')

st.info('This App builds machine learning model')

with st.expander('Data'):
  st.write('**Raw Data**')
  url = 'https://raw.githubusercontent.com/IKESUYI/ike-machinelearning/master/penguin%20dataset.csv'
  df = pd.read_csv(url, sep=',')
  df.drop(columns=['Unnamed: 0'], inplace=True)
  df
  



