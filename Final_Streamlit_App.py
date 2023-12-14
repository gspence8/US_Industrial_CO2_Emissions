# Import packages

import pandas as pd
import altair as alt
import seaborn as sb 
import matplotlib.pyplot as plt
import streamlit as st
alt.data_transformers.disable_max_rows()

st.title("How have Industrial CO2 Emissions in the US Changed Since 1970?")

#Running st.cache_data() will make streamlit run faster for the viewer.
st.cache_data()    

# Create tabs to different pages
tab1, tab2 = st.tabs(["Overall US CO2 Emissions", "Statewide CO2 Emissions"])

with tab1:
    #read in the industrial CO2 emission data set as emissions df
    emissions = pd.read_csv('Midterm_Industrial_Data_CO2.csv', index_col=0)
    #read in the US population data set as population df - make it per million by dividing by 1M and using that instead
    population = pd.read_csv('Midterm_Industrial_Data_pop.csv', index_col=0)
    population = population/1000000
    #make a new df called per_cap for the emissions per million capita by year
    year = emissions.index
    per_cap=pd.DataFrame(index=year)
    for state in emissions:
        per_cap[state] = (emissions[state]/population[state])
    #reset indexes for all 3 data frames after calculation
    emissions = emissions.reset_index()
    population = population.reset_index()
    per_cap = per_cap.reset_index()
    #adjust Year column to be a string
    emissions['Year'] = emissions['Year'].astype(str)
    population['Year'] = population['Year'].astype(str)
    per_cap['Year'] = per_cap['Year'].astype(str)

    #make a layered plot of total US Population & CO2 Emissions by year using the emissions df
    emissions_chart = alt.Chart(emissions, title="Total US CO2 Emissions & Population").mark_line(point=True).encode(
        x=alt.X('Year', title='Year', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('US Total', title='CO2 Emissions (Mmt)', scale=alt.Scale(domain=(emissions['US Total'].min(), emissions['US Total'].max()))),
        tooltip=['Year', 'US Total']
    ).properties(
        width=800,
        height=500
    )

    pop_chart = alt.Chart(population).mark_line(color='maroon', interpolate='monotone').encode(
        x=alt.X('Year', title='Year'),
        y=alt.Y('US Total', title='Population (Millions)', scale=alt.Scale(domain=(population['US Total'].min(), population['US Total'].max()))),
        tooltip=['Year', 'US Total']
    ).properties(
        width=800,
        height=500
    )

    st.altair_chart(alt.layer(emissions_chart, pop_chart).resolve_scale(y='independent'))

    st.markdown(
        """
        <div style="
            border: 2px solid #e5e5e5;
            border-radius: 15px;
            padding: 14px; 
            margin-top: 10px;
            margin-bottom: 100px;
            margin-left: 80px;
            margin-right: 10px;
            background-color: #add8e6;
            border-radius: 5px;
            color: black;
        ">
            In the chart above we can see how the Industrial CO2 emissions in the US have changed over the course of 40 years.
            Note how the population has changed over 40 years!
        </div>
        """,
       unsafe_allow_html=True
    )

    #make a chart of total CO2 emissions per capita by year using the per_cap df
    cap_chart = alt.Chart(per_cap.reset_index(), title="Total US CO2 Emissions per Capita by Year").encode(
        x=alt.X('Year', title='Year', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('US Total', title='CO2 Emission per Capita (mt/person)', scale=alt.Scale(domain=(per_cap['US Total'].min()-1, per_cap['US Total'].max()+1))),
        tooltip=['Year', 'US Total']
    ).properties(
        width=800,
        height=500
    )

    total_trendline = st.checkbox("Show Trendline", key="checkbox_trendline", value=True)

    # Create regression line chart if checkbox is checked
    if total_trendline:
        per_cap_regression_line = cap_chart.transform_regression('Year', 'US Total').mark_line(color='red')
        st.altair_chart(cap_chart.mark_line(color='green') + 
                    cap_chart.mark_circle(size=60, color='green') + 
                    per_cap_regression_line,
                    use_container_width=True    
                    )
    else:
        st.altair_chart(cap_chart.mark_line(color='green') + 
                    cap_chart.mark_circle(size=60, color='green'),
                    use_container_width=True    
                    )

    st.markdown(
        """
        <div style="
            border: 2px solid #e5e5e5;
            border-radius: 15px;
            padding: 14px; 
            margin-top: 10px;
            margin-bottom: 100px;
            margin-left: 80px;
            margin-right: 10px;
            background-color: #add8e6;
            border-radius: 5px;
            color: black;
        ">
            In this graph we can see a little more detail on how the emissions have changed per person on average.
            With this being Industrial data, per capita would suggest businesses in the US.
        </div>
        """,
       unsafe_allow_html=True
    )

with tab2:
    st.header('What does per capita look like at state level?')

    #select a specific state and make a new df of that state's data only as state_df
    sel_state = st.selectbox("Select State:", emissions.columns[2:])
    #sel_state='California' # this will be from the "STATE SELECT" field
    state_df=pd.DataFrame(data=(emissions['Year']))
    state_df['State CO2'] = emissions[sel_state]
    state_df['State Pop'] = population[sel_state]
    state_df['State PerCap'] = per_cap[sel_state]


    #make the same layered plot as above but for the selected Population & CO2 Emissions by year using the state_df df
    state_emissions_chart = alt.Chart(state_df, title="State Population & CO2 Emissions by Year").mark_line(point=True).encode(
        x=alt.X('Year', title='Year', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('State CO2', title='CO2 Emissions (Mmt)', scale=alt.Scale(domain=(state_df['State CO2'].min(), state_df['State CO2'].max()))),
        tooltip=['Year', 'State CO2']
    ).properties(
        width=800,
        height=500
    )

    state_pop_chart = alt.Chart(state_df).mark_line(color='maroon', interpolate='monotone').encode(
        x=alt.X('Year', title='Year'),
        y=alt.Y('State Pop', title='Population (Millions)', scale=alt.Scale(domain=(state_df['State Pop'].min(), state_df['State Pop'].max()))),
        tooltip=['Year', 'State Pop']
    ).properties(
        width=800,
        height=500
    )

    st.altair_chart(alt.layer(state_emissions_chart, state_pop_chart).resolve_scale(y='independent'))

    #make a State version fo the CO2 emissions per capita by year chart using the state_df df
    state_cap_chart = alt.Chart(state_df.reset_index(), title="State CO2 Emissions per Capita by Year").encode(
        x=alt.X('Year', title='Year', axis=alt.Axis(labelAngle=-45)),
        y=alt.Y('State PerCap', title='CO2 Emission per Capita (mt/person)', scale=alt.Scale(domain=(state_df['State PerCap'].min()-1, state_df['State PerCap'].max()+1))),
       tooltip=['Year', 'State PerCap']
    ).properties(
        width=800,
        height=500
    )

    show_trendline = st.checkbox("Show Trendline", value=True)

    # Create regression line chart if checkbox is checked
    if show_trendline:
        regression_line = state_cap_chart.transform_regression('Year', 'State PerCap').mark_line(color='red')
        st.altair_chart(state_cap_chart.mark_line(color='green') + 
                    state_cap_chart.mark_circle(size=60, color='green') + 
                    regression_line,
                    use_container_width=True    
                    )
    else:
        st.altair_chart(state_cap_chart.mark_line(color='green') + 
                    state_cap_chart.mark_circle(size=60, color='green'),
                    use_container_width=True    
                    )

    st.markdown(
        """
        <div style="
            border: 2px solid #e5e5e5;
            border-radius: 15px;
            padding: 14px; 
            margin-top: 10px;
            margin-bottom: 100px;
            margin-left: 80px;
            margin-right: 10px;
            background-color: #add8e6;
            border-radius: 5px;
            color: black;
        ">
            In this graph we can see a little more detail on how the emissions have changed per person over the years.
        </div>
        """,
       unsafe_allow_html=True
    )