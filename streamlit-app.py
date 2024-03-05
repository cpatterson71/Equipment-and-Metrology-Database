#streamlit-app
import pandas as pd
import numpy as np
import streamlit as st
from st_aggrid import AgGrid
#import boto3

# s3 = boto3.client('s3',
#                   aws_access_key_id = 'AKIASCPKVVLRRR24MAEI',
#                   aws_secret_access_key = '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'
#                     )
# s3.download_file('carldata', 'My_Equipment_file.xlsx', 'My_Equiptment_file.xlsx')
# file = 'My_Equipment_File.xlsx'

data = pd.read_csv('Equipment and Metrology.csv', index_col=False)
temp = pd.DataFrame(data)

st.set_page_config(layout='wide')
st.title('Equipment and Metrology Database')

@st.cache
def load_data():
    df = pd.read_csv('Equipment and Methrology.csv', index_col=False)
    return df

df = load_data

def search(data, column, search_term):
    if column =='Owner':
        search_term = (search_term)

    indexes = data.loc[data[column].isin([search_term])].index
    if indexes.size > 0:
        return data.iloc[indexes]
    else:
        return []
    
col2, col3 = st.columns([20, 20])
  
with col2:
    key = st.sidebar.selectbox("Key",['Location', 'Type', 'Serial #', 'Description', 'Cal. Date',
                                      'Cal. due Date', 'Comment', 'Owner'])

with col3:
    search_term = st.sidebar.text_input('Search')
    if key != '' and search_term !="":
        df = search(data, key, search_term)

col2, col3 = st.columns([1000,100])

with col2 :
    if not df.empty:
        AgGrid(df, height=500, use_container_width=True)
    else:
        st.write('Did not find any item matching the critieria')