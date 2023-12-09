# Import packages

import pandas as pd
import altair as alt
import seaborn as sb 
import matplotlib.pyplot as plt
import streamlit as st
alt.data_transformers.disable_max_rows()

st.header('How have Industrial CO2 Emissions in the US Changed Since 1970?')

# Load traffic stops data and create a dataframe called stops
# and check the columns and their types
industrial = pd.read_csv('Midterm_Industrial_Data.csv')
industrial.head()

industrial['State'] = industrial['State'].astype(str)
#industrial['State Total Year'] = pd.to_datetime(industrial['State Total Year'], format='%Y')

line_chart = alt.Chart(industrial).mark_circle(size=60).encode(
    x=alt.X('US Total', title='US Total Year'),
    y=alt.Y('State Total Emissions Count', title='Total Emissions Mmt'),
#    tooltip=['State Total Year', 'State Total Emissions Count']
).properties(
    width=600,
    height=400
)

# Display the line chart in Streamlit
st.altair_chart(line_chart, use_container_width=True)
