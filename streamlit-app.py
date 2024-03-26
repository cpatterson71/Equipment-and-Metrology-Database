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

temp = temp.loc[:, ['Location', 'Type', 'Serial #', 'Description', 'Cal_Date', 'Cal_Due_Date',
         'Owner', 'Comment']]

# def new_func(temp):
#     temp['Cal_Date'] = pd.to_datetime(temp['Cal_Date'], format='%Y-%m-%d')

#     temp['Cal_Due_Date'] = pd.to_datetime(temp['Cal_Due_Date'], format='%Y-%m-%d')

# new_func(temp)

# temp['MonthNumber'] = temp['Cal_Due_Date'].dt.month
# st.dataframe(temp)

@st.cache
def load_data():
    df = temp
    return df

df = load_data


col1, col2 = st.columns([100,100])

with col1:
    min = st.date_input('Beginning Date', dt.date(2024, 1, 1), format='YYYY-MM-DD')
    min = dt.datetime.strptime(min).date()

    max = st.date_input('End Date', dt.date(2024, 1, 1), format='YYYY-MM-DD')
    max = dt.datetime.strptime(max).date()
                        
    df_filtered = temp[temp['Cal_Due_Date'].dt.strftime(date_format='%Y-%m-%d').between(min, max)]
    # df.query("Cal_Due_Date" >= min and "Cal_Due_Date" < max)
    # temp.loc[(temp['Cal_Due_Date'] >= min) & (temp['Cal_Due_Date'] >= max)]

st.write('#### Query Result')

with col2:
    if not df_filtered.empty:
        AgGrid(df, height=500, editable=False, use_container_width=True)
    else:
        st.write('Did not find any item matching the critieria')
    
# with col2:
#     start_date = st.sidebar.date_input('Start Date')
#     end_date = st.sidebar.date_input('End Date')

#     st.sidebar.button('Enter', type='primary')
#     df = date_time(data)

# with col3:
#     key = st.sidebar.selectbox("Key",['Location', 'Type', 'Serial #', 'Description', 'Cal. Date',
#                                       'Cal. due Date', 'Comment', 'Owner'])

# with col4:
#     search_term = st.sidebar.text_input('Search')
#     if key != '' and search_term !='':
#         df = search(data, key, search_term) 

    # st.button.sidebar('Enter', type='primary')    

# buffer, col1 = st.columns([1,100])

# with col1 :
#     if not data.empty:
#         AgGrid(data, height=500, editable=False, use_container_width=True)
#     else:
#         st.write('Did not find any item matching the critieria')
