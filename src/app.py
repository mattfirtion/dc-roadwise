import streamlit as st
import pandas as pd

# Load the CSV file
@st.cache
def load_data():
    data = pd.read_csv('data/moving_violations_summary_2014.csv')
    return data

data = load_data()

# Sidebar
st.sidebar.title('DC RoadWise Analytics Dashboard')
selected_year = st.sidebar.selectbox('Select Year', sorted(data['Year'].unique()))

# Filter data based on selected year
filtered_data = data[data['Year'] == selected_year]

# Main content
st.title('DC RoadWise Analytics Dashboard')
st.write(f"Displaying data for year {selected_year}")

# Show basic statistics
st.subheader('Basic Statistics')
st.write(filtered_data.describe())

# Visualize data
st.subheader('Violation Type Distribution')
violation_counts = filtered_data['Violation Type'].value_counts()
st.bar_chart(violation_counts)
