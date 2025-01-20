import streamlit as st
import pandas as pd
import numpy as np

st.title('Machine Learning App')

st.info('This App builds machine learning model')

url = 'https://raw.githubusercontent.com/IKESUYI/ike-machinelearning/master/penguin%20dataset.csv'
df = pd.read_csv(url)
print(df.head())



