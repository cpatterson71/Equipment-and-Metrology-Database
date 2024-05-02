#streamlit-app.py
import pandas as pd
import streamlit as st
import numpy as np
from st_aggrid import AgGrid
import boto3

s3 = boto3.client('s3',
                  aws_access_key_id = 'AKIASCPKVVLRRR24MAEI',
                  aws_secret_access_key = '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'
                    )
s3.download_file('carldata', 'Equipment_and_Metrology_Database.xlsx', 'Equipment_and_Metrology_Database.xlsx')

file = 'Equpment_and_Metrology_Database.xlsx'
excel = pd.read_excel('Equipment_and_Metrology_Database.xlsx', index_col=False)
temp = pd.DataFrame(excel)

temp = temp.loc[:,['ID_No', 'Location', 'Type', 'Serial_No', 'Description', 'Cal_Date',
            'Cal_Due_Date', 'Owner', 'Comment' ]]

tests = temp['Cal_Date'].astype(str)
dates = []
for test in tests:
     dates.append(test[:-9])
temp['Cal_Date'] = dates

boys = temp['Cal_Due_Date'].astype(str)
why = []
for boy in boys:
     why.append(boy[:-9])
temp['Cal_Due_Date'] = why

temp.to_csv('Equipment_and_Metrology_Database.csv', index=False)

st.set_page_config(layout='wide')
st.title('Equipment and Metrology Database')

Search_Box = ('ID_No', 'Location', 'Type','Serial_No', 'Description', 'Cal_Date',
            'Cal_Due_Date')

file='Equipment_and_Metrology_Database.csv'
data = pd.read_csv(file, index_col=False)
temp = pd.DataFrame(data)
temp = temp.astype('str')

@st.cache
def load_data():
    dead = data
    return dead

dead = load_data

def search(data, column, search_term):
    if column == 'Location':
        search_term = (search_term)

    indexes = data.loc[data[column].isin([search_term])].index
    if indexes.size > 0:
        return data.iloc[indexes]
    else:
        return []
        
buffer, col2, col3 = st.columns([1, 20, 60])

with col2:
    key = st.sidebar.selectbox("Key",Search_Box)

with col3:
    search_term = st.sidebar.text_input("Search")
    if key != '' and search_term != '':
        dead = search(data, key, search_term)

buffer, col2 = st.columns([1, 100])

with col2:
    if  not dead.empty:
        AgGrid(dead, height=500, use_container_width=True)
    else:
        st.write('Did not find any data matching criteria')