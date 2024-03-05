#streamlit-app
import pandas as pd
import numpy as np
import streamlit as st
from st_aggrid import AgGrid
import altair as alt
import boto3

s3 = boto3.client('s3',
                  aws_access_key_id = 'AKIASCPKVVLRRR24MAEI',
                  aws_secret_access_key = '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'
                    )
s3.download_file('carldata', 'My_Equipment_file.xlsx', 'My_Equiptment_file.xlsx')
file = 'My_Equipment_File.xlsx'

excel = pd.read_excel(file, index_col=False)
temp = pd.DataFrame(excel)

