# Displaying tables and data in dashboard
import pandas as pd
import streamlit as st
from os import path
from menu import menu


# Set up the page layout to use the full width of the web page
st.set_page_config(page_title="Life Expectancy", page_icon="📈", layout="wide")

st.markdown("# Power Generation")
st.sidebar.header("Power Generation")


@st.cache_data
def get_data():
    """        """
    URL = 'data/energy-consumption-by-source-and-country.csv'
    df = pd.read_csv(URL)
    return df


try:
    df = get_data()
    #st.subheader('st.dataframe, width = 600px, height = 200px')
    #st.dataframe(df, width=600, height=200)

    st.markdown("[![Click me](./app/static/fossil-fuels-per-capita.png)](./app/static/fossil-fuels-per-capita.png)")
    #st.image(('../static/fossil-fuels-per-capita.png'))
except TypeError:
    st.write('break point')

    
menu()
