import streamlit as st
import pandas as pd

import plotly.express as px

st.title('Coffee Database')
DATA_URL = ('https://raw.githubusercontent.com/jldbc/coffee-quality-database/refs/heads/master/data/arabica_data_cleaned.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# st.subheader('Number of pickups by hour')
species_counts = data['country.of.origin'].value_counts()
fig = px.bar(species_counts, x=species_counts.index, y=species_counts.values,
                     labels={'x': 'Country', 'y': 'Count'}, title='Coffee Count by Country')
st.plotly_chart(fig)
