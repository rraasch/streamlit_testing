import streamlit as st
import pandas as pd
import numpy as np

st.write("Here's our first attempt at using data to create a table:")
st.text("plain text")
st.table(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

x = st.slider('x', 0, 10)
st.write(x, 'squared is', x*x)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.text_input("Input latitude", key = "lat")
st.text_input("Input longitude", key = "lon")

if st.session_state.lat =="" or st.session_state.lon =="":
    lat, lon = 34, -118
else:
    lat = float(st.session_state.lat)
    lon = float(st.session_state.lon)


map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [lat, lon],
    columns=['lat', 'lon'])

st.map(map_df)

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['second column'])

'You selected: ', option


import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


import streamlit.components.v1 as components  # Import Streamlit

# Render the h1 block, contained in a frame of size 200x200.
components.html("<br><html><body><h1>Here is embedded HTML header</h1></body></html>", width=600, height=200)
