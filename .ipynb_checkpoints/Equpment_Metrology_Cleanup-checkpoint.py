# %%
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from datetime import datetime as dt

# %%
excel = pd.read_excel('Equipment_and_Metrology_Database.xlsx',index_col='ID #')
temp = pd.DataFrame(excel)
temp.head()

# %%
temp.columns

# %%
temp.info()

# %%
tests = temp['Cal. Date'].astype(str)
dates = []
for test in tests:
    dates.append(test[:-9])
temp['Cal. Date']=dates
temp.head()

# %%
date = temp['Cal. due Date'].astype(str)
why = []
for date in date:
    why.append(date[:-9])
temp['Cal. due Date'] = why
temp.head()

# %%
temp.columns

# %%
temp = temp.loc[:,['Location', 'Type', 'Serial #', 'Description', 'Cal. Date', 'Cal. due Date',
                   'Comment', 'Owner']]


# %%
temp.dropna()

# %%

# %%
temp.to_csv('Equipment and Metrology.csv', index=True)

# %% [markdown]
# ### Create Streamlit Page

# %%
file = 'Equipment and Metrology.csv'
st.set_page_config(layout='wide')
st.title('Equipment and Metrology')

# %%
@st.cache
def load_data():
    df = pd.read_csv(file, index_col=False)
    return df

df = load_data

# %%
def search(data, column, search_term):
    if column == 'Location':
        search_term = (search_term)

    indexes = df.loc[df[column].isin([search_term])].index
    if indexes.size > 0:
        return df.iloc[indexes]
    else:
        return []
    


