# US_Industrial_CO2_Emissions
A look at how the US Industrial emissions have changed over the past 50 years. Each state and its total industrial emissions are viewable. I wanted to take a deeper dive into the industrial CO2 emissions throughout the US and at a state level per capita. Since the early 2000s the US has really started to crack down on emissions everywhere and in some extreme cases very heavy restrictions. After doing some analysis one might see these trends and large drops over time and can compare that to lws and restrictions that have been put in place.

**Streamlit app**: https://us-industrial-co2-emissions-analysis.streamlit.app/

The app has two pages:

**Main Page**: Overview of US Industrial CO2 Emissions

**Second Page**: Contains a more in depth look at state level industrial CO2 emissions and population data.

# Data Preparation
The data is from the epi.gov website where the government has reported lots of different CO2 emissions data within the US. In addition to the industrial CO2 emissions data I used for analysis, I also grabbed US census data from the United States Census Bureau.

The data sources for each of the datasets I created were from:


**-https://www.census.gov/data/tables/time-series/demo/popest/2020s-state-total.html**

**-https://www.eia.gov/environment/emissions/state/**

I had to readjust the columns for data analysis purposes. Once I did that I could create some data frames and indexes in order to create graphs with appropriate metrics for my analysis.

# Future Analysis
Some great future analysis ideas would be to add in other sectors of CO2 emissions within the US. I am realy interested in seeing there are any sectors where the CO2 emissions have actually increased not just because population may have increased. I would also like to add some other filtering techniques and hopefully an interactive map to my app in the future.
