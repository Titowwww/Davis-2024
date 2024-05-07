import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

# Mount Data
# file_path = "Financial.csv"
data = pd.read_csv("Financial.csv")

st.title('Financial Dashboard')

# Bar Chart Country by Units Sold
st.subheader("Country by Units Sold")
plt.bar(data['Country'], data['Units Sold'])
plt.xlabel('Country')
plt.ylabel('Units Sold')
st.pyplot()

# Bar Chart Top 3 Job Title by Salary
st.subheader("Top 3 Job Title by Salary")
data_sorted = data.sort_values(by='salary', ascending=False)
top_3 = data_sorted.head(3)
st.bar_chart(top_3['salary'], top_3['job_title']) 
st.title("Top 3 Salaries")
st.xlabel('Job Title')
st.ylabel('Salary')
st.pyplot()
