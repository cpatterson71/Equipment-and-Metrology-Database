#streamlit-app
import pandas as pd
import numpy as np
import streamlit as st
import datetime

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
    
def df_filter(message, df):
    dates_selection = st.sidebar.slider('%s' % (message),
                               min_value = min(df['Date']),
                               max_value = max(df['Date']),
                               value =(min(df['Date']),max(df['Date'])))
    mask = df['Date'].between(dates_selection)
    number_of_result= df[mask].shape[0]
    filtered_df = df[mask]
    return filtered_df


filtered_df = df_filter('Move sliders to filter data', df)
filtered_df.sort_values(by='Date', inplace=True)

# ss = st.session_state
# ss.analysis = {"filter":{}}

# def updateDateRange():
#     if 'dateRange' is ss and isinstance(ss.dateRange, tuple) and len(ss.dateRange)==2:
#         st.write("##########")
#         ss["analysis"]["filter"]['dateRange'] = (ss.dateRange[0].strftime("%YYYY-%DD-%MM"), ss.dateRange[1].strftime("%YYYY-%DD-%MM"))

# base = datetime.date(2022,7,1)
# dates = [base + datetime.timedelta(days=x) for x in range(5)]

# if "dateRange" not in ss:
#     ss.defaultDateRange = (dates[0], dates[-1])



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
          
buffer, col2, col3, col4 = st.columns([20, 20, 20, 20])

with col2:
    AgGrid(df, height=500, editable=False, use_container_width=True)
        

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
