# US_Industrial_CO2_Emissions
This application aims to look at how the US Industrial emissions have changed over the past 50 years. Each state and its total industrial emissions are viewable. I wanted to take a deeper dive into the industrial CO2 emissions throughout the US and at a state level per capita. Since the early 2000s the US has really started to crack down on emissions everywhere, and in some extreme cases, very heavy restrictions. Using the application to view the data at a country and statewide level, one can see how the trends in CO2 emissions per capita decrease over time - in most cases. These trends could be linked to the political spot light on global climate change and our efforts to combat it via reduction in CO2 emissions.

**Streamlit app**: https://us-industrial-co2-emissions-analysis.streamlit.app/

The app has two pages:

  **Main Page**: Overview of US Industrial CO2 Emissions

  **Second Page**: Contains a more in depth look at state level industrial CO2 emissions and population data.

# Data Preparation
The data is from the eia.gov website where the government has reported lots of different CO2 emissions data within the US. In addition to the industrial CO2 emissions data I used for analysis, I also grabbed US census data from the United States Census Bureau.

The data sources for each of the datasets I created were from:

**-https://www.census.gov/data/tables/time-series/demo/popest/2020s-state-total.html**

**-https://www.eia.gov/environment/emissions/state/**

In order to produce a more accurate reading of CO2 emissions, I utilized population data (in Millions) to calcualte the CO2 emissions per capita. I had to readjust the columns for data analysis purposes. Doing so, I was able to create data frames and indexes in order to generate graphs with appropriate metrics for my analysis.

# Future Analysis
Some great future analysis ideas would be to add in other sectors of CO2 emissions within the US. I am realy interested in seeing if there are any sectors where the CO2 emissions have actually increased, not just due to the rise in the US population over the years. I would also like to add some other filtering techniques such as an interactive map in the future.
