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
  X_raw=df.drop('species',axis=1)
  X_raw

  st.write('**y**')
  y_raw=df.species
  y_raw

with st.expander('Data Visualization'):
  #bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g
  st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')

# Data Preparation: interactive eda:
with st.sidebar:
  st.header('Input Features')
  # island,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,sex
  island= st.selectbox('Island', ('Torgersen','Biscoe','Dream'))
  sex= st.selectbox('Sex', ('male','female'))
  bill_length_mm= st.slider('Bill length (mm)', 32.1,59.6,43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1,21.5,17.2)
  flipper_length_mm= st.slider('Flipper length (mm)',172.0,231.0,201.0)
  body_mass_g= st.slider('Body_mass (g)', 2700.0,6300.0, 4207.0)

  #create a Dataframe for the input features
  data={'island':island,
        'bill_length_mm':bill_length_mm,
        'bill_depth_mm': bill_depth_mm,
        'flipper_length_mm':flipper_length_mm,
        'body_mass_g':body_mass_g,
        'sex':sex}
  input_df=pd.DataFrame(data, index=[0])
  input_penguins= pd.concat([input_df,X_raw], axis=0)

# Encode X
encode= ['island','sex']
df_penguins= pd.get_dummies(input_penguins,prefix=encode)
input_row=df_penguins[:1]

#encode y:
target_mapper={'Adelie':0,
               'Chinstrap':1,
               'Gentoo':2}
def target_encode(val):
  return target_mapper[val]

y= y_raw.apply(target_encode)
y
y_raw


with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguins data**')
  input_penguins
  st.write('**Encoded input penguins**')
  input_row



 
        
        

  



