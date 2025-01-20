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

  st.write('**X**')
  X=df.drop('species',axis=1)
  X

  st.write('**y**')
  y=df.species
  y

with st.expander('Data Visualization'):
  #bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')

  



