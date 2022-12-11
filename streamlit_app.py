import streamlit as st
from collections import namedtuple
import math
import pandas as pd
import numpy as np
import plost                # this package is used to create plots/charts within streamlit
from PIL import Image       # this package is used to put images within streamlit

#from api_connection import get_data_from_api       # keep this commented if not using it otherwise brakes the app

# Page setting
st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
f1 = pd.read_csv('ranking.csv')
# replace the previous data with your own streamed data from API

### Here starts the web app design
# Row A
a1, a2, a3 = st.columns(3)
a1.image(Image.open('F1_logo.png'))
a2.metric("Last race", "Qatar")
a2.image(Image.open('Qatar.png'))
a3.metric("World Champion", "Max Verstapen", "454 PTS")
a3.image(Image.open('Verstappen.png'))

# Row B

b1, b2,  = st.columns(2)
b1.metric("Constructors Champioship", "Red Bull")
b1.image(Image.open('RBR.png'))
b2.metric("Fastest Pit stop", "1.98 Sec", "Mclaren")
b2.image(Image.open('mclaren.png'))

# Row C
c1,c2 = st.columns((10,3))
with c1:
    st.markdown('### Points on drivers championship 2022')
    chart_data = pd.DataFrame(index=f1['driver'])
    chart_data['point'] = np.array(f1['points'])
    chart_data = chart_data.sort_values(by='point' ,ascending= True)
    st.bar_chart(data=chart_data)
    
#with c2:
    #st.markdown('### Heatmap')              # text is created with markdown
    #plost.time_hist(                        # histogram
    #data=seattle_weather,
    #date='date',
    #x_unit='week',
    #y_unit='day',
    #color='temp_max',
    #aggregate='median',
    #legend=None)