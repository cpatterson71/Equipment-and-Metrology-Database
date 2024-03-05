#equipment and calibration database
#import libraries
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import altair as alt

#load file to view
excel = pd.read_excel('Equipment_and_Metrology_Database.xlsx', index_col='ID #')
temp = pd.DataFrame(excel)
