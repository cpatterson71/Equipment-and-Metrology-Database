#streamlit-app
import pandas as pd
import streamlit as st
import datetime as dt
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

Months =('January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December')

Search_Box = ('Location', 'Type', 'Serial #', 'Description', 'Cal_Date',
            'Cal_Due_Date', 'Owner')

st.set_page_config(layout='wide')
st.title('Equipment and Metrology Database')

file = 'Equipment_and_Metrology_Database.xlsx'
data = pd.read_excel(file, index_col=False)

temp = pd.DataFrame(data)

tests = temp['Cal_Date'].astype(str)
dates = []
for test in tests:
     dates.append(test[:-9])
temp['Cal_Date'] = dates

date = temp['Cal_Due_Date'].astype(str)
why = []
for date in dates:
     why.append(date[:-9])
temp['Cal_Due_Date'] = why

temp['Cal_Due_Date'] = dt.date(temp['Cal_Due_Date'], format='%Y-%m-%d')
temp['Cal_Date'] = dt.date(temp['Cal_Date'], format='%Y-%m-%d')

temp = temp.loc[:, ['Location', 'Type', 'Serial #', 'Description', 'Cal_Date', 'Cal_Due_Date',
         'Owner', 'Comment']]

def search(data, column, search_term):
    if column == 'Description':
        search_term = (search_term)

        indexes = data.loc[data[column].isin([search_term])].index
        if indexes.size > 0:
            return data.iloc[indexes]
        else:
            return []
@st.cache
def load_data():
    df = temp
    return df

df = load_data

buffer, col1, col2, col3 = st.columns([1, 20, 60])

with col1:
    key = st.sidebar.selectbox["key",  ['Location', 'Type', 'Serial #', 'Description', 'Cal_Date', 'Cal_Due_Date',
         'Owner', 'Comment']]

    with col2:
        search_term = st.sidebar.text("Search")
        if key != '' and search_term != '':
            df = search(data, key, search_term)
                        
    # temp[temp['Cal_Due_Date'].dt.strftime(date_format='%Y-%m-%d').between(min, max)]
    # df.query("Cal_Due_Date" >= min and "Cal_Due_Date" < max)


with col3:
    if not df.empty:
        AgGrid(temp, height=500, editable=False, use_container_width=True)
    else:
        st.write('Did not find any item matching the critieria')
    