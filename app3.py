import pandas as pd 
import streamlit as st

import plotly.express as px 

df = pd.read_csv('./bquery1.csv')

graph px.line(df, x= 'station_name', y='num')




st.write(df)