# app.py

import streamlit as st
import pandas as pd

st.title("Week 1 Demo Dashboard")

df = pd.read_csv("cleaned_data/voters.csv")
st.write("Here are the first five rows of the dataset:")
st.dataframe(df.head())

st.line_chart(df['age'])
