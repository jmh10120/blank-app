import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Data Science App")
st.write("Welcome to my app!")

st.sidebar.title("Select dataset")

st.image("cat.jpg")


## Data Visualisation
df = pd.read_csv("tips.csv")
app_mode = st.sidebar.selectbox("Select a page >>", ["01 Introduction", "02 Data Visualisation"])

if app_mode == "01 Introduction":
    st.write("Let's start exploring the dataset:")
    df = pd.read_csv("tips.csv")

    st.dataframe(df.head(5))

    st.markdown("### Statistics Summary of the dataset >>")
    st.dataframe(df.describe())

elif app_mode == "02 Data Visualisation":
    st.write("Let's start doing data vis")
    list_of_var = df.columns
    user_selection = st.selectbox("Select a variable", list_of_var)

    st.markdown("### Bar chart")
    st.bar_chart(df[user_selection])

    st.markdown("### Line chart")
    st.line_chart(df[user_selection])


    user_selections = st.multiselect("Select a variable", list_of_var, ["total_bill","tip"])
    fig, ax= plt.subplots(figsize=(6,4))
    sns.barplot(x=user_selections[0],y=user_selections[1], data=df, palette='Blues')
    st.pyplot(fig)