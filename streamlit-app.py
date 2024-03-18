#streamlit-app
import pandas as pd
import numpy as np
import streamlit as st
#import datetime as dt

from st_aggrid import AgGrid
# import boto3

# s3 = boto3.client('s3',
#                   aws_access_key_id = 'AKIASCPKVVLRRR24MAEI',
#                   aws_secret_access_key = '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'
#                     )
# s3.download_file('carldata', 'My_Equipment_file.xlsx', 'My_Equiptment_file.xlsx')
# file = 'My_Equipment_File.xlsx'
# excel = pd.read_excel('Equipment_and_Metrology_Database.xlsx', index_col=False)
# temp = pd.DataFrame(excel)

st.set_page_config(layout='wide')
st.title('Equipment and Metrology Database')

file = 'Equipment_and_Metrology_Database.xlsx'
data = pd.read_excel(file, index_col=False)

@st.cache
def load_data():
    df = data
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

# def date_time(data):
#     if st.button(start_date > end_date):
#        st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
#        indexes = data.date_range(start=start_date, end=end_date).index
#        if indexes.size > 0:
#            return data.iloc[indexes]
#        else:
#            return []
       
#     else:
#         st.error('Error: End date must fall after start date.')
          
buffer, col3, col4 = st.columns([20, 20, 20])

# with col2:
#     start_date = st.sidebar.date_input('Start Date')
#     end_date = st.sidebar.date_input('End Date')

#     st.sidebar.button('Enter', type='primary')
#     df = date_time(data)

with col3:
    key = st.sidebar.selectbox("Key",['Location', 'Type', 'Serial #', 'Description', 'Cal. Date',
                                      'Cal. due Date', 'Comment', 'Owner'])

with col4:
    search_term = st.sidebar.text_input('Search')
    if key != '' and search_term !='':
        df = search(data, key, search_term)

    # st.button.sidebar('Enter', type='primary')    

buffer, col1 = st.columns([1,100])

with col1 :
    if not data.empty:
        AgGrid(data, height=500, editable=False, use_container_width=True)
    else:
        st.write('Did not find any item matching the critieria')
