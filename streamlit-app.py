#streamlit-app
import pandas as pd
import streamlit as st
from streamlit_date_picker import date_range_picker, PickerType, Unit, date_picker

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

date_range_string = date_range_picker(picker_type=PickerType.date.string_value,
                                      start=-30, end=0, unit=Unit.days.string_value,
                                      key='range_picker',
                                      refresh_button={'is_show': True, 'button_name': 'Refresh last 30min',
                                                      'refresh_date': -30,
                                                        })

if date_range_string is not None:
    start_datetime = date_range_string[0]
    end_datetime = date_range_string[1]
    st.write(f"Date Range [{start_datetime}, {end_datetime}]")

def date_range(df):
     if start_datetime < end_datetime:
        indexes = df.date_range(start=start_datetime, end=end_datetime, freq='D').index
        return df.loc[indexes]
     else:
          return []
    
        
# date_string = date_range_picker(picker_type=PickerType.time.string_value, value=0, unit=Unit.days.string_value,
#                           key='date_picker')


# if date_string is not None:
#     st.write('Date Picker: ', date_string)

# def df_filter(message, data):
#     dates_selection = st.sidebar.slider('%s' % (message),
#                                min_value = min(df['Cal. Due Date']),
#                                max_value = max(df['Cal. Due Date']),
#                                value =(min(df['Cal. Due Date']),max(df['Cal. Due Date'])))
#     mask = data['Date'].between(dates_selection)
#     filtered_df = data[mask].shape[0]
#     return filtered_df
# def search(data, column, search_term):
#     if column =='Owner':
#         search_term = (search_term)

#     indexes = data.loc[data[column].isin([search_term])].index
#     if indexes.size > 0:
#         return data.iloc[indexes]
#     else:
#         return []

# filtered_df = df_filter('Move sliders to filter data', df)
# filtered_df.sort_values(by='Date', inplace=True)

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
#        indexes = data.date_range(start=start_date, end=end_date).index
#        if indexes.size > 0:
#            return data.iloc[indexes]
#        else:
#            return []
       
#     else:
#         st.error('Error: End date must fall after start date.')
          
# col2, col3, col4 = st.columns([20, 20, 20])

# with col2:
#     df_filter

buffer, col1 = st.columns([1,100])

with col1:
        if date_range is not None:
            df = AgGrid(data, height=500, editable=False, use_container_width=True)
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
