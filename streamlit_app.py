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

# Data Preparation: interactive eda:
with st.sidebar:
  st.header('Input Features')
  # island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
  island= st.selectbox('Island', ('Torgersen','Biscoe','Dream'))
  gender= st.selectbox('Gender', ('male','female'))
  bill_length_mm= st.slider('Bill length (mm)', 32.1,59.6,43.9)
  bill_depth_mm = st.slider('Bill length (mm)', 13.1,21.5,17.2)
  flipper_length_mm= st.slider('Flipper length (mm)',172.0,231.0,201.0)
  body_mass_g= st.slider('Body_mass (g)', 2700.0,6300.0, 4207.0)

  #create a Dataframe for the input features
  data={'island':island,
        'bill_length_mm':bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm':flipper_length_mm,
        'body_mass_g':body_mass_g,
        'gender':gender}
  input_df=pd.DataFrame(data, index=[0])
  input_penguins= pd.concat([input_df,X], axis=0)
input_df
#input_penguins
 
        
        

  



