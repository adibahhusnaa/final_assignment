import streamlit as st
import numpy as np
import pandas as pd

st.header("Report Team Adibah Mamasab Bakery 2021 App")
st.write("#### Data below shows Report From January to October 2021")
st.write(pd.DataFrame({
    'Months': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October'],
    'Sales': [5235.5, 6450.5, 5433.8, 6044.8, 6235.5, 5400.8, 6053.5, 6011.5, 6464.5, 5211.8],
    'Profit': [2617.75, 3225.25, 2716.9, 3022.4, 3117.75, 2700.4, 3026.75, 3005.75, 3232.25, 2605.9]
}))

chart_data = pd.DataFrame(
      np.random.randn(11, 1),
     columns=['Profit'])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(
      np.random.randn(11, 1),
     columns=['sales'])
st.bar_chart(chart_data)


option = st.sidebar.selectbox(
    'Select a mini project',
     ['bar chart','line chart'])

if option=='line chart':
    chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['sales', 'Profit'])

    st.line_chart(chart_data)






